from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateBookMarkRequest")


@_attrs_define
class UpdateBookMarkRequest:
    """Bookmark update request

    Attributes:
        title (str | Unset):
        cfi (str | Unset):
        color (str | Unset):
        notes (str | Unset):
        priority (int | Unset):
        page_number (int | Unset):
    """

    title: str | Unset = UNSET
    cfi: str | Unset = UNSET
    color: str | Unset = UNSET
    notes: str | Unset = UNSET
    priority: int | Unset = UNSET
    page_number: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        title = self.title

        cfi = self.cfi

        color = self.color

        notes = self.notes

        priority = self.priority

        page_number = self.page_number

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if title is not UNSET:
            field_dict["title"] = title
        if cfi is not UNSET:
            field_dict["cfi"] = cfi
        if color is not UNSET:
            field_dict["color"] = color
        if notes is not UNSET:
            field_dict["notes"] = notes
        if priority is not UNSET:
            field_dict["priority"] = priority
        if page_number is not UNSET:
            field_dict["pageNumber"] = page_number

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        title = d.pop("title", UNSET)

        cfi = d.pop("cfi", UNSET)

        color = d.pop("color", UNSET)

        notes = d.pop("notes", UNSET)

        priority = d.pop("priority", UNSET)

        page_number = d.pop("pageNumber", UNSET)

        update_book_mark_request = cls(
            title=title,
            cfi=cfi,
            color=color,
            notes=notes,
            priority=priority,
            page_number=page_number,
        )

        update_book_mark_request.additional_properties = d
        return update_book_mark_request

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
