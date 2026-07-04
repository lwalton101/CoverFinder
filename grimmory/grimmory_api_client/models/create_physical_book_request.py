from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreatePhysicalBookRequest")


@_attrs_define
class CreatePhysicalBookRequest:
    """Physical book creation request

    Attributes:
        library_id (int):
        isbn (str | Unset):
        title (str | Unset):
        authors (list[str] | Unset):
        description (str | Unset):
        publisher (str | Unset):
        published_date (str | Unset):
        language (str | Unset):
        page_count (int | Unset):
        categories (list[str] | Unset):
        thumbnail_url (str | Unset):
    """

    library_id: int
    isbn: str | Unset = UNSET
    title: str | Unset = UNSET
    authors: list[str] | Unset = UNSET
    description: str | Unset = UNSET
    publisher: str | Unset = UNSET
    published_date: str | Unset = UNSET
    language: str | Unset = UNSET
    page_count: int | Unset = UNSET
    categories: list[str] | Unset = UNSET
    thumbnail_url: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        library_id = self.library_id

        isbn = self.isbn

        title = self.title

        authors: list[str] | Unset = UNSET
        if not isinstance(self.authors, Unset):
            authors = self.authors

        description = self.description

        publisher = self.publisher

        published_date = self.published_date

        language = self.language

        page_count = self.page_count

        categories: list[str] | Unset = UNSET
        if not isinstance(self.categories, Unset):
            categories = self.categories

        thumbnail_url = self.thumbnail_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "libraryId": library_id,
            }
        )
        if isbn is not UNSET:
            field_dict["isbn"] = isbn
        if title is not UNSET:
            field_dict["title"] = title
        if authors is not UNSET:
            field_dict["authors"] = authors
        if description is not UNSET:
            field_dict["description"] = description
        if publisher is not UNSET:
            field_dict["publisher"] = publisher
        if published_date is not UNSET:
            field_dict["publishedDate"] = published_date
        if language is not UNSET:
            field_dict["language"] = language
        if page_count is not UNSET:
            field_dict["pageCount"] = page_count
        if categories is not UNSET:
            field_dict["categories"] = categories
        if thumbnail_url is not UNSET:
            field_dict["thumbnailUrl"] = thumbnail_url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        library_id = d.pop("libraryId")

        isbn = d.pop("isbn", UNSET)

        title = d.pop("title", UNSET)

        authors = cast(list[str], d.pop("authors", UNSET))

        description = d.pop("description", UNSET)

        publisher = d.pop("publisher", UNSET)

        published_date = d.pop("publishedDate", UNSET)

        language = d.pop("language", UNSET)

        page_count = d.pop("pageCount", UNSET)

        categories = cast(list[str], d.pop("categories", UNSET))

        thumbnail_url = d.pop("thumbnailUrl", UNSET)

        create_physical_book_request = cls(
            library_id=library_id,
            isbn=isbn,
            title=title,
            authors=authors,
            description=description,
            publisher=publisher,
            published_date=published_date,
            language=language,
            page_count=page_count,
            categories=categories,
            thumbnail_url=thumbnail_url,
        )

        create_physical_book_request.additional_properties = d
        return create_physical_book_request

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
