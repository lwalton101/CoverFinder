from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GenreStatisticsResponse")


@_attrs_define
class GenreStatisticsResponse:
    """
    Attributes:
        genre (str | Unset):
        book_count (int | Unset):
        total_sessions (int | Unset):
        total_duration_seconds (int | Unset):
        average_sessions_per_book (float | Unset):
    """

    genre: str | Unset = UNSET
    book_count: int | Unset = UNSET
    total_sessions: int | Unset = UNSET
    total_duration_seconds: int | Unset = UNSET
    average_sessions_per_book: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        genre = self.genre

        book_count = self.book_count

        total_sessions = self.total_sessions

        total_duration_seconds = self.total_duration_seconds

        average_sessions_per_book = self.average_sessions_per_book

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if genre is not UNSET:
            field_dict["genre"] = genre
        if book_count is not UNSET:
            field_dict["bookCount"] = book_count
        if total_sessions is not UNSET:
            field_dict["totalSessions"] = total_sessions
        if total_duration_seconds is not UNSET:
            field_dict["totalDurationSeconds"] = total_duration_seconds
        if average_sessions_per_book is not UNSET:
            field_dict["averageSessionsPerBook"] = average_sessions_per_book

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        genre = d.pop("genre", UNSET)

        book_count = d.pop("bookCount", UNSET)

        total_sessions = d.pop("totalSessions", UNSET)

        total_duration_seconds = d.pop("totalDurationSeconds", UNSET)

        average_sessions_per_book = d.pop("averageSessionsPerBook", UNSET)

        genre_statistics_response = cls(
            genre=genre,
            book_count=book_count,
            total_sessions=total_sessions,
            total_duration_seconds=total_duration_seconds,
            average_sessions_per_book=average_sessions_per_book,
        )

        genre_statistics_response.additional_properties = d
        return genre_statistics_response

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
