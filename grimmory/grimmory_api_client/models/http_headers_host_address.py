from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="HttpHeadersHostAddress")


@_attrs_define
class HttpHeadersHostAddress:
    """
    Attributes:
        address (str | Unset):
        host_address (str | Unset):
        link_local_address (bool | Unset):
        host_name (str | Unset):
        multicast_address (bool | Unset):
        any_local_address (bool | Unset):
        loopback_address (bool | Unset):
        site_local_address (bool | Unset):
        mcglobal (bool | Unset):
        mcnode_local (bool | Unset):
        mclink_local (bool | Unset):
        mcsite_local (bool | Unset):
        mcorg_local (bool | Unset):
        canonical_host_name (str | Unset):
    """

    address: str | Unset = UNSET
    host_address: str | Unset = UNSET
    link_local_address: bool | Unset = UNSET
    host_name: str | Unset = UNSET
    multicast_address: bool | Unset = UNSET
    any_local_address: bool | Unset = UNSET
    loopback_address: bool | Unset = UNSET
    site_local_address: bool | Unset = UNSET
    mcglobal: bool | Unset = UNSET
    mcnode_local: bool | Unset = UNSET
    mclink_local: bool | Unset = UNSET
    mcsite_local: bool | Unset = UNSET
    mcorg_local: bool | Unset = UNSET
    canonical_host_name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        address = self.address

        host_address = self.host_address

        link_local_address = self.link_local_address

        host_name = self.host_name

        multicast_address = self.multicast_address

        any_local_address = self.any_local_address

        loopback_address = self.loopback_address

        site_local_address = self.site_local_address

        mcglobal = self.mcglobal

        mcnode_local = self.mcnode_local

        mclink_local = self.mclink_local

        mcsite_local = self.mcsite_local

        mcorg_local = self.mcorg_local

        canonical_host_name = self.canonical_host_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if address is not UNSET:
            field_dict["address"] = address
        if host_address is not UNSET:
            field_dict["hostAddress"] = host_address
        if link_local_address is not UNSET:
            field_dict["linkLocalAddress"] = link_local_address
        if host_name is not UNSET:
            field_dict["hostName"] = host_name
        if multicast_address is not UNSET:
            field_dict["multicastAddress"] = multicast_address
        if any_local_address is not UNSET:
            field_dict["anyLocalAddress"] = any_local_address
        if loopback_address is not UNSET:
            field_dict["loopbackAddress"] = loopback_address
        if site_local_address is not UNSET:
            field_dict["siteLocalAddress"] = site_local_address
        if mcglobal is not UNSET:
            field_dict["mcglobal"] = mcglobal
        if mcnode_local is not UNSET:
            field_dict["mcnodeLocal"] = mcnode_local
        if mclink_local is not UNSET:
            field_dict["mclinkLocal"] = mclink_local
        if mcsite_local is not UNSET:
            field_dict["mcsiteLocal"] = mcsite_local
        if mcorg_local is not UNSET:
            field_dict["mcorgLocal"] = mcorg_local
        if canonical_host_name is not UNSET:
            field_dict["canonicalHostName"] = canonical_host_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        address = d.pop("address", UNSET)

        host_address = d.pop("hostAddress", UNSET)

        link_local_address = d.pop("linkLocalAddress", UNSET)

        host_name = d.pop("hostName", UNSET)

        multicast_address = d.pop("multicastAddress", UNSET)

        any_local_address = d.pop("anyLocalAddress", UNSET)

        loopback_address = d.pop("loopbackAddress", UNSET)

        site_local_address = d.pop("siteLocalAddress", UNSET)

        mcglobal = d.pop("mcglobal", UNSET)

        mcnode_local = d.pop("mcnodeLocal", UNSET)

        mclink_local = d.pop("mclinkLocal", UNSET)

        mcsite_local = d.pop("mcsiteLocal", UNSET)

        mcorg_local = d.pop("mcorgLocal", UNSET)

        canonical_host_name = d.pop("canonicalHostName", UNSET)

        http_headers_host_address = cls(
            address=address,
            host_address=host_address,
            link_local_address=link_local_address,
            host_name=host_name,
            multicast_address=multicast_address,
            any_local_address=any_local_address,
            loopback_address=loopback_address,
            site_local_address=site_local_address,
            mcglobal=mcglobal,
            mcnode_local=mcnode_local,
            mclink_local=mclink_local,
            mcsite_local=mcsite_local,
            mcorg_local=mcorg_local,
            canonical_host_name=canonical_host_name,
        )

        http_headers_host_address.additional_properties = d
        return http_headers_host_address

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
