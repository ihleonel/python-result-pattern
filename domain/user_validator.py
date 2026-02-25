from typing import Optional
from result import Error, Success, Result



class UserValidator:
    @staticmethod
    def validate(
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

        if '@' not in email:
            errors["email"] = "Email is invalid"

        if errors:
            return Error(errors)

        return Success(None)
