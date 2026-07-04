from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.magic_shelf_icon_type import MagicShelfIconType
from ..types import UNSET, Unset

T = TypeVar("T", bound="MagicShelf")


@_attrs_define
class MagicShelf:
    """Magic shelf object

    Attributes:
        name (str):
        filter_json (str):
        id (int | Unset):
        icon (str | Unset):
        icon_type (MagicShelfIconType | Unset):
        is_public (bool | Unset):
    """

    name: str
    filter_json: str
    id: int | Unset = UNSET
    icon: str | Unset = UNSET
    icon_type: MagicShelfIconType | Unset = UNSET
    is_public: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        filter_json = self.filter_json

        id = self.id

        icon = self.icon

        icon_type: str | Unset = UNSET
        if not isinstance(self.icon_type, Unset):
            icon_type = self.icon_type.value

        is_public = self.is_public

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "filterJson": filter_json,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if icon is not UNSET:
            field_dict["icon"] = icon
        if icon_type is not UNSET:
            field_dict["iconType"] = icon_type
        if is_public is not UNSET:
            field_dict["isPublic"] = is_public

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        filter_json = d.pop("filterJson")

        id = d.pop("id", UNSET)

        icon = d.pop("icon", UNSET)

        _icon_type = d.pop("iconType", UNSET)
        icon_type: MagicShelfIconType | Unset
        if isinstance(_icon_type, Unset):
            icon_type = UNSET
        else:
            icon_type = MagicShelfIconType(_icon_type)

        is_public = d.pop("isPublic", UNSET)

        magic_shelf = cls(
            name=name,
            filter_json=filter_json,
            id=id,
            icon=icon,
            icon_type=icon_type,
            is_public=is_public,
        )

        magic_shelf.additional_properties = d
        return magic_shelf

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
