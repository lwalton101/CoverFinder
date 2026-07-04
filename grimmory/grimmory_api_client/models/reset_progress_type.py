from enum import Enum


class ResetProgressType(str, Enum):
    BOOKLORE = "BOOKLORE"
    KOBO = "KOBO"
    KOREADER = "KOREADER"

    def __str__(self) -> str:
        return str(self.value)
