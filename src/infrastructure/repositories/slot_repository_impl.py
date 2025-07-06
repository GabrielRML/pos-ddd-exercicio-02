from sqlalchemy.orm import Session
from domain.entities.slot import Slot
from domain.repositories.slot_repository import SlotRepository
from ..models.slot_model import SlotModel

class SlotRepositoryImpl(SlotRepository):
    def __init__(self, session: Session):
        self.session = session

    def get_all(self):
        return self.session.query(SlotModel).all()

    def get_by_id(self, slot_id: int):
        return self.session.query(SlotModel).filter_by(id=slot_id).first()

    def save(self, slot: Slot):
        slot_model = SlotModel(
            event_id=slot.event_id,
            participant_id=slot.participant_id,
            status=slot.status
        )
        self.session.add(slot_model)
        self.session.commit()

    def delete(self, slot_id: int):
        slot = self.session.query(SlotModel).filter_by(id=slot_id).first()
        if slot:
            self.session.delete(slot)
            self.session.commit()
