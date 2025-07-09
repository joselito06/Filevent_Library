from dataclasses import dataclass, field
from datetime import datetime

@dataclass
class Event:
    type_event: str
    detail: str
    user: str
    timestamp: str = field(default_factory=lambda: datetime.now().isoformat())
    read: bool = False

    def to_dict(self):
        return self.__dict__

    @staticmethod
    def from_dict(data: dict):
        return Event(**data)