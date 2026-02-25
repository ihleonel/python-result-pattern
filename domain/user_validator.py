from typing import Optional
from domain.user_repository import UserRepository
from result import Error, Success, Result



class UserValidator:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def validate(
        self,
        id: Optional[int],
        name: str,
        email: str
    ) -> Result[None]:
        errors: dict[str, str] = {}

        if id is not None and id <= 0:
            errors["id"] = f"Invalid user ID: {id}"

        if not name:
            errors["name"] = "Name is required"

        if not email:
            errors["email"] = "Email is required"
        elif '@' not in email:
            errors["email"] = "Email is invalid"
        elif isinstance(self.user_repository.find_by_email(email), Success):
            errors["email"] = "Email already exists"

        if errors:
            return Error(errors)

        return Success(None)
