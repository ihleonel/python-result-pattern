from result import Result


class Error(Result):
    def __init__(self, errors):
        self.errors = errors

    def is_success(self) -> bool:
        return False

    def is_error(self) -> bool:
        return True

    def get_errors(self):
        return self.errors
