from enum import Enum


class BookStatusUpdateResponseReadStatus(str, Enum):
    ABANDONED = "ABANDONED"
    PARTIALLY_READ = "PARTIALLY_READ"
    PAUSED = "PAUSED"
    READ = "READ"
    READING = "READING"
    RE_READING = "RE_READING"
    UNREAD = "UNREAD"
    UNSET = "UNSET"
    WONT_READ = "WONT_READ"

    def __str__(self) -> str:
        return str(self.value)
