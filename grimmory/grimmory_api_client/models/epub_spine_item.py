from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="EpubSpineItem")


@_attrs_define
class EpubSpineItem:
    """
    Attributes:
        idref (str | Unset):
        href (str | Unset):
        media_type (str | Unset):
        linear (bool | Unset):
    """

    idref: str | Unset = UNSET
    href: str | Unset = UNSET
    media_type: str | Unset = UNSET
    linear: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        idref = self.idref

        href = self.href

        media_type = self.media_type

        linear = self.linear

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if idref is not UNSET:
            field_dict["idref"] = idref
        if href is not UNSET:
            field_dict["href"] = href
        if media_type is not UNSET:
            field_dict["mediaType"] = media_type
        if linear is not UNSET:
            field_dict["linear"] = linear

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        idref = d.pop("idref", UNSET)

        href = d.pop("href", UNSET)

        media_type = d.pop("mediaType", UNSET)

        linear = d.pop("linear", UNSET)

        epub_spine_item = cls(
            idref=idref,
            href=href,
            media_type=media_type,
            linear=linear,
        )

        epub_spine_item.additional_properties = d
        return epub_spine_item

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
