from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AppMagicShelfSummary")


@_attrs_define
class AppMagicShelfSummary:
    """
    Attributes:
        id (int | Unset):
        name (str | Unset):
        icon (str | Unset):
        icon_type (str | Unset):
        public_shelf (bool | Unset):
    """

    id: int | Unset = UNSET
    name: str | Unset = UNSET
    icon: str | Unset = UNSET
    icon_type: str | Unset = UNSET
    public_shelf: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        icon = self.icon

        icon_type = self.icon_type

        public_shelf = self.public_shelf

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if icon is not UNSET:
            field_dict["icon"] = icon
        if icon_type is not UNSET:
            field_dict["iconType"] = icon_type
        if public_shelf is not UNSET:
            field_dict["publicShelf"] = public_shelf

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        icon = d.pop("icon", UNSET)

        icon_type = d.pop("iconType", UNSET)

        public_shelf = d.pop("publicShelf", UNSET)

        app_magic_shelf_summary = cls(
            id=id,
            name=name,
            icon=icon,
            icon_type=icon_type,
            public_shelf=public_shelf,
        )

        app_magic_shelf_summary.additional_properties = d
        return app_magic_shelf_summary

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
