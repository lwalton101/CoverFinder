from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.reading_streak_day import ReadingStreakDay


T = TypeVar("T", bound="ReadingStreakResponse")


@_attrs_define
class ReadingStreakResponse:
    """
    Attributes:
        current_streak (int | Unset):
        longest_streak (int | Unset):
        total_reading_days (int | Unset):
        last_52_weeks (list[ReadingStreakDay] | Unset):
    """

    current_streak: int | Unset = UNSET
    longest_streak: int | Unset = UNSET
    total_reading_days: int | Unset = UNSET
    last_52_weeks: list[ReadingStreakDay] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        current_streak = self.current_streak

        longest_streak = self.longest_streak

        total_reading_days = self.total_reading_days

        last_52_weeks: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.last_52_weeks, Unset):
            last_52_weeks = []
            for last_52_weeks_item_data in self.last_52_weeks:
                last_52_weeks_item = last_52_weeks_item_data.to_dict()
                last_52_weeks.append(last_52_weeks_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if current_streak is not UNSET:
            field_dict["currentStreak"] = current_streak
        if longest_streak is not UNSET:
            field_dict["longestStreak"] = longest_streak
        if total_reading_days is not UNSET:
            field_dict["totalReadingDays"] = total_reading_days
        if last_52_weeks is not UNSET:
            field_dict["last52Weeks"] = last_52_weeks

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.reading_streak_day import ReadingStreakDay

        d = dict(src_dict)
        current_streak = d.pop("currentStreak", UNSET)

        longest_streak = d.pop("longestStreak", UNSET)

        total_reading_days = d.pop("totalReadingDays", UNSET)

        _last_52_weeks = d.pop("last52Weeks", UNSET)
        last_52_weeks: list[ReadingStreakDay] | Unset = UNSET
        if _last_52_weeks is not UNSET:
            last_52_weeks = []
            for last_52_weeks_item_data in _last_52_weeks:
                last_52_weeks_item = ReadingStreakDay.from_dict(last_52_weeks_item_data)

                last_52_weeks.append(last_52_weeks_item)

        reading_streak_response = cls(
            current_streak=current_streak,
            longest_streak=longest_streak,
            total_reading_days=total_reading_days,
            last_52_weeks=last_52_weeks,
        )

        reading_streak_response.additional_properties = d
        return reading_streak_response

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
