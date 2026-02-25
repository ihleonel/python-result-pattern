from abc import ABC, abstractmethod
from domain.user import User
from result import Result

class UserRepository(ABC):
    @abstractmethod
    def save(self, user: User) -> Result[User]:
        ...

    @abstractmethod
    def search(self, user_id: int) -> Result[User]:
        ...

    @abstractmethod
    def find_by_email(self, email: str) -> Result[User]:
        ...
