from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.book import Book


T = TypeVar("T", bound="BookRecommendation")


@_attrs_define
class BookRecommendation:
    """
    Attributes:
        book (Book | Unset):
        similarity_score (float | Unset):
    """

    book: Book | Unset = UNSET
    similarity_score: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        book: dict[str, Any] | Unset = UNSET
        if not isinstance(self.book, Unset):
            book = self.book.to_dict()

        similarity_score = self.similarity_score

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if book is not UNSET:
            field_dict["book"] = book
        if similarity_score is not UNSET:
            field_dict["similarityScore"] = similarity_score

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.book import Book

        d = dict(src_dict)
        _book = d.pop("book", UNSET)
        book: Book | Unset
        if isinstance(_book, Unset):
            book = UNSET
        else:
            book = Book.from_dict(_book)

        similarity_score = d.pop("similarityScore", UNSET)

        book_recommendation = cls(
            book=book,
            similarity_score=similarity_score,
        )

        book_recommendation.additional_properties = d
        return book_recommendation

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
