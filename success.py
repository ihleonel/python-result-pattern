
from typing import Any

from result import Result


class Success(Result):
    def __init__(self, value: Any) -> None:
        self.value = value

    def is_success(self) -> bool:
        return True

    def is_error(self) -> bool:
        return False

    def get_value(self) -> Any:
        return self.value
