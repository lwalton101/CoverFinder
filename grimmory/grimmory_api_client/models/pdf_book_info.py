from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.pdf_outline_item import PdfOutlineItem


T = TypeVar("T", bound="PdfBookInfo")


@_attrs_define
class PdfBookInfo:
    """
    Attributes:
        page_count (int | Unset):
        outline (list[PdfOutlineItem] | Unset):
    """

    page_count: int | Unset = UNSET
    outline: list[PdfOutlineItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        page_count = self.page_count

        outline: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.outline, Unset):
            outline = []
            for outline_item_data in self.outline:
                outline_item = outline_item_data.to_dict()
                outline.append(outline_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if page_count is not UNSET:
            field_dict["pageCount"] = page_count
        if outline is not UNSET:
            field_dict["outline"] = outline

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.pdf_outline_item import PdfOutlineItem

        d = dict(src_dict)
        page_count = d.pop("pageCount", UNSET)

        _outline = d.pop("outline", UNSET)
        outline: list[PdfOutlineItem] | Unset = UNSET
        if _outline is not UNSET:
            outline = []
            for outline_item_data in _outline:
                outline_item = PdfOutlineItem.from_dict(outline_item_data)

                outline.append(outline_item)

        pdf_book_info = cls(
            page_count=page_count,
            outline=outline,
        )

        pdf_book_info.additional_properties = d
        return pdf_book_info

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
