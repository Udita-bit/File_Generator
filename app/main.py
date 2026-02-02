from fastapi import FastAPI, Depends, HTTPException
from fastapi.responses import FileResponse
from sqlalchemy.orm import Session

from app.database.db import SessionLocal, engine
from app.database.models import FileRecord, Base
from app.services.ai_service import generate_content
from app.services.file_service import save_file, delete_file
from app.models.schema import CreateFileRequest

Base.metadata.create_all(bind=engine)

app = FastAPI(title="AI File Generator with RAG")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/create-file")
def create_file(request: CreateFileRequest, db: Session = Depends(get_db)):
    topic = request.topic
    filename = topic.replace(" ", "_").lower() + ".txt"

    content = generate_content(topic)
    save_file(filename, content)

    record = FileRecord(topic=topic, filename=filename)
    db.add(record)
    db.commit()

    return {"message": "File created", "filename": filename}

@app.get("/files")
def list_files(db: Session = Depends(get_db)):
    return db.query(FileRecord).all()

@app.get("/download/{filename}")
def download(filename: str):
    return FileResponse(f"app/files/{filename}", filename=filename)

@app.delete("/delete/{filename}")
def delete(filename: str, db: Session = Depends(get_db)):
    deleted = delete_file(filename)
    if not deleted:
        raise HTTPException(status_code=404, detail="File not found")

    db.query(FileRecord).filter(FileRecord.filename == filename).delete()
    db.commit()

    return {"message": "File deleted"}