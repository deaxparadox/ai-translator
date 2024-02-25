from fastapi import APIRouter, Depends, status
from fastapi.responses import Response, JSONResponse
from sqlalchemy.orm import Session


from app.database import get_db
from . import crud, models, schema
import app.schema

router = APIRouter()

@router.post("/create")
def create_user(
    response: Response, 
    db: Session = Depends(get_db),
    token: schema.Token | None = None,
    responses={
        422: {
            "model": app.schema.Message,
            "description": "Invalid english sentence"
        },
        409: {
            "model": app.schema.Message,
            "description": "Token conflict"
        }
    }
):
    if not token or token.token == "":
        return JSONResponse(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            content = { "message": "Invalid token" }
        )
    if crud.token_exists(db, token):
        return JSONResponse(
            status_code=status.HTTP_409_CONFLICT,
            content={"message": "Token already exists"}
        )
    crud.create_user(db, token)
    response.status_code = status.HTTP_201_CREATED
    return token