from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CbxPageDimension")


@_attrs_define
class CbxPageDimension:
    """
    Attributes:
        page_number (int | Unset):
        width (int | Unset):
        height (int | Unset):
        wide (bool | Unset):
    """

    page_number: int | Unset = UNSET
    width: int | Unset = UNSET
    height: int | Unset = UNSET
    wide: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        page_number = self.page_number

        width = self.width

        height = self.height

        wide = self.wide

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if page_number is not UNSET:
            field_dict["pageNumber"] = page_number
        if width is not UNSET:
            field_dict["width"] = width
        if height is not UNSET:
            field_dict["height"] = height
        if wide is not UNSET:
            field_dict["wide"] = wide

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        page_number = d.pop("pageNumber", UNSET)

        width = d.pop("width", UNSET)

        height = d.pop("height", UNSET)

        wide = d.pop("wide", UNSET)

        cbx_page_dimension = cls(
            page_number=page_number,
            width=width,
            height=height,
            wide=wide,
        )

        cbx_page_dimension.additional_properties = d
        return cbx_page_dimension

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
