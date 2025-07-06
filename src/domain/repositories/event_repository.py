from abc import ABC, abstractmethod
from typing import List, Optional
from ..entities.event import Event

class EventRepository(ABC):

    @abstractmethod
    def get_all(self) -> List[Event]:
        pass

    @abstractmethod
    def get_by_id(self, event_id: int) -> Optional[Event]:
        pass

    @abstractmethod
    def save(self, event: Event) -> Event:
        pass

    @abstractmethod
    def delete(self, event_id: int) -> bool:
        pass

    @abstractmethod
    def find_by_name(self, name: str) -> List[Event]:
        pass
