from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ListeningHeatmapResponse")


@_attrs_define
class ListeningHeatmapResponse:
    """
    Attributes:
        date (datetime.date | Unset):
        sessions (int | Unset):
        duration_minutes (int | Unset):
    """

    date: datetime.date | Unset = UNSET
    sessions: int | Unset = UNSET
    duration_minutes: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        date: str | Unset = UNSET
        if not isinstance(self.date, Unset):
            date = self.date.isoformat()

        sessions = self.sessions

        duration_minutes = self.duration_minutes

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if date is not UNSET:
            field_dict["date"] = date
        if sessions is not UNSET:
            field_dict["sessions"] = sessions
        if duration_minutes is not UNSET:
            field_dict["durationMinutes"] = duration_minutes

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

        sessions = d.pop("sessions", UNSET)

        duration_minutes = d.pop("durationMinutes", UNSET)

        listening_heatmap_response = cls(
            date=date,
            sessions=sessions,
            duration_minutes=duration_minutes,
        )

        listening_heatmap_response.additional_properties = d
        return listening_heatmap_response

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
