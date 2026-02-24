from dataclasses import dataclass
from typing import Optional


@dataclass(frozen=True)
class User:
    name: str
    email: str
    id: Optional[int] = None

