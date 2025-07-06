from domain.entities.event import Event
from domain.repositories.event_repository import EventRepository
from ..dtos.event_dto import EventDTO

class CreateEventUseCase:
    def __init__(self, event_repository: EventRepository):
        self.event_repository = event_repository

    def execute(self, name: str, description: str, date: str) -> EventDTO:
        event = Event(id=None, name=name, description=description, date=date, slots=[])
        
        saved_event = self.event_repository.save(event)
        
        return EventDTO(
            id=saved_event.id,
            name=saved_event.name,
            description=saved_event.description,
            date=saved_event.date
        )
