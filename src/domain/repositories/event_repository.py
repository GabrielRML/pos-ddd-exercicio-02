from abc import ABC, abstractmethod
from typing import List
from ..entities.event import Event

class EventRepository(ABC):

    @abstractmethod
    def get_all(self) -> List[Event]:
        pass

    @abstractmethod
    def get_by_id(self, event_id: int) -> Event:
        pass

    @abstractmethod
    def save(self, event: Event) -> None:
        pass

    @abstractmethod
    def delete(self, event_id: int) -> None:
        pass
