from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.app_library_summary_allowed_formats_item import AppLibrarySummaryAllowedFormatsItem
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.path_summary import PathSummary


T = TypeVar("T", bound="AppLibrarySummary")


@_attrs_define
class AppLibrarySummary:
    """
    Attributes:
        id (int | Unset):
        name (str | Unset):
        icon (str | Unset):
        book_count (int | Unset):
        allowed_formats (list[AppLibrarySummaryAllowedFormatsItem] | Unset):
        paths (list[PathSummary] | Unset):
    """

    id: int | Unset = UNSET
    name: str | Unset = UNSET
    icon: str | Unset = UNSET
    book_count: int | Unset = UNSET
    allowed_formats: list[AppLibrarySummaryAllowedFormatsItem] | Unset = UNSET
    paths: list[PathSummary] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        icon = self.icon

        book_count = self.book_count

        allowed_formats: list[str] | Unset = UNSET
        if not isinstance(self.allowed_formats, Unset):
            allowed_formats = []
            for allowed_formats_item_data in self.allowed_formats:
                allowed_formats_item = allowed_formats_item_data.value
                allowed_formats.append(allowed_formats_item)

        paths: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.paths, Unset):
            paths = []
            for paths_item_data in self.paths:
                paths_item = paths_item_data.to_dict()
                paths.append(paths_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if icon is not UNSET:
            field_dict["icon"] = icon
        if book_count is not UNSET:
            field_dict["bookCount"] = book_count
        if allowed_formats is not UNSET:
            field_dict["allowedFormats"] = allowed_formats
        if paths is not UNSET:
            field_dict["paths"] = paths

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.path_summary import PathSummary

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        icon = d.pop("icon", UNSET)

        book_count = d.pop("bookCount", UNSET)

        _allowed_formats = d.pop("allowedFormats", UNSET)
        allowed_formats: list[AppLibrarySummaryAllowedFormatsItem] | Unset = UNSET
        if _allowed_formats is not UNSET:
            allowed_formats = []
            for allowed_formats_item_data in _allowed_formats:
                allowed_formats_item = AppLibrarySummaryAllowedFormatsItem(allowed_formats_item_data)

                allowed_formats.append(allowed_formats_item)

        _paths = d.pop("paths", UNSET)
        paths: list[PathSummary] | Unset = UNSET
        if _paths is not UNSET:
            paths = []
            for paths_item_data in _paths:
                paths_item = PathSummary.from_dict(paths_item_data)

                paths.append(paths_item)

        app_library_summary = cls(
            id=id,
            name=name,
            icon=icon,
            book_count=book_count,
            allowed_formats=allowed_formats,
            paths=paths,
        )

        app_library_summary.additional_properties = d
        return app_library_summary

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
