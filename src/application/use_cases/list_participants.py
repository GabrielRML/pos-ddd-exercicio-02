from typing import List
from domain.repositories.participant_repository import ParticipantRepository
from application.dtos.participant_dto import ParticipantDTO

class ListParticipantsUseCase:
    def __init__(self, participant_repository: ParticipantRepository):
        self.participant_repository = participant_repository

    def execute(self) -> List[ParticipantDTO]:
        participants = self.participant_repository.get_all()
        return [ParticipantDTO(id=participant.id, name=participant.name, email=participant.email) for participant in participants]
