from sqlalchemy.orm import Session

from .models import History

def get_all(db: Session):
    return db.query(History).all()

def create(db: Session, english: str, hindi: str) -> History:
    history = db.add(History)