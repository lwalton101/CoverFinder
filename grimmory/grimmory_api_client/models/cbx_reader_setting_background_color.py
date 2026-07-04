from enum import Enum


class CbxReaderSettingBackgroundColor(str, Enum):
    BLACK = "BLACK"
    GRAY = "GRAY"
    WHITE = "WHITE"

    def __str__(self) -> str:
        return str(self.value)
