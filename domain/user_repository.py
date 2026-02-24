from abc import ABC, abstractmethod
from domain.user import User
from result import Result

class UserRepository(ABC):
    @abstractmethod
    def get_by_id(self, user_id: int) -> Result[User]:
        ...

    @abstractmethod
    def update(self, user: User) -> Result[User]:
        ...
