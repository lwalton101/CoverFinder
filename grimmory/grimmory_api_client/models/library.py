from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.library_allowed_formats_item import LibraryAllowedFormatsItem
from ..models.library_format_priority_item import LibraryFormatPriorityItem
from ..models.library_icon_type import LibraryIconType
from ..models.library_metadata_source import LibraryMetadataSource
from ..models.library_organization_mode import LibraryOrganizationMode
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.library_path import LibraryPath
    from ..models.sort import Sort


T = TypeVar("T", bound="Library")


@_attrs_define
class Library:
    """
    Attributes:
        id (int | Unset):
        name (str | Unset):
        sort (Sort | Unset):
        icon (str | Unset):
        icon_type (LibraryIconType | Unset):
        file_naming_pattern (str | Unset):
        watch (bool | Unset):
        paths (list[LibraryPath] | Unset):
        format_priority (list[LibraryFormatPriorityItem] | Unset):
        allowed_formats (list[LibraryAllowedFormatsItem] | Unset):
        organization_mode (LibraryOrganizationMode | Unset):
        metadata_source (LibraryMetadataSource | Unset):
    """

    id: int | Unset = UNSET
    name: str | Unset = UNSET
    sort: Sort | Unset = UNSET
    icon: str | Unset = UNSET
    icon_type: LibraryIconType | Unset = UNSET
    file_naming_pattern: str | Unset = UNSET
    watch: bool | Unset = UNSET
    paths: list[LibraryPath] | Unset = UNSET
    format_priority: list[LibraryFormatPriorityItem] | Unset = UNSET
    allowed_formats: list[LibraryAllowedFormatsItem] | Unset = UNSET
    organization_mode: LibraryOrganizationMode | Unset = UNSET
    metadata_source: LibraryMetadataSource | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        sort: dict[str, Any] | Unset = UNSET
        if not isinstance(self.sort, Unset):
            sort = self.sort.to_dict()

        icon = self.icon

        icon_type: str | Unset = UNSET
        if not isinstance(self.icon_type, Unset):
            icon_type = self.icon_type.value

        file_naming_pattern = self.file_naming_pattern

        watch = self.watch

        paths: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.paths, Unset):
            paths = []
            for paths_item_data in self.paths:
                paths_item = paths_item_data.to_dict()
                paths.append(paths_item)

        format_priority: list[str] | Unset = UNSET
        if not isinstance(self.format_priority, Unset):
            format_priority = []
            for format_priority_item_data in self.format_priority:
                format_priority_item = format_priority_item_data.value
                format_priority.append(format_priority_item)

        allowed_formats: list[str] | Unset = UNSET
        if not isinstance(self.allowed_formats, Unset):
            allowed_formats = []
            for allowed_formats_item_data in self.allowed_formats:
                allowed_formats_item = allowed_formats_item_data.value
                allowed_formats.append(allowed_formats_item)

        organization_mode: str | Unset = UNSET
        if not isinstance(self.organization_mode, Unset):
            organization_mode = self.organization_mode.value

        metadata_source: str | Unset = UNSET
        if not isinstance(self.metadata_source, Unset):
            metadata_source = self.metadata_source.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if sort is not UNSET:
            field_dict["sort"] = sort
        if icon is not UNSET:
            field_dict["icon"] = icon
        if icon_type is not UNSET:
            field_dict["iconType"] = icon_type
        if file_naming_pattern is not UNSET:
            field_dict["fileNamingPattern"] = file_naming_pattern
        if watch is not UNSET:
            field_dict["watch"] = watch
        if paths is not UNSET:
            field_dict["paths"] = paths
        if format_priority is not UNSET:
            field_dict["formatPriority"] = format_priority
        if allowed_formats is not UNSET:
            field_dict["allowedFormats"] = allowed_formats
        if organization_mode is not UNSET:
            field_dict["organizationMode"] = organization_mode
        if metadata_source is not UNSET:
            field_dict["metadataSource"] = metadata_source

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.library_path import LibraryPath
        from ..models.sort import Sort

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        _sort = d.pop("sort", UNSET)
        sort: Sort | Unset
        if isinstance(_sort, Unset):
            sort = UNSET
        else:
            sort = Sort.from_dict(_sort)

        icon = d.pop("icon", UNSET)

        _icon_type = d.pop("iconType", UNSET)
        icon_type: LibraryIconType | Unset
        if isinstance(_icon_type, Unset):
            icon_type = UNSET
        else:
            icon_type = LibraryIconType(_icon_type)

        file_naming_pattern = d.pop("fileNamingPattern", UNSET)

        watch = d.pop("watch", UNSET)

        _paths = d.pop("paths", UNSET)
        paths: list[LibraryPath] | Unset = UNSET
        if _paths is not UNSET:
            paths = []
            for paths_item_data in _paths:
                paths_item = LibraryPath.from_dict(paths_item_data)

                paths.append(paths_item)

        _format_priority = d.pop("formatPriority", UNSET)
        format_priority: list[LibraryFormatPriorityItem] | Unset = UNSET
        if _format_priority is not UNSET:
            format_priority = []
            for format_priority_item_data in _format_priority:
                format_priority_item = LibraryFormatPriorityItem(format_priority_item_data)

                format_priority.append(format_priority_item)

        _allowed_formats = d.pop("allowedFormats", UNSET)
        allowed_formats: list[LibraryAllowedFormatsItem] | Unset = UNSET
        if _allowed_formats is not UNSET:
            allowed_formats = []
            for allowed_formats_item_data in _allowed_formats:
                allowed_formats_item = LibraryAllowedFormatsItem(allowed_formats_item_data)

                allowed_formats.append(allowed_formats_item)

        _organization_mode = d.pop("organizationMode", UNSET)
        organization_mode: LibraryOrganizationMode | Unset
        if isinstance(_organization_mode, Unset):
            organization_mode = UNSET
        else:
            organization_mode = LibraryOrganizationMode(_organization_mode)

        _metadata_source = d.pop("metadataSource", UNSET)
        metadata_source: LibraryMetadataSource | Unset
        if isinstance(_metadata_source, Unset):
            metadata_source = UNSET
        else:
            metadata_source = LibraryMetadataSource(_metadata_source)

        library = cls(
            id=id,
            name=name,
            sort=sort,
            icon=icon,
            icon_type=icon_type,
            file_naming_pattern=file_naming_pattern,
            watch=watch,
            paths=paths,
            format_priority=format_priority,
            allowed_formats=allowed_formats,
            organization_mode=organization_mode,
            metadata_source=metadata_source,
        )

        library.additional_properties = d
        return library

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
