from abc import ABC, abstractmethod
from typing import List
from ..entities.slot import Slot

class SlotRepository(ABC):

    @abstractmethod
    def get_all(self) -> List[Slot]:
        pass

    @abstractmethod
    def get_by_id(self, slot_id: int) -> Slot:
        pass

    @abstractmethod
    def save(self, slot: Slot) -> None:
        pass

    @abstractmethod
    def delete(self, slot_id: int) -> None:
        pass
