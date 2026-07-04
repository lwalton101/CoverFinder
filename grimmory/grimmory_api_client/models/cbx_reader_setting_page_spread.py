from enum import Enum


class CbxReaderSettingPageSpread(str, Enum):
    EVEN = "EVEN"
    ODD = "ODD"

    def __str__(self) -> str:
        return str(self.value)
