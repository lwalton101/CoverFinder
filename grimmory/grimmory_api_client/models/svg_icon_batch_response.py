from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.icon_save_result import IconSaveResult


T = TypeVar("T", bound="SvgIconBatchResponse")


@_attrs_define
class SvgIconBatchResponse:
    """
    Attributes:
        total_requested (int | Unset):
        success_count (int | Unset):
        failure_count (int | Unset):
        results (list[IconSaveResult] | Unset):
    """

    total_requested: int | Unset = UNSET
    success_count: int | Unset = UNSET
    failure_count: int | Unset = UNSET
    results: list[IconSaveResult] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        total_requested = self.total_requested

        success_count = self.success_count

        failure_count = self.failure_count

        results: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.results, Unset):
            results = []
            for results_item_data in self.results:
                results_item = results_item_data.to_dict()
                results.append(results_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if total_requested is not UNSET:
            field_dict["totalRequested"] = total_requested
        if success_count is not UNSET:
            field_dict["successCount"] = success_count
        if failure_count is not UNSET:
            field_dict["failureCount"] = failure_count
        if results is not UNSET:
            field_dict["results"] = results

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.icon_save_result import IconSaveResult

        d = dict(src_dict)
        total_requested = d.pop("totalRequested", UNSET)

        success_count = d.pop("successCount", UNSET)

        failure_count = d.pop("failureCount", UNSET)

        _results = d.pop("results", UNSET)
        results: list[IconSaveResult] | Unset = UNSET
        if _results is not UNSET:
            results = []
            for results_item_data in _results:
                results_item = IconSaveResult.from_dict(results_item_data)

                results.append(results_item)

        svg_icon_batch_response = cls(
            total_requested=total_requested,
            success_count=success_count,
            failure_count=failure_count,
            results=results,
        )

        svg_icon_batch_response.additional_properties = d
        return svg_icon_batch_response

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
