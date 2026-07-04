from enum import Enum


class NewPdfViewerPreferencesBackgroundColor(str, Enum):
    BLACK = "BLACK"
    GRAY = "GRAY"
    WHITE = "WHITE"

    def __str__(self) -> str:
        return str(self.value)
