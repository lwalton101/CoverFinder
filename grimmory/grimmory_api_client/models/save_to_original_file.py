from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.format_settings import FormatSettings


T = TypeVar("T", bound="SaveToOriginalFile")


@_attrs_define
class SaveToOriginalFile:
    """
    Attributes:
        epub (FormatSettings | Unset):
        pdf (FormatSettings | Unset):
        cbx (FormatSettings | Unset):
        audiobook (FormatSettings | Unset):
        any_format_enabled (bool | Unset):
    """

    epub: FormatSettings | Unset = UNSET
    pdf: FormatSettings | Unset = UNSET
    cbx: FormatSettings | Unset = UNSET
    audiobook: FormatSettings | Unset = UNSET
    any_format_enabled: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        epub: dict[str, Any] | Unset = UNSET
        if not isinstance(self.epub, Unset):
            epub = self.epub.to_dict()

        pdf: dict[str, Any] | Unset = UNSET
        if not isinstance(self.pdf, Unset):
            pdf = self.pdf.to_dict()

        cbx: dict[str, Any] | Unset = UNSET
        if not isinstance(self.cbx, Unset):
            cbx = self.cbx.to_dict()

        audiobook: dict[str, Any] | Unset = UNSET
        if not isinstance(self.audiobook, Unset):
            audiobook = self.audiobook.to_dict()

        any_format_enabled = self.any_format_enabled

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if epub is not UNSET:
            field_dict["epub"] = epub
        if pdf is not UNSET:
            field_dict["pdf"] = pdf
        if cbx is not UNSET:
            field_dict["cbx"] = cbx
        if audiobook is not UNSET:
            field_dict["audiobook"] = audiobook
        if any_format_enabled is not UNSET:
            field_dict["anyFormatEnabled"] = any_format_enabled

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.format_settings import FormatSettings

        d = dict(src_dict)
        _epub = d.pop("epub", UNSET)
        epub: FormatSettings | Unset
        if isinstance(_epub, Unset):
            epub = UNSET
        else:
            epub = FormatSettings.from_dict(_epub)

        _pdf = d.pop("pdf", UNSET)
        pdf: FormatSettings | Unset
        if isinstance(_pdf, Unset):
            pdf = UNSET
        else:
            pdf = FormatSettings.from_dict(_pdf)

        _cbx = d.pop("cbx", UNSET)
        cbx: FormatSettings | Unset
        if isinstance(_cbx, Unset):
            cbx = UNSET
        else:
            cbx = FormatSettings.from_dict(_cbx)

        _audiobook = d.pop("audiobook", UNSET)
        audiobook: FormatSettings | Unset
        if isinstance(_audiobook, Unset):
            audiobook = UNSET
        else:
            audiobook = FormatSettings.from_dict(_audiobook)

        any_format_enabled = d.pop("anyFormatEnabled", UNSET)

        save_to_original_file = cls(
            epub=epub,
            pdf=pdf,
            cbx=cbx,
            audiobook=audiobook,
            any_format_enabled=any_format_enabled,
        )

        save_to_original_file.additional_properties = d
        return save_to_original_file

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
