from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PdfOutlineItem")


@_attrs_define
class PdfOutlineItem:
    """
    Attributes:
        title (str | Unset):
        page_number (int | Unset):
        children (list[PdfOutlineItem] | Unset):
    """

    title: str | Unset = UNSET
    page_number: int | Unset = UNSET
    children: list[PdfOutlineItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        title = self.title

        page_number = self.page_number

        children: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.children, Unset):
            children = []
            for children_item_data in self.children:
                children_item = children_item_data.to_dict()
                children.append(children_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if title is not UNSET:
            field_dict["title"] = title
        if page_number is not UNSET:
            field_dict["pageNumber"] = page_number
        if children is not UNSET:
            field_dict["children"] = children

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        title = d.pop("title", UNSET)

        page_number = d.pop("pageNumber", UNSET)

        _children = d.pop("children", UNSET)
        children: list[PdfOutlineItem] | Unset = UNSET
        if _children is not UNSET:
            children = []
            for children_item_data in _children:
                children_item = PdfOutlineItem.from_dict(children_item_data)

                children.append(children_item)

        pdf_outline_item = cls(
            title=title,
            page_number=page_number,
            children=children,
        )

        pdf_outline_item.additional_properties = d
        return pdf_outline_item

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
