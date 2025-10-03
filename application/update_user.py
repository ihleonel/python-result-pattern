from domain.user import User
from domain.user_repository import UserRepository
from result import Result


class UpdateUser:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def __call__(self, id: int, name: str, email: str) -> Result:
        result: Result = self.user_repository.get_by_id(id)
        if result.is_error():
            return result

        user: User = result.get_value()

        result: Result = self.user_repository.update(User(id=user.id, name=name, email=email))

        return result
