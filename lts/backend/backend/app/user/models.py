from sqlalchemy import String, Column
from sqlalchemy.orm import relationship
import datetime

# from app.history import models as history_models

from app.database import Base


def generate_history_id(self):
    return datetime.datetime.now().isoformat()


class Token(Base):
    __tablename__ = "tokens"
    id = Column(String, default=generate_history_id, primary_key=True, unique=True)
    token = Column(String)

    # histories = relationship("history_models.History", back_populates="token")