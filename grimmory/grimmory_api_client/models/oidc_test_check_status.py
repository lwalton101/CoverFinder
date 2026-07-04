from enum import Enum


class OidcTestCheckStatus(str, Enum):
    FAIL = "FAIL"
    PASS = "PASS"
    SKIP = "SKIP"
    WARN = "WARN"

    def __str__(self) -> str:
        return str(self.value)
