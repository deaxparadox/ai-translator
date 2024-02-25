from pydantic import BaseModel


class EnglishSchema(BaseModel):
    english: str

class HindiSchema(EnglishSchema):
    hindi: str

class HistorySchema(HindiSchema):
    pass

class HistoryWithID(HistorySchema):
    id: str

class Histories(BaseModel):
    histories: list[HistoryWithID]

class EnglishTokenSchema(EnglishSchema):
    token: str
    