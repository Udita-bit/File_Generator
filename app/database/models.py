from sqlalchemy import Column, Integer, String
from app.database.db import Base

class FileRecord(Base):
    __tablename__ = "files"

    id = Column(Integer, primary_key=True, index=True)
    topic = Column(String, nullable=False)
    filename = Column(String, unique=True, nullable=False)