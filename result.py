from dataclasses import dataclass
from typing import TypeVar, Generic, Union

T = TypeVar('T')

@dataclass
class Success(Generic[T]):
    value: T

@dataclass
class Error:
    error: dict[str, str]

Result = Union[Success[T], Error]
