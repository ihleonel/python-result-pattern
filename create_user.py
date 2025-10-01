from user import User
from success import Success
from error import Error
from result import Result


class CreateUser:
    def __call__(self, id: int, name: str, email: str) -> Result:
        try:
            user = User(id, name, email)
            return Success(user)
        except ValueError as e:
            return Error(e.args[0])
