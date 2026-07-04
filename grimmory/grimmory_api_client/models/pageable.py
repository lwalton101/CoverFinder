from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Pageable")


@_attrs_define
class Pageable:
    """
    Attributes:
        page (int | Unset):
        size (int | Unset):
        sort (list[str] | Unset):
    """

    page: int | Unset = UNSET
    size: int | Unset = UNSET
    sort: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        page = self.page

        size = self.size

        sort: list[str] | Unset = UNSET
        if not isinstance(self.sort, Unset):
            sort = self.sort

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if page is not UNSET:
            field_dict["page"] = page
        if size is not UNSET:
            field_dict["size"] = size
        if sort is not UNSET:
            field_dict["sort"] = sort

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        page = d.pop("page", UNSET)

        size = d.pop("size", UNSET)

        sort = cast(list[str], d.pop("sort", UNSET))

        pageable = cls(
            page=page,
            size=size,
            sort=sort,
        )

        pageable.additional_properties = d
        return pageable

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
