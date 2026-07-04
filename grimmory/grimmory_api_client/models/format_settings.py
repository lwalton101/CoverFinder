from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="FormatSettings")


@_attrs_define
class FormatSettings:
    """
    Attributes:
        enabled (bool | Unset):
        max_file_size_in_mb (int | Unset):
    """

    enabled: bool | Unset = UNSET
    max_file_size_in_mb: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        enabled = self.enabled

        max_file_size_in_mb = self.max_file_size_in_mb

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if max_file_size_in_mb is not UNSET:
            field_dict["maxFileSizeInMb"] = max_file_size_in_mb

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        enabled = d.pop("enabled", UNSET)

        max_file_size_in_mb = d.pop("maxFileSizeInMb", UNSET)

        format_settings = cls(
            enabled=enabled,
            max_file_size_in_mb=max_file_size_in_mb,
        )

        format_settings.additional_properties = d
        return format_settings

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
