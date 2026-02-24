from domain.user_repository import UserRepository
from result import Result, Error, Success
from domain.user import User

class UserRepositoryMySql(UserRepository):
    def search(self, user_id: int) -> Result[User]:
        if user_id <= 0:
            return Error(f"Invalid user ID: {user_id}")

        return Success(User(id=user_id, name="Juan Pérez", email="juan@example.com"))

    def save(self, user: User) -> Result[User]:
        if user.id is None:
            return Success(User(id=1, name=user.name, email=user.email))

        return Success(user)
