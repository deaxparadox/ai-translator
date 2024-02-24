from sqlalchemy.orm import Session
from sqlalchemy.orm import Query
from typing import List

from . import models, schema

def get_user(db: Session, id: str) -> models.Token:
    return db.query(models.Token).get(id)

def create_user(db: Session, token: schema.Token):
    token_instance = models.Token(token=token.token)
    db.add(token_instance)
    db.commit()
    db.refresh(token_instance)
    return token_instance

def token_exists(db: Session, token: schema.Token) -> bool:
    tokens: List = db.query(models.Token).filter(models.Token.token == token.token).all()
    print(tokens)
    if len(tokens) > 0:
        return True
    return False

# def token(delete)