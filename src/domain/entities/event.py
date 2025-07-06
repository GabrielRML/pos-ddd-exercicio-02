from typing import List
from dataclasses import dataclass
from .slot import Slot

@dataclass
class Event:
    id: int
    name: str
    description: str
    date: str
    slots: List[Slot]
