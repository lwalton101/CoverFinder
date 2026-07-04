from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.claim_mapping import ClaimMapping


T = TypeVar("T", bound="OidcProviderDetails")


@_attrs_define
class OidcProviderDetails:
    """
    Attributes:
        provider_name (str | Unset):
        client_id (str | Unset):
        client_secret (str | Unset):
        issuer_uri (str | Unset):
        scopes (str | Unset):
        claim_mapping (ClaimMapping | Unset):
    """

    provider_name: str | Unset = UNSET
    client_id: str | Unset = UNSET
    client_secret: str | Unset = UNSET
    issuer_uri: str | Unset = UNSET
    scopes: str | Unset = UNSET
    claim_mapping: ClaimMapping | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        provider_name = self.provider_name

        client_id = self.client_id

        client_secret = self.client_secret

        issuer_uri = self.issuer_uri

        scopes = self.scopes

        claim_mapping: dict[str, Any] | Unset = UNSET
        if not isinstance(self.claim_mapping, Unset):
            claim_mapping = self.claim_mapping.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if provider_name is not UNSET:
            field_dict["providerName"] = provider_name
        if client_id is not UNSET:
            field_dict["clientId"] = client_id
        if client_secret is not UNSET:
            field_dict["clientSecret"] = client_secret
        if issuer_uri is not UNSET:
            field_dict["issuerUri"] = issuer_uri
        if scopes is not UNSET:
            field_dict["scopes"] = scopes
        if claim_mapping is not UNSET:
            field_dict["claimMapping"] = claim_mapping

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.claim_mapping import ClaimMapping

        d = dict(src_dict)
        provider_name = d.pop("providerName", UNSET)

        client_id = d.pop("clientId", UNSET)

        client_secret = d.pop("clientSecret", UNSET)

        issuer_uri = d.pop("issuerUri", UNSET)

        scopes = d.pop("scopes", UNSET)

        _claim_mapping = d.pop("claimMapping", UNSET)
        claim_mapping: ClaimMapping | Unset
        if isinstance(_claim_mapping, Unset):
            claim_mapping = UNSET
        else:
            claim_mapping = ClaimMapping.from_dict(_claim_mapping)

        oidc_provider_details = cls(
            provider_name=provider_name,
            client_id=client_id,
            client_secret=client_secret,
            issuer_uri=issuer_uri,
            scopes=scopes,
            claim_mapping=claim_mapping,
        )

        oidc_provider_details.additional_properties = d
        return oidc_provider_details

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
