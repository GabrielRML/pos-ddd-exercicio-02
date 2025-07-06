from domain.repositories.participant_repository import ParticipantRepository

class DeleteParticipantUseCase:
    def __init__(self, participant_repository: ParticipantRepository):
        self.participant_repository = participant_repository

    def execute(self, participant_id: int):
        self.participant_repository.delete(participant_id)
