from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateBookNoteRequest")


@_attrs_define
class CreateBookNoteRequest:
    """Note creation request

    Attributes:
        book_id (int):
        content (str):
        id (int | Unset):
        title (str | Unset):
    """

    book_id: int
    content: str
    id: int | Unset = UNSET
    title: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        book_id = self.book_id

        content = self.content

        id = self.id

        title = self.title

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "bookId": book_id,
                "content": content,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if title is not UNSET:
            field_dict["title"] = title

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        book_id = d.pop("bookId")

        content = d.pop("content")

        id = d.pop("id", UNSET)

        title = d.pop("title", UNSET)

        create_book_note_request = cls(
            book_id=book_id,
            content=content,
            id=id,
            title=title,
        )

        create_book_note_request.additional_properties = d
        return create_book_note_request

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
