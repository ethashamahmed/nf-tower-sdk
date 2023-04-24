from enum import Enum


class Visibility(str, Enum):
    PRIVATE = "PRIVATE"
    PUBLIC = "PUBLIC"
    SHARED = "SHARED"

    def __str__(self) -> str:
        return str(self.value)
