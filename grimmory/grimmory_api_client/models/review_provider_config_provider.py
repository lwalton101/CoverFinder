from enum import Enum


class ReviewProviderConfigProvider(str, Enum):
    AMAZON = "Amazon"
    AUDIBLE = "Audible"
    COMICVINE = "Comicvine"
    DOUBAN = "Douban"
    GOODREADS = "GoodReads"
    GOOGLE = "Google"
    HARDCOVER = "Hardcover"
    LUBIMYCZYTAC = "Lubimyczytac"
    RANOBEDB = "Ranobedb"

    def __str__(self) -> str:
        return str(self.value)
