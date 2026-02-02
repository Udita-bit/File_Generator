from pydantic import BaseModel

class CreateFileRequest(BaseModel):
    topic: str