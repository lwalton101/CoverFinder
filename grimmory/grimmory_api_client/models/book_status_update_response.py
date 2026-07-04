from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.book_status_update_response_read_status import BookStatusUpdateResponseReadStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="BookStatusUpdateResponse")


@_attrs_define
class BookStatusUpdateResponse:
    """
    Attributes:
        book_id (int | Unset):
        read_status (BookStatusUpdateResponseReadStatus | Unset):
        read_status_modified_time (datetime.datetime | Unset):
        date_finished (datetime.datetime | Unset):
    """

    book_id: int | Unset = UNSET
    read_status: BookStatusUpdateResponseReadStatus | Unset = UNSET
    read_status_modified_time: datetime.datetime | Unset = UNSET
    date_finished: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        book_id = self.book_id

        read_status: str | Unset = UNSET
        if not isinstance(self.read_status, Unset):
            read_status = self.read_status.value

        read_status_modified_time: str | Unset = UNSET
        if not isinstance(self.read_status_modified_time, Unset):
            read_status_modified_time = self.read_status_modified_time.isoformat()

        date_finished: str | Unset = UNSET
        if not isinstance(self.date_finished, Unset):
            date_finished = self.date_finished.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if book_id is not UNSET:
            field_dict["bookId"] = book_id
        if read_status is not UNSET:
            field_dict["readStatus"] = read_status
        if read_status_modified_time is not UNSET:
            field_dict["readStatusModifiedTime"] = read_status_modified_time
        if date_finished is not UNSET:
            field_dict["dateFinished"] = date_finished

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        book_id = d.pop("bookId", UNSET)

        _read_status = d.pop("readStatus", UNSET)
        read_status: BookStatusUpdateResponseReadStatus | Unset
        if isinstance(_read_status, Unset):
            read_status = UNSET
        else:
            read_status = BookStatusUpdateResponseReadStatus(_read_status)

        _read_status_modified_time = d.pop("readStatusModifiedTime", UNSET)
        read_status_modified_time: datetime.datetime | Unset
        if isinstance(_read_status_modified_time, Unset):
            read_status_modified_time = UNSET
        else:
            read_status_modified_time = datetime.datetime.fromisoformat(_read_status_modified_time)

        _date_finished = d.pop("dateFinished", UNSET)
        date_finished: datetime.datetime | Unset
        if isinstance(_date_finished, Unset):
            date_finished = UNSET
        else:
            date_finished = datetime.datetime.fromisoformat(_date_finished)

        book_status_update_response = cls(
            book_id=book_id,
            read_status=read_status,
            read_status_modified_time=read_status_modified_time,
            date_finished=date_finished,
        )

        book_status_update_response.additional_properties = d
        return book_status_update_response

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
