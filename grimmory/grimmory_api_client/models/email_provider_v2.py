from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="EmailProviderV2")


@_attrs_define
class EmailProviderV2:
    """
    Attributes:
        id (int | Unset):
        user_id (int | Unset):
        name (str | Unset):
        host (str | Unset):
        port (int | Unset):
        username (str | Unset):
        from_address (str | Unset):
        auth (bool | Unset):
        start_tls (bool | Unset):
        default_provider (bool | Unset):
        shared (bool | Unset):
    """

    id: int | Unset = UNSET
    user_id: int | Unset = UNSET
    name: str | Unset = UNSET
    host: str | Unset = UNSET
    port: int | Unset = UNSET
    username: str | Unset = UNSET
    from_address: str | Unset = UNSET
    auth: bool | Unset = UNSET
    start_tls: bool | Unset = UNSET
    default_provider: bool | Unset = UNSET
    shared: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        user_id = self.user_id

        name = self.name

        host = self.host

        port = self.port

        username = self.username

        from_address = self.from_address

        auth = self.auth

        start_tls = self.start_tls

        default_provider = self.default_provider

        shared = self.shared

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if user_id is not UNSET:
            field_dict["userId"] = user_id
        if name is not UNSET:
            field_dict["name"] = name
        if host is not UNSET:
            field_dict["host"] = host
        if port is not UNSET:
            field_dict["port"] = port
        if username is not UNSET:
            field_dict["username"] = username
        if from_address is not UNSET:
            field_dict["fromAddress"] = from_address
        if auth is not UNSET:
            field_dict["auth"] = auth
        if start_tls is not UNSET:
            field_dict["startTls"] = start_tls
        if default_provider is not UNSET:
            field_dict["defaultProvider"] = default_provider
        if shared is not UNSET:
            field_dict["shared"] = shared

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        user_id = d.pop("userId", UNSET)

        name = d.pop("name", UNSET)

        host = d.pop("host", UNSET)

        port = d.pop("port", UNSET)

        username = d.pop("username", UNSET)

        from_address = d.pop("fromAddress", UNSET)

        auth = d.pop("auth", UNSET)

        start_tls = d.pop("startTls", UNSET)

        default_provider = d.pop("defaultProvider", UNSET)

        shared = d.pop("shared", UNSET)

        email_provider_v2 = cls(
            id=id,
            user_id=user_id,
            name=name,
            host=host,
            port=port,
            username=username,
            from_address=from_address,
            auth=auth,
            start_tls=start_tls,
            default_provider=default_provider,
            shared=shared,
        )

        email_provider_v2.additional_properties = d
        return email_provider_v2

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
