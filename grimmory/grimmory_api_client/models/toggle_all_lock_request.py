from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.toggle_all_lock_request_lock import ToggleAllLockRequestLock
from ..types import UNSET, Unset

T = TypeVar("T", bound="ToggleAllLockRequest")


@_attrs_define
class ToggleAllLockRequest:
    """Toggle all lock request

    Attributes:
        book_ids (list[int] | Unset):
        lock (ToggleAllLockRequestLock | Unset):
    """

    book_ids: list[int] | Unset = UNSET
    lock: ToggleAllLockRequestLock | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        book_ids: list[int] | Unset = UNSET
        if not isinstance(self.book_ids, Unset):
            book_ids = self.book_ids

        lock: str | Unset = UNSET
        if not isinstance(self.lock, Unset):
            lock = self.lock.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if book_ids is not UNSET:
            field_dict["bookIds"] = book_ids
        if lock is not UNSET:
            field_dict["lock"] = lock

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        book_ids = cast(list[int], d.pop("bookIds", UNSET))

        _lock = d.pop("lock", UNSET)
        lock: ToggleAllLockRequestLock | Unset
        if isinstance(_lock, Unset):
            lock = UNSET
        else:
            lock = ToggleAllLockRequestLock(_lock)

        toggle_all_lock_request = cls(
            book_ids=book_ids,
            lock=lock,
        )

        toggle_all_lock_request.additional_properties = d
        return toggle_all_lock_request

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
