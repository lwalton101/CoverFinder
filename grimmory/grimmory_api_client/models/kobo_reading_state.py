from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.current_bookmark import CurrentBookmark
    from ..models.statistics import Statistics
    from ..models.status_info import StatusInfo


T = TypeVar("T", bound="KoboReadingState")


@_attrs_define
class KoboReadingState:
    """
    Attributes:
        entitlement_id (str | Unset):
        created (str | Unset):
        last_modified (str | Unset):
        status_info (StatusInfo | Unset):
        statistics (Statistics | Unset):
        current_bookmark (CurrentBookmark | Unset):
        priority_timestamp (str | Unset):
    """

    entitlement_id: str | Unset = UNSET
    created: str | Unset = UNSET
    last_modified: str | Unset = UNSET
    status_info: StatusInfo | Unset = UNSET
    statistics: Statistics | Unset = UNSET
    current_bookmark: CurrentBookmark | Unset = UNSET
    priority_timestamp: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        entitlement_id = self.entitlement_id

        created = self.created

        last_modified = self.last_modified

        status_info: dict[str, Any] | Unset = UNSET
        if not isinstance(self.status_info, Unset):
            status_info = self.status_info.to_dict()

        statistics: dict[str, Any] | Unset = UNSET
        if not isinstance(self.statistics, Unset):
            statistics = self.statistics.to_dict()

        current_bookmark: dict[str, Any] | Unset = UNSET
        if not isinstance(self.current_bookmark, Unset):
            current_bookmark = self.current_bookmark.to_dict()

        priority_timestamp = self.priority_timestamp

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if entitlement_id is not UNSET:
            field_dict["entitlementId"] = entitlement_id
        if created is not UNSET:
            field_dict["created"] = created
        if last_modified is not UNSET:
            field_dict["lastModified"] = last_modified
        if status_info is not UNSET:
            field_dict["statusInfo"] = status_info
        if statistics is not UNSET:
            field_dict["statistics"] = statistics
        if current_bookmark is not UNSET:
            field_dict["currentBookmark"] = current_bookmark
        if priority_timestamp is not UNSET:
            field_dict["priorityTimestamp"] = priority_timestamp

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.current_bookmark import CurrentBookmark
        from ..models.statistics import Statistics
        from ..models.status_info import StatusInfo

        d = dict(src_dict)
        entitlement_id = d.pop("entitlementId", UNSET)

        created = d.pop("created", UNSET)

        last_modified = d.pop("lastModified", UNSET)

        _status_info = d.pop("statusInfo", UNSET)
        status_info: StatusInfo | Unset
        if isinstance(_status_info, Unset):
            status_info = UNSET
        else:
            status_info = StatusInfo.from_dict(_status_info)

        _statistics = d.pop("statistics", UNSET)
        statistics: Statistics | Unset
        if isinstance(_statistics, Unset):
            statistics = UNSET
        else:
            statistics = Statistics.from_dict(_statistics)

        _current_bookmark = d.pop("currentBookmark", UNSET)
        current_bookmark: CurrentBookmark | Unset
        if isinstance(_current_bookmark, Unset):
            current_bookmark = UNSET
        else:
            current_bookmark = CurrentBookmark.from_dict(_current_bookmark)

        priority_timestamp = d.pop("priorityTimestamp", UNSET)

        kobo_reading_state = cls(
            entitlement_id=entitlement_id,
            created=created,
            last_modified=last_modified,
            status_info=status_info,
            statistics=statistics,
            current_bookmark=current_bookmark,
            priority_timestamp=priority_timestamp,
        )

        kobo_reading_state.additional_properties = d
        return kobo_reading_state

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
