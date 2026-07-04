from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SeriesCoverBook")


@_attrs_define
class SeriesCoverBook:
    """
    Attributes:
        book_id (int | Unset):
        cover_updated_on (datetime.datetime | Unset):
        series_number (float | Unset):
        primary_file_type (str | Unset):
    """

    book_id: int | Unset = UNSET
    cover_updated_on: datetime.datetime | Unset = UNSET
    series_number: float | Unset = UNSET
    primary_file_type: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        book_id = self.book_id

        cover_updated_on: str | Unset = UNSET
        if not isinstance(self.cover_updated_on, Unset):
            cover_updated_on = self.cover_updated_on.isoformat()

        series_number = self.series_number

        primary_file_type = self.primary_file_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if book_id is not UNSET:
            field_dict["bookId"] = book_id
        if cover_updated_on is not UNSET:
            field_dict["coverUpdatedOn"] = cover_updated_on
        if series_number is not UNSET:
            field_dict["seriesNumber"] = series_number
        if primary_file_type is not UNSET:
            field_dict["primaryFileType"] = primary_file_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        book_id = d.pop("bookId", UNSET)

        _cover_updated_on = d.pop("coverUpdatedOn", UNSET)
        cover_updated_on: datetime.datetime | Unset
        if isinstance(_cover_updated_on, Unset):
            cover_updated_on = UNSET
        else:
            cover_updated_on = datetime.datetime.fromisoformat(_cover_updated_on)

        series_number = d.pop("seriesNumber", UNSET)

        primary_file_type = d.pop("primaryFileType", UNSET)

        series_cover_book = cls(
            book_id=book_id,
            cover_updated_on=cover_updated_on,
            series_number=series_number,
            primary_file_type=primary_file_type,
        )

        series_cover_book.additional_properties = d
        return series_cover_book

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
