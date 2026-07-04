from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BulkMetadataUpdateRequest")


@_attrs_define
class BulkMetadataUpdateRequest:
    """Bulk metadata update request

    Attributes:
        book_ids (list[int] | Unset):
        authors (list[str] | Unset):
        clear_authors (bool | Unset):
        publisher (str | Unset):
        clear_publisher (bool | Unset):
        language (str | Unset):
        clear_language (bool | Unset):
        series_name (str | Unset):
        clear_series_name (bool | Unset):
        series_total (int | Unset):
        clear_series_total (bool | Unset):
        published_date (datetime.date | Unset):
        clear_published_date (bool | Unset):
        genres (list[str] | Unset):
        clear_genres (bool | Unset):
        moods (list[str] | Unset):
        clear_moods (bool | Unset):
        tags (list[str] | Unset):
        clear_tags (bool | Unset):
        merge_categories (bool | Unset):
        merge_moods (bool | Unset):
        merge_tags (bool | Unset):
        age_rating (int | Unset):
        clear_age_rating (bool | Unset):
        content_rating (str | Unset):
        clear_content_rating (bool | Unset):
    """

    book_ids: list[int] | Unset = UNSET
    authors: list[str] | Unset = UNSET
    clear_authors: bool | Unset = UNSET
    publisher: str | Unset = UNSET
    clear_publisher: bool | Unset = UNSET
    language: str | Unset = UNSET
    clear_language: bool | Unset = UNSET
    series_name: str | Unset = UNSET
    clear_series_name: bool | Unset = UNSET
    series_total: int | Unset = UNSET
    clear_series_total: bool | Unset = UNSET
    published_date: datetime.date | Unset = UNSET
    clear_published_date: bool | Unset = UNSET
    genres: list[str] | Unset = UNSET
    clear_genres: bool | Unset = UNSET
    moods: list[str] | Unset = UNSET
    clear_moods: bool | Unset = UNSET
    tags: list[str] | Unset = UNSET
    clear_tags: bool | Unset = UNSET
    merge_categories: bool | Unset = UNSET
    merge_moods: bool | Unset = UNSET
    merge_tags: bool | Unset = UNSET
    age_rating: int | Unset = UNSET
    clear_age_rating: bool | Unset = UNSET
    content_rating: str | Unset = UNSET
    clear_content_rating: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        book_ids: list[int] | Unset = UNSET
        if not isinstance(self.book_ids, Unset):
            book_ids = self.book_ids

        authors: list[str] | Unset = UNSET
        if not isinstance(self.authors, Unset):
            authors = self.authors

        clear_authors = self.clear_authors

        publisher = self.publisher

        clear_publisher = self.clear_publisher

        language = self.language

        clear_language = self.clear_language

        series_name = self.series_name

        clear_series_name = self.clear_series_name

        series_total = self.series_total

        clear_series_total = self.clear_series_total

        published_date: str | Unset = UNSET
        if not isinstance(self.published_date, Unset):
            published_date = self.published_date.isoformat()

        clear_published_date = self.clear_published_date

        genres: list[str] | Unset = UNSET
        if not isinstance(self.genres, Unset):
            genres = self.genres

        clear_genres = self.clear_genres

        moods: list[str] | Unset = UNSET
        if not isinstance(self.moods, Unset):
            moods = self.moods

        clear_moods = self.clear_moods

        tags: list[str] | Unset = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags

        clear_tags = self.clear_tags

        merge_categories = self.merge_categories

        merge_moods = self.merge_moods

        merge_tags = self.merge_tags

        age_rating = self.age_rating

        clear_age_rating = self.clear_age_rating

        content_rating = self.content_rating

        clear_content_rating = self.clear_content_rating

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if book_ids is not UNSET:
            field_dict["bookIds"] = book_ids
        if authors is not UNSET:
            field_dict["authors"] = authors
        if clear_authors is not UNSET:
            field_dict["clearAuthors"] = clear_authors
        if publisher is not UNSET:
            field_dict["publisher"] = publisher
        if clear_publisher is not UNSET:
            field_dict["clearPublisher"] = clear_publisher
        if language is not UNSET:
            field_dict["language"] = language
        if clear_language is not UNSET:
            field_dict["clearLanguage"] = clear_language
        if series_name is not UNSET:
            field_dict["seriesName"] = series_name
        if clear_series_name is not UNSET:
            field_dict["clearSeriesName"] = clear_series_name
        if series_total is not UNSET:
            field_dict["seriesTotal"] = series_total
        if clear_series_total is not UNSET:
            field_dict["clearSeriesTotal"] = clear_series_total
        if published_date is not UNSET:
            field_dict["publishedDate"] = published_date
        if clear_published_date is not UNSET:
            field_dict["clearPublishedDate"] = clear_published_date
        if genres is not UNSET:
            field_dict["genres"] = genres
        if clear_genres is not UNSET:
            field_dict["clearGenres"] = clear_genres
        if moods is not UNSET:
            field_dict["moods"] = moods
        if clear_moods is not UNSET:
            field_dict["clearMoods"] = clear_moods
        if tags is not UNSET:
            field_dict["tags"] = tags
        if clear_tags is not UNSET:
            field_dict["clearTags"] = clear_tags
        if merge_categories is not UNSET:
            field_dict["mergeCategories"] = merge_categories
        if merge_moods is not UNSET:
            field_dict["mergeMoods"] = merge_moods
        if merge_tags is not UNSET:
            field_dict["mergeTags"] = merge_tags
        if age_rating is not UNSET:
            field_dict["ageRating"] = age_rating
        if clear_age_rating is not UNSET:
            field_dict["clearAgeRating"] = clear_age_rating
        if content_rating is not UNSET:
            field_dict["contentRating"] = content_rating
        if clear_content_rating is not UNSET:
            field_dict["clearContentRating"] = clear_content_rating

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        book_ids = cast(list[int], d.pop("bookIds", UNSET))

        authors = cast(list[str], d.pop("authors", UNSET))

        clear_authors = d.pop("clearAuthors", UNSET)

        publisher = d.pop("publisher", UNSET)

        clear_publisher = d.pop("clearPublisher", UNSET)

        language = d.pop("language", UNSET)

        clear_language = d.pop("clearLanguage", UNSET)

        series_name = d.pop("seriesName", UNSET)

        clear_series_name = d.pop("clearSeriesName", UNSET)

        series_total = d.pop("seriesTotal", UNSET)

        clear_series_total = d.pop("clearSeriesTotal", UNSET)

        _published_date = d.pop("publishedDate", UNSET)
        published_date: datetime.date | Unset
        if isinstance(_published_date, Unset):
            published_date = UNSET
        else:
            published_date = datetime.date.fromisoformat(_published_date)

        clear_published_date = d.pop("clearPublishedDate", UNSET)

        genres = cast(list[str], d.pop("genres", UNSET))

        clear_genres = d.pop("clearGenres", UNSET)

        moods = cast(list[str], d.pop("moods", UNSET))

        clear_moods = d.pop("clearMoods", UNSET)

        tags = cast(list[str], d.pop("tags", UNSET))

        clear_tags = d.pop("clearTags", UNSET)

        merge_categories = d.pop("mergeCategories", UNSET)

        merge_moods = d.pop("mergeMoods", UNSET)

        merge_tags = d.pop("mergeTags", UNSET)

        age_rating = d.pop("ageRating", UNSET)

        clear_age_rating = d.pop("clearAgeRating", UNSET)

        content_rating = d.pop("contentRating", UNSET)

        clear_content_rating = d.pop("clearContentRating", UNSET)

        bulk_metadata_update_request = cls(
            book_ids=book_ids,
            authors=authors,
            clear_authors=clear_authors,
            publisher=publisher,
            clear_publisher=clear_publisher,
            language=language,
            clear_language=clear_language,
            series_name=series_name,
            clear_series_name=clear_series_name,
            series_total=series_total,
            clear_series_total=clear_series_total,
            published_date=published_date,
            clear_published_date=clear_published_date,
            genres=genres,
            clear_genres=clear_genres,
            moods=moods,
            clear_moods=clear_moods,
            tags=tags,
            clear_tags=clear_tags,
            merge_categories=merge_categories,
            merge_moods=merge_moods,
            merge_tags=merge_tags,
            age_rating=age_rating,
            clear_age_rating=clear_age_rating,
            content_rating=content_rating,
            clear_content_rating=clear_content_rating,
        )

        bulk_metadata_update_request.additional_properties = d
        return bulk_metadata_update_request

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
