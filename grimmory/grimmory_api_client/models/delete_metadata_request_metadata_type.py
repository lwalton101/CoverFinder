from enum import Enum


class DeleteMetadataRequestMetadataType(str, Enum):
    AUTHORS = "authors"
    CATEGORIES = "categories"
    LANGUAGES = "languages"
    MOODS = "moods"
    PUBLISHERS = "publishers"
    SERIES = "series"
    TAGS = "tags"

    def __str__(self) -> str:
        return str(self.value)
