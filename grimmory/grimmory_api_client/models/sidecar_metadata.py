from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.sidecar_book_metadata import SidecarBookMetadata
    from ..models.sidecar_cover_info import SidecarCoverInfo


T = TypeVar("T", bound="SidecarMetadata")


@_attrs_define
class SidecarMetadata:
    """
    Attributes:
        version (str | Unset):
        generated_at (datetime.datetime | Unset):
        generated_by (str | Unset):
        metadata (SidecarBookMetadata | Unset):
        cover (SidecarCoverInfo | Unset):
    """

    version: str | Unset = UNSET
    generated_at: datetime.datetime | Unset = UNSET
    generated_by: str | Unset = UNSET
    metadata: SidecarBookMetadata | Unset = UNSET
    cover: SidecarCoverInfo | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        version = self.version

        generated_at: str | Unset = UNSET
        if not isinstance(self.generated_at, Unset):
            generated_at = self.generated_at.isoformat()

        generated_by = self.generated_by

        metadata: dict[str, Any] | Unset = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        cover: dict[str, Any] | Unset = UNSET
        if not isinstance(self.cover, Unset):
            cover = self.cover.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if version is not UNSET:
            field_dict["version"] = version
        if generated_at is not UNSET:
            field_dict["generatedAt"] = generated_at
        if generated_by is not UNSET:
            field_dict["generatedBy"] = generated_by
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if cover is not UNSET:
            field_dict["cover"] = cover

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.sidecar_book_metadata import SidecarBookMetadata
        from ..models.sidecar_cover_info import SidecarCoverInfo

        d = dict(src_dict)
        version = d.pop("version", UNSET)

        _generated_at = d.pop("generatedAt", UNSET)
        generated_at: datetime.datetime | Unset
        if isinstance(_generated_at, Unset):
            generated_at = UNSET
        else:
            generated_at = datetime.datetime.fromisoformat(_generated_at)

        generated_by = d.pop("generatedBy", UNSET)

        _metadata = d.pop("metadata", UNSET)
        metadata: SidecarBookMetadata | Unset
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = SidecarBookMetadata.from_dict(_metadata)

        _cover = d.pop("cover", UNSET)
        cover: SidecarCoverInfo | Unset
        if isinstance(_cover, Unset):
            cover = UNSET
        else:
            cover = SidecarCoverInfo.from_dict(_cover)

        sidecar_metadata = cls(
            version=version,
            generated_at=generated_at,
            generated_by=generated_by,
            metadata=metadata,
            cover=cover,
        )

        sidecar_metadata.additional_properties = d
        return sidecar_metadata

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
