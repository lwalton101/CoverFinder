from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.shelf_create_request_icon_type import ShelfCreateRequestIconType
from ..types import UNSET, Unset

T = TypeVar("T", bound="ShelfCreateRequest")


@_attrs_define
class ShelfCreateRequest:
    """Shelf creation request

    Attributes:
        name (str):
        id (int | Unset):
        icon (str | Unset):
        icon_type (ShelfCreateRequestIconType | Unset):
        public_shelf (bool | Unset):
    """

    name: str
    id: int | Unset = UNSET
    icon: str | Unset = UNSET
    icon_type: ShelfCreateRequestIconType | Unset = UNSET
    public_shelf: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        id = self.id

        icon = self.icon

        icon_type: str | Unset = UNSET
        if not isinstance(self.icon_type, Unset):
            icon_type = self.icon_type.value

        public_shelf = self.public_shelf

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
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
        name = d.pop("name")

        id = d.pop("id", UNSET)

        icon = d.pop("icon", UNSET)

        _icon_type = d.pop("iconType", UNSET)
        icon_type: ShelfCreateRequestIconType | Unset
        if isinstance(_icon_type, Unset):
            icon_type = UNSET
        else:
            icon_type = ShelfCreateRequestIconType(_icon_type)

        public_shelf = d.pop("publicShelf", UNSET)

        shelf_create_request = cls(
            name=name,
            id=id,
            icon=icon,
            icon_type=icon_type,
            public_shelf=public_shelf,
        )

        shelf_create_request.additional_properties = d
        return shelf_create_request

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
