from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateEmailProviderRequest")


@_attrs_define
class CreateEmailProviderRequest:
    """Email provider creation request

    Attributes:
        name (str | Unset):
        host (str | Unset):
        port (int | Unset):
        username (str | Unset):
        password (str | Unset):
        from_address (str | Unset):
        auth (bool | Unset):
        start_tls (bool | Unset):
        shared (bool | Unset):
    """

    name: str | Unset = UNSET
    host: str | Unset = UNSET
    port: int | Unset = UNSET
    username: str | Unset = UNSET
    password: str | Unset = UNSET
    from_address: str | Unset = UNSET
    auth: bool | Unset = UNSET
    start_tls: bool | Unset = UNSET
    shared: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        host = self.host

        port = self.port

        username = self.username

        password = self.password

        from_address = self.from_address

        auth = self.auth

        start_tls = self.start_tls

        shared = self.shared

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if host is not UNSET:
            field_dict["host"] = host
        if port is not UNSET:
            field_dict["port"] = port
        if username is not UNSET:
            field_dict["username"] = username
        if password is not UNSET:
            field_dict["password"] = password
        if from_address is not UNSET:
            field_dict["fromAddress"] = from_address
        if auth is not UNSET:
            field_dict["auth"] = auth
        if start_tls is not UNSET:
            field_dict["startTls"] = start_tls
        if shared is not UNSET:
            field_dict["shared"] = shared

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name", UNSET)

        host = d.pop("host", UNSET)

        port = d.pop("port", UNSET)

        username = d.pop("username", UNSET)

        password = d.pop("password", UNSET)

        from_address = d.pop("fromAddress", UNSET)

        auth = d.pop("auth", UNSET)

        start_tls = d.pop("startTls", UNSET)

        shared = d.pop("shared", UNSET)

        create_email_provider_request = cls(
            name=name,
            host=host,
            port=port,
            username=username,
            password=password,
            from_address=from_address,
            auth=auth,
            start_tls=start_tls,
            shared=shared,
        )

        create_email_provider_request.additional_properties = d
        return create_email_provider_request

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
