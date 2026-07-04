from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.permissions import Permissions


T = TypeVar("T", bound="UserUpdateRequest")


@_attrs_define
class UserUpdateRequest:
    """User update request

    Attributes:
        name (str | Unset):
        email (str | Unset):
        permissions (Permissions | Unset):
        assigned_libraries (list[int] | Unset):
    """

    name: str | Unset = UNSET
    email: str | Unset = UNSET
    permissions: Permissions | Unset = UNSET
    assigned_libraries: list[int] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        email = self.email

        permissions: dict[str, Any] | Unset = UNSET
        if not isinstance(self.permissions, Unset):
            permissions = self.permissions.to_dict()

        assigned_libraries: list[int] | Unset = UNSET
        if not isinstance(self.assigned_libraries, Unset):
            assigned_libraries = self.assigned_libraries

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if email is not UNSET:
            field_dict["email"] = email
        if permissions is not UNSET:
            field_dict["permissions"] = permissions
        if assigned_libraries is not UNSET:
            field_dict["assignedLibraries"] = assigned_libraries

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.permissions import Permissions

        d = dict(src_dict)
        name = d.pop("name", UNSET)

        email = d.pop("email", UNSET)

        _permissions = d.pop("permissions", UNSET)
        permissions: Permissions | Unset
        if isinstance(_permissions, Unset):
            permissions = UNSET
        else:
            permissions = Permissions.from_dict(_permissions)

        assigned_libraries = cast(list[int], d.pop("assignedLibraries", UNSET))

        user_update_request = cls(
            name=name,
            email=email,
            permissions=permissions,
            assigned_libraries=assigned_libraries,
        )

        user_update_request.additional_properties = d
        return user_update_request

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
