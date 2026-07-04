from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PageTurnerScoreResponse")


@_attrs_define
class PageTurnerScoreResponse:
    """
    Attributes:
        book_id (int | Unset):
        book_title (str | Unset):
        categories (list[str] | Unset):
        page_count (int | Unset):
        personal_rating (int | Unset):
        grip_score (int | Unset):
        total_sessions (int | Unset):
        avg_session_duration_seconds (float | Unset):
        session_acceleration (float | Unset):
        gap_reduction (float | Unset):
        finish_burst (bool | Unset):
    """

    book_id: int | Unset = UNSET
    book_title: str | Unset = UNSET
    categories: list[str] | Unset = UNSET
    page_count: int | Unset = UNSET
    personal_rating: int | Unset = UNSET
    grip_score: int | Unset = UNSET
    total_sessions: int | Unset = UNSET
    avg_session_duration_seconds: float | Unset = UNSET
    session_acceleration: float | Unset = UNSET
    gap_reduction: float | Unset = UNSET
    finish_burst: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        book_id = self.book_id

        book_title = self.book_title

        categories: list[str] | Unset = UNSET
        if not isinstance(self.categories, Unset):
            categories = self.categories

        page_count = self.page_count

        personal_rating = self.personal_rating

        grip_score = self.grip_score

        total_sessions = self.total_sessions

        avg_session_duration_seconds = self.avg_session_duration_seconds

        session_acceleration = self.session_acceleration

        gap_reduction = self.gap_reduction

        finish_burst = self.finish_burst

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if book_id is not UNSET:
            field_dict["bookId"] = book_id
        if book_title is not UNSET:
            field_dict["bookTitle"] = book_title
        if categories is not UNSET:
            field_dict["categories"] = categories
        if page_count is not UNSET:
            field_dict["pageCount"] = page_count
        if personal_rating is not UNSET:
            field_dict["personalRating"] = personal_rating
        if grip_score is not UNSET:
            field_dict["gripScore"] = grip_score
        if total_sessions is not UNSET:
            field_dict["totalSessions"] = total_sessions
        if avg_session_duration_seconds is not UNSET:
            field_dict["avgSessionDurationSeconds"] = avg_session_duration_seconds
        if session_acceleration is not UNSET:
            field_dict["sessionAcceleration"] = session_acceleration
        if gap_reduction is not UNSET:
            field_dict["gapReduction"] = gap_reduction
        if finish_burst is not UNSET:
            field_dict["finishBurst"] = finish_burst

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        book_id = d.pop("bookId", UNSET)

        book_title = d.pop("bookTitle", UNSET)

        categories = cast(list[str], d.pop("categories", UNSET))

        page_count = d.pop("pageCount", UNSET)

        personal_rating = d.pop("personalRating", UNSET)

        grip_score = d.pop("gripScore", UNSET)

        total_sessions = d.pop("totalSessions", UNSET)

        avg_session_duration_seconds = d.pop("avgSessionDurationSeconds", UNSET)

        session_acceleration = d.pop("sessionAcceleration", UNSET)

        gap_reduction = d.pop("gapReduction", UNSET)

        finish_burst = d.pop("finishBurst", UNSET)

        page_turner_score_response = cls(
            book_id=book_id,
            book_title=book_title,
            categories=categories,
            page_count=page_count,
            personal_rating=personal_rating,
            grip_score=grip_score,
            total_sessions=total_sessions,
            avg_session_duration_seconds=avg_session_duration_seconds,
            session_acceleration=session_acceleration,
            gap_reduction=gap_reduction,
            finish_burst=finish_burst,
        )

        page_turner_score_response.additional_properties = d
        return page_turner_score_response

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
