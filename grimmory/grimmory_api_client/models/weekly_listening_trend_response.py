from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WeeklyListeningTrendResponse")


@_attrs_define
class WeeklyListeningTrendResponse:
    """
    Attributes:
        year (int | Unset):
        week (int | Unset):
        total_duration_seconds (int | Unset):
        sessions (int | Unset):
    """

    year: int | Unset = UNSET
    week: int | Unset = UNSET
    total_duration_seconds: int | Unset = UNSET
    sessions: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        year = self.year

        week = self.week

        total_duration_seconds = self.total_duration_seconds

        sessions = self.sessions

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if year is not UNSET:
            field_dict["year"] = year
        if week is not UNSET:
            field_dict["week"] = week
        if total_duration_seconds is not UNSET:
            field_dict["totalDurationSeconds"] = total_duration_seconds
        if sessions is not UNSET:
            field_dict["sessions"] = sessions

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        year = d.pop("year", UNSET)

        week = d.pop("week", UNSET)

        total_duration_seconds = d.pop("totalDurationSeconds", UNSET)

        sessions = d.pop("sessions", UNSET)

        weekly_listening_trend_response = cls(
            year=year,
            week=week,
            total_duration_seconds=total_duration_seconds,
            sessions=sessions,
        )

        weekly_listening_trend_response.additional_properties = d
        return weekly_listening_trend_response

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
