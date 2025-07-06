from abc import ABC, abstractmethod
from typing import List
from ..entities.participant import Participant

class ParticipantRepository(ABC):

    @abstractmethod
    def get_all(self) -> List[Participant]:
        pass

    @abstractmethod
    def get_by_id(self, participant_id: int) -> Participant:
        pass

    @abstractmethod
    def save(self, participant: Participant) -> None:
        pass

    @abstractmethod
    def delete(self, participant_id: int) -> None:
        pass
