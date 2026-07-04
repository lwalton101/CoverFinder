from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ListeningAuthorResponse")


@_attrs_define
class ListeningAuthorResponse:
    """
    Attributes:
        author (str | Unset):
        book_count (int | Unset):
        total_sessions (int | Unset):
        total_duration_seconds (int | Unset):
    """

    author: str | Unset = UNSET
    book_count: int | Unset = UNSET
    total_sessions: int | Unset = UNSET
    total_duration_seconds: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        author = self.author

        book_count = self.book_count

        total_sessions = self.total_sessions

        total_duration_seconds = self.total_duration_seconds

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if author is not UNSET:
            field_dict["author"] = author
        if book_count is not UNSET:
            field_dict["bookCount"] = book_count
        if total_sessions is not UNSET:
            field_dict["totalSessions"] = total_sessions
        if total_duration_seconds is not UNSET:
            field_dict["totalDurationSeconds"] = total_duration_seconds

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        author = d.pop("author", UNSET)

        book_count = d.pop("bookCount", UNSET)

        total_sessions = d.pop("totalSessions", UNSET)

        total_duration_seconds = d.pop("totalDurationSeconds", UNSET)

        listening_author_response = cls(
            author=author,
            book_count=book_count,
            total_sessions=total_sessions,
            total_duration_seconds=total_duration_seconds,
        )

        listening_author_response.additional_properties = d
        return listening_author_response

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
