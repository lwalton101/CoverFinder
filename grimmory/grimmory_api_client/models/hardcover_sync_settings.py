from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="HardcoverSyncSettings")


@_attrs_define
class HardcoverSyncSettings:
    """
    Attributes:
        hardcover_api_key (str | Unset):
        hardcover_sync_enabled (bool | Unset):
    """

    hardcover_api_key: str | Unset = UNSET
    hardcover_sync_enabled: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        hardcover_api_key = self.hardcover_api_key

        hardcover_sync_enabled = self.hardcover_sync_enabled

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if hardcover_api_key is not UNSET:
            field_dict["hardcoverApiKey"] = hardcover_api_key
        if hardcover_sync_enabled is not UNSET:
            field_dict["hardcoverSyncEnabled"] = hardcover_sync_enabled

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        hardcover_api_key = d.pop("hardcoverApiKey", UNSET)

        hardcover_sync_enabled = d.pop("hardcoverSyncEnabled", UNSET)

        hardcover_sync_settings = cls(
            hardcover_api_key=hardcover_api_key,
            hardcover_sync_enabled=hardcover_sync_enabled,
        )

        hardcover_sync_settings.additional_properties = d
        return hardcover_sync_settings

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
