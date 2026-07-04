from enum import Enum


class BookFileArchiveType(str, Enum):
    RAR = "RAR"
    SEVEN_ZIP = "SEVEN_ZIP"
    UNKNOWN = "UNKNOWN"
    ZIP = "ZIP"

    def __str__(self) -> str:
        return str(self.value)
