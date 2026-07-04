from enum import Enum


class SortDirection(str, Enum):
    ASCENDING = "ASCENDING"
    DESCENDING = "DESCENDING"

    def __str__(self) -> str:
        return str(self.value)
