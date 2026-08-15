from dataclasses import dataclass, field
from itertools import count

_ids = count(1)


@dataclass
class Task:
    title: str
    done: bool = False
    remind_at: str = None
    id: int = field(default_factory=lambda: next(_ids))
