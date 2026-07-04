from enum import Enum


class StatusInfoStatus(str, Enum):
    FINISHED = "Finished"
    READING = "Reading"
    READYTOREAD = "ReadyToRead"

    def __str__(self) -> str:
        return str(self.value)
