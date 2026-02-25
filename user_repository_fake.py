from typing import List
from result import Result, Error, Success
from domain.user_repository import UserRepository
from domain.user import User

class UserRepositoryFake(UserRepository):
    users: List[User] = [
        User(id=1, name="Carlos Pérez", email="carlos@example.com")
    ]

    def search(self, user_id: int) -> Result[User]:
        if user_id <= 0:
            return Error(f"Invalid user ID: {user_id}")

        return Success(User(id=user_id, name="Juan Pérez", email="juan@example.com"))

    def save(self, user: User) -> Result[User]:
        return Success(user)

    def find_by_email(self, email: str) -> Result[User]:
        for user in self.users:
            if user.email == email:
                return Success(user)
        return Error(f"User with email {email} not found")
