from dataclasses import dataclass


@dataclass(frozen=True)
class User:
    id: int
    name: str
    email: str

    def __post_init__(self):
        errors: dict[str, str] = {}

        if self.id <= 0:
            errors['id'] = "El campo 'id' debe ser un número positivo"

        if not self.name or not self.name.strip():
            errors['name'] = "El campo 'name' no puede ser nulo o estar vacío"

        if not self.email or not self.email.strip():
            errors['email'] = "El campo 'email' no puede ser nulo o estar vacío"
        elif "@" not in self.email:
            errors['email'] = "El campo 'email' debe tener un formato válido"

        if errors:
            raise ValueError(errors)

