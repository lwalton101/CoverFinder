from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="MonthlyPaceResponse")


@_attrs_define
class MonthlyPaceResponse:
    """
    Attributes:
        year (int | Unset):
        month (int | Unset):
        books_completed (int | Unset):
        total_listening_seconds (int | Unset):
    """

    year: int | Unset = UNSET
    month: int | Unset = UNSET
    books_completed: int | Unset = UNSET
    total_listening_seconds: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        year = self.year

        month = self.month

        books_completed = self.books_completed

        total_listening_seconds = self.total_listening_seconds

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if year is not UNSET:
            field_dict["year"] = year
        if month is not UNSET:
            field_dict["month"] = month
        if books_completed is not UNSET:
            field_dict["booksCompleted"] = books_completed
        if total_listening_seconds is not UNSET:
            field_dict["totalListeningSeconds"] = total_listening_seconds

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        year = d.pop("year", UNSET)

        month = d.pop("month", UNSET)

        books_completed = d.pop("booksCompleted", UNSET)

        total_listening_seconds = d.pop("totalListeningSeconds", UNSET)

        monthly_pace_response = cls(
            year=year,
            month=month,
            books_completed=books_completed,
            total_listening_seconds=total_listening_seconds,
        )

        monthly_pace_response.additional_properties = d
        return monthly_pace_response

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
