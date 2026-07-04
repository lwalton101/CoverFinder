from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="EpubManifestItem")


@_attrs_define
class EpubManifestItem:
    """
    Attributes:
        id (str | Unset):
        href (str | Unset):
        media_type (str | Unset):
        properties (list[str] | Unset):
        size (int | Unset):
    """

    id: str | Unset = UNSET
    href: str | Unset = UNSET
    media_type: str | Unset = UNSET
    properties: list[str] | Unset = UNSET
    size: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        href = self.href

        media_type = self.media_type

        properties: list[str] | Unset = UNSET
        if not isinstance(self.properties, Unset):
            properties = self.properties

        size = self.size

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if href is not UNSET:
            field_dict["href"] = href
        if media_type is not UNSET:
            field_dict["mediaType"] = media_type
        if properties is not UNSET:
            field_dict["properties"] = properties
        if size is not UNSET:
            field_dict["size"] = size

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        href = d.pop("href", UNSET)

        media_type = d.pop("mediaType", UNSET)

        properties = cast(list[str], d.pop("properties", UNSET))

        size = d.pop("size", UNSET)

        epub_manifest_item = cls(
            id=id,
            href=href,
            media_type=media_type,
            properties=properties,
            size=size,
        )

        epub_manifest_item.additional_properties = d
        return epub_manifest_item

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
