from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateBookNoteV2Request")


@_attrs_define
class CreateBookNoteV2Request:
    """Note creation request

    Attributes:
        book_id (int):
        cfi (str):
        note_content (str):
        selected_text (str | Unset):
        color (str | Unset):
        chapter_title (str | Unset):
    """

    book_id: int
    cfi: str
    note_content: str
    selected_text: str | Unset = UNSET
    color: str | Unset = UNSET
    chapter_title: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        book_id = self.book_id

        cfi = self.cfi

        note_content = self.note_content

        selected_text = self.selected_text

        color = self.color

        chapter_title = self.chapter_title

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "bookId": book_id,
                "cfi": cfi,
                "noteContent": note_content,
            }
        )
        if selected_text is not UNSET:
            field_dict["selectedText"] = selected_text
        if color is not UNSET:
            field_dict["color"] = color
        if chapter_title is not UNSET:
            field_dict["chapterTitle"] = chapter_title

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        book_id = d.pop("bookId")

        cfi = d.pop("cfi")

        note_content = d.pop("noteContent")

        selected_text = d.pop("selectedText", UNSET)

        color = d.pop("color", UNSET)

        chapter_title = d.pop("chapterTitle", UNSET)

        create_book_note_v2_request = cls(
            book_id=book_id,
            cfi=cfi,
            note_content=note_content,
            selected_text=selected_text,
            color=color,
            chapter_title=chapter_title,
        )

        create_book_note_v2_request.additional_properties = d
        return create_book_note_v2_request

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
