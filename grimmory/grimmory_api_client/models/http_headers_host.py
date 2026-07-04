from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.http_headers_host_address import HttpHeadersHostAddress


T = TypeVar("T", bound="HttpHeadersHost")


@_attrs_define
class HttpHeadersHost:
    """
    Attributes:
        address (HttpHeadersHostAddress | Unset):
        port (int | Unset):
        host_name (str | Unset):
        host_string (str | Unset):
        unresolved (bool | Unset):
    """

    address: HttpHeadersHostAddress | Unset = UNSET
    port: int | Unset = UNSET
    host_name: str | Unset = UNSET
    host_string: str | Unset = UNSET
    unresolved: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        address: dict[str, Any] | Unset = UNSET
        if not isinstance(self.address, Unset):
            address = self.address.to_dict()

        port = self.port

        host_name = self.host_name

        host_string = self.host_string

        unresolved = self.unresolved

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if address is not UNSET:
            field_dict["address"] = address
        if port is not UNSET:
            field_dict["port"] = port
        if host_name is not UNSET:
            field_dict["hostName"] = host_name
        if host_string is not UNSET:
            field_dict["hostString"] = host_string
        if unresolved is not UNSET:
            field_dict["unresolved"] = unresolved

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.http_headers_host_address import HttpHeadersHostAddress

        d = dict(src_dict)
        _address = d.pop("address", UNSET)
        address: HttpHeadersHostAddress | Unset
        if isinstance(_address, Unset):
            address = UNSET
        else:
            address = HttpHeadersHostAddress.from_dict(_address)

        port = d.pop("port", UNSET)

        host_name = d.pop("hostName", UNSET)

        host_string = d.pop("hostString", UNSET)

        unresolved = d.pop("unresolved", UNSET)

        http_headers_host = cls(
            address=address,
            port=port,
            host_name=host_name,
            host_string=host_string,
            unresolved=unresolved,
        )

        http_headers_host.additional_properties = d
        return http_headers_host

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
