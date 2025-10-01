from abc import ABC, abstractmethod


class Result(ABC):
    @abstractmethod
    def is_success(self) -> bool:
        """Retorna True si el resultado es exitoso."""
        pass

    @abstractmethod
    def is_error(self) -> bool:
        """Retorna True si el resultado es un error."""
        pass
