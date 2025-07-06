from dataclasses import dataclass
from domain.entities.slot import SlotStatus

@dataclass
class SlotDTO:
    id: int
    event_id: int
    participant_id: int
    status: SlotStatus
