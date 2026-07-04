from enum import Enum


class MagicShelfIconType(str, Enum):
    CUSTOM_SVG = "CUSTOM_SVG"
    LUCIDE = "LUCIDE"

    def __str__(self) -> str:
        return str(self.value)
