from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BookDeletionResponse")


@_attrs_define
class BookDeletionResponse:
    """
    Attributes:
        deleted (list[int] | Unset):
        failed_file_deletions (list[int] | Unset):
    """

    deleted: list[int] | Unset = UNSET
    failed_file_deletions: list[int] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        deleted: list[int] | Unset = UNSET
        if not isinstance(self.deleted, Unset):
            deleted = self.deleted

        failed_file_deletions: list[int] | Unset = UNSET
        if not isinstance(self.failed_file_deletions, Unset):
            failed_file_deletions = self.failed_file_deletions

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if deleted is not UNSET:
            field_dict["deleted"] = deleted
        if failed_file_deletions is not UNSET:
            field_dict["failedFileDeletions"] = failed_file_deletions

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        deleted = cast(list[int], d.pop("deleted", UNSET))

        failed_file_deletions = cast(list[int], d.pop("failedFileDeletions", UNSET))

        book_deletion_response = cls(
            deleted=deleted,
            failed_file_deletions=failed_file_deletions,
        )

        book_deletion_response.additional_properties = d
        return book_deletion_response

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
