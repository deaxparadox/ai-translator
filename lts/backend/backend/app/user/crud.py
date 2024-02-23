from sqlalchemy.orm import Session

from .models import Token

def get_user(db: Session, id: str) -> Token:
    return db.query(Token).get(id)