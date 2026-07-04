from enum import Enum


class TaskCreateResponseStatus(str, Enum):
    ACCEPTED = "ACCEPTED"
    CANCELLED = "CANCELLED"
    COMPLETED = "COMPLETED"
    FAILED = "FAILED"
    IN_PROGRESS = "IN_PROGRESS"

    def __str__(self) -> str:
        return str(self.value)
