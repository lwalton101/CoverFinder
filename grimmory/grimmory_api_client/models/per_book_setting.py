from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.per_book_setting_cbx import PerBookSettingCbx
from ..models.per_book_setting_epub import PerBookSettingEpub
from ..models.per_book_setting_new_pdf import PerBookSettingNewPdf
from ..models.per_book_setting_pdf import PerBookSettingPdf
from ..types import UNSET, Unset

T = TypeVar("T", bound="PerBookSetting")


@_attrs_define
class PerBookSetting:
    """
    Attributes:
        pdf (PerBookSettingPdf | Unset):
        epub (PerBookSettingEpub | Unset):
        cbx (PerBookSettingCbx | Unset):
        new_pdf (PerBookSettingNewPdf | Unset):
    """

    pdf: PerBookSettingPdf | Unset = UNSET
    epub: PerBookSettingEpub | Unset = UNSET
    cbx: PerBookSettingCbx | Unset = UNSET
    new_pdf: PerBookSettingNewPdf | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        pdf: str | Unset = UNSET
        if not isinstance(self.pdf, Unset):
            pdf = self.pdf.value

        epub: str | Unset = UNSET
        if not isinstance(self.epub, Unset):
            epub = self.epub.value

        cbx: str | Unset = UNSET
        if not isinstance(self.cbx, Unset):
            cbx = self.cbx.value

        new_pdf: str | Unset = UNSET
        if not isinstance(self.new_pdf, Unset):
            new_pdf = self.new_pdf.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if pdf is not UNSET:
            field_dict["pdf"] = pdf
        if epub is not UNSET:
            field_dict["epub"] = epub
        if cbx is not UNSET:
            field_dict["cbx"] = cbx
        if new_pdf is not UNSET:
            field_dict["newPdf"] = new_pdf

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _pdf = d.pop("pdf", UNSET)
        pdf: PerBookSettingPdf | Unset
        if isinstance(_pdf, Unset):
            pdf = UNSET
        else:
            pdf = PerBookSettingPdf(_pdf)

        _epub = d.pop("epub", UNSET)
        epub: PerBookSettingEpub | Unset
        if isinstance(_epub, Unset):
            epub = UNSET
        else:
            epub = PerBookSettingEpub(_epub)

        _cbx = d.pop("cbx", UNSET)
        cbx: PerBookSettingCbx | Unset
        if isinstance(_cbx, Unset):
            cbx = UNSET
        else:
            cbx = PerBookSettingCbx(_cbx)

        _new_pdf = d.pop("newPdf", UNSET)
        new_pdf: PerBookSettingNewPdf | Unset
        if isinstance(_new_pdf, Unset):
            new_pdf = UNSET
        else:
            new_pdf = PerBookSettingNewPdf(_new_pdf)

        per_book_setting = cls(
            pdf=pdf,
            epub=epub,
            cbx=cbx,
            new_pdf=new_pdf,
        )

        per_book_setting.additional_properties = d
        return per_book_setting

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
