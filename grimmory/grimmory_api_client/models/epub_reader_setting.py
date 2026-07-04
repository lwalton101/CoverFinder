from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="EpubReaderSetting")


@_attrs_define
class EpubReaderSetting:
    """
    Attributes:
        theme (str | Unset):
        font (str | Unset):
        font_size (int | Unset):
        letter_spacing (float | Unset):
        line_height (float | Unset):
        flow (str | Unset):
        spread (str | Unset):
    """

    theme: str | Unset = UNSET
    font: str | Unset = UNSET
    font_size: int | Unset = UNSET
    letter_spacing: float | Unset = UNSET
    line_height: float | Unset = UNSET
    flow: str | Unset = UNSET
    spread: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        theme = self.theme

        font = self.font

        font_size = self.font_size

        letter_spacing = self.letter_spacing

        line_height = self.line_height

        flow = self.flow

        spread = self.spread

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if theme is not UNSET:
            field_dict["theme"] = theme
        if font is not UNSET:
            field_dict["font"] = font
        if font_size is not UNSET:
            field_dict["fontSize"] = font_size
        if letter_spacing is not UNSET:
            field_dict["letterSpacing"] = letter_spacing
        if line_height is not UNSET:
            field_dict["lineHeight"] = line_height
        if flow is not UNSET:
            field_dict["flow"] = flow
        if spread is not UNSET:
            field_dict["spread"] = spread

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        theme = d.pop("theme", UNSET)

        font = d.pop("font", UNSET)

        font_size = d.pop("fontSize", UNSET)

        letter_spacing = d.pop("letterSpacing", UNSET)

        line_height = d.pop("lineHeight", UNSET)

        flow = d.pop("flow", UNSET)

        spread = d.pop("spread", UNSET)

        epub_reader_setting = cls(
            theme=theme,
            font=font,
            font_size=font_size,
            letter_spacing=letter_spacing,
            line_height=line_height,
            flow=flow,
            spread=spread,
        )

        epub_reader_setting.additional_properties = d
        return epub_reader_setting

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
