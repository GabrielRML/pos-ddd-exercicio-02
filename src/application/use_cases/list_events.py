from typing import List
from domain.repositories.event_repository import EventRepository
from application.dtos.event_dto import EventDTO

class ListEventsUseCase:
    def __init__(self, event_repository: EventRepository):
        self.event_repository = event_repository

    def execute(self) -> List[EventDTO]:
        events = self.event_repository.get_all()
        return [EventDTO(id=event.id, name=event.name, description=event.description, date=event.date) for event in events]
