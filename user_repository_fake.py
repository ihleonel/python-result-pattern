from typing import List
from result import Result, Error, Success
from domain.user_repository import UserRepository
from domain.user import User

class UserRepositoryFake(UserRepository):
    def __init__(self):
        self.users: List[User] = [
            User(id=1, name="Carlos Pérez", email="carlos@example.com")
        ]

    def search(self, user_id: int) -> Result[User]:
        for user in self.users:
            if user.id == user_id:
                return Success(user)
        return Error(f"User with ID {user_id} not found")

    def save(self, user: User) -> Result[User]:
        for i, existing_user in enumerate(self.users):
            if existing_user.id == user.id:
                self.users[i] = user
                return Success(user)

        self.users.append(user)
        return Success(user)

    def find_by_email(self, email: str) -> Result[User]:
        for user in self.users:
            if user.email == email:
                return Success(user)
        return Error(f"User with email {email} not found")
