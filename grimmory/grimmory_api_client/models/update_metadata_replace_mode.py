from enum import Enum


class UpdateMetadataReplaceMode(str, Enum):
    REPLACE_ALL = "REPLACE_ALL"
    REPLACE_MISSING = "REPLACE_MISSING"
    REPLACE_WHEN_PROVIDED = "REPLACE_WHEN_PROVIDED"

    def __str__(self) -> str:
        return str(self.value)
