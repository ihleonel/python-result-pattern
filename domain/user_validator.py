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

        validate_id_result = self.validate_id(id)
        if isinstance(validate_id_result, Error):
            errors.update(validate_id_result.error)

        validate_name_result = self.validate_name(name)
        if isinstance(validate_name_result, Error):
            errors.update(validate_name_result.error)

        validate_email_result = self.validate_email(email)
        if isinstance(validate_email_result, Error):
            errors.update(validate_email_result.error)

        if errors:
            return Error(errors)

        return Success(None)

    def validate_id(self, id: Optional[int]) -> Result[None]:
        if id is None or id <= 0:
            return Error({'id': f"Invalid user ID: {id}"})
        return Success(None)

    def validate_name(self, name: str) -> Result[None]:
        if not name:
            return Error({'name': "Name is required"})
        return Success(None)

    def validate_email(self, email: str) -> Result[None]:
        if not email:
            return Error({'email': "Email is required"})
        elif '@' not in email:
            return Error({'email': "Email is invalid"})
        elif isinstance(self.user_repository.find_by_email(email), Success):
            return Error({'email': "Email already exists"})
        return Success(None)
