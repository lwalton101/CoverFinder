from enum import Enum


class BookdropFileStatus(str, Enum):
    FINALIZED = "FINALIZED"
    PENDING_REVIEW = "PENDING_REVIEW"

    def __str__(self) -> str:
        return str(self.value)
