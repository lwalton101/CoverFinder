from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ReleaseNote")


@_attrs_define
class ReleaseNote:
    """
    Attributes:
        version (str | Unset):
        name (str | Unset):
        changelog (str | Unset):
        url (str | Unset):
        published_at (datetime.datetime | Unset):
    """

    version: str | Unset = UNSET
    name: str | Unset = UNSET
    changelog: str | Unset = UNSET
    url: str | Unset = UNSET
    published_at: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        version = self.version

        name = self.name

        changelog = self.changelog

        url = self.url

        published_at: str | Unset = UNSET
        if not isinstance(self.published_at, Unset):
            published_at = self.published_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if version is not UNSET:
            field_dict["version"] = version
        if name is not UNSET:
            field_dict["name"] = name
        if changelog is not UNSET:
            field_dict["changelog"] = changelog
        if url is not UNSET:
            field_dict["url"] = url
        if published_at is not UNSET:
            field_dict["publishedAt"] = published_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        version = d.pop("version", UNSET)

        name = d.pop("name", UNSET)

        changelog = d.pop("changelog", UNSET)

        url = d.pop("url", UNSET)

        _published_at = d.pop("publishedAt", UNSET)
        published_at: datetime.datetime | Unset
        if isinstance(_published_at, Unset):
            published_at = UNSET
        else:
            published_at = datetime.datetime.fromisoformat(_published_at)

        release_note = cls(
            version=version,
            name=name,
            changelog=changelog,
            url=url,
            published_at=published_at,
        )

        release_note.additional_properties = d
        return release_note

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
