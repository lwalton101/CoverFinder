from enum import Enum


class CbxReaderSettingScrollMode(str, Enum):
    INFINITE = "INFINITE"
    LONG_STRIP = "LONG_STRIP"
    PAGINATED = "PAGINATED"

    def __str__(self) -> str:
        return str(self.value)
