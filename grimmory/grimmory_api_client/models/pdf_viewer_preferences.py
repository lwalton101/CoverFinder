from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PdfViewerPreferences")


@_attrs_define
class PdfViewerPreferences:
    """
    Attributes:
        book_id (int | Unset):
        zoom (str | Unset):
        spread (str | Unset):
        is_dark_theme (bool | Unset):
    """

    book_id: int | Unset = UNSET
    zoom: str | Unset = UNSET
    spread: str | Unset = UNSET
    is_dark_theme: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        book_id = self.book_id

        zoom = self.zoom

        spread = self.spread

        is_dark_theme = self.is_dark_theme

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if book_id is not UNSET:
            field_dict["bookId"] = book_id
        if zoom is not UNSET:
            field_dict["zoom"] = zoom
        if spread is not UNSET:
            field_dict["spread"] = spread
        if is_dark_theme is not UNSET:
            field_dict["isDarkTheme"] = is_dark_theme

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        book_id = d.pop("bookId", UNSET)

        zoom = d.pop("zoom", UNSET)

        spread = d.pop("spread", UNSET)

        is_dark_theme = d.pop("isDarkTheme", UNSET)

        pdf_viewer_preferences = cls(
            book_id=book_id,
            zoom=zoom,
            spread=spread,
            is_dark_theme=is_dark_theme,
        )

        pdf_viewer_preferences.additional_properties = d
        return pdf_viewer_preferences

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
