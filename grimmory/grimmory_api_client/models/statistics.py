from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Statistics")


@_attrs_define
class Statistics:
    """
    Attributes:
        last_modified (str | Unset):
        spent_reading_minutes (int | Unset):
        remaining_time_minutes (int | Unset):
    """

    last_modified: str | Unset = UNSET
    spent_reading_minutes: int | Unset = UNSET
    remaining_time_minutes: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        last_modified = self.last_modified

        spent_reading_minutes = self.spent_reading_minutes

        remaining_time_minutes = self.remaining_time_minutes

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if last_modified is not UNSET:
            field_dict["lastModified"] = last_modified
        if spent_reading_minutes is not UNSET:
            field_dict["spentReadingMinutes"] = spent_reading_minutes
        if remaining_time_minutes is not UNSET:
            field_dict["remainingTimeMinutes"] = remaining_time_minutes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        last_modified = d.pop("lastModified", UNSET)

        spent_reading_minutes = d.pop("spentReadingMinutes", UNSET)

        remaining_time_minutes = d.pop("remainingTimeMinutes", UNSET)

        statistics = cls(
            last_modified=last_modified,
            spent_reading_minutes=spent_reading_minutes,
            remaining_time_minutes=remaining_time_minutes,
        )

        statistics.additional_properties = d
        return statistics

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
