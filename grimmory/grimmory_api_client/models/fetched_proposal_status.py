from enum import Enum


class FetchedProposalStatus(str, Enum):
    ACCEPTED = "ACCEPTED"
    FETCHED = "FETCHED"
    REJECTED = "REJECTED"

    def __str__(self) -> str:
        return str(self.value)
