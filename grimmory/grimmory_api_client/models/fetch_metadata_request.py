from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.fetch_metadata_request_providers_item import FetchMetadataRequestProvidersItem
from ..types import UNSET, Unset

T = TypeVar("T", bound="FetchMetadataRequest")


@_attrs_define
class FetchMetadataRequest:
    """Fetch metadata request

    Attributes:
        book_id (int | Unset):
        providers (list[FetchMetadataRequestProvidersItem] | Unset):
        isbn (str | Unset):
        title (str | Unset):
        author (str | Unset):
        asin (str | Unset):
    """

    book_id: int | Unset = UNSET
    providers: list[FetchMetadataRequestProvidersItem] | Unset = UNSET
    isbn: str | Unset = UNSET
    title: str | Unset = UNSET
    author: str | Unset = UNSET
    asin: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        book_id = self.book_id

        providers: list[str] | Unset = UNSET
        if not isinstance(self.providers, Unset):
            providers = []
            for providers_item_data in self.providers:
                providers_item = providers_item_data.value
                providers.append(providers_item)

        isbn = self.isbn

        title = self.title

        author = self.author

        asin = self.asin

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if book_id is not UNSET:
            field_dict["bookId"] = book_id
        if providers is not UNSET:
            field_dict["providers"] = providers
        if isbn is not UNSET:
            field_dict["isbn"] = isbn
        if title is not UNSET:
            field_dict["title"] = title
        if author is not UNSET:
            field_dict["author"] = author
        if asin is not UNSET:
            field_dict["asin"] = asin

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        book_id = d.pop("bookId", UNSET)

        _providers = d.pop("providers", UNSET)
        providers: list[FetchMetadataRequestProvidersItem] | Unset = UNSET
        if _providers is not UNSET:
            providers = []
            for providers_item_data in _providers:
                providers_item = FetchMetadataRequestProvidersItem(providers_item_data)

                providers.append(providers_item)

        isbn = d.pop("isbn", UNSET)

        title = d.pop("title", UNSET)

        author = d.pop("author", UNSET)

        asin = d.pop("asin", UNSET)

        fetch_metadata_request = cls(
            book_id=book_id,
            providers=providers,
            isbn=isbn,
            title=title,
            author=author,
            asin=asin,
        )

        fetch_metadata_request.additional_properties = d
        return fetch_metadata_request

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
