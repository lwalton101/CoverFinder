from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SidecarSettings")


@_attrs_define
class SidecarSettings:
    """
    Attributes:
        enabled (bool | Unset):
        write_on_update (bool | Unset):
        write_on_scan (bool | Unset):
        include_cover_file (bool | Unset):
    """

    enabled: bool | Unset = UNSET
    write_on_update: bool | Unset = UNSET
    write_on_scan: bool | Unset = UNSET
    include_cover_file: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        enabled = self.enabled

        write_on_update = self.write_on_update

        write_on_scan = self.write_on_scan

        include_cover_file = self.include_cover_file

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if write_on_update is not UNSET:
            field_dict["writeOnUpdate"] = write_on_update
        if write_on_scan is not UNSET:
            field_dict["writeOnScan"] = write_on_scan
        if include_cover_file is not UNSET:
            field_dict["includeCoverFile"] = include_cover_file

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        enabled = d.pop("enabled", UNSET)

        write_on_update = d.pop("writeOnUpdate", UNSET)

        write_on_scan = d.pop("writeOnScan", UNSET)

        include_cover_file = d.pop("includeCoverFile", UNSET)

        sidecar_settings = cls(
            enabled=enabled,
            write_on_update=write_on_update,
            write_on_scan=write_on_scan,
            include_cover_file=include_cover_file,
        )

        sidecar_settings.additional_properties = d
        return sidecar_settings

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
