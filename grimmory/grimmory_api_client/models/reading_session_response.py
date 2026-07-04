from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.reading_session_response_book_type import ReadingSessionResponseBookType
from ..types import UNSET, Unset

T = TypeVar("T", bound="ReadingSessionResponse")


@_attrs_define
class ReadingSessionResponse:
    """
    Attributes:
        id (int | Unset):
        book_id (int | Unset):
        book_title (str | Unset):
        book_type (ReadingSessionResponseBookType | Unset):
        start_time (datetime.datetime | Unset):
        end_time (datetime.datetime | Unset):
        duration_seconds (int | Unset):
        start_progress (float | Unset):
        end_progress (float | Unset):
        progress_delta (float | Unset):
        start_location (str | Unset):
        end_location (str | Unset):
        created_at (datetime.datetime | Unset):
    """

    id: int | Unset = UNSET
    book_id: int | Unset = UNSET
    book_title: str | Unset = UNSET
    book_type: ReadingSessionResponseBookType | Unset = UNSET
    start_time: datetime.datetime | Unset = UNSET
    end_time: datetime.datetime | Unset = UNSET
    duration_seconds: int | Unset = UNSET
    start_progress: float | Unset = UNSET
    end_progress: float | Unset = UNSET
    progress_delta: float | Unset = UNSET
    start_location: str | Unset = UNSET
    end_location: str | Unset = UNSET
    created_at: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        book_id = self.book_id

        book_title = self.book_title

        book_type: str | Unset = UNSET
        if not isinstance(self.book_type, Unset):
            book_type = self.book_type.value

        start_time: str | Unset = UNSET
        if not isinstance(self.start_time, Unset):
            start_time = self.start_time.isoformat()

        end_time: str | Unset = UNSET
        if not isinstance(self.end_time, Unset):
            end_time = self.end_time.isoformat()

        duration_seconds = self.duration_seconds

        start_progress = self.start_progress

        end_progress = self.end_progress

        progress_delta = self.progress_delta

        start_location = self.start_location

        end_location = self.end_location

        created_at: str | Unset = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if book_id is not UNSET:
            field_dict["bookId"] = book_id
        if book_title is not UNSET:
            field_dict["bookTitle"] = book_title
        if book_type is not UNSET:
            field_dict["bookType"] = book_type
        if start_time is not UNSET:
            field_dict["startTime"] = start_time
        if end_time is not UNSET:
            field_dict["endTime"] = end_time
        if duration_seconds is not UNSET:
            field_dict["durationSeconds"] = duration_seconds
        if start_progress is not UNSET:
            field_dict["startProgress"] = start_progress
        if end_progress is not UNSET:
            field_dict["endProgress"] = end_progress
        if progress_delta is not UNSET:
            field_dict["progressDelta"] = progress_delta
        if start_location is not UNSET:
            field_dict["startLocation"] = start_location
        if end_location is not UNSET:
            field_dict["endLocation"] = end_location
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        book_id = d.pop("bookId", UNSET)

        book_title = d.pop("bookTitle", UNSET)

        _book_type = d.pop("bookType", UNSET)
        book_type: ReadingSessionResponseBookType | Unset
        if isinstance(_book_type, Unset):
            book_type = UNSET
        else:
            book_type = ReadingSessionResponseBookType(_book_type)

        _start_time = d.pop("startTime", UNSET)
        start_time: datetime.datetime | Unset
        if isinstance(_start_time, Unset):
            start_time = UNSET
        else:
            start_time = datetime.datetime.fromisoformat(_start_time)

        _end_time = d.pop("endTime", UNSET)
        end_time: datetime.datetime | Unset
        if isinstance(_end_time, Unset):
            end_time = UNSET
        else:
            end_time = datetime.datetime.fromisoformat(_end_time)

        duration_seconds = d.pop("durationSeconds", UNSET)

        start_progress = d.pop("startProgress", UNSET)

        end_progress = d.pop("endProgress", UNSET)

        progress_delta = d.pop("progressDelta", UNSET)

        start_location = d.pop("startLocation", UNSET)

        end_location = d.pop("endLocation", UNSET)

        _created_at = d.pop("createdAt", UNSET)
        created_at: datetime.datetime | Unset
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = datetime.datetime.fromisoformat(_created_at)

        reading_session_response = cls(
            id=id,
            book_id=book_id,
            book_title=book_title,
            book_type=book_type,
            start_time=start_time,
            end_time=end_time,
            duration_seconds=duration_seconds,
            start_progress=start_progress,
            end_progress=end_progress,
            progress_delta=progress_delta,
            start_location=start_location,
            end_location=end_location,
            created_at=created_at,
        )

        reading_session_response.additional_properties = d
        return reading_session_response

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
