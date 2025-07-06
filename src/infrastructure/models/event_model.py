from sqlalchemy import Column, Integer, String, Date
from .base import Base

class EventModel(Base):
    __tablename__ = 'events'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=True)
    date = Column(Date, nullable=False)
