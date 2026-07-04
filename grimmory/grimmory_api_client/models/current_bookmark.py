from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.location import Location


T = TypeVar("T", bound="CurrentBookmark")


@_attrs_define
class CurrentBookmark:
    """
    Attributes:
        last_modified (str | Unset):
        progress_percent (int | Unset):
        content_source_progress_percent (int | Unset):
        location (Location | Unset):
    """

    last_modified: str | Unset = UNSET
    progress_percent: int | Unset = UNSET
    content_source_progress_percent: int | Unset = UNSET
    location: Location | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        last_modified = self.last_modified

        progress_percent = self.progress_percent

        content_source_progress_percent = self.content_source_progress_percent

        location: dict[str, Any] | Unset = UNSET
        if not isinstance(self.location, Unset):
            location = self.location.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if last_modified is not UNSET:
            field_dict["lastModified"] = last_modified
        if progress_percent is not UNSET:
            field_dict["progressPercent"] = progress_percent
        if content_source_progress_percent is not UNSET:
            field_dict["contentSourceProgressPercent"] = content_source_progress_percent
        if location is not UNSET:
            field_dict["location"] = location

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.location import Location

        d = dict(src_dict)
        last_modified = d.pop("lastModified", UNSET)

        progress_percent = d.pop("progressPercent", UNSET)

        content_source_progress_percent = d.pop("contentSourceProgressPercent", UNSET)

        _location = d.pop("location", UNSET)
        location: Location | Unset
        if isinstance(_location, Unset):
            location = UNSET
        else:
            location = Location.from_dict(_location)

        current_bookmark = cls(
            last_modified=last_modified,
            progress_percent=progress_percent,
            content_source_progress_percent=content_source_progress_percent,
            location=location,
        )

        current_bookmark.additional_properties = d
        return current_bookmark

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
