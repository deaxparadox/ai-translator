from pydantic import BaseModel

class HelloModel(BaseModel):
    message: str

class Message(BaseModel):
    message: str