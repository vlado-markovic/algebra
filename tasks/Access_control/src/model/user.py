from sqlalchemy import Boolean, Column, Integer, String
from src.ent.entities.base import Base

class User(Base):
    __tablename__ = "User"

    id = Column(Integer, primary_key=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    password = Column(String(256), nullable=False)
    active = Column(Boolean, nullable=False)
    system = Column(Boolean, nullable=False)

    def __repr__(self):
        return f"User({self.id=!r}, {self.first_name=!r}, {self.last_name=!r}, {self.active=!r}, {self.system=!r})"