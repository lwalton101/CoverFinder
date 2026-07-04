from enum import Enum


class AdditionalFileUploadAdditionalFileBookType(str, Enum):
    AUDIOBOOK = "AUDIOBOOK"
    AZW3 = "AZW3"
    CBX = "CBX"
    EPUB = "EPUB"
    FB2 = "FB2"
    MOBI = "MOBI"
    PDF = "PDF"

    def __str__(self) -> str:
        return str(self.value)
