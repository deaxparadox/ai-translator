from typing import Union

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

import backend.settings.local as settings
from backend.models import HelloModel

app = FastAPI()



app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_HOSTS,
    allow_credentials=True,
    allow_methods=settings.ALLOWED_METHODS,
    allow_headers=settings.ALLOWED_HEADERS,
)


@app.get("/", response_model=HelloModel)
def read_root():

    return {"message": settings.transcriber("hello everyone")[0]["translation_text"]}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}