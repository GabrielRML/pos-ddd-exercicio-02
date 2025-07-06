from typing import List, Optional
from dataclasses import dataclass
from datetime import datetime
from .slot import Slot

@dataclass
class Event:
    id: Optional[int]
    name: str
    description: str
    date: str
    slots: List[Slot]
    
    def __post_init__(self):
        """Validate business rules after initialization"""
        if not self.name or len(self.name.strip()) == 0:
            raise ValueError("Event name cannot be empty")
        
        if not self.description:
            self.description = ""
            
        if len(self.name) > 100:
            raise ValueError("Event name cannot exceed 100 characters")
    
    def add_slot(self, slot: Slot) -> None:
        """Add a slot to the event (business logic)"""
        if slot.event_id != self.id:
            raise ValueError("Slot must belong to this event")
        self.slots.append(slot)
    
    def get_available_slots_count(self) -> int:
        """Business rule: count available slots"""
        from .slot import SlotStatus
        return len([slot for slot in self.slots 
                   if slot.status not in [SlotStatus.CONFIRMED, SlotStatus.CANCELED]])
    
    def is_full(self) -> bool:
        """Business rule: check if event is full"""
        return self.get_available_slots_count() == 0
