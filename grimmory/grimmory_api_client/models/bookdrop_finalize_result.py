from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bookdrop_file_result import BookdropFileResult


T = TypeVar("T", bound="BookdropFinalizeResult")


@_attrs_define
class BookdropFinalizeResult:
    """
    Attributes:
        total_files (int | Unset):
        successfully_imported (int | Unset):
        failed (int | Unset):
        processed_at (datetime.datetime | Unset):
        results (list[BookdropFileResult] | Unset):
    """

    total_files: int | Unset = UNSET
    successfully_imported: int | Unset = UNSET
    failed: int | Unset = UNSET
    processed_at: datetime.datetime | Unset = UNSET
    results: list[BookdropFileResult] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        total_files = self.total_files

        successfully_imported = self.successfully_imported

        failed = self.failed

        processed_at: str | Unset = UNSET
        if not isinstance(self.processed_at, Unset):
            processed_at = self.processed_at.isoformat()

        results: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.results, Unset):
            results = []
            for results_item_data in self.results:
                results_item = results_item_data.to_dict()
                results.append(results_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if total_files is not UNSET:
            field_dict["totalFiles"] = total_files
        if successfully_imported is not UNSET:
            field_dict["successfullyImported"] = successfully_imported
        if failed is not UNSET:
            field_dict["failed"] = failed
        if processed_at is not UNSET:
            field_dict["processedAt"] = processed_at
        if results is not UNSET:
            field_dict["results"] = results

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bookdrop_file_result import BookdropFileResult

        d = dict(src_dict)
        total_files = d.pop("totalFiles", UNSET)

        successfully_imported = d.pop("successfullyImported", UNSET)

        failed = d.pop("failed", UNSET)

        _processed_at = d.pop("processedAt", UNSET)
        processed_at: datetime.datetime | Unset
        if isinstance(_processed_at, Unset):
            processed_at = UNSET
        else:
            processed_at = datetime.datetime.fromisoformat(_processed_at)

        _results = d.pop("results", UNSET)
        results: list[BookdropFileResult] | Unset = UNSET
        if _results is not UNSET:
            results = []
            for results_item_data in _results:
                results_item = BookdropFileResult.from_dict(results_item_data)

                results.append(results_item)

        bookdrop_finalize_result = cls(
            total_files=total_files,
            successfully_imported=successfully_imported,
            failed=failed,
            processed_at=processed_at,
            results=results,
        )

        bookdrop_finalize_result.additional_properties = d
        return bookdrop_finalize_result

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
