from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AudiobookTrack")


@_attrs_define
class AudiobookTrack:
    """
    Attributes:
        index (int | Unset):
        file_name (str | Unset):
        title (str | Unset):
        duration_ms (int | Unset):
        file_size_bytes (int | Unset):
        cumulative_start_ms (int | Unset):
    """

    index: int | Unset = UNSET
    file_name: str | Unset = UNSET
    title: str | Unset = UNSET
    duration_ms: int | Unset = UNSET
    file_size_bytes: int | Unset = UNSET
    cumulative_start_ms: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        index = self.index

        file_name = self.file_name

        title = self.title

        duration_ms = self.duration_ms

        file_size_bytes = self.file_size_bytes

        cumulative_start_ms = self.cumulative_start_ms

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if index is not UNSET:
            field_dict["index"] = index
        if file_name is not UNSET:
            field_dict["fileName"] = file_name
        if title is not UNSET:
            field_dict["title"] = title
        if duration_ms is not UNSET:
            field_dict["durationMs"] = duration_ms
        if file_size_bytes is not UNSET:
            field_dict["fileSizeBytes"] = file_size_bytes
        if cumulative_start_ms is not UNSET:
            field_dict["cumulativeStartMs"] = cumulative_start_ms

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        index = d.pop("index", UNSET)

        file_name = d.pop("fileName", UNSET)

        title = d.pop("title", UNSET)

        duration_ms = d.pop("durationMs", UNSET)

        file_size_bytes = d.pop("fileSizeBytes", UNSET)

        cumulative_start_ms = d.pop("cumulativeStartMs", UNSET)

        audiobook_track = cls(
            index=index,
            file_name=file_name,
            title=title,
            duration_ms=duration_ms,
            file_size_bytes=file_size_bytes,
            cumulative_start_ms=cumulative_start_ms,
        )

        audiobook_track.additional_properties = d
        return audiobook_track

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
