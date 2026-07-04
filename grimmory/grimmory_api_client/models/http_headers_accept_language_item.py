from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="HttpHeadersAcceptLanguageItem")


@_attrs_define
class HttpHeadersAcceptLanguageItem:
    """
    Attributes:
        range_ (str | Unset):
        weight (float | Unset):
    """

    range_: str | Unset = UNSET
    weight: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        range_ = self.range_

        weight = self.weight

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if range_ is not UNSET:
            field_dict["range"] = range_
        if weight is not UNSET:
            field_dict["weight"] = weight

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        range_ = d.pop("range", UNSET)

        weight = d.pop("weight", UNSET)

        http_headers_accept_language_item = cls(
            range_=range_,
            weight=weight,
        )

        http_headers_accept_language_item.additional_properties = d
        return http_headers_accept_language_item

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
