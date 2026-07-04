from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SidecarIdentifiers")


@_attrs_define
class SidecarIdentifiers:
    """
    Attributes:
        asin (str | Unset):
        goodreads_id (str | Unset):
        google_id (str | Unset):
        hardcover_id (str | Unset):
        hardcover_book_id (str | Unset):
        comicvine_id (str | Unset):
        lubimyczytac_id (str | Unset):
        ranobedb_id (str | Unset):
        audible_id (str | Unset):
    """

    asin: str | Unset = UNSET
    goodreads_id: str | Unset = UNSET
    google_id: str | Unset = UNSET
    hardcover_id: str | Unset = UNSET
    hardcover_book_id: str | Unset = UNSET
    comicvine_id: str | Unset = UNSET
    lubimyczytac_id: str | Unset = UNSET
    ranobedb_id: str | Unset = UNSET
    audible_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        asin = self.asin

        goodreads_id = self.goodreads_id

        google_id = self.google_id

        hardcover_id = self.hardcover_id

        hardcover_book_id = self.hardcover_book_id

        comicvine_id = self.comicvine_id

        lubimyczytac_id = self.lubimyczytac_id

        ranobedb_id = self.ranobedb_id

        audible_id = self.audible_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if asin is not UNSET:
            field_dict["asin"] = asin
        if goodreads_id is not UNSET:
            field_dict["goodreadsId"] = goodreads_id
        if google_id is not UNSET:
            field_dict["googleId"] = google_id
        if hardcover_id is not UNSET:
            field_dict["hardcoverId"] = hardcover_id
        if hardcover_book_id is not UNSET:
            field_dict["hardcoverBookId"] = hardcover_book_id
        if comicvine_id is not UNSET:
            field_dict["comicvineId"] = comicvine_id
        if lubimyczytac_id is not UNSET:
            field_dict["lubimyczytacId"] = lubimyczytac_id
        if ranobedb_id is not UNSET:
            field_dict["ranobedbId"] = ranobedb_id
        if audible_id is not UNSET:
            field_dict["audibleId"] = audible_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        asin = d.pop("asin", UNSET)

        goodreads_id = d.pop("goodreadsId", UNSET)

        google_id = d.pop("googleId", UNSET)

        hardcover_id = d.pop("hardcoverId", UNSET)

        hardcover_book_id = d.pop("hardcoverBookId", UNSET)

        comicvine_id = d.pop("comicvineId", UNSET)

        lubimyczytac_id = d.pop("lubimyczytacId", UNSET)

        ranobedb_id = d.pop("ranobedbId", UNSET)

        audible_id = d.pop("audibleId", UNSET)

        sidecar_identifiers = cls(
            asin=asin,
            goodreads_id=goodreads_id,
            google_id=google_id,
            hardcover_id=hardcover_id,
            hardcover_book_id=hardcover_book_id,
            comicvine_id=comicvine_id,
            lubimyczytac_id=lubimyczytac_id,
            ranobedb_id=ranobedb_id,
            audible_id=audible_id,
        )

        sidecar_identifiers.additional_properties = d
        return sidecar_identifiers

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
