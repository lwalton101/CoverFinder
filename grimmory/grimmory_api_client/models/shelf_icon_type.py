from enum import Enum


class ShelfIconType(str, Enum):
    CUSTOM_SVG = "CUSTOM_SVG"
    LUCIDE = "LUCIDE"

    def __str__(self) -> str:
        return str(self.value)
