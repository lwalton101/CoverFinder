from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.book import Book


T = TypeVar("T", bound="DuplicateGroup")


@_attrs_define
class DuplicateGroup:
    """
    Attributes:
        suggested_target_book_id (int | Unset):
        match_reason (str | Unset):
        books (list[Book] | Unset):
    """

    suggested_target_book_id: int | Unset = UNSET
    match_reason: str | Unset = UNSET
    books: list[Book] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        suggested_target_book_id = self.suggested_target_book_id

        match_reason = self.match_reason

        books: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.books, Unset):
            books = []
            for books_item_data in self.books:
                books_item = books_item_data.to_dict()
                books.append(books_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if suggested_target_book_id is not UNSET:
            field_dict["suggestedTargetBookId"] = suggested_target_book_id
        if match_reason is not UNSET:
            field_dict["matchReason"] = match_reason
        if books is not UNSET:
            field_dict["books"] = books

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.book import Book

        d = dict(src_dict)
        suggested_target_book_id = d.pop("suggestedTargetBookId", UNSET)

        match_reason = d.pop("matchReason", UNSET)

        _books = d.pop("books", UNSET)
        books: list[Book] | Unset = UNSET
        if _books is not UNSET:
            books = []
            for books_item_data in _books:
                books_item = Book.from_dict(books_item_data)

                books.append(books_item)

        duplicate_group = cls(
            suggested_target_book_id=suggested_target_book_id,
            match_reason=match_reason,
            books=books,
        )

        duplicate_group.additional_properties = d
        return duplicate_group

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
