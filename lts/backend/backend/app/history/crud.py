from sqlalchemy.orm import Session

from app.helpers import translate
from . import models, schema

def get_all(db: Session):
    """
    Fetch all history object and and return it to the client.
    """
    return db.query(models.History).all()


def create(db: Session, english: schema.EnglishSchema) -> models.History:
    """
    Create a history and store it in the database.
    """
    history = models.History(english=english.english, hindi=translate(english.english))
    db.add(history)
    db.commit()
    db.refresh(history)
    return history