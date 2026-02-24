from domain.user_repository import UserRepository
from result import Result, Error, Success
from domain.user import User

class UserRepositoryMySql(UserRepository):
    def get_by_id(self, user_id: int) -> Result[User]:
        if user_id <= 0:
            return Error(f"Invalid user ID: {user_id}")

        return Success(User(id=user_id, name="Juan Pérez", email="juan@example.com"))

    def update(self, user: User) -> Result[User]:
        return Success(user)
