from enum import Enum


class ContentRestrictionMode(str, Enum):
    ALLOW_ONLY = "ALLOW_ONLY"
    EXCLUDE = "EXCLUDE"

    def __str__(self) -> str:
        return str(self.value)
