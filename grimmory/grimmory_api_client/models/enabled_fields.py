from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="EnabledFields")


@_attrs_define
class EnabledFields:
    """
    Attributes:
        title (bool | Unset):
        subtitle (bool | Unset):
        description (bool | Unset):
        authors (bool | Unset):
        publisher (bool | Unset):
        published_date (bool | Unset):
        series_name (bool | Unset):
        series_number (bool | Unset):
        series_total (bool | Unset):
        isbn13 (bool | Unset):
        isbn10 (bool | Unset):
        language (bool | Unset):
        categories (bool | Unset):
        cover (bool | Unset):
        page_count (bool | Unset):
        asin (bool | Unset):
        goodreads_id (bool | Unset):
        comicvine_id (bool | Unset):
        hardcover_id (bool | Unset):
        hardcover_book_id (bool | Unset):
        google_id (bool | Unset):
        lubimyczytac_id (bool | Unset):
        amazon_rating (bool | Unset):
        amazon_review_count (bool | Unset):
        goodreads_rating (bool | Unset):
        goodreads_review_count (bool | Unset):
        hardcover_rating (bool | Unset):
        hardcover_review_count (bool | Unset):
        lubimyczytac_rating (bool | Unset):
        ranobedb_id (bool | Unset):
        ranobedb_rating (bool | Unset):
        audible_id (bool | Unset):
        audible_rating (bool | Unset):
        audible_review_count (bool | Unset):
        moods (bool | Unset):
        tags (bool | Unset):
    """

    title: bool | Unset = UNSET
    subtitle: bool | Unset = UNSET
    description: bool | Unset = UNSET
    authors: bool | Unset = UNSET
    publisher: bool | Unset = UNSET
    published_date: bool | Unset = UNSET
    series_name: bool | Unset = UNSET
    series_number: bool | Unset = UNSET
    series_total: bool | Unset = UNSET
    isbn13: bool | Unset = UNSET
    isbn10: bool | Unset = UNSET
    language: bool | Unset = UNSET
    categories: bool | Unset = UNSET
    cover: bool | Unset = UNSET
    page_count: bool | Unset = UNSET
    asin: bool | Unset = UNSET
    goodreads_id: bool | Unset = UNSET
    comicvine_id: bool | Unset = UNSET
    hardcover_id: bool | Unset = UNSET
    hardcover_book_id: bool | Unset = UNSET
    google_id: bool | Unset = UNSET
    lubimyczytac_id: bool | Unset = UNSET
    amazon_rating: bool | Unset = UNSET
    amazon_review_count: bool | Unset = UNSET
    goodreads_rating: bool | Unset = UNSET
    goodreads_review_count: bool | Unset = UNSET
    hardcover_rating: bool | Unset = UNSET
    hardcover_review_count: bool | Unset = UNSET
    lubimyczytac_rating: bool | Unset = UNSET
    ranobedb_id: bool | Unset = UNSET
    ranobedb_rating: bool | Unset = UNSET
    audible_id: bool | Unset = UNSET
    audible_rating: bool | Unset = UNSET
    audible_review_count: bool | Unset = UNSET
    moods: bool | Unset = UNSET
    tags: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        title = self.title

        subtitle = self.subtitle

        description = self.description

        authors = self.authors

        publisher = self.publisher

        published_date = self.published_date

        series_name = self.series_name

        series_number = self.series_number

        series_total = self.series_total

        isbn13 = self.isbn13

        isbn10 = self.isbn10

        language = self.language

        categories = self.categories

        cover = self.cover

        page_count = self.page_count

        asin = self.asin

        goodreads_id = self.goodreads_id

        comicvine_id = self.comicvine_id

        hardcover_id = self.hardcover_id

        hardcover_book_id = self.hardcover_book_id

        google_id = self.google_id

        lubimyczytac_id = self.lubimyczytac_id

        amazon_rating = self.amazon_rating

        amazon_review_count = self.amazon_review_count

        goodreads_rating = self.goodreads_rating

        goodreads_review_count = self.goodreads_review_count

        hardcover_rating = self.hardcover_rating

        hardcover_review_count = self.hardcover_review_count

        lubimyczytac_rating = self.lubimyczytac_rating

        ranobedb_id = self.ranobedb_id

        ranobedb_rating = self.ranobedb_rating

        audible_id = self.audible_id

        audible_rating = self.audible_rating

        audible_review_count = self.audible_review_count

        moods = self.moods

        tags = self.tags

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if title is not UNSET:
            field_dict["title"] = title
        if subtitle is not UNSET:
            field_dict["subtitle"] = subtitle
        if description is not UNSET:
            field_dict["description"] = description
        if authors is not UNSET:
            field_dict["authors"] = authors
        if publisher is not UNSET:
            field_dict["publisher"] = publisher
        if published_date is not UNSET:
            field_dict["publishedDate"] = published_date
        if series_name is not UNSET:
            field_dict["seriesName"] = series_name
        if series_number is not UNSET:
            field_dict["seriesNumber"] = series_number
        if series_total is not UNSET:
            field_dict["seriesTotal"] = series_total
        if isbn13 is not UNSET:
            field_dict["isbn13"] = isbn13
        if isbn10 is not UNSET:
            field_dict["isbn10"] = isbn10
        if language is not UNSET:
            field_dict["language"] = language
        if categories is not UNSET:
            field_dict["categories"] = categories
        if cover is not UNSET:
            field_dict["cover"] = cover
        if page_count is not UNSET:
            field_dict["pageCount"] = page_count
        if asin is not UNSET:
            field_dict["asin"] = asin
        if goodreads_id is not UNSET:
            field_dict["goodreadsId"] = goodreads_id
        if comicvine_id is not UNSET:
            field_dict["comicvineId"] = comicvine_id
        if hardcover_id is not UNSET:
            field_dict["hardcoverId"] = hardcover_id
        if hardcover_book_id is not UNSET:
            field_dict["hardcoverBookId"] = hardcover_book_id
        if google_id is not UNSET:
            field_dict["googleId"] = google_id
        if lubimyczytac_id is not UNSET:
            field_dict["lubimyczytacId"] = lubimyczytac_id
        if amazon_rating is not UNSET:
            field_dict["amazonRating"] = amazon_rating
        if amazon_review_count is not UNSET:
            field_dict["amazonReviewCount"] = amazon_review_count
        if goodreads_rating is not UNSET:
            field_dict["goodreadsRating"] = goodreads_rating
        if goodreads_review_count is not UNSET:
            field_dict["goodreadsReviewCount"] = goodreads_review_count
        if hardcover_rating is not UNSET:
            field_dict["hardcoverRating"] = hardcover_rating
        if hardcover_review_count is not UNSET:
            field_dict["hardcoverReviewCount"] = hardcover_review_count
        if lubimyczytac_rating is not UNSET:
            field_dict["lubimyczytacRating"] = lubimyczytac_rating
        if ranobedb_id is not UNSET:
            field_dict["ranobedbId"] = ranobedb_id
        if ranobedb_rating is not UNSET:
            field_dict["ranobedbRating"] = ranobedb_rating
        if audible_id is not UNSET:
            field_dict["audibleId"] = audible_id
        if audible_rating is not UNSET:
            field_dict["audibleRating"] = audible_rating
        if audible_review_count is not UNSET:
            field_dict["audibleReviewCount"] = audible_review_count
        if moods is not UNSET:
            field_dict["moods"] = moods
        if tags is not UNSET:
            field_dict["tags"] = tags

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        title = d.pop("title", UNSET)

        subtitle = d.pop("subtitle", UNSET)

        description = d.pop("description", UNSET)

        authors = d.pop("authors", UNSET)

        publisher = d.pop("publisher", UNSET)

        published_date = d.pop("publishedDate", UNSET)

        series_name = d.pop("seriesName", UNSET)

        series_number = d.pop("seriesNumber", UNSET)

        series_total = d.pop("seriesTotal", UNSET)

        isbn13 = d.pop("isbn13", UNSET)

        isbn10 = d.pop("isbn10", UNSET)

        language = d.pop("language", UNSET)

        categories = d.pop("categories", UNSET)

        cover = d.pop("cover", UNSET)

        page_count = d.pop("pageCount", UNSET)

        asin = d.pop("asin", UNSET)

        goodreads_id = d.pop("goodreadsId", UNSET)

        comicvine_id = d.pop("comicvineId", UNSET)

        hardcover_id = d.pop("hardcoverId", UNSET)

        hardcover_book_id = d.pop("hardcoverBookId", UNSET)

        google_id = d.pop("googleId", UNSET)

        lubimyczytac_id = d.pop("lubimyczytacId", UNSET)

        amazon_rating = d.pop("amazonRating", UNSET)

        amazon_review_count = d.pop("amazonReviewCount", UNSET)

        goodreads_rating = d.pop("goodreadsRating", UNSET)

        goodreads_review_count = d.pop("goodreadsReviewCount", UNSET)

        hardcover_rating = d.pop("hardcoverRating", UNSET)

        hardcover_review_count = d.pop("hardcoverReviewCount", UNSET)

        lubimyczytac_rating = d.pop("lubimyczytacRating", UNSET)

        ranobedb_id = d.pop("ranobedbId", UNSET)

        ranobedb_rating = d.pop("ranobedbRating", UNSET)

        audible_id = d.pop("audibleId", UNSET)

        audible_rating = d.pop("audibleRating", UNSET)

        audible_review_count = d.pop("audibleReviewCount", UNSET)

        moods = d.pop("moods", UNSET)

        tags = d.pop("tags", UNSET)

        enabled_fields = cls(
            title=title,
            subtitle=subtitle,
            description=description,
            authors=authors,
            publisher=publisher,
            published_date=published_date,
            series_name=series_name,
            series_number=series_number,
            series_total=series_total,
            isbn13=isbn13,
            isbn10=isbn10,
            language=language,
            categories=categories,
            cover=cover,
            page_count=page_count,
            asin=asin,
            goodreads_id=goodreads_id,
            comicvine_id=comicvine_id,
            hardcover_id=hardcover_id,
            hardcover_book_id=hardcover_book_id,
            google_id=google_id,
            lubimyczytac_id=lubimyczytac_id,
            amazon_rating=amazon_rating,
            amazon_review_count=amazon_review_count,
            goodreads_rating=goodreads_rating,
            goodreads_review_count=goodreads_review_count,
            hardcover_rating=hardcover_rating,
            hardcover_review_count=hardcover_review_count,
            lubimyczytac_rating=lubimyczytac_rating,
            ranobedb_id=ranobedb_id,
            ranobedb_rating=ranobedb_rating,
            audible_id=audible_id,
            audible_rating=audible_rating,
            audible_review_count=audible_review_count,
            moods=moods,
            tags=tags,
        )

        enabled_fields.additional_properties = d
        return enabled_fields

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
