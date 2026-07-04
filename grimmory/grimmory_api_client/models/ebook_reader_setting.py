from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="EbookReaderSetting")


@_attrs_define
class EbookReaderSetting:
    """
    Attributes:
        font_family (str | Unset):
        font_size (int | Unset):
        gap (float | Unset):
        hyphenate (bool | Unset):
        is_dark (bool | Unset):
        justify (bool | Unset):
        line_height (float | Unset):
        max_block_size (int | Unset):
        max_column_count (int | Unset):
        max_inline_size (int | Unset):
        theme (str | Unset):
        flow (str | Unset):
    """

    font_family: str | Unset = UNSET
    font_size: int | Unset = UNSET
    gap: float | Unset = UNSET
    hyphenate: bool | Unset = UNSET
    is_dark: bool | Unset = UNSET
    justify: bool | Unset = UNSET
    line_height: float | Unset = UNSET
    max_block_size: int | Unset = UNSET
    max_column_count: int | Unset = UNSET
    max_inline_size: int | Unset = UNSET
    theme: str | Unset = UNSET
    flow: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        font_family = self.font_family

        font_size = self.font_size

        gap = self.gap

        hyphenate = self.hyphenate

        is_dark = self.is_dark

        justify = self.justify

        line_height = self.line_height

        max_block_size = self.max_block_size

        max_column_count = self.max_column_count

        max_inline_size = self.max_inline_size

        theme = self.theme

        flow = self.flow

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if font_family is not UNSET:
            field_dict["fontFamily"] = font_family
        if font_size is not UNSET:
            field_dict["fontSize"] = font_size
        if gap is not UNSET:
            field_dict["gap"] = gap
        if hyphenate is not UNSET:
            field_dict["hyphenate"] = hyphenate
        if is_dark is not UNSET:
            field_dict["isDark"] = is_dark
        if justify is not UNSET:
            field_dict["justify"] = justify
        if line_height is not UNSET:
            field_dict["lineHeight"] = line_height
        if max_block_size is not UNSET:
            field_dict["maxBlockSize"] = max_block_size
        if max_column_count is not UNSET:
            field_dict["maxColumnCount"] = max_column_count
        if max_inline_size is not UNSET:
            field_dict["maxInlineSize"] = max_inline_size
        if theme is not UNSET:
            field_dict["theme"] = theme
        if flow is not UNSET:
            field_dict["flow"] = flow

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        font_family = d.pop("fontFamily", UNSET)

        font_size = d.pop("fontSize", UNSET)

        gap = d.pop("gap", UNSET)

        hyphenate = d.pop("hyphenate", UNSET)

        is_dark = d.pop("isDark", UNSET)

        justify = d.pop("justify", UNSET)

        line_height = d.pop("lineHeight", UNSET)

        max_block_size = d.pop("maxBlockSize", UNSET)

        max_column_count = d.pop("maxColumnCount", UNSET)

        max_inline_size = d.pop("maxInlineSize", UNSET)

        theme = d.pop("theme", UNSET)

        flow = d.pop("flow", UNSET)

        ebook_reader_setting = cls(
            font_family=font_family,
            font_size=font_size,
            gap=gap,
            hyphenate=hyphenate,
            is_dark=is_dark,
            justify=justify,
            line_height=line_height,
            max_block_size=max_block_size,
            max_column_count=max_column_count,
            max_inline_size=max_inline_size,
            theme=theme,
            flow=flow,
        )

        ebook_reader_setting.additional_properties = d
        return ebook_reader_setting

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
