from dataclasses import dataclass
from datetime import datetime

@dataclass
class Event:
    type_event: str
    detail: str
    user: str
    timestamp: str = datetime.now().isoformat()