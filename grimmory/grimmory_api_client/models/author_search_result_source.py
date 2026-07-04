from enum import Enum


class AuthorSearchResultSource(str, Enum):
    AUDNEXUS = "AUDNEXUS"

    def __str__(self) -> str:
        return str(self.value)
