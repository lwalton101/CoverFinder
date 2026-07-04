from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.book import Book


T = TypeVar("T", bound="DetachBookFileResponse")


@_attrs_define
class DetachBookFileResponse:
    """
    Attributes:
        source_book (Book | Unset):
        new_book (Book | Unset):
    """

    source_book: Book | Unset = UNSET
    new_book: Book | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        source_book: dict[str, Any] | Unset = UNSET
        if not isinstance(self.source_book, Unset):
            source_book = self.source_book.to_dict()

        new_book: dict[str, Any] | Unset = UNSET
        if not isinstance(self.new_book, Unset):
            new_book = self.new_book.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if source_book is not UNSET:
            field_dict["sourceBook"] = source_book
        if new_book is not UNSET:
            field_dict["newBook"] = new_book

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.book import Book

        d = dict(src_dict)
        _source_book = d.pop("sourceBook", UNSET)
        source_book: Book | Unset
        if isinstance(_source_book, Unset):
            source_book = UNSET
        else:
            source_book = Book.from_dict(_source_book)

        _new_book = d.pop("newBook", UNSET)
        new_book: Book | Unset
        if isinstance(_new_book, Unset):
            new_book = UNSET
        else:
            new_book = Book.from_dict(_new_book)

        detach_book_file_response = cls(
            source_book=source_book,
            new_book=new_book,
        )

        detach_book_file_response.additional_properties = d
        return detach_book_file_response

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
