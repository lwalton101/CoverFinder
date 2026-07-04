from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="MetadataMatchWeights")


@_attrs_define
class MetadataMatchWeights:
    """
    Attributes:
        title (int | Unset):
        subtitle (int | Unset):
        description (int | Unset):
        authors (int | Unset):
        publisher (int | Unset):
        published_date (int | Unset):
        series_name (int | Unset):
        series_number (int | Unset):
        series_total (int | Unset):
        isbn13 (int | Unset):
        isbn10 (int | Unset):
        language (int | Unset):
        page_count (int | Unset):
        categories (int | Unset):
        amazon_rating (int | Unset):
        amazon_review_count (int | Unset):
        goodreads_rating (int | Unset):
        goodreads_review_count (int | Unset):
        hardcover_rating (int | Unset):
        hardcover_review_count (int | Unset):
        douban_rating (int | Unset):
        douban_review_count (int | Unset):
        ranobedb_rating (int | Unset):
        lubimyczytac_rating (int | Unset):
        audible_rating (int | Unset):
        audible_review_count (int | Unset):
        cover_image (int | Unset):
    """

    title: int | Unset = UNSET
    subtitle: int | Unset = UNSET
    description: int | Unset = UNSET
    authors: int | Unset = UNSET
    publisher: int | Unset = UNSET
    published_date: int | Unset = UNSET
    series_name: int | Unset = UNSET
    series_number: int | Unset = UNSET
    series_total: int | Unset = UNSET
    isbn13: int | Unset = UNSET
    isbn10: int | Unset = UNSET
    language: int | Unset = UNSET
    page_count: int | Unset = UNSET
    categories: int | Unset = UNSET
    amazon_rating: int | Unset = UNSET
    amazon_review_count: int | Unset = UNSET
    goodreads_rating: int | Unset = UNSET
    goodreads_review_count: int | Unset = UNSET
    hardcover_rating: int | Unset = UNSET
    hardcover_review_count: int | Unset = UNSET
    douban_rating: int | Unset = UNSET
    douban_review_count: int | Unset = UNSET
    ranobedb_rating: int | Unset = UNSET
    lubimyczytac_rating: int | Unset = UNSET
    audible_rating: int | Unset = UNSET
    audible_review_count: int | Unset = UNSET
    cover_image: int | Unset = UNSET
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

        page_count = self.page_count

        categories = self.categories

        amazon_rating = self.amazon_rating

        amazon_review_count = self.amazon_review_count

        goodreads_rating = self.goodreads_rating

        goodreads_review_count = self.goodreads_review_count

        hardcover_rating = self.hardcover_rating

        hardcover_review_count = self.hardcover_review_count

        douban_rating = self.douban_rating

        douban_review_count = self.douban_review_count

        ranobedb_rating = self.ranobedb_rating

        lubimyczytac_rating = self.lubimyczytac_rating

        audible_rating = self.audible_rating

        audible_review_count = self.audible_review_count

        cover_image = self.cover_image

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
        if page_count is not UNSET:
            field_dict["pageCount"] = page_count
        if categories is not UNSET:
            field_dict["categories"] = categories
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
        if douban_rating is not UNSET:
            field_dict["doubanRating"] = douban_rating
        if douban_review_count is not UNSET:
            field_dict["doubanReviewCount"] = douban_review_count
        if ranobedb_rating is not UNSET:
            field_dict["ranobedbRating"] = ranobedb_rating
        if lubimyczytac_rating is not UNSET:
            field_dict["lubimyczytacRating"] = lubimyczytac_rating
        if audible_rating is not UNSET:
            field_dict["audibleRating"] = audible_rating
        if audible_review_count is not UNSET:
            field_dict["audibleReviewCount"] = audible_review_count
        if cover_image is not UNSET:
            field_dict["coverImage"] = cover_image

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

        page_count = d.pop("pageCount", UNSET)

        categories = d.pop("categories", UNSET)

        amazon_rating = d.pop("amazonRating", UNSET)

        amazon_review_count = d.pop("amazonReviewCount", UNSET)

        goodreads_rating = d.pop("goodreadsRating", UNSET)

        goodreads_review_count = d.pop("goodreadsReviewCount", UNSET)

        hardcover_rating = d.pop("hardcoverRating", UNSET)

        hardcover_review_count = d.pop("hardcoverReviewCount", UNSET)

        douban_rating = d.pop("doubanRating", UNSET)

        douban_review_count = d.pop("doubanReviewCount", UNSET)

        ranobedb_rating = d.pop("ranobedbRating", UNSET)

        lubimyczytac_rating = d.pop("lubimyczytacRating", UNSET)

        audible_rating = d.pop("audibleRating", UNSET)

        audible_review_count = d.pop("audibleReviewCount", UNSET)

        cover_image = d.pop("coverImage", UNSET)

        metadata_match_weights = cls(
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
            page_count=page_count,
            categories=categories,
            amazon_rating=amazon_rating,
            amazon_review_count=amazon_review_count,
            goodreads_rating=goodreads_rating,
            goodreads_review_count=goodreads_review_count,
            hardcover_rating=hardcover_rating,
            hardcover_review_count=hardcover_review_count,
            douban_rating=douban_rating,
            douban_review_count=douban_review_count,
            ranobedb_rating=ranobedb_rating,
            lubimyczytac_rating=lubimyczytac_rating,
            audible_rating=audible_rating,
            audible_review_count=audible_review_count,
            cover_image=cover_image,
        )

        metadata_match_weights.additional_properties = d
        return metadata_match_weights

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
