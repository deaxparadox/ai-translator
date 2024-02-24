from fastapi import APIRouter, Depends, status, Form
from fastapi.responses import Response, JSONResponse
from fastapi.requests import Request
from sqlalchemy.orm import Session
from typing import Annotated

from app.database import get_db
from . import crud, models, schema
import app.schema

router = APIRouter()

@router.get("", response_model=schema.Histories)
def get_all_history(resposne: Response, db: Session = Depends(get_db)):

    resposne.status_code = status.HTTP_200_OK
    return {
        "histories": crud.get_all(db)
    }

@router.post(
    "/create", 
    response_model=schema.HistoryWithID,
    responses={
        422: {
            "model": app.schema.Message,
            "description": "Invalid english sentence"
        }
    }
)
def create_history(
    response: Response,
    english: schema.EnglishSchema | None = None,
    # english: Annotated[str, Form()],
    db: Session = Depends(get_db), 
):
    print(english)
    if not english or english.english == "":
        return JSONResponse(
            status_code=422,
            content = { "message": "Invalid english sentence" }
        )


    history = crud.create(db, english)
    response.status_code = status.HTTP_201_CREATED
    return history



@router.post(
    "/create2", 
    response_model=schema.EnglishSchema,
    responses={
        422: {
            "model": app.schema.Message,
            "description": "Invalid english sentence"
        }
    }
)
def create_history_2_test(
    response: Response,
    english: schema.EnglishSchema | None = None,
    db: Session = Depends(get_db), 
):
    if not english or english.english == "":
        return JSONResponse(
            status_code=422,
            content = { "message": "Invalid english sentence" }
        )

    response.status_code = status.HTTP_201_CREATED
    return english