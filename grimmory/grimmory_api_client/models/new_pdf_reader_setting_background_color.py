from enum import Enum


class NewPdfReaderSettingBackgroundColor(str, Enum):
    BLACK = "BLACK"
    GRAY = "GRAY"
    WHITE = "WHITE"

    def __str__(self) -> str:
        return str(self.value)
