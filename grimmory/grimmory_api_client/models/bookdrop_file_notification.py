from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BookdropFileNotification")


@_attrs_define
class BookdropFileNotification:
    """
    Attributes:
        pending_count (int | Unset):
        total_count (int | Unset):
        last_updated_at (str | Unset):
    """

    pending_count: int | Unset = UNSET
    total_count: int | Unset = UNSET
    last_updated_at: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        pending_count = self.pending_count

        total_count = self.total_count

        last_updated_at = self.last_updated_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if pending_count is not UNSET:
            field_dict["pendingCount"] = pending_count
        if total_count is not UNSET:
            field_dict["totalCount"] = total_count
        if last_updated_at is not UNSET:
            field_dict["lastUpdatedAt"] = last_updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        pending_count = d.pop("pendingCount", UNSET)

        total_count = d.pop("totalCount", UNSET)

        last_updated_at = d.pop("lastUpdatedAt", UNSET)

        bookdrop_file_notification = cls(
            pending_count=pending_count,
            total_count=total_count,
            last_updated_at=last_updated_at,
        )

        bookdrop_file_notification.additional_properties = d
        return bookdrop_file_notification

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
