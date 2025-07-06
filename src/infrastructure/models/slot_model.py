from sqlalchemy import Column, Integer, Enum, ForeignKey
from .base import Base
from domain.entities.slot import SlotStatus

class SlotModel(Base):
    __tablename__ = 'slots'

    id = Column(Integer, primary_key=True, autoincrement=True)
    event_id = Column(Integer, ForeignKey('events.id'), nullable=False)
    participant_id = Column(Integer, ForeignKey('participants.id'), nullable=False)
    status = Column(Enum(SlotStatus), nullable=False)
