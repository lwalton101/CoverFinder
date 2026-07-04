from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="FavoriteReadingDaysResponse")


@_attrs_define
class FavoriteReadingDaysResponse:
    """
    Attributes:
        day_of_week (int | Unset):
        day_name (str | Unset):
        session_count (int | Unset):
        total_duration_seconds (int | Unset):
    """

    day_of_week: int | Unset = UNSET
    day_name: str | Unset = UNSET
    session_count: int | Unset = UNSET
    total_duration_seconds: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        day_of_week = self.day_of_week

        day_name = self.day_name

        session_count = self.session_count

        total_duration_seconds = self.total_duration_seconds

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if day_of_week is not UNSET:
            field_dict["dayOfWeek"] = day_of_week
        if day_name is not UNSET:
            field_dict["dayName"] = day_name
        if session_count is not UNSET:
            field_dict["sessionCount"] = session_count
        if total_duration_seconds is not UNSET:
            field_dict["totalDurationSeconds"] = total_duration_seconds

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        day_of_week = d.pop("dayOfWeek", UNSET)

        day_name = d.pop("dayName", UNSET)

        session_count = d.pop("sessionCount", UNSET)

        total_duration_seconds = d.pop("totalDurationSeconds", UNSET)

        favorite_reading_days_response = cls(
            day_of_week=day_of_week,
            day_name=day_name,
            session_count=session_count,
            total_duration_seconds=total_duration_seconds,
        )

        favorite_reading_days_response.additional_properties = d
        return favorite_reading_days_response

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
