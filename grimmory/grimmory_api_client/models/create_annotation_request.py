from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateAnnotationRequest")


@_attrs_define
class CreateAnnotationRequest:
    """Annotation creation request

    Attributes:
        book_id (int):
        cfi (str):
        text (str):
        color (str | Unset):
        style (str | Unset):
        note (str | Unset):
        chapter_title (str | Unset):
    """

    book_id: int
    cfi: str
    text: str
    color: str | Unset = UNSET
    style: str | Unset = UNSET
    note: str | Unset = UNSET
    chapter_title: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        book_id = self.book_id

        cfi = self.cfi

        text = self.text

        color = self.color

        style = self.style

        note = self.note

        chapter_title = self.chapter_title

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "bookId": book_id,
                "cfi": cfi,
                "text": text,
            }
        )
        if color is not UNSET:
            field_dict["color"] = color
        if style is not UNSET:
            field_dict["style"] = style
        if note is not UNSET:
            field_dict["note"] = note
        if chapter_title is not UNSET:
            field_dict["chapterTitle"] = chapter_title

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        book_id = d.pop("bookId")

        cfi = d.pop("cfi")

        text = d.pop("text")

        color = d.pop("color", UNSET)

        style = d.pop("style", UNSET)

        note = d.pop("note", UNSET)

        chapter_title = d.pop("chapterTitle", UNSET)

        create_annotation_request = cls(
            book_id=book_id,
            cfi=cfi,
            text=text,
            color=color,
            style=style,
            note=note,
            chapter_title=chapter_title,
        )

        create_annotation_request.additional_properties = d
        return create_annotation_request

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
