from domain.entities.participant import Participant
from domain.repositories.participant_repository import ParticipantRepository

class CreateParticipantUseCase:
    def __init__(self, participant_repository: ParticipantRepository):
        self.participant_repository = participant_repository

    def execute(self, name: str, email: str):
        participant = Participant(id=None, name=name, email=email)
        self.participant_repository.save(participant)
