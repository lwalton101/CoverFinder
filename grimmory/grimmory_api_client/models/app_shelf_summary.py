from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AppShelfSummary")


@_attrs_define
class AppShelfSummary:
    """
    Attributes:
        id (int | Unset):
        name (str | Unset):
        icon (str | Unset):
        book_count (int | Unset):
        public_shelf (bool | Unset):
    """

    id: int | Unset = UNSET
    name: str | Unset = UNSET
    icon: str | Unset = UNSET
    book_count: int | Unset = UNSET
    public_shelf: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        icon = self.icon

        book_count = self.book_count

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
        if book_count is not UNSET:
            field_dict["bookCount"] = book_count
        if public_shelf is not UNSET:
            field_dict["publicShelf"] = public_shelf

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        icon = d.pop("icon", UNSET)

        book_count = d.pop("bookCount", UNSET)

        public_shelf = d.pop("publicShelf", UNSET)

        app_shelf_summary = cls(
            id=id,
            name=name,
            icon=icon,
            book_count=book_count,
            public_shelf=public_shelf,
        )

        app_shelf_summary.additional_properties = d
        return app_shelf_summary

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
