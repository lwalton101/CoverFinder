from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.completion_timeline_response_status_breakdown import CompletionTimelineResponseStatusBreakdown


T = TypeVar("T", bound="CompletionTimelineResponse")


@_attrs_define
class CompletionTimelineResponse:
    """
    Attributes:
        year (int | Unset):
        month (int | Unset):
        total_books (int | Unset):
        status_breakdown (CompletionTimelineResponseStatusBreakdown | Unset):
        finished_books (int | Unset):
        completion_rate (float | Unset):
    """

    year: int | Unset = UNSET
    month: int | Unset = UNSET
    total_books: int | Unset = UNSET
    status_breakdown: CompletionTimelineResponseStatusBreakdown | Unset = UNSET
    finished_books: int | Unset = UNSET
    completion_rate: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        year = self.year

        month = self.month

        total_books = self.total_books

        status_breakdown: dict[str, Any] | Unset = UNSET
        if not isinstance(self.status_breakdown, Unset):
            status_breakdown = self.status_breakdown.to_dict()

        finished_books = self.finished_books

        completion_rate = self.completion_rate

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if year is not UNSET:
            field_dict["year"] = year
        if month is not UNSET:
            field_dict["month"] = month
        if total_books is not UNSET:
            field_dict["totalBooks"] = total_books
        if status_breakdown is not UNSET:
            field_dict["statusBreakdown"] = status_breakdown
        if finished_books is not UNSET:
            field_dict["finishedBooks"] = finished_books
        if completion_rate is not UNSET:
            field_dict["completionRate"] = completion_rate

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.completion_timeline_response_status_breakdown import CompletionTimelineResponseStatusBreakdown

        d = dict(src_dict)
        year = d.pop("year", UNSET)

        month = d.pop("month", UNSET)

        total_books = d.pop("totalBooks", UNSET)

        _status_breakdown = d.pop("statusBreakdown", UNSET)
        status_breakdown: CompletionTimelineResponseStatusBreakdown | Unset
        if isinstance(_status_breakdown, Unset):
            status_breakdown = UNSET
        else:
            status_breakdown = CompletionTimelineResponseStatusBreakdown.from_dict(_status_breakdown)

        finished_books = d.pop("finishedBooks", UNSET)

        completion_rate = d.pop("completionRate", UNSET)

        completion_timeline_response = cls(
            year=year,
            month=month,
            total_books=total_books,
            status_breakdown=status_breakdown,
            finished_books=finished_books,
            completion_rate=completion_rate,
        )

        completion_timeline_response.additional_properties = d
        return completion_timeline_response

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
