from enum import Enum


class NewPdfReaderSettingScrollMode(str, Enum):
    INFINITE = "INFINITE"
    PAGINATED = "PAGINATED"

    def __str__(self) -> str:
        return str(self.value)
