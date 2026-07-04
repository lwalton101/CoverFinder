from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="OidcAutoProvisionDetails")


@_attrs_define
class OidcAutoProvisionDetails:
    """
    Attributes:
        enable_auto_provisioning (bool | Unset):
        allow_local_account_linking (bool | Unset):
        default_permissions (list[str] | Unset):
        default_library_ids (list[int] | Unset):
    """

    enable_auto_provisioning: bool | Unset = UNSET
    allow_local_account_linking: bool | Unset = UNSET
    default_permissions: list[str] | Unset = UNSET
    default_library_ids: list[int] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        enable_auto_provisioning = self.enable_auto_provisioning

        allow_local_account_linking = self.allow_local_account_linking

        default_permissions: list[str] | Unset = UNSET
        if not isinstance(self.default_permissions, Unset):
            default_permissions = self.default_permissions

        default_library_ids: list[int] | Unset = UNSET
        if not isinstance(self.default_library_ids, Unset):
            default_library_ids = self.default_library_ids

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if enable_auto_provisioning is not UNSET:
            field_dict["enableAutoProvisioning"] = enable_auto_provisioning
        if allow_local_account_linking is not UNSET:
            field_dict["allowLocalAccountLinking"] = allow_local_account_linking
        if default_permissions is not UNSET:
            field_dict["defaultPermissions"] = default_permissions
        if default_library_ids is not UNSET:
            field_dict["defaultLibraryIds"] = default_library_ids

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        enable_auto_provisioning = d.pop("enableAutoProvisioning", UNSET)

        allow_local_account_linking = d.pop("allowLocalAccountLinking", UNSET)

        default_permissions = cast(list[str], d.pop("defaultPermissions", UNSET))

        default_library_ids = cast(list[int], d.pop("defaultLibraryIds", UNSET))

        oidc_auto_provision_details = cls(
            enable_auto_provisioning=enable_auto_provisioning,
            allow_local_account_linking=allow_local_account_linking,
            default_permissions=default_permissions,
            default_library_ids=default_library_ids,
        )

        oidc_auto_provision_details.additional_properties = d
        return oidc_auto_provision_details

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
