from sqlalchemy.orm import Session
from domain.entities.participant import Participant
from domain.repositories.participant_repository import ParticipantRepository
from ..models.participant_model import ParticipantModel

class ParticipantRepositoryImpl(ParticipantRepository):
    def __init__(self, session: Session):
        self.session = session

    def get_all(self):
        return self.session.query(ParticipantModel).all()

    def get_by_id(self, participant_id: int):
        return self.session.query(ParticipantModel).filter_by(id=participant_id).first()

    def save(self, participant: Participant):
        participant_model = ParticipantModel(
            name=participant.name,
            email=participant.email
        )
        self.session.add(participant_model)
        self.session.commit()

    def delete(self, participant_id: int):
        participant = self.session.query(ParticipantModel).filter_by(id=participant_id).first()
        if participant:
            self.session.delete(participant)
            self.session.commit()
