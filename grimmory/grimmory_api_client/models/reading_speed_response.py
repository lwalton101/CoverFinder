from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ReadingSpeedResponse")


@_attrs_define
class ReadingSpeedResponse:
    """
    Attributes:
        date (datetime.date | Unset):
        avg_progress_per_minute (float | Unset):
        total_sessions (int | Unset):
    """

    date: datetime.date | Unset = UNSET
    avg_progress_per_minute: float | Unset = UNSET
    total_sessions: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        date: str | Unset = UNSET
        if not isinstance(self.date, Unset):
            date = self.date.isoformat()

        avg_progress_per_minute = self.avg_progress_per_minute

        total_sessions = self.total_sessions

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if date is not UNSET:
            field_dict["date"] = date
        if avg_progress_per_minute is not UNSET:
            field_dict["avgProgressPerMinute"] = avg_progress_per_minute
        if total_sessions is not UNSET:
            field_dict["totalSessions"] = total_sessions

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _date = d.pop("date", UNSET)
        date: datetime.date | Unset
        if isinstance(_date, Unset):
            date = UNSET
        else:
            date = datetime.date.fromisoformat(_date)

        avg_progress_per_minute = d.pop("avgProgressPerMinute", UNSET)

        total_sessions = d.pop("totalSessions", UNSET)

        reading_speed_response = cls(
            date=date,
            avg_progress_per_minute=avg_progress_per_minute,
            total_sessions=total_sessions,
        )

        reading_speed_response.additional_properties = d
        return reading_speed_response

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
