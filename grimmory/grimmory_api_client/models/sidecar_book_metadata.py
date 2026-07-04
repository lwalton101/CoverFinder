from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.comic_metadata import ComicMetadata
    from ..models.sidecar_identifiers import SidecarIdentifiers
    from ..models.sidecar_ratings import SidecarRatings
    from ..models.sidecar_series import SidecarSeries


T = TypeVar("T", bound="SidecarBookMetadata")


@_attrs_define
class SidecarBookMetadata:
    """
    Attributes:
        title (str | Unset):
        subtitle (str | Unset):
        authors (list[str] | Unset):
        publisher (str | Unset):
        published_date (datetime.date | Unset):
        description (str | Unset):
        isbn10 (str | Unset):
        isbn13 (str | Unset):
        language (str | Unset):
        page_count (int | Unset):
        categories (list[str] | Unset):
        moods (list[str] | Unset):
        tags (list[str] | Unset):
        series (SidecarSeries | Unset):
        identifiers (SidecarIdentifiers | Unset):
        ratings (SidecarRatings | Unset):
        age_rating (int | Unset):
        content_rating (str | Unset):
        narrator (str | Unset):
        abridged (bool | Unset):
        comic_metadata (ComicMetadata | Unset):
    """

    title: str | Unset = UNSET
    subtitle: str | Unset = UNSET
    authors: list[str] | Unset = UNSET
    publisher: str | Unset = UNSET
    published_date: datetime.date | Unset = UNSET
    description: str | Unset = UNSET
    isbn10: str | Unset = UNSET
    isbn13: str | Unset = UNSET
    language: str | Unset = UNSET
    page_count: int | Unset = UNSET
    categories: list[str] | Unset = UNSET
    moods: list[str] | Unset = UNSET
    tags: list[str] | Unset = UNSET
    series: SidecarSeries | Unset = UNSET
    identifiers: SidecarIdentifiers | Unset = UNSET
    ratings: SidecarRatings | Unset = UNSET
    age_rating: int | Unset = UNSET
    content_rating: str | Unset = UNSET
    narrator: str | Unset = UNSET
    abridged: bool | Unset = UNSET
    comic_metadata: ComicMetadata | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        title = self.title

        subtitle = self.subtitle

        authors: list[str] | Unset = UNSET
        if not isinstance(self.authors, Unset):
            authors = self.authors

        publisher = self.publisher

        published_date: str | Unset = UNSET
        if not isinstance(self.published_date, Unset):
            published_date = self.published_date.isoformat()

        description = self.description

        isbn10 = self.isbn10

        isbn13 = self.isbn13

        language = self.language

        page_count = self.page_count

        categories: list[str] | Unset = UNSET
        if not isinstance(self.categories, Unset):
            categories = self.categories

        moods: list[str] | Unset = UNSET
        if not isinstance(self.moods, Unset):
            moods = self.moods

        tags: list[str] | Unset = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags

        series: dict[str, Any] | Unset = UNSET
        if not isinstance(self.series, Unset):
            series = self.series.to_dict()

        identifiers: dict[str, Any] | Unset = UNSET
        if not isinstance(self.identifiers, Unset):
            identifiers = self.identifiers.to_dict()

        ratings: dict[str, Any] | Unset = UNSET
        if not isinstance(self.ratings, Unset):
            ratings = self.ratings.to_dict()

        age_rating = self.age_rating

        content_rating = self.content_rating

        narrator = self.narrator

        abridged = self.abridged

        comic_metadata: dict[str, Any] | Unset = UNSET
        if not isinstance(self.comic_metadata, Unset):
            comic_metadata = self.comic_metadata.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if title is not UNSET:
            field_dict["title"] = title
        if subtitle is not UNSET:
            field_dict["subtitle"] = subtitle
        if authors is not UNSET:
            field_dict["authors"] = authors
        if publisher is not UNSET:
            field_dict["publisher"] = publisher
        if published_date is not UNSET:
            field_dict["publishedDate"] = published_date
        if description is not UNSET:
            field_dict["description"] = description
        if isbn10 is not UNSET:
            field_dict["isbn10"] = isbn10
        if isbn13 is not UNSET:
            field_dict["isbn13"] = isbn13
        if language is not UNSET:
            field_dict["language"] = language
        if page_count is not UNSET:
            field_dict["pageCount"] = page_count
        if categories is not UNSET:
            field_dict["categories"] = categories
        if moods is not UNSET:
            field_dict["moods"] = moods
        if tags is not UNSET:
            field_dict["tags"] = tags
        if series is not UNSET:
            field_dict["series"] = series
        if identifiers is not UNSET:
            field_dict["identifiers"] = identifiers
        if ratings is not UNSET:
            field_dict["ratings"] = ratings
        if age_rating is not UNSET:
            field_dict["ageRating"] = age_rating
        if content_rating is not UNSET:
            field_dict["contentRating"] = content_rating
        if narrator is not UNSET:
            field_dict["narrator"] = narrator
        if abridged is not UNSET:
            field_dict["abridged"] = abridged
        if comic_metadata is not UNSET:
            field_dict["comicMetadata"] = comic_metadata

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.comic_metadata import ComicMetadata
        from ..models.sidecar_identifiers import SidecarIdentifiers
        from ..models.sidecar_ratings import SidecarRatings
        from ..models.sidecar_series import SidecarSeries

        d = dict(src_dict)
        title = d.pop("title", UNSET)

        subtitle = d.pop("subtitle", UNSET)

        authors = cast(list[str], d.pop("authors", UNSET))

        publisher = d.pop("publisher", UNSET)

        _published_date = d.pop("publishedDate", UNSET)
        published_date: datetime.date | Unset
        if isinstance(_published_date, Unset):
            published_date = UNSET
        else:
            published_date = datetime.date.fromisoformat(_published_date)

        description = d.pop("description", UNSET)

        isbn10 = d.pop("isbn10", UNSET)

        isbn13 = d.pop("isbn13", UNSET)

        language = d.pop("language", UNSET)

        page_count = d.pop("pageCount", UNSET)

        categories = cast(list[str], d.pop("categories", UNSET))

        moods = cast(list[str], d.pop("moods", UNSET))

        tags = cast(list[str], d.pop("tags", UNSET))

        _series = d.pop("series", UNSET)
        series: SidecarSeries | Unset
        if isinstance(_series, Unset):
            series = UNSET
        else:
            series = SidecarSeries.from_dict(_series)

        _identifiers = d.pop("identifiers", UNSET)
        identifiers: SidecarIdentifiers | Unset
        if isinstance(_identifiers, Unset):
            identifiers = UNSET
        else:
            identifiers = SidecarIdentifiers.from_dict(_identifiers)

        _ratings = d.pop("ratings", UNSET)
        ratings: SidecarRatings | Unset
        if isinstance(_ratings, Unset):
            ratings = UNSET
        else:
            ratings = SidecarRatings.from_dict(_ratings)

        age_rating = d.pop("ageRating", UNSET)

        content_rating = d.pop("contentRating", UNSET)

        narrator = d.pop("narrator", UNSET)

        abridged = d.pop("abridged", UNSET)

        _comic_metadata = d.pop("comicMetadata", UNSET)
        comic_metadata: ComicMetadata | Unset
        if isinstance(_comic_metadata, Unset):
            comic_metadata = UNSET
        else:
            comic_metadata = ComicMetadata.from_dict(_comic_metadata)

        sidecar_book_metadata = cls(
            title=title,
            subtitle=subtitle,
            authors=authors,
            publisher=publisher,
            published_date=published_date,
            description=description,
            isbn10=isbn10,
            isbn13=isbn13,
            language=language,
            page_count=page_count,
            categories=categories,
            moods=moods,
            tags=tags,
            series=series,
            identifiers=identifiers,
            ratings=ratings,
            age_rating=age_rating,
            content_rating=content_rating,
            narrator=narrator,
            abridged=abridged,
            comic_metadata=comic_metadata,
        )

        sidecar_book_metadata.additional_properties = d
        return sidecar_book_metadata

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
