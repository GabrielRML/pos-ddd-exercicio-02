from dataclasses import dataclass

@dataclass
class EventDTO:
    id: int
    name: str
    description: str
    date: str
