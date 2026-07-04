from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BookdropBulkEditResult")


@_attrs_define
class BookdropBulkEditResult:
    """
    Attributes:
        total_files (int | Unset):
        successfully_updated (int | Unset):
        failed (int | Unset):
    """

    total_files: int | Unset = UNSET
    successfully_updated: int | Unset = UNSET
    failed: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        total_files = self.total_files

        successfully_updated = self.successfully_updated

        failed = self.failed

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if total_files is not UNSET:
            field_dict["totalFiles"] = total_files
        if successfully_updated is not UNSET:
            field_dict["successfullyUpdated"] = successfully_updated
        if failed is not UNSET:
            field_dict["failed"] = failed

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        total_files = d.pop("totalFiles", UNSET)

        successfully_updated = d.pop("successfullyUpdated", UNSET)

        failed = d.pop("failed", UNSET)

        bookdrop_bulk_edit_result = cls(
            total_files=total_files,
            successfully_updated=successfully_updated,
            failed=failed,
        )

        bookdrop_bulk_edit_result.additional_properties = d
        return bookdrop_bulk_edit_result

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
