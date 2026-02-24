from result import Result
from typing import List


class Error(Result):
    def __init__(self, errors: List[str]) -> None:
        self.errors = errors

    def is_success(self) -> bool:
        return False

    def is_error(self) -> bool:
        return True

    def get_errors(self) -> List[str]:
        return self.errors

    def get_value(self) -> List[str]:
        return self.errors
