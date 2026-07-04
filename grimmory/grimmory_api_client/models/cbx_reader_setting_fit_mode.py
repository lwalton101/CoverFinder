from enum import Enum


class CbxReaderSettingFitMode(str, Enum):
    ACTUAL_SIZE = "ACTUAL_SIZE"
    AUTO = "AUTO"
    FIT_HEIGHT = "FIT_HEIGHT"
    FIT_PAGE = "FIT_PAGE"
    FIT_WIDTH = "FIT_WIDTH"

    def __str__(self) -> str:
        return str(self.value)
