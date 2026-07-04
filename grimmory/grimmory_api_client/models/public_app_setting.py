from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.oidc_provider_details import OidcProviderDetails


T = TypeVar("T", bound="PublicAppSetting")


@_attrs_define
class PublicAppSetting:
    """
    Attributes:
        oidc_enabled (bool | Unset):
        remote_auth_enabled (bool | Unset):
        oidc_provider_details (OidcProviderDetails | Unset):
        oidc_force_only_mode (bool | Unset):
    """

    oidc_enabled: bool | Unset = UNSET
    remote_auth_enabled: bool | Unset = UNSET
    oidc_provider_details: OidcProviderDetails | Unset = UNSET
    oidc_force_only_mode: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        oidc_enabled = self.oidc_enabled

        remote_auth_enabled = self.remote_auth_enabled

        oidc_provider_details: dict[str, Any] | Unset = UNSET
        if not isinstance(self.oidc_provider_details, Unset):
            oidc_provider_details = self.oidc_provider_details.to_dict()

        oidc_force_only_mode = self.oidc_force_only_mode

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if oidc_enabled is not UNSET:
            field_dict["oidcEnabled"] = oidc_enabled
        if remote_auth_enabled is not UNSET:
            field_dict["remoteAuthEnabled"] = remote_auth_enabled
        if oidc_provider_details is not UNSET:
            field_dict["oidcProviderDetails"] = oidc_provider_details
        if oidc_force_only_mode is not UNSET:
            field_dict["oidcForceOnlyMode"] = oidc_force_only_mode

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.oidc_provider_details import OidcProviderDetails

        d = dict(src_dict)
        oidc_enabled = d.pop("oidcEnabled", UNSET)

        remote_auth_enabled = d.pop("remoteAuthEnabled", UNSET)

        _oidc_provider_details = d.pop("oidcProviderDetails", UNSET)
        oidc_provider_details: OidcProviderDetails | Unset
        if isinstance(_oidc_provider_details, Unset):
            oidc_provider_details = UNSET
        else:
            oidc_provider_details = OidcProviderDetails.from_dict(_oidc_provider_details)

        oidc_force_only_mode = d.pop("oidcForceOnlyMode", UNSET)

        public_app_setting = cls(
            oidc_enabled=oidc_enabled,
            remote_auth_enabled=remote_auth_enabled,
            oidc_provider_details=oidc_provider_details,
            oidc_force_only_mode=oidc_force_only_mode,
        )

        public_app_setting.additional_properties = d
        return public_app_setting

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
