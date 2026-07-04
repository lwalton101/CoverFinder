from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CompletionRaceResponse")


@_attrs_define
class CompletionRaceResponse:
    """
    Attributes:
        book_id (int | Unset):
        book_title (str | Unset):
        session_date (datetime.datetime | Unset):
        end_progress (float | Unset):
    """

    book_id: int | Unset = UNSET
    book_title: str | Unset = UNSET
    session_date: datetime.datetime | Unset = UNSET
    end_progress: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        book_id = self.book_id

        book_title = self.book_title

        session_date: str | Unset = UNSET
        if not isinstance(self.session_date, Unset):
            session_date = self.session_date.isoformat()

        end_progress = self.end_progress

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if book_id is not UNSET:
            field_dict["bookId"] = book_id
        if book_title is not UNSET:
            field_dict["bookTitle"] = book_title
        if session_date is not UNSET:
            field_dict["sessionDate"] = session_date
        if end_progress is not UNSET:
            field_dict["endProgress"] = end_progress

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        book_id = d.pop("bookId", UNSET)

        book_title = d.pop("bookTitle", UNSET)

        _session_date = d.pop("sessionDate", UNSET)
        session_date: datetime.datetime | Unset
        if isinstance(_session_date, Unset):
            session_date = UNSET
        else:
            session_date = datetime.datetime.fromisoformat(_session_date)

        end_progress = d.pop("endProgress", UNSET)

        completion_race_response = cls(
            book_id=book_id,
            book_title=book_title,
            session_date=session_date,
            end_progress=end_progress,
        )

        completion_race_response.additional_properties = d
        return completion_race_response

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
