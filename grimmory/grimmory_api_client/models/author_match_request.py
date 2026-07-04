from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.author_match_request_source import AuthorMatchRequestSource
from ..types import UNSET, Unset

T = TypeVar("T", bound="AuthorMatchRequest")


@_attrs_define
class AuthorMatchRequest:
    """
    Attributes:
        source (AuthorMatchRequestSource | Unset):
        asin (str | Unset):
        region (str | Unset):
    """

    source: AuthorMatchRequestSource | Unset = UNSET
    asin: str | Unset = UNSET
    region: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        source: str | Unset = UNSET
        if not isinstance(self.source, Unset):
            source = self.source.value

        asin = self.asin

        region = self.region

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if source is not UNSET:
            field_dict["source"] = source
        if asin is not UNSET:
            field_dict["asin"] = asin
        if region is not UNSET:
            field_dict["region"] = region

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _source = d.pop("source", UNSET)
        source: AuthorMatchRequestSource | Unset
        if isinstance(_source, Unset):
            source = UNSET
        else:
            source = AuthorMatchRequestSource(_source)

        asin = d.pop("asin", UNSET)

        region = d.pop("region", UNSET)

        author_match_request = cls(
            source=source,
            asin=asin,
            region=region,
        )

        author_match_request.additional_properties = d
        return author_match_request

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
