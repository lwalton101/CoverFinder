from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.review_provider_config import ReviewProviderConfig


T = TypeVar("T", bound="MetadataPublicReviewsSettings")


@_attrs_define
class MetadataPublicReviewsSettings:
    """
    Attributes:
        download_enabled (bool | Unset):
        auto_download_enabled (bool | Unset):
        providers (list[ReviewProviderConfig] | Unset):
    """

    download_enabled: bool | Unset = UNSET
    auto_download_enabled: bool | Unset = UNSET
    providers: list[ReviewProviderConfig] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        download_enabled = self.download_enabled

        auto_download_enabled = self.auto_download_enabled

        providers: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.providers, Unset):
            providers = []
            for providers_item_data in self.providers:
                providers_item = providers_item_data.to_dict()
                providers.append(providers_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if download_enabled is not UNSET:
            field_dict["downloadEnabled"] = download_enabled
        if auto_download_enabled is not UNSET:
            field_dict["autoDownloadEnabled"] = auto_download_enabled
        if providers is not UNSET:
            field_dict["providers"] = providers

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.review_provider_config import ReviewProviderConfig

        d = dict(src_dict)
        download_enabled = d.pop("downloadEnabled", UNSET)

        auto_download_enabled = d.pop("autoDownloadEnabled", UNSET)

        _providers = d.pop("providers", UNSET)
        providers: list[ReviewProviderConfig] | Unset = UNSET
        if _providers is not UNSET:
            providers = []
            for providers_item_data in _providers:
                providers_item = ReviewProviderConfig.from_dict(providers_item_data)

                providers.append(providers_item)

        metadata_public_reviews_settings = cls(
            download_enabled=download_enabled,
            auto_download_enabled=auto_download_enabled,
            providers=providers,
        )

        metadata_public_reviews_settings.additional_properties = d
        return metadata_public_reviews_settings

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
