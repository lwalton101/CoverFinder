from enum import Enum


class OpdsUserV2SortOrder(str, Enum):
    AUTHOR_ASC = "AUTHOR_ASC"
    AUTHOR_DESC = "AUTHOR_DESC"
    RATING_ASC = "RATING_ASC"
    RATING_DESC = "RATING_DESC"
    RECENT = "RECENT"
    SERIES_ASC = "SERIES_ASC"
    SERIES_DESC = "SERIES_DESC"
    TITLE_ASC = "TITLE_ASC"
    TITLE_DESC = "TITLE_DESC"

    def __str__(self) -> str:
        return str(self.value)
