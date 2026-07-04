from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PdfReaderSetting")


@_attrs_define
class PdfReaderSetting:
    """
    Attributes:
        page_spread (str | Unset):
        page_zoom (str | Unset):
        scroll_layout (str | Unset):
    """

    page_spread: str | Unset = UNSET
    page_zoom: str | Unset = UNSET
    scroll_layout: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        page_spread = self.page_spread

        page_zoom = self.page_zoom

        scroll_layout = self.scroll_layout

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if page_spread is not UNSET:
            field_dict["pageSpread"] = page_spread
        if page_zoom is not UNSET:
            field_dict["pageZoom"] = page_zoom
        if scroll_layout is not UNSET:
            field_dict["scrollLayout"] = scroll_layout

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        page_spread = d.pop("pageSpread", UNSET)

        page_zoom = d.pop("pageZoom", UNSET)

        scroll_layout = d.pop("scrollLayout", UNSET)

        pdf_reader_setting = cls(
            page_spread=page_spread,
            page_zoom=page_zoom,
            scroll_layout=scroll_layout,
        )

        pdf_reader_setting.additional_properties = d
        return pdf_reader_setting

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
