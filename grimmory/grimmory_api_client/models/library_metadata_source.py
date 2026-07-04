from enum import Enum


class LibraryMetadataSource(str, Enum):
    EMBEDDED = "EMBEDDED"
    NONE = "NONE"
    PREFER_EMBEDDED = "PREFER_EMBEDDED"
    PREFER_SIDECAR = "PREFER_SIDECAR"
    SIDECAR = "SIDECAR"

    def __str__(self) -> str:
        return str(self.value)
