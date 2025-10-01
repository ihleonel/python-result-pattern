
from result import Result


class Success(Result):
    def __init__(self, value):
        self.value = value

    def is_success(self) -> bool:
        return True

    def is_error(self) -> bool:
        return False

    def get_value(self):
        return self.value
