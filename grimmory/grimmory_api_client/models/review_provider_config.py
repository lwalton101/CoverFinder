from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.review_provider_config_provider import ReviewProviderConfigProvider
from ..types import UNSET, Unset

T = TypeVar("T", bound="ReviewProviderConfig")


@_attrs_define
class ReviewProviderConfig:
    """
    Attributes:
        provider (ReviewProviderConfigProvider | Unset):
        enabled (bool | Unset):
        max_reviews (int | Unset):
    """

    provider: ReviewProviderConfigProvider | Unset = UNSET
    enabled: bool | Unset = UNSET
    max_reviews: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        provider: str | Unset = UNSET
        if not isinstance(self.provider, Unset):
            provider = self.provider.value

        enabled = self.enabled

        max_reviews = self.max_reviews

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if provider is not UNSET:
            field_dict["provider"] = provider
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if max_reviews is not UNSET:
            field_dict["maxReviews"] = max_reviews

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _provider = d.pop("provider", UNSET)
        provider: ReviewProviderConfigProvider | Unset
        if isinstance(_provider, Unset):
            provider = UNSET
        else:
            provider = ReviewProviderConfigProvider(_provider)

        enabled = d.pop("enabled", UNSET)

        max_reviews = d.pop("maxReviews", UNSET)

        review_provider_config = cls(
            provider=provider,
            enabled=enabled,
            max_reviews=max_reviews,
        )

        review_provider_config.additional_properties = d
        return review_provider_config

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
