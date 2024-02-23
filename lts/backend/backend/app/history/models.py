from sqlalchemy import String, Column
from sqlalchemy.orm import relationship
import datetime

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

    def __str__(self) -> str:
        return f"{self.english} {self.hindi}"
    

