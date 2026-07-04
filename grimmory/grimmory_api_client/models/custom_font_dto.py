from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.custom_font_dto_format import CustomFontDtoFormat
from ..types import UNSET, Unset

T = TypeVar("T", bound="CustomFontDto")


@_attrs_define
class CustomFontDto:
    """
    Attributes:
        id (int | Unset):
        font_name (str | Unset):
        original_file_name (str | Unset):
        format_ (CustomFontDtoFormat | Unset):
        file_size (int | Unset):
        uploaded_at (datetime.datetime | Unset):
    """

    id: int | Unset = UNSET
    font_name: str | Unset = UNSET
    original_file_name: str | Unset = UNSET
    format_: CustomFontDtoFormat | Unset = UNSET
    file_size: int | Unset = UNSET
    uploaded_at: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        font_name = self.font_name

        original_file_name = self.original_file_name

        format_: str | Unset = UNSET
        if not isinstance(self.format_, Unset):
            format_ = self.format_.value

        file_size = self.file_size

        uploaded_at: str | Unset = UNSET
        if not isinstance(self.uploaded_at, Unset):
            uploaded_at = self.uploaded_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if font_name is not UNSET:
            field_dict["fontName"] = font_name
        if original_file_name is not UNSET:
            field_dict["originalFileName"] = original_file_name
        if format_ is not UNSET:
            field_dict["format"] = format_
        if file_size is not UNSET:
            field_dict["fileSize"] = file_size
        if uploaded_at is not UNSET:
            field_dict["uploadedAt"] = uploaded_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        font_name = d.pop("fontName", UNSET)

        original_file_name = d.pop("originalFileName", UNSET)

        _format_ = d.pop("format", UNSET)
        format_: CustomFontDtoFormat | Unset
        if isinstance(_format_, Unset):
            format_ = UNSET
        else:
            format_ = CustomFontDtoFormat(_format_)

        file_size = d.pop("fileSize", UNSET)

        _uploaded_at = d.pop("uploadedAt", UNSET)
        uploaded_at: datetime.datetime | Unset
        if isinstance(_uploaded_at, Unset):
            uploaded_at = UNSET
        else:
            uploaded_at = datetime.datetime.fromisoformat(_uploaded_at)

        custom_font_dto = cls(
            id=id,
            font_name=font_name,
            original_file_name=original_file_name,
            format_=format_,
            file_size=file_size,
            uploaded_at=uploaded_at,
        )

        custom_font_dto.additional_properties = d
        return custom_font_dto

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
