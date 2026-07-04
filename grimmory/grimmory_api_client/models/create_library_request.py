from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.create_library_request_allowed_formats_item import CreateLibraryRequestAllowedFormatsItem
from ..models.create_library_request_format_priority_item import CreateLibraryRequestFormatPriorityItem
from ..models.create_library_request_icon_type import CreateLibraryRequestIconType
from ..models.create_library_request_metadata_source import CreateLibraryRequestMetadataSource
from ..models.create_library_request_organization_mode import CreateLibraryRequestOrganizationMode
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.library_path import LibraryPath


T = TypeVar("T", bound="CreateLibraryRequest")


@_attrs_define
class CreateLibraryRequest:
    """Library creation request with paths to scan

    Attributes:
        name (str):
        paths (list[LibraryPath]):
        icon (str | Unset):
        icon_type (CreateLibraryRequestIconType | Unset):
        watch (bool | Unset):
        format_priority (list[CreateLibraryRequestFormatPriorityItem] | Unset):
        allowed_formats (list[CreateLibraryRequestAllowedFormatsItem] | Unset):
        metadata_source (CreateLibraryRequestMetadataSource | Unset):
        organization_mode (CreateLibraryRequestOrganizationMode | Unset):
    """

    name: str
    paths: list[LibraryPath]
    icon: str | Unset = UNSET
    icon_type: CreateLibraryRequestIconType | Unset = UNSET
    watch: bool | Unset = UNSET
    format_priority: list[CreateLibraryRequestFormatPriorityItem] | Unset = UNSET
    allowed_formats: list[CreateLibraryRequestAllowedFormatsItem] | Unset = UNSET
    metadata_source: CreateLibraryRequestMetadataSource | Unset = UNSET
    organization_mode: CreateLibraryRequestOrganizationMode | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        paths = []
        for paths_item_data in self.paths:
            paths_item = paths_item_data.to_dict()
            paths.append(paths_item)

        icon = self.icon

        icon_type: str | Unset = UNSET
        if not isinstance(self.icon_type, Unset):
            icon_type = self.icon_type.value

        watch = self.watch

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

        metadata_source: str | Unset = UNSET
        if not isinstance(self.metadata_source, Unset):
            metadata_source = self.metadata_source.value

        organization_mode: str | Unset = UNSET
        if not isinstance(self.organization_mode, Unset):
            organization_mode = self.organization_mode.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "paths": paths,
            }
        )
        if icon is not UNSET:
            field_dict["icon"] = icon
        if icon_type is not UNSET:
            field_dict["iconType"] = icon_type
        if watch is not UNSET:
            field_dict["watch"] = watch
        if format_priority is not UNSET:
            field_dict["formatPriority"] = format_priority
        if allowed_formats is not UNSET:
            field_dict["allowedFormats"] = allowed_formats
        if metadata_source is not UNSET:
            field_dict["metadataSource"] = metadata_source
        if organization_mode is not UNSET:
            field_dict["organizationMode"] = organization_mode

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.library_path import LibraryPath

        d = dict(src_dict)
        name = d.pop("name")

        paths = []
        _paths = d.pop("paths")
        for paths_item_data in _paths:
            paths_item = LibraryPath.from_dict(paths_item_data)

            paths.append(paths_item)

        icon = d.pop("icon", UNSET)

        _icon_type = d.pop("iconType", UNSET)
        icon_type: CreateLibraryRequestIconType | Unset
        if isinstance(_icon_type, Unset):
            icon_type = UNSET
        else:
            icon_type = CreateLibraryRequestIconType(_icon_type)

        watch = d.pop("watch", UNSET)

        _format_priority = d.pop("formatPriority", UNSET)
        format_priority: list[CreateLibraryRequestFormatPriorityItem] | Unset = UNSET
        if _format_priority is not UNSET:
            format_priority = []
            for format_priority_item_data in _format_priority:
                format_priority_item = CreateLibraryRequestFormatPriorityItem(format_priority_item_data)

                format_priority.append(format_priority_item)

        _allowed_formats = d.pop("allowedFormats", UNSET)
        allowed_formats: list[CreateLibraryRequestAllowedFormatsItem] | Unset = UNSET
        if _allowed_formats is not UNSET:
            allowed_formats = []
            for allowed_formats_item_data in _allowed_formats:
                allowed_formats_item = CreateLibraryRequestAllowedFormatsItem(allowed_formats_item_data)

                allowed_formats.append(allowed_formats_item)

        _metadata_source = d.pop("metadataSource", UNSET)
        metadata_source: CreateLibraryRequestMetadataSource | Unset
        if isinstance(_metadata_source, Unset):
            metadata_source = UNSET
        else:
            metadata_source = CreateLibraryRequestMetadataSource(_metadata_source)

        _organization_mode = d.pop("organizationMode", UNSET)
        organization_mode: CreateLibraryRequestOrganizationMode | Unset
        if isinstance(_organization_mode, Unset):
            organization_mode = UNSET
        else:
            organization_mode = CreateLibraryRequestOrganizationMode(_organization_mode)

        create_library_request = cls(
            name=name,
            paths=paths,
            icon=icon,
            icon_type=icon_type,
            watch=watch,
            format_priority=format_priority,
            allowed_formats=allowed_formats,
            metadata_source=metadata_source,
            organization_mode=organization_mode,
        )

        create_library_request.additional_properties = d
        return create_library_request

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
