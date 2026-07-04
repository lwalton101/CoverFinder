from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.book import Book


T = TypeVar("T", bound="AttachBookFileResponse")


@_attrs_define
class AttachBookFileResponse:
    """
    Attributes:
        updated_book (Book | Unset):
        deleted_source_book_ids (list[int] | Unset):
    """

    updated_book: Book | Unset = UNSET
    deleted_source_book_ids: list[int] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        updated_book: dict[str, Any] | Unset = UNSET
        if not isinstance(self.updated_book, Unset):
            updated_book = self.updated_book.to_dict()

        deleted_source_book_ids: list[int] | Unset = UNSET
        if not isinstance(self.deleted_source_book_ids, Unset):
            deleted_source_book_ids = self.deleted_source_book_ids

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if updated_book is not UNSET:
            field_dict["updatedBook"] = updated_book
        if deleted_source_book_ids is not UNSET:
            field_dict["deletedSourceBookIds"] = deleted_source_book_ids

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.book import Book

        d = dict(src_dict)
        _updated_book = d.pop("updatedBook", UNSET)
        updated_book: Book | Unset
        if isinstance(_updated_book, Unset):
            updated_book = UNSET
        else:
            updated_book = Book.from_dict(_updated_book)

        deleted_source_book_ids = cast(list[int], d.pop("deletedSourceBookIds", UNSET))

        attach_book_file_response = cls(
            updated_book=updated_book,
            deleted_source_book_ids=deleted_source_book_ids,
        )

        attach_book_file_response.additional_properties = d
        return attach_book_file_response

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
