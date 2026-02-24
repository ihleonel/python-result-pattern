from typing import Optional
from domain.user import User
from result import Error, Success, Result



class UserValidator:
    @staticmethod
    def validate(
        id: Optional[int],
        name: str,
        email: str
    ) -> Result[User]:
        errors: dict[str, str] = {}

        if id is not None and id <= 0:
            errors["id"] = f"Invalid user ID: {id}"

        if not name:
            errors["name"] = "Name is required"

        if not email:
            errors["email"] = "Email is required"

        if '@' not in email:
            errors["email"] = "Email is invalid"

        if errors:
            return Error(errors)

        return Success(User(id=id, name=name, email=email))
