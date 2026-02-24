from abc import ABC, abstractmethod
from typing import Any


class Result(ABC):
    @abstractmethod
    def is_success(self) -> bool:
        """Retorna True si el resultado es exitoso."""
        pass

    @abstractmethod
    def is_error(self) -> bool:
        """Retorna True si el resultado es un error."""
        pass

    @abstractmethod
    def get_value(self) -> Any:
        """Retorna el valor del resultado si es exitoso, o None si es un error."""
        pass
