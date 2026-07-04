from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SessionScatterResponse")


@_attrs_define
class SessionScatterResponse:
    """
    Attributes:
        hour_of_day (float | Unset):
        duration_minutes (float | Unset):
        day_of_week (int | Unset):
    """

    hour_of_day: float | Unset = UNSET
    duration_minutes: float | Unset = UNSET
    day_of_week: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        hour_of_day = self.hour_of_day

        duration_minutes = self.duration_minutes

        day_of_week = self.day_of_week

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if hour_of_day is not UNSET:
            field_dict["hourOfDay"] = hour_of_day
        if duration_minutes is not UNSET:
            field_dict["durationMinutes"] = duration_minutes
        if day_of_week is not UNSET:
            field_dict["dayOfWeek"] = day_of_week

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        hour_of_day = d.pop("hourOfDay", UNSET)

        duration_minutes = d.pop("durationMinutes", UNSET)

        day_of_week = d.pop("dayOfWeek", UNSET)

        session_scatter_response = cls(
            hour_of_day=hour_of_day,
            duration_minutes=duration_minutes,
            day_of_week=day_of_week,
        )

        session_scatter_response.additional_properties = d
        return session_scatter_response

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
