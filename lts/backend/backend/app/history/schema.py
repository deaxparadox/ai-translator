from pydantic import BaseModel

class HistorySchema(BaseModel):
    english: str
    hindi: str

class HistoryWithID(HistorySchema):
    id: str

class Histories(BaseModel):
    histories: list[HistoryWithID]