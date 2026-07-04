from enum import Enum


class BookLoreUserProvisioningMethod(str, Enum):
    LOCAL = "LOCAL"
    OIDC = "OIDC"
    REMOTE = "REMOTE"

    def __str__(self) -> str:
        return str(self.value)
