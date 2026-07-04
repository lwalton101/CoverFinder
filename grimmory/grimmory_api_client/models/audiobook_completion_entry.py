from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AudiobookCompletionEntry")


@_attrs_define
class AudiobookCompletionEntry:
    """
    Attributes:
        book_id (int | Unset):
        title (str | Unset):
        progress_percent (float | Unset):
        total_duration_seconds (int | Unset):
        listened_duration_seconds (int | Unset):
    """

    book_id: int | Unset = UNSET
    title: str | Unset = UNSET
    progress_percent: float | Unset = UNSET
    total_duration_seconds: int | Unset = UNSET
    listened_duration_seconds: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        book_id = self.book_id

        title = self.title

        progress_percent = self.progress_percent

        total_duration_seconds = self.total_duration_seconds

        listened_duration_seconds = self.listened_duration_seconds

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if book_id is not UNSET:
            field_dict["bookId"] = book_id
        if title is not UNSET:
            field_dict["title"] = title
        if progress_percent is not UNSET:
            field_dict["progressPercent"] = progress_percent
        if total_duration_seconds is not UNSET:
            field_dict["totalDurationSeconds"] = total_duration_seconds
        if listened_duration_seconds is not UNSET:
            field_dict["listenedDurationSeconds"] = listened_duration_seconds

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        book_id = d.pop("bookId", UNSET)

        title = d.pop("title", UNSET)

        progress_percent = d.pop("progressPercent", UNSET)

        total_duration_seconds = d.pop("totalDurationSeconds", UNSET)

        listened_duration_seconds = d.pop("listenedDurationSeconds", UNSET)

        audiobook_completion_entry = cls(
            book_id=book_id,
            title=title,
            progress_percent=progress_percent,
            total_duration_seconds=total_duration_seconds,
            listened_duration_seconds=listened_duration_seconds,
        )

        audiobook_completion_entry.additional_properties = d
        return audiobook_completion_entry

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
