from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.status_info_status import StatusInfoStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="StatusInfo")


@_attrs_define
class StatusInfo:
    """
    Attributes:
        last_modified (str | Unset):
        status (StatusInfoStatus | Unset):
        times_started_reading (int | Unset):
        last_time_started_reading (str | Unset):
        last_time_finished (str | Unset):
    """

    last_modified: str | Unset = UNSET
    status: StatusInfoStatus | Unset = UNSET
    times_started_reading: int | Unset = UNSET
    last_time_started_reading: str | Unset = UNSET
    last_time_finished: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        last_modified = self.last_modified

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        times_started_reading = self.times_started_reading

        last_time_started_reading = self.last_time_started_reading

        last_time_finished = self.last_time_finished

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if last_modified is not UNSET:
            field_dict["lastModified"] = last_modified
        if status is not UNSET:
            field_dict["status"] = status
        if times_started_reading is not UNSET:
            field_dict["timesStartedReading"] = times_started_reading
        if last_time_started_reading is not UNSET:
            field_dict["lastTimeStartedReading"] = last_time_started_reading
        if last_time_finished is not UNSET:
            field_dict["lastTimeFinished"] = last_time_finished

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        last_modified = d.pop("lastModified", UNSET)

        _status = d.pop("status", UNSET)
        status: StatusInfoStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = StatusInfoStatus(_status)

        times_started_reading = d.pop("timesStartedReading", UNSET)

        last_time_started_reading = d.pop("lastTimeStartedReading", UNSET)

        last_time_finished = d.pop("lastTimeFinished", UNSET)

        status_info = cls(
            last_modified=last_modified,
            status=status,
            times_started_reading=times_started_reading,
            last_time_started_reading=last_time_started_reading,
            last_time_finished=last_time_finished,
        )

        status_info.additional_properties = d
        return status_info

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
