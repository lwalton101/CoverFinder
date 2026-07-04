from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CoverCroppingSettings")


@_attrs_define
class CoverCroppingSettings:
    """
    Attributes:
        vertical_cropping_enabled (bool | Unset):
        horizontal_cropping_enabled (bool | Unset):
        aspect_ratio_threshold (float | Unset):
        smart_cropping_enabled (bool | Unset):
    """

    vertical_cropping_enabled: bool | Unset = UNSET
    horizontal_cropping_enabled: bool | Unset = UNSET
    aspect_ratio_threshold: float | Unset = UNSET
    smart_cropping_enabled: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        vertical_cropping_enabled = self.vertical_cropping_enabled

        horizontal_cropping_enabled = self.horizontal_cropping_enabled

        aspect_ratio_threshold = self.aspect_ratio_threshold

        smart_cropping_enabled = self.smart_cropping_enabled

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if vertical_cropping_enabled is not UNSET:
            field_dict["verticalCroppingEnabled"] = vertical_cropping_enabled
        if horizontal_cropping_enabled is not UNSET:
            field_dict["horizontalCroppingEnabled"] = horizontal_cropping_enabled
        if aspect_ratio_threshold is not UNSET:
            field_dict["aspectRatioThreshold"] = aspect_ratio_threshold
        if smart_cropping_enabled is not UNSET:
            field_dict["smartCroppingEnabled"] = smart_cropping_enabled

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        vertical_cropping_enabled = d.pop("verticalCroppingEnabled", UNSET)

        horizontal_cropping_enabled = d.pop("horizontalCroppingEnabled", UNSET)

        aspect_ratio_threshold = d.pop("aspectRatioThreshold", UNSET)

        smart_cropping_enabled = d.pop("smartCroppingEnabled", UNSET)

        cover_cropping_settings = cls(
            vertical_cropping_enabled=vertical_cropping_enabled,
            horizontal_cropping_enabled=horizontal_cropping_enabled,
            aspect_ratio_threshold=aspect_ratio_threshold,
            smart_cropping_enabled=smart_cropping_enabled,
        )

        cover_cropping_settings.additional_properties = d
        return cover_cropping_settings

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
