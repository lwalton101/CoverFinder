from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BookTimelineResponse")


@_attrs_define
class BookTimelineResponse:
    """
    Attributes:
        book_id (int | Unset):
        title (str | Unset):
        page_count (int | Unset):
        first_session_date (datetime.date | Unset):
        last_session_date (datetime.date | Unset):
        total_sessions (int | Unset):
        total_duration_seconds (int | Unset):
        max_progress (float | Unset):
        read_status (str | Unset):
    """

    book_id: int | Unset = UNSET
    title: str | Unset = UNSET
    page_count: int | Unset = UNSET
    first_session_date: datetime.date | Unset = UNSET
    last_session_date: datetime.date | Unset = UNSET
    total_sessions: int | Unset = UNSET
    total_duration_seconds: int | Unset = UNSET
    max_progress: float | Unset = UNSET
    read_status: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        book_id = self.book_id

        title = self.title

        page_count = self.page_count

        first_session_date: str | Unset = UNSET
        if not isinstance(self.first_session_date, Unset):
            first_session_date = self.first_session_date.isoformat()

        last_session_date: str | Unset = UNSET
        if not isinstance(self.last_session_date, Unset):
            last_session_date = self.last_session_date.isoformat()

        total_sessions = self.total_sessions

        total_duration_seconds = self.total_duration_seconds

        max_progress = self.max_progress

        read_status = self.read_status

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if book_id is not UNSET:
            field_dict["bookId"] = book_id
        if title is not UNSET:
            field_dict["title"] = title
        if page_count is not UNSET:
            field_dict["pageCount"] = page_count
        if first_session_date is not UNSET:
            field_dict["firstSessionDate"] = first_session_date
        if last_session_date is not UNSET:
            field_dict["lastSessionDate"] = last_session_date
        if total_sessions is not UNSET:
            field_dict["totalSessions"] = total_sessions
        if total_duration_seconds is not UNSET:
            field_dict["totalDurationSeconds"] = total_duration_seconds
        if max_progress is not UNSET:
            field_dict["maxProgress"] = max_progress
        if read_status is not UNSET:
            field_dict["readStatus"] = read_status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        book_id = d.pop("bookId", UNSET)

        title = d.pop("title", UNSET)

        page_count = d.pop("pageCount", UNSET)

        _first_session_date = d.pop("firstSessionDate", UNSET)
        first_session_date: datetime.date | Unset
        if isinstance(_first_session_date, Unset):
            first_session_date = UNSET
        else:
            first_session_date = datetime.date.fromisoformat(_first_session_date)

        _last_session_date = d.pop("lastSessionDate", UNSET)
        last_session_date: datetime.date | Unset
        if isinstance(_last_session_date, Unset):
            last_session_date = UNSET
        else:
            last_session_date = datetime.date.fromisoformat(_last_session_date)

        total_sessions = d.pop("totalSessions", UNSET)

        total_duration_seconds = d.pop("totalDurationSeconds", UNSET)

        max_progress = d.pop("maxProgress", UNSET)

        read_status = d.pop("readStatus", UNSET)

        book_timeline_response = cls(
            book_id=book_id,
            title=title,
            page_count=page_count,
            first_session_date=first_session_date,
            last_session_date=last_session_date,
            total_sessions=total_sessions,
            total_duration_seconds=total_duration_seconds,
            max_progress=max_progress,
            read_status=read_status,
        )

        book_timeline_response.additional_properties = d
        return book_timeline_response

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
