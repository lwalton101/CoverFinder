from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AppAuthorDetail")


@_attrs_define
class AppAuthorDetail:
    """
    Attributes:
        id (int | Unset):
        name (str | Unset):
        description (str | Unset):
        asin (str | Unset):
        book_count (int | Unset):
        has_photo (bool | Unset):
    """

    id: int | Unset = UNSET
    name: str | Unset = UNSET
    description: str | Unset = UNSET
    asin: str | Unset = UNSET
    book_count: int | Unset = UNSET
    has_photo: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        description = self.description

        asin = self.asin

        book_count = self.book_count

        has_photo = self.has_photo

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if asin is not UNSET:
            field_dict["asin"] = asin
        if book_count is not UNSET:
            field_dict["bookCount"] = book_count
        if has_photo is not UNSET:
            field_dict["hasPhoto"] = has_photo

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        asin = d.pop("asin", UNSET)

        book_count = d.pop("bookCount", UNSET)

        has_photo = d.pop("hasPhoto", UNSET)

        app_author_detail = cls(
            id=id,
            name=name,
            description=description,
            asin=asin,
            book_count=book_count,
            has_photo=has_photo,
        )

        app_author_detail.additional_properties = d
        return app_author_detail

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
