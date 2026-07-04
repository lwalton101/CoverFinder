from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ChapterInfo")


@_attrs_define
class ChapterInfo:
    """
    Attributes:
        index (int | Unset):
        title (str | Unset):
        start_time_ms (int | Unset):
        end_time_ms (int | Unset):
        duration_ms (int | Unset):
    """

    index: int | Unset = UNSET
    title: str | Unset = UNSET
    start_time_ms: int | Unset = UNSET
    end_time_ms: int | Unset = UNSET
    duration_ms: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        index = self.index

        title = self.title

        start_time_ms = self.start_time_ms

        end_time_ms = self.end_time_ms

        duration_ms = self.duration_ms

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if index is not UNSET:
            field_dict["index"] = index
        if title is not UNSET:
            field_dict["title"] = title
        if start_time_ms is not UNSET:
            field_dict["startTimeMs"] = start_time_ms
        if end_time_ms is not UNSET:
            field_dict["endTimeMs"] = end_time_ms
        if duration_ms is not UNSET:
            field_dict["durationMs"] = duration_ms

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        index = d.pop("index", UNSET)

        title = d.pop("title", UNSET)

        start_time_ms = d.pop("startTimeMs", UNSET)

        end_time_ms = d.pop("endTimeMs", UNSET)

        duration_ms = d.pop("durationMs", UNSET)

        chapter_info = cls(
            index=index,
            title=title,
            start_time_ms=start_time_ms,
            end_time_ms=end_time_ms,
            duration_ms=duration_ms,
        )

        chapter_info.additional_properties = d
        return chapter_info

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
