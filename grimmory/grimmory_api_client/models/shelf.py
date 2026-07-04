from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.shelf_icon_type import ShelfIconType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.sort import Sort


T = TypeVar("T", bound="Shelf")


@_attrs_define
class Shelf:
    """
    Attributes:
        id (int | Unset):
        name (str | Unset):
        icon (str | Unset):
        icon_type (ShelfIconType | Unset):
        sort (Sort | Unset):
        user_id (int | Unset):
        public_shelf (bool | Unset):
        book_count (int | Unset):
    """

    id: int | Unset = UNSET
    name: str | Unset = UNSET
    icon: str | Unset = UNSET
    icon_type: ShelfIconType | Unset = UNSET
    sort: Sort | Unset = UNSET
    user_id: int | Unset = UNSET
    public_shelf: bool | Unset = UNSET
    book_count: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        icon = self.icon

        icon_type: str | Unset = UNSET
        if not isinstance(self.icon_type, Unset):
            icon_type = self.icon_type.value

        sort: dict[str, Any] | Unset = UNSET
        if not isinstance(self.sort, Unset):
            sort = self.sort.to_dict()

        user_id = self.user_id

        public_shelf = self.public_shelf

        book_count = self.book_count

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
        if sort is not UNSET:
            field_dict["sort"] = sort
        if user_id is not UNSET:
            field_dict["userId"] = user_id
        if public_shelf is not UNSET:
            field_dict["publicShelf"] = public_shelf
        if book_count is not UNSET:
            field_dict["bookCount"] = book_count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.sort import Sort

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        icon = d.pop("icon", UNSET)

        _icon_type = d.pop("iconType", UNSET)
        icon_type: ShelfIconType | Unset
        if isinstance(_icon_type, Unset):
            icon_type = UNSET
        else:
            icon_type = ShelfIconType(_icon_type)

        _sort = d.pop("sort", UNSET)
        sort: Sort | Unset
        if isinstance(_sort, Unset):
            sort = UNSET
        else:
            sort = Sort.from_dict(_sort)

        user_id = d.pop("userId", UNSET)

        public_shelf = d.pop("publicShelf", UNSET)

        book_count = d.pop("bookCount", UNSET)

        shelf = cls(
            id=id,
            name=name,
            icon=icon,
            icon_type=icon_type,
            sort=sort,
            user_id=user_id,
            public_shelf=public_shelf,
            book_count=book_count,
        )

        shelf.additional_properties = d
        return shelf

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
