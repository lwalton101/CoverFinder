from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="OidcGroupMapping")


@_attrs_define
class OidcGroupMapping:
    """
    Attributes:
        id (int | Unset):
        oidc_group_claim (str | Unset):
        is_admin (bool | Unset):
        permissions (list[str] | Unset):
        library_ids (list[int] | Unset):
        description (str | Unset):
    """

    id: int | Unset = UNSET
    oidc_group_claim: str | Unset = UNSET
    is_admin: bool | Unset = UNSET
    permissions: list[str] | Unset = UNSET
    library_ids: list[int] | Unset = UNSET
    description: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        oidc_group_claim = self.oidc_group_claim

        is_admin = self.is_admin

        permissions: list[str] | Unset = UNSET
        if not isinstance(self.permissions, Unset):
            permissions = self.permissions

        library_ids: list[int] | Unset = UNSET
        if not isinstance(self.library_ids, Unset):
            library_ids = self.library_ids

        description = self.description

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if oidc_group_claim is not UNSET:
            field_dict["oidcGroupClaim"] = oidc_group_claim
        if is_admin is not UNSET:
            field_dict["isAdmin"] = is_admin
        if permissions is not UNSET:
            field_dict["permissions"] = permissions
        if library_ids is not UNSET:
            field_dict["libraryIds"] = library_ids
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        oidc_group_claim = d.pop("oidcGroupClaim", UNSET)

        is_admin = d.pop("isAdmin", UNSET)

        permissions = cast(list[str], d.pop("permissions", UNSET))

        library_ids = cast(list[int], d.pop("libraryIds", UNSET))

        description = d.pop("description", UNSET)

        oidc_group_mapping = cls(
            id=id,
            oidc_group_claim=oidc_group_claim,
            is_admin=is_admin,
            permissions=permissions,
            library_ids=library_ids,
            description=description,
        )

        oidc_group_mapping.additional_properties = d
        return oidc_group_mapping

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
