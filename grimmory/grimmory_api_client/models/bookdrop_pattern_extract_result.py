from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.file_extraction_result import FileExtractionResult


T = TypeVar("T", bound="BookdropPatternExtractResult")


@_attrs_define
class BookdropPatternExtractResult:
    """
    Attributes:
        total_files (int | Unset):
        successfully_extracted (int | Unset):
        failed (int | Unset):
        results (list[FileExtractionResult] | Unset):
    """

    total_files: int | Unset = UNSET
    successfully_extracted: int | Unset = UNSET
    failed: int | Unset = UNSET
    results: list[FileExtractionResult] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        total_files = self.total_files

        successfully_extracted = self.successfully_extracted

        failed = self.failed

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
        if successfully_extracted is not UNSET:
            field_dict["successfullyExtracted"] = successfully_extracted
        if failed is not UNSET:
            field_dict["failed"] = failed
        if results is not UNSET:
            field_dict["results"] = results

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.file_extraction_result import FileExtractionResult

        d = dict(src_dict)
        total_files = d.pop("totalFiles", UNSET)

        successfully_extracted = d.pop("successfullyExtracted", UNSET)

        failed = d.pop("failed", UNSET)

        _results = d.pop("results", UNSET)
        results: list[FileExtractionResult] | Unset = UNSET
        if _results is not UNSET:
            results = []
            for results_item_data in _results:
                results_item = FileExtractionResult.from_dict(results_item_data)

                results.append(results_item)

        bookdrop_pattern_extract_result = cls(
            total_files=total_files,
            successfully_extracted=successfully_extracted,
            failed=failed,
            results=results,
        )

        bookdrop_pattern_extract_result.additional_properties = d
        return bookdrop_pattern_extract_result

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
