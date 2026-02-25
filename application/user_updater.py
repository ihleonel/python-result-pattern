from domain.user import User
from domain.user_repository import UserRepository
from domain.user_validator import UserValidator
from result import Error, Result


class UserUpdater:
    def __init__(self, user_repository: UserRepository, user_validator: UserValidator):
        self.user_repository = user_repository
        self.user_validator = user_validator

    def __call__(self, id: int, name: str, email: str) -> Result[User]:
        validation_result: Result[None] = self.user_validator.validate(id=id, name=name, email=email)
        if isinstance(validation_result, Error):
            return validation_result

        save_result: Result[User] = self.user_repository.save(
            User(id=id, name=name, email=email)
        )

        return save_result
