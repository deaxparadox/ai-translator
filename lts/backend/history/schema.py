from pydantic import BaseModel

class HistorySchema(BaseModel):
    id: str
    english: str
    hindi: str