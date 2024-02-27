from sqlalchemy import String, Column, ForeignKey
from sqlalchemy.orm import relationship
import datetime

# from app.user import models as user_models

from app.database import Base

# i = 0

# def mydefault():
#     global i
#     i += 1
#     return i

# t = Table(
#     "mytable",
#     metadata_obj,
#     Column("id", Integer, primary_key=True, default=mydefault),
# )

def generate_history_id(self):
    return datetime.datetime.now().isoformat()

class History(Base):
    __tablename__ = "histories"

    id = Column(String, default=generate_history_id, primary_key=True, unique=True)
    english = Column(String)
    hindi = Column(String)
    # token = relationship("user_models.Token", back_populates="histories")
    # token = Column(String, ForeignKey("users.id"))

    # user = relationship("User", back_populates="items")


    def __str__(self) -> str:
        return f"{self.english} {self.hindi}"
    

