from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.reading_session_timeline_response_book_type import ReadingSessionTimelineResponseBookType
from ..types import UNSET, Unset

T = TypeVar("T", bound="ReadingSessionTimelineResponse")


@_attrs_define
class ReadingSessionTimelineResponse:
    """
    Attributes:
        book_id (int | Unset):
        book_title (str | Unset):
        book_type (ReadingSessionTimelineResponseBookType | Unset):
        start_date (datetime.datetime | Unset):
        end_date (datetime.datetime | Unset):
        total_sessions (int | Unset):
        total_duration_seconds (int | Unset):
    """

    book_id: int | Unset = UNSET
    book_title: str | Unset = UNSET
    book_type: ReadingSessionTimelineResponseBookType | Unset = UNSET
    start_date: datetime.datetime | Unset = UNSET
    end_date: datetime.datetime | Unset = UNSET
    total_sessions: int | Unset = UNSET
    total_duration_seconds: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        book_id = self.book_id

        book_title = self.book_title

        book_type: str | Unset = UNSET
        if not isinstance(self.book_type, Unset):
            book_type = self.book_type.value

        start_date: str | Unset = UNSET
        if not isinstance(self.start_date, Unset):
            start_date = self.start_date.isoformat()

        end_date: str | Unset = UNSET
        if not isinstance(self.end_date, Unset):
            end_date = self.end_date.isoformat()

        total_sessions = self.total_sessions

        total_duration_seconds = self.total_duration_seconds

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if book_id is not UNSET:
            field_dict["bookId"] = book_id
        if book_title is not UNSET:
            field_dict["bookTitle"] = book_title
        if book_type is not UNSET:
            field_dict["bookType"] = book_type
        if start_date is not UNSET:
            field_dict["startDate"] = start_date
        if end_date is not UNSET:
            field_dict["endDate"] = end_date
        if total_sessions is not UNSET:
            field_dict["totalSessions"] = total_sessions
        if total_duration_seconds is not UNSET:
            field_dict["totalDurationSeconds"] = total_duration_seconds

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        book_id = d.pop("bookId", UNSET)

        book_title = d.pop("bookTitle", UNSET)

        _book_type = d.pop("bookType", UNSET)
        book_type: ReadingSessionTimelineResponseBookType | Unset
        if isinstance(_book_type, Unset):
            book_type = UNSET
        else:
            book_type = ReadingSessionTimelineResponseBookType(_book_type)

        _start_date = d.pop("startDate", UNSET)
        start_date: datetime.datetime | Unset
        if isinstance(_start_date, Unset):
            start_date = UNSET
        else:
            start_date = datetime.datetime.fromisoformat(_start_date)

        _end_date = d.pop("endDate", UNSET)
        end_date: datetime.datetime | Unset
        if isinstance(_end_date, Unset):
            end_date = UNSET
        else:
            end_date = datetime.datetime.fromisoformat(_end_date)

        total_sessions = d.pop("totalSessions", UNSET)

        total_duration_seconds = d.pop("totalDurationSeconds", UNSET)

        reading_session_timeline_response = cls(
            book_id=book_id,
            book_title=book_title,
            book_type=book_type,
            start_date=start_date,
            end_date=end_date,
            total_sessions=total_sessions,
            total_duration_seconds=total_duration_seconds,
        )

        reading_session_timeline_response.additional_properties = d
        return reading_session_timeline_response

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
