from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BookMark")


@_attrs_define
class BookMark:
    """
    Attributes:
        id (int | Unset):
        user_id (int | Unset):
        book_id (int | Unset):
        cfi (str | Unset):
        position_ms (int | Unset):
        track_index (int | Unset):
        page_number (int | Unset):
        title (str | Unset):
        color (str | Unset):
        notes (str | Unset):
        priority (int | Unset):
        created_at (datetime.datetime | Unset):
        updated_at (datetime.datetime | Unset):
    """

    id: int | Unset = UNSET
    user_id: int | Unset = UNSET
    book_id: int | Unset = UNSET
    cfi: str | Unset = UNSET
    position_ms: int | Unset = UNSET
    track_index: int | Unset = UNSET
    page_number: int | Unset = UNSET
    title: str | Unset = UNSET
    color: str | Unset = UNSET
    notes: str | Unset = UNSET
    priority: int | Unset = UNSET
    created_at: datetime.datetime | Unset = UNSET
    updated_at: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        user_id = self.user_id

        book_id = self.book_id

        cfi = self.cfi

        position_ms = self.position_ms

        track_index = self.track_index

        page_number = self.page_number

        title = self.title

        color = self.color

        notes = self.notes

        priority = self.priority

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
        if user_id is not UNSET:
            field_dict["userId"] = user_id
        if book_id is not UNSET:
            field_dict["bookId"] = book_id
        if cfi is not UNSET:
            field_dict["cfi"] = cfi
        if position_ms is not UNSET:
            field_dict["positionMs"] = position_ms
        if track_index is not UNSET:
            field_dict["trackIndex"] = track_index
        if page_number is not UNSET:
            field_dict["pageNumber"] = page_number
        if title is not UNSET:
            field_dict["title"] = title
        if color is not UNSET:
            field_dict["color"] = color
        if notes is not UNSET:
            field_dict["notes"] = notes
        if priority is not UNSET:
            field_dict["priority"] = priority
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if updated_at is not UNSET:
            field_dict["updatedAt"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        user_id = d.pop("userId", UNSET)

        book_id = d.pop("bookId", UNSET)

        cfi = d.pop("cfi", UNSET)

        position_ms = d.pop("positionMs", UNSET)

        track_index = d.pop("trackIndex", UNSET)

        page_number = d.pop("pageNumber", UNSET)

        title = d.pop("title", UNSET)

        color = d.pop("color", UNSET)

        notes = d.pop("notes", UNSET)

        priority = d.pop("priority", UNSET)

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

        book_mark = cls(
            id=id,
            user_id=user_id,
            book_id=book_id,
            cfi=cfi,
            position_ms=position_ms,
            track_index=track_index,
            page_number=page_number,
            title=title,
            color=color,
            notes=notes,
            priority=priority,
            created_at=created_at,
            updated_at=updated_at,
        )

        book_mark.additional_properties = d
        return book_mark

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
