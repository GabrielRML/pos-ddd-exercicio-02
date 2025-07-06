from .connection import engine
from ..models.base import Base
from ..models.event_model import EventModel
from ..models.participant_model import ParticipantModel
from ..models.slot_model import SlotModel

def init_db():
    Base.metadata.create_all(bind=engine)
