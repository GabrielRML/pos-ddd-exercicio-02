from domain.entities.event import Event
from domain.repositories.event_repository import EventRepository

class CreateEventUseCase:
    def __init__(self, event_repository: EventRepository):
        self.event_repository = event_repository

    def execute(self, name: str, description: str, date: str):
        event = Event(id=None, name=name, description=description, date=date, slots=[])
        self.event_repository.save(event)
