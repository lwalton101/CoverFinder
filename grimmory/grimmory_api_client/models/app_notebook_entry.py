from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AppNotebookEntry")


@_attrs_define
class AppNotebookEntry:
    """
    Attributes:
        id (int | Unset):
        type_ (str | Unset):
        book_id (int | Unset):
        text (str | Unset):
        note (str | Unset):
        color (str | Unset):
        style (str | Unset):
        chapter_title (str | Unset):
        created_at (datetime.datetime | Unset):
        updated_at (datetime.datetime | Unset):
    """

    id: int | Unset = UNSET
    type_: str | Unset = UNSET
    book_id: int | Unset = UNSET
    text: str | Unset = UNSET
    note: str | Unset = UNSET
    color: str | Unset = UNSET
    style: str | Unset = UNSET
    chapter_title: str | Unset = UNSET
    created_at: datetime.datetime | Unset = UNSET
    updated_at: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        type_ = self.type_

        book_id = self.book_id

        text = self.text

        note = self.note

        color = self.color

        style = self.style

        chapter_title = self.chapter_title

        created_at: str | Unset = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        updated_at: str | Unset = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if type_ is not UNSET:
            field_dict["type"] = type_
        if book_id is not UNSET:
            field_dict["bookId"] = book_id
        if text is not UNSET:
            field_dict["text"] = text
        if note is not UNSET:
            field_dict["note"] = note
        if color is not UNSET:
            field_dict["color"] = color
        if style is not UNSET:
            field_dict["style"] = style
        if chapter_title is not UNSET:
            field_dict["chapterTitle"] = chapter_title
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if updated_at is not UNSET:
            field_dict["updatedAt"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        type_ = d.pop("type", UNSET)

        book_id = d.pop("bookId", UNSET)

        text = d.pop("text", UNSET)

        note = d.pop("note", UNSET)

        color = d.pop("color", UNSET)

        style = d.pop("style", UNSET)

        chapter_title = d.pop("chapterTitle", UNSET)

        _created_at = d.pop("createdAt", UNSET)
        created_at: datetime.datetime | Unset
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = datetime.datetime.fromisoformat(_created_at)

        _updated_at = d.pop("updatedAt", UNSET)
        updated_at: datetime.datetime | Unset
        if isinstance(_updated_at, Unset):
            updated_at = UNSET
        else:
            updated_at = datetime.datetime.fromisoformat(_updated_at)

        app_notebook_entry = cls(
            id=id,
            type_=type_,
            book_id=book_id,
            text=text,
            note=note,
            color=color,
            style=style,
            chapter_title=chapter_title,
            created_at=created_at,
            updated_at=updated_at,
        )

        app_notebook_entry.additional_properties = d
        return app_notebook_entry

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
