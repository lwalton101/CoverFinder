from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ScrollerConfig")


@_attrs_define
class ScrollerConfig:
    """
    Attributes:
        id (str | Unset):
        type_ (str | Unset):
        title (str | Unset):
        enabled (bool | Unset):
        order (int | Unset):
        max_items (int | Unset):
        magic_shelf_id (int | Unset):
        sort_field (str | Unset):
        sort_direction (str | Unset):
    """

    id: str | Unset = UNSET
    type_: str | Unset = UNSET
    title: str | Unset = UNSET
    enabled: bool | Unset = UNSET
    order: int | Unset = UNSET
    max_items: int | Unset = UNSET
    magic_shelf_id: int | Unset = UNSET
    sort_field: str | Unset = UNSET
    sort_direction: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        type_ = self.type_

        title = self.title

        enabled = self.enabled

        order = self.order

        max_items = self.max_items

        magic_shelf_id = self.magic_shelf_id

        sort_field = self.sort_field

        sort_direction = self.sort_direction

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if type_ is not UNSET:
            field_dict["type"] = type_
        if title is not UNSET:
            field_dict["title"] = title
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if order is not UNSET:
            field_dict["order"] = order
        if max_items is not UNSET:
            field_dict["maxItems"] = max_items
        if magic_shelf_id is not UNSET:
            field_dict["magicShelfId"] = magic_shelf_id
        if sort_field is not UNSET:
            field_dict["sortField"] = sort_field
        if sort_direction is not UNSET:
            field_dict["sortDirection"] = sort_direction

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        type_ = d.pop("type", UNSET)

        title = d.pop("title", UNSET)

        enabled = d.pop("enabled", UNSET)

        order = d.pop("order", UNSET)

        max_items = d.pop("maxItems", UNSET)

        magic_shelf_id = d.pop("magicShelfId", UNSET)

        sort_field = d.pop("sortField", UNSET)

        sort_direction = d.pop("sortDirection", UNSET)

        scroller_config = cls(
            id=id,
            type_=type_,
            title=title,
            enabled=enabled,
            order=order,
            max_items=max_items,
            magic_shelf_id=magic_shelf_id,
            sort_field=sort_field,
            sort_direction=sort_direction,
        )

        scroller_config.additional_properties = d
        return scroller_config

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
