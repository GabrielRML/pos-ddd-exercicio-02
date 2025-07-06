from sqlalchemy.orm import Session
from domain.entities.event import Event
from domain.repositories.event_repository import EventRepository
from ..models.event_model import EventModel

class EventRepositoryImpl(EventRepository):
    def __init__(self, session: Session):
        self.session = session

    def get_all(self):
        return self.session.query(EventModel).all()

    def get_by_id(self, event_id: int):
        return self.session.query(EventModel).filter_by(id=event_id).first()

    def save(self, event: Event):
        event_model = EventModel(
            name=event.name,
            description=event.description,
            date=event.date
        )
        self.session.add(event_model)
        self.session.commit()

    def delete(self, event_id: int):
        event = self.session.query(EventModel).filter_by(id=event_id).first()
        if event:
            self.session.delete(event)
            self.session.commit()
