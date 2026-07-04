from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.reading_session_request_book_type import ReadingSessionRequestBookType
from ..types import UNSET, Unset

T = TypeVar("T", bound="ReadingSessionRequest")


@_attrs_define
class ReadingSessionRequest:
    """
    Attributes:
        book_id (int):
        start_time (datetime.datetime):
        end_time (datetime.datetime):
        duration_seconds (int):
        book_type (ReadingSessionRequestBookType | Unset):
        duration_formatted (str | Unset):
        start_progress (float | Unset):
        end_progress (float | Unset):
        progress_delta (float | Unset):
        start_location (str | Unset):
        end_location (str | Unset):
    """

    book_id: int
    start_time: datetime.datetime
    end_time: datetime.datetime
    duration_seconds: int
    book_type: ReadingSessionRequestBookType | Unset = UNSET
    duration_formatted: str | Unset = UNSET
    start_progress: float | Unset = UNSET
    end_progress: float | Unset = UNSET
    progress_delta: float | Unset = UNSET
    start_location: str | Unset = UNSET
    end_location: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        book_id = self.book_id

        start_time = self.start_time.isoformat()

        end_time = self.end_time.isoformat()

        duration_seconds = self.duration_seconds

        book_type: str | Unset = UNSET
        if not isinstance(self.book_type, Unset):
            book_type = self.book_type.value

        duration_formatted = self.duration_formatted

        start_progress = self.start_progress

        end_progress = self.end_progress

        progress_delta = self.progress_delta

        start_location = self.start_location

        end_location = self.end_location

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "bookId": book_id,
                "startTime": start_time,
                "endTime": end_time,
                "durationSeconds": duration_seconds,
            }
        )
        if book_type is not UNSET:
            field_dict["bookType"] = book_type
        if duration_formatted is not UNSET:
            field_dict["durationFormatted"] = duration_formatted
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

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        book_id = d.pop("bookId")

        start_time = datetime.datetime.fromisoformat(d.pop("startTime"))

        end_time = datetime.datetime.fromisoformat(d.pop("endTime"))

        duration_seconds = d.pop("durationSeconds")

        _book_type = d.pop("bookType", UNSET)
        book_type: ReadingSessionRequestBookType | Unset
        if isinstance(_book_type, Unset):
            book_type = UNSET
        else:
            book_type = ReadingSessionRequestBookType(_book_type)

        duration_formatted = d.pop("durationFormatted", UNSET)

        start_progress = d.pop("startProgress", UNSET)

        end_progress = d.pop("endProgress", UNSET)

        progress_delta = d.pop("progressDelta", UNSET)

        start_location = d.pop("startLocation", UNSET)

        end_location = d.pop("endLocation", UNSET)

        reading_session_request = cls(
            book_id=book_id,
            start_time=start_time,
            end_time=end_time,
            duration_seconds=duration_seconds,
            book_type=book_type,
            duration_formatted=duration_formatted,
            start_progress=start_progress,
            end_progress=end_progress,
            progress_delta=progress_delta,
            start_location=start_location,
            end_location=end_location,
        )

        reading_session_request.additional_properties = d
        return reading_session_request

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
