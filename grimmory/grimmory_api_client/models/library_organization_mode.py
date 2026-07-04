from enum import Enum


class LibraryOrganizationMode(str, Enum):
    AUTO_DETECT = "AUTO_DETECT"
    BOOK_PER_FILE = "BOOK_PER_FILE"
    BOOK_PER_FOLDER = "BOOK_PER_FOLDER"

    def __str__(self) -> str:
        return str(self.value)
