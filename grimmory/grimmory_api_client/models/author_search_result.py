from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.author_search_result_source import AuthorSearchResultSource
from ..types import UNSET, Unset

T = TypeVar("T", bound="AuthorSearchResult")


@_attrs_define
class AuthorSearchResult:
    """
    Attributes:
        source (AuthorSearchResultSource | Unset):
        asin (str | Unset):
        name (str | Unset):
        description (str | Unset):
        image_url (str | Unset):
    """

    source: AuthorSearchResultSource | Unset = UNSET
    asin: str | Unset = UNSET
    name: str | Unset = UNSET
    description: str | Unset = UNSET
    image_url: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        source: str | Unset = UNSET
        if not isinstance(self.source, Unset):
            source = self.source.value

        asin = self.asin

        name = self.name

        description = self.description

        image_url = self.image_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if source is not UNSET:
            field_dict["source"] = source
        if asin is not UNSET:
            field_dict["asin"] = asin
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if image_url is not UNSET:
            field_dict["imageUrl"] = image_url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _source = d.pop("source", UNSET)
        source: AuthorSearchResultSource | Unset
        if isinstance(_source, Unset):
            source = UNSET
        else:
            source = AuthorSearchResultSource(_source)

        asin = d.pop("asin", UNSET)

        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        image_url = d.pop("imageUrl", UNSET)

        author_search_result = cls(
            source=source,
            asin=asin,
            name=name,
            description=description,
            image_url=image_url,
        )

        author_search_result.additional_properties = d
        return author_search_result

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
