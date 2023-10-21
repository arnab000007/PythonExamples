
from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Optional
import copy
from time import sleep

class Cloneable(ABC):
    
    @abstractmethod
    def clone(self):
        pass

class User(Cloneable):
    def __init__(
        self, id: int, first_name: str, last_name: str, email: str, phone: str
    ):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone = phone

        sleep(5)  # Simulate API call

    def clone(self) -> User:
        return copy.deepcopy(self)


class UserRegistry(ABC):
    @abstractmethod
    def get_prototype(self, role: str) -> Optional[User]:
        pass

    @abstractmethod
    def add_prototype(self, role: str, user: User) -> None:
        pass

    def clone(self, role: str) -> Optional[User]:
        prototype = self.get_prototype(role)
        if prototype is None:
            raise Exception(f"Prototype with role {role} not found")

        return prototype.clone()
    


class UserRegistryImpl(UserRegistry):
    def __init__(self):
        self.prototypes: dict[str, User] = {}

    def get_prototype(self, role: str) -> Optional[User]:
        if role not in self.prototypes:
            return None

        return self.prototypes[role]

    def add_prototype(self, role: str, user: User) -> None:
        self.prototypes[role] = user