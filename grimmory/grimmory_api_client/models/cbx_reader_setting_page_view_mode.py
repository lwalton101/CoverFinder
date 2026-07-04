from enum import Enum


class CbxReaderSettingPageViewMode(str, Enum):
    SINGLE_PAGE = "SINGLE_PAGE"
    TWO_PAGE = "TWO_PAGE"

    def __str__(self) -> str:
        return str(self.value)
