from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ContentDisposition")


@_attrs_define
class ContentDisposition:
    """
    Attributes:
        type_ (str | Unset):
        name (str | Unset):
        filename (str | Unset):
        charset (str | Unset):
        attachment (bool | Unset):
        form_data (bool | Unset):
        inline (bool | Unset):
    """

    type_: str | Unset = UNSET
    name: str | Unset = UNSET
    filename: str | Unset = UNSET
    charset: str | Unset = UNSET
    attachment: bool | Unset = UNSET
    form_data: bool | Unset = UNSET
    inline: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        name = self.name

        filename = self.filename

        charset = self.charset

        attachment = self.attachment

        form_data = self.form_data

        inline = self.inline

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type_ is not UNSET:
            field_dict["type"] = type_
        if name is not UNSET:
            field_dict["name"] = name
        if filename is not UNSET:
            field_dict["filename"] = filename
        if charset is not UNSET:
            field_dict["charset"] = charset
        if attachment is not UNSET:
            field_dict["attachment"] = attachment
        if form_data is not UNSET:
            field_dict["formData"] = form_data
        if inline is not UNSET:
            field_dict["inline"] = inline

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = d.pop("type", UNSET)

        name = d.pop("name", UNSET)

        filename = d.pop("filename", UNSET)

        charset = d.pop("charset", UNSET)

        attachment = d.pop("attachment", UNSET)

        form_data = d.pop("formData", UNSET)

        inline = d.pop("inline", UNSET)

        content_disposition = cls(
            type_=type_,
            name=name,
            filename=filename,
            charset=charset,
            attachment=attachment,
            form_data=form_data,
            inline=inline,
        )

        content_disposition.additional_properties = d
        return content_disposition

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
