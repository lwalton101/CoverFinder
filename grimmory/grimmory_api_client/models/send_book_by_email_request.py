from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SendBookByEmailRequest")


@_attrs_define
class SendBookByEmailRequest:
    """Send book by email request

    Attributes:
        book_id (int):
        provider_id (int):
        recipient_id (int):
        book_file_id (int | Unset):
    """

    book_id: int
    provider_id: int
    recipient_id: int
    book_file_id: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        book_id = self.book_id

        provider_id = self.provider_id

        recipient_id = self.recipient_id

        book_file_id = self.book_file_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "bookId": book_id,
                "providerId": provider_id,
                "recipientId": recipient_id,
            }
        )
        if book_file_id is not UNSET:
            field_dict["bookFileId"] = book_file_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        book_id = d.pop("bookId")

        provider_id = d.pop("providerId")

        recipient_id = d.pop("recipientId")

        book_file_id = d.pop("bookFileId", UNSET)

        send_book_by_email_request = cls(
            book_id=book_id,
            provider_id=provider_id,
            recipient_id=recipient_id,
            book_file_id=book_file_id,
        )

        send_book_by_email_request.additional_properties = d
        return send_book_by_email_request

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
