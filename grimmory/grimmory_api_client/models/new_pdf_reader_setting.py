from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.new_pdf_reader_setting_background_color import NewPdfReaderSettingBackgroundColor
from ..models.new_pdf_reader_setting_fit_mode import NewPdfReaderSettingFitMode
from ..models.new_pdf_reader_setting_page_spread import NewPdfReaderSettingPageSpread
from ..models.new_pdf_reader_setting_page_view_mode import NewPdfReaderSettingPageViewMode
from ..models.new_pdf_reader_setting_scroll_mode import NewPdfReaderSettingScrollMode
from ..types import UNSET, Unset

T = TypeVar("T", bound="NewPdfReaderSetting")


@_attrs_define
class NewPdfReaderSetting:
    """
    Attributes:
        page_spread (NewPdfReaderSettingPageSpread | Unset):
        page_view_mode (NewPdfReaderSettingPageViewMode | Unset):
        background_color (NewPdfReaderSettingBackgroundColor | Unset):
        fit_mode (NewPdfReaderSettingFitMode | Unset):
        scroll_mode (NewPdfReaderSettingScrollMode | Unset):
    """

    page_spread: NewPdfReaderSettingPageSpread | Unset = UNSET
    page_view_mode: NewPdfReaderSettingPageViewMode | Unset = UNSET
    background_color: NewPdfReaderSettingBackgroundColor | Unset = UNSET
    fit_mode: NewPdfReaderSettingFitMode | Unset = UNSET
    scroll_mode: NewPdfReaderSettingScrollMode | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        page_spread: str | Unset = UNSET
        if not isinstance(self.page_spread, Unset):
            page_spread = self.page_spread.value

        page_view_mode: str | Unset = UNSET
        if not isinstance(self.page_view_mode, Unset):
            page_view_mode = self.page_view_mode.value

        background_color: str | Unset = UNSET
        if not isinstance(self.background_color, Unset):
            background_color = self.background_color.value

        fit_mode: str | Unset = UNSET
        if not isinstance(self.fit_mode, Unset):
            fit_mode = self.fit_mode.value

        scroll_mode: str | Unset = UNSET
        if not isinstance(self.scroll_mode, Unset):
            scroll_mode = self.scroll_mode.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if page_spread is not UNSET:
            field_dict["pageSpread"] = page_spread
        if page_view_mode is not UNSET:
            field_dict["pageViewMode"] = page_view_mode
        if background_color is not UNSET:
            field_dict["backgroundColor"] = background_color
        if fit_mode is not UNSET:
            field_dict["fitMode"] = fit_mode
        if scroll_mode is not UNSET:
            field_dict["scrollMode"] = scroll_mode

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _page_spread = d.pop("pageSpread", UNSET)
        page_spread: NewPdfReaderSettingPageSpread | Unset
        if isinstance(_page_spread, Unset):
            page_spread = UNSET
        else:
            page_spread = NewPdfReaderSettingPageSpread(_page_spread)

        _page_view_mode = d.pop("pageViewMode", UNSET)
        page_view_mode: NewPdfReaderSettingPageViewMode | Unset
        if isinstance(_page_view_mode, Unset):
            page_view_mode = UNSET
        else:
            page_view_mode = NewPdfReaderSettingPageViewMode(_page_view_mode)

        _background_color = d.pop("backgroundColor", UNSET)
        background_color: NewPdfReaderSettingBackgroundColor | Unset
        if isinstance(_background_color, Unset):
            background_color = UNSET
        else:
            background_color = NewPdfReaderSettingBackgroundColor(_background_color)

        _fit_mode = d.pop("fitMode", UNSET)
        fit_mode: NewPdfReaderSettingFitMode | Unset
        if isinstance(_fit_mode, Unset):
            fit_mode = UNSET
        else:
            fit_mode = NewPdfReaderSettingFitMode(_fit_mode)

        _scroll_mode = d.pop("scrollMode", UNSET)
        scroll_mode: NewPdfReaderSettingScrollMode | Unset
        if isinstance(_scroll_mode, Unset):
            scroll_mode = UNSET
        else:
            scroll_mode = NewPdfReaderSettingScrollMode(_scroll_mode)

        new_pdf_reader_setting = cls(
            page_spread=page_spread,
            page_view_mode=page_view_mode,
            background_color=background_color,
            fit_mode=fit_mode,
            scroll_mode=scroll_mode,
        )

        new_pdf_reader_setting.additional_properties = d
        return new_pdf_reader_setting

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
