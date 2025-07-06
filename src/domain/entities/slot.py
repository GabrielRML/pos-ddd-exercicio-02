from enum import Enum
from dataclasses import dataclass

class SlotStatus(Enum):
    RESERVED = "reserved"
    PENDING_CONFIRMATION = "pending_confirmation"
    CONFIRMED = "confirmed"
    CANCELED = "canceled"

@dataclass
class Slot:
    id: int
    event_id: int
    participant_id: int
    status: SlotStatus
