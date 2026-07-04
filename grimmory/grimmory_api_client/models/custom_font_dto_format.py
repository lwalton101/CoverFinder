from enum import Enum


class CustomFontDtoFormat(str, Enum):
    OTF = "OTF"
    TTF = "TTF"
    WOFF = "WOFF"
    WOFF2 = "WOFF2"

    def __str__(self) -> str:
        return str(self.value)
