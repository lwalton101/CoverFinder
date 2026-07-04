from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CoverFetchRequest")


@_attrs_define
class CoverFetchRequest:
    """Cover fetch request

    Attributes:
        isbn (str | Unset):
        title (str | Unset):
        author (str | Unset):
        cover_type (str | Unset):
    """

    isbn: str | Unset = UNSET
    title: str | Unset = UNSET
    author: str | Unset = UNSET
    cover_type: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        isbn = self.isbn

        title = self.title

        author = self.author

        cover_type = self.cover_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if isbn is not UNSET:
            field_dict["isbn"] = isbn
        if title is not UNSET:
            field_dict["title"] = title
        if author is not UNSET:
            field_dict["author"] = author
        if cover_type is not UNSET:
            field_dict["coverType"] = cover_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        isbn = d.pop("isbn", UNSET)

        title = d.pop("title", UNSET)

        author = d.pop("author", UNSET)

        cover_type = d.pop("coverType", UNSET)

        cover_fetch_request = cls(
            isbn=isbn,
            title=title,
            author=author,
            cover_type=cover_type,
        )

        cover_fetch_request.additional_properties = d
        return cover_fetch_request

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
