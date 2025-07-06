from domain.repositories.event_repository import EventRepository

class DeleteEventUseCase:
    def __init__(self, event_repository: EventRepository):
        self.event_repository = event_repository

    def execute(self, event_id: int):
        self.event_repository.delete(event_id)
