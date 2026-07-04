from enum import Enum


class NewPdfReaderSettingPageSpread(str, Enum):
    EVEN = "EVEN"
    ODD = "ODD"

    def __str__(self) -> str:
        return str(self.value)
