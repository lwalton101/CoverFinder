from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="MetadataProviderSpecificFields")


@_attrs_define
class MetadataProviderSpecificFields:
    """
    Attributes:
        asin (bool | Unset):
        amazon_rating (bool | Unset):
        amazon_review_count (bool | Unset):
        google_id (bool | Unset):
        goodreads_id (bool | Unset):
        goodreads_rating (bool | Unset):
        goodreads_review_count (bool | Unset):
        hardcover_id (bool | Unset):
        hardcover_book_id (bool | Unset):
        hardcover_rating (bool | Unset):
        hardcover_review_count (bool | Unset):
        comicvine_id (bool | Unset):
        lubimyczytac_id (bool | Unset):
        lubimyczytac_rating (bool | Unset):
        ranobedb_id (bool | Unset):
        ranobedb_rating (bool | Unset):
        audible_id (bool | Unset):
        audible_rating (bool | Unset):
        audible_review_count (bool | Unset):
    """

    asin: bool | Unset = UNSET
    amazon_rating: bool | Unset = UNSET
    amazon_review_count: bool | Unset = UNSET
    google_id: bool | Unset = UNSET
    goodreads_id: bool | Unset = UNSET
    goodreads_rating: bool | Unset = UNSET
    goodreads_review_count: bool | Unset = UNSET
    hardcover_id: bool | Unset = UNSET
    hardcover_book_id: bool | Unset = UNSET
    hardcover_rating: bool | Unset = UNSET
    hardcover_review_count: bool | Unset = UNSET
    comicvine_id: bool | Unset = UNSET
    lubimyczytac_id: bool | Unset = UNSET
    lubimyczytac_rating: bool | Unset = UNSET
    ranobedb_id: bool | Unset = UNSET
    ranobedb_rating: bool | Unset = UNSET
    audible_id: bool | Unset = UNSET
    audible_rating: bool | Unset = UNSET
    audible_review_count: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        asin = self.asin

        amazon_rating = self.amazon_rating

        amazon_review_count = self.amazon_review_count

        google_id = self.google_id

        goodreads_id = self.goodreads_id

        goodreads_rating = self.goodreads_rating

        goodreads_review_count = self.goodreads_review_count

        hardcover_id = self.hardcover_id

        hardcover_book_id = self.hardcover_book_id

        hardcover_rating = self.hardcover_rating

        hardcover_review_count = self.hardcover_review_count

        comicvine_id = self.comicvine_id

        lubimyczytac_id = self.lubimyczytac_id

        lubimyczytac_rating = self.lubimyczytac_rating

        ranobedb_id = self.ranobedb_id

        ranobedb_rating = self.ranobedb_rating

        audible_id = self.audible_id

        audible_rating = self.audible_rating

        audible_review_count = self.audible_review_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if asin is not UNSET:
            field_dict["asin"] = asin
        if amazon_rating is not UNSET:
            field_dict["amazonRating"] = amazon_rating
        if amazon_review_count is not UNSET:
            field_dict["amazonReviewCount"] = amazon_review_count
        if google_id is not UNSET:
            field_dict["googleId"] = google_id
        if goodreads_id is not UNSET:
            field_dict["goodreadsId"] = goodreads_id
        if goodreads_rating is not UNSET:
            field_dict["goodreadsRating"] = goodreads_rating
        if goodreads_review_count is not UNSET:
            field_dict["goodreadsReviewCount"] = goodreads_review_count
        if hardcover_id is not UNSET:
            field_dict["hardcoverId"] = hardcover_id
        if hardcover_book_id is not UNSET:
            field_dict["hardcoverBookId"] = hardcover_book_id
        if hardcover_rating is not UNSET:
            field_dict["hardcoverRating"] = hardcover_rating
        if hardcover_review_count is not UNSET:
            field_dict["hardcoverReviewCount"] = hardcover_review_count
        if comicvine_id is not UNSET:
            field_dict["comicvineId"] = comicvine_id
        if lubimyczytac_id is not UNSET:
            field_dict["lubimyczytacId"] = lubimyczytac_id
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

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        asin = d.pop("asin", UNSET)

        amazon_rating = d.pop("amazonRating", UNSET)

        amazon_review_count = d.pop("amazonReviewCount", UNSET)

        google_id = d.pop("googleId", UNSET)

        goodreads_id = d.pop("goodreadsId", UNSET)

        goodreads_rating = d.pop("goodreadsRating", UNSET)

        goodreads_review_count = d.pop("goodreadsReviewCount", UNSET)

        hardcover_id = d.pop("hardcoverId", UNSET)

        hardcover_book_id = d.pop("hardcoverBookId", UNSET)

        hardcover_rating = d.pop("hardcoverRating", UNSET)

        hardcover_review_count = d.pop("hardcoverReviewCount", UNSET)

        comicvine_id = d.pop("comicvineId", UNSET)

        lubimyczytac_id = d.pop("lubimyczytacId", UNSET)

        lubimyczytac_rating = d.pop("lubimyczytacRating", UNSET)

        ranobedb_id = d.pop("ranobedbId", UNSET)

        ranobedb_rating = d.pop("ranobedbRating", UNSET)

        audible_id = d.pop("audibleId", UNSET)

        audible_rating = d.pop("audibleRating", UNSET)

        audible_review_count = d.pop("audibleReviewCount", UNSET)

        metadata_provider_specific_fields = cls(
            asin=asin,
            amazon_rating=amazon_rating,
            amazon_review_count=amazon_review_count,
            google_id=google_id,
            goodreads_id=goodreads_id,
            goodreads_rating=goodreads_rating,
            goodreads_review_count=goodreads_review_count,
            hardcover_id=hardcover_id,
            hardcover_book_id=hardcover_book_id,
            hardcover_rating=hardcover_rating,
            hardcover_review_count=hardcover_review_count,
            comicvine_id=comicvine_id,
            lubimyczytac_id=lubimyczytac_id,
            lubimyczytac_rating=lubimyczytac_rating,
            ranobedb_id=ranobedb_id,
            ranobedb_rating=ranobedb_rating,
            audible_id=audible_id,
            audible_rating=audible_rating,
            audible_review_count=audible_review_count,
        )

        metadata_provider_specific_fields.additional_properties = d
        return metadata_provider_specific_fields

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
