from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.book_review_metadata_provider import BookReviewMetadataProvider
from ..types import UNSET, Unset

T = TypeVar("T", bound="BookReview")


@_attrs_define
class BookReview:
    """
    Attributes:
        id (int | Unset):
        metadata_provider (BookReviewMetadataProvider | Unset):
        reviewer_name (str | Unset):
        title (str | Unset):
        rating (float | Unset):
        date (datetime.datetime | Unset):
        body (str | Unset):
        country (str | Unset):
        spoiler (bool | Unset):
        followers_count (int | Unset):
        text_reviews_count (int | Unset):
    """

    id: int | Unset = UNSET
    metadata_provider: BookReviewMetadataProvider | Unset = UNSET
    reviewer_name: str | Unset = UNSET
    title: str | Unset = UNSET
    rating: float | Unset = UNSET
    date: datetime.datetime | Unset = UNSET
    body: str | Unset = UNSET
    country: str | Unset = UNSET
    spoiler: bool | Unset = UNSET
    followers_count: int | Unset = UNSET
    text_reviews_count: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        metadata_provider: str | Unset = UNSET
        if not isinstance(self.metadata_provider, Unset):
            metadata_provider = self.metadata_provider.value

        reviewer_name = self.reviewer_name

        title = self.title

        rating = self.rating

        date: str | Unset = UNSET
        if not isinstance(self.date, Unset):
            date = self.date.isoformat()

        body = self.body

        country = self.country

        spoiler = self.spoiler

        followers_count = self.followers_count

        text_reviews_count = self.text_reviews_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if metadata_provider is not UNSET:
            field_dict["metadataProvider"] = metadata_provider
        if reviewer_name is not UNSET:
            field_dict["reviewerName"] = reviewer_name
        if title is not UNSET:
            field_dict["title"] = title
        if rating is not UNSET:
            field_dict["rating"] = rating
        if date is not UNSET:
            field_dict["date"] = date
        if body is not UNSET:
            field_dict["body"] = body
        if country is not UNSET:
            field_dict["country"] = country
        if spoiler is not UNSET:
            field_dict["spoiler"] = spoiler
        if followers_count is not UNSET:
            field_dict["followersCount"] = followers_count
        if text_reviews_count is not UNSET:
            field_dict["textReviewsCount"] = text_reviews_count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        _metadata_provider = d.pop("metadataProvider", UNSET)
        metadata_provider: BookReviewMetadataProvider | Unset
        if isinstance(_metadata_provider, Unset):
            metadata_provider = UNSET
        else:
            metadata_provider = BookReviewMetadataProvider(_metadata_provider)

        reviewer_name = d.pop("reviewerName", UNSET)

        title = d.pop("title", UNSET)

        rating = d.pop("rating", UNSET)

        _date = d.pop("date", UNSET)
        date: datetime.datetime | Unset
        if isinstance(_date, Unset):
            date = UNSET
        else:
            date = datetime.datetime.fromisoformat(_date)

        body = d.pop("body", UNSET)

        country = d.pop("country", UNSET)

        spoiler = d.pop("spoiler", UNSET)

        followers_count = d.pop("followersCount", UNSET)

        text_reviews_count = d.pop("textReviewsCount", UNSET)

        book_review = cls(
            id=id,
            metadata_provider=metadata_provider,
            reviewer_name=reviewer_name,
            title=title,
            rating=rating,
            date=date,
            body=body,
            country=country,
            spoiler=spoiler,
            followers_count=followers_count,
            text_reviews_count=text_reviews_count,
        )

        book_review.additional_properties = d
        return book_review

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
