from enum import Enum


class PerBookSettingEpub(str, Enum):
    GLOBAL = "Global"
    INDIVIDUAL = "Individual"

    def __str__(self) -> str:
        return str(self.value)
