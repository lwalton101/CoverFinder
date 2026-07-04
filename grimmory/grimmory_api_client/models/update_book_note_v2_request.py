from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateBookNoteV2Request")


@_attrs_define
class UpdateBookNoteV2Request:
    """Note update request

    Attributes:
        note_content (str | Unset):
        color (str | Unset):
        chapter_title (str | Unset):
    """

    note_content: str | Unset = UNSET
    color: str | Unset = UNSET
    chapter_title: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        note_content = self.note_content

        color = self.color

        chapter_title = self.chapter_title

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if note_content is not UNSET:
            field_dict["noteContent"] = note_content
        if color is not UNSET:
            field_dict["color"] = color
        if chapter_title is not UNSET:
            field_dict["chapterTitle"] = chapter_title

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        note_content = d.pop("noteContent", UNSET)

        color = d.pop("color", UNSET)

        chapter_title = d.pop("chapterTitle", UNSET)

        update_book_note_v2_request = cls(
            note_content=note_content,
            color=color,
            chapter_title=chapter_title,
        )

        update_book_note_v2_request.additional_properties = d
        return update_book_note_v2_request

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
