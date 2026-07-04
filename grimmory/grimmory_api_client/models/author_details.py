from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AuthorDetails")


@_attrs_define
class AuthorDetails:
    """
    Attributes:
        id (int | Unset):
        name (str | Unset):
        description (str | Unset):
        asin (str | Unset):
        name_locked (bool | Unset):
        description_locked (bool | Unset):
        asin_locked (bool | Unset):
        photo_locked (bool | Unset):
    """

    id: int | Unset = UNSET
    name: str | Unset = UNSET
    description: str | Unset = UNSET
    asin: str | Unset = UNSET
    name_locked: bool | Unset = UNSET
    description_locked: bool | Unset = UNSET
    asin_locked: bool | Unset = UNSET
    photo_locked: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        description = self.description

        asin = self.asin

        name_locked = self.name_locked

        description_locked = self.description_locked

        asin_locked = self.asin_locked

        photo_locked = self.photo_locked

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
        if name_locked is not UNSET:
            field_dict["nameLocked"] = name_locked
        if description_locked is not UNSET:
            field_dict["descriptionLocked"] = description_locked
        if asin_locked is not UNSET:
            field_dict["asinLocked"] = asin_locked
        if photo_locked is not UNSET:
            field_dict["photoLocked"] = photo_locked

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        asin = d.pop("asin", UNSET)

        name_locked = d.pop("nameLocked", UNSET)

        description_locked = d.pop("descriptionLocked", UNSET)

        asin_locked = d.pop("asinLocked", UNSET)

        photo_locked = d.pop("photoLocked", UNSET)

        author_details = cls(
            id=id,
            name=name,
            description=description,
            asin=asin,
            name_locked=name_locked,
            description_locked=description_locked,
            asin_locked=asin_locked,
            photo_locked=photo_locked,
        )

        author_details.additional_properties = d
        return author_details

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
