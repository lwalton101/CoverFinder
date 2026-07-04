from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AudiobookProgress")


@_attrs_define
class AudiobookProgress:
    """
    Attributes:
        position_ms (int):
        percentage (float):
        track_index (int | Unset):
        track_position_ms (int | Unset):
    """

    position_ms: int
    percentage: float
    track_index: int | Unset = UNSET
    track_position_ms: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        position_ms = self.position_ms

        percentage = self.percentage

        track_index = self.track_index

        track_position_ms = self.track_position_ms

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "positionMs": position_ms,
                "percentage": percentage,
            }
        )
        if track_index is not UNSET:
            field_dict["trackIndex"] = track_index
        if track_position_ms is not UNSET:
            field_dict["trackPositionMs"] = track_position_ms

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        position_ms = d.pop("positionMs")

        percentage = d.pop("percentage")

        track_index = d.pop("trackIndex", UNSET)

        track_position_ms = d.pop("trackPositionMs", UNSET)

        audiobook_progress = cls(
            position_ms=position_ms,
            percentage=percentage,
            track_index=track_index,
            track_position_ms=track_position_ms,
        )

        audiobook_progress.additional_properties = d
        return audiobook_progress

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
