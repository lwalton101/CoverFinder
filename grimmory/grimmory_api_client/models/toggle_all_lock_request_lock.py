from enum import Enum


class ToggleAllLockRequestLock(str, Enum):
    LOCK = "LOCK"
    UNLOCK = "UNLOCK"

    def __str__(self) -> str:
        return str(self.value)
