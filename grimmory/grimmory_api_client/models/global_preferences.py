from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.sort_criterion import SortCriterion


T = TypeVar("T", bound="GlobalPreferences")


@_attrs_define
class GlobalPreferences:
    """
    Attributes:
        sort_key (str | Unset):
        sort_dir (str | Unset):
        sort_criteria (list[SortCriterion] | Unset):
        view (str | Unset):
        cover_size (float | Unset):
        series_collapsed (bool | Unset):
        overlay_book_type (bool | Unset):
    """

    sort_key: str | Unset = UNSET
    sort_dir: str | Unset = UNSET
    sort_criteria: list[SortCriterion] | Unset = UNSET
    view: str | Unset = UNSET
    cover_size: float | Unset = UNSET
    series_collapsed: bool | Unset = UNSET
    overlay_book_type: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        sort_key = self.sort_key

        sort_dir = self.sort_dir

        sort_criteria: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.sort_criteria, Unset):
            sort_criteria = []
            for sort_criteria_item_data in self.sort_criteria:
                sort_criteria_item = sort_criteria_item_data.to_dict()
                sort_criteria.append(sort_criteria_item)

        view = self.view

        cover_size = self.cover_size

        series_collapsed = self.series_collapsed

        overlay_book_type = self.overlay_book_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if sort_key is not UNSET:
            field_dict["sortKey"] = sort_key
        if sort_dir is not UNSET:
            field_dict["sortDir"] = sort_dir
        if sort_criteria is not UNSET:
            field_dict["sortCriteria"] = sort_criteria
        if view is not UNSET:
            field_dict["view"] = view
        if cover_size is not UNSET:
            field_dict["coverSize"] = cover_size
        if series_collapsed is not UNSET:
            field_dict["seriesCollapsed"] = series_collapsed
        if overlay_book_type is not UNSET:
            field_dict["overlayBookType"] = overlay_book_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.sort_criterion import SortCriterion

        d = dict(src_dict)
        sort_key = d.pop("sortKey", UNSET)

        sort_dir = d.pop("sortDir", UNSET)

        _sort_criteria = d.pop("sortCriteria", UNSET)
        sort_criteria: list[SortCriterion] | Unset = UNSET
        if _sort_criteria is not UNSET:
            sort_criteria = []
            for sort_criteria_item_data in _sort_criteria:
                sort_criteria_item = SortCriterion.from_dict(sort_criteria_item_data)

                sort_criteria.append(sort_criteria_item)

        view = d.pop("view", UNSET)

        cover_size = d.pop("coverSize", UNSET)

        series_collapsed = d.pop("seriesCollapsed", UNSET)

        overlay_book_type = d.pop("overlayBookType", UNSET)

        global_preferences = cls(
            sort_key=sort_key,
            sort_dir=sort_dir,
            sort_criteria=sort_criteria,
            view=view,
            cover_size=cover_size,
            series_collapsed=series_collapsed,
            overlay_book_type=overlay_book_type,
        )

        global_preferences.additional_properties = d
        return global_preferences

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
