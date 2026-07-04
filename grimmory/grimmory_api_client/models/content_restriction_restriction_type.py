from enum import Enum


class ContentRestrictionRestrictionType(str, Enum):
    AGE_RATING = "AGE_RATING"
    CATEGORY = "CATEGORY"
    CONTENT_RATING = "CONTENT_RATING"
    MOOD = "MOOD"
    TAG = "TAG"

    def __str__(self) -> str:
        return str(self.value)
