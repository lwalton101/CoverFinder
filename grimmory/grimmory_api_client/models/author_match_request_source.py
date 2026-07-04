from enum import Enum


class AuthorMatchRequestSource(str, Enum):
    AUDNEXUS = "AUDNEXUS"

    def __str__(self) -> str:
        return str(self.value)
