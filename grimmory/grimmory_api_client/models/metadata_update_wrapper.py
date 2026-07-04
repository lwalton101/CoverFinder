from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.book_metadata import BookMetadata
    from ..models.metadata_clear_flags import MetadataClearFlags


T = TypeVar("T", bound="MetadataUpdateWrapper")


@_attrs_define
class MetadataUpdateWrapper:
    """Metadata update wrapper

    Attributes:
        metadata (BookMetadata | Unset):
        clear_flags (MetadataClearFlags | Unset):
    """

    metadata: BookMetadata | Unset = UNSET
    clear_flags: MetadataClearFlags | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        metadata: dict[str, Any] | Unset = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        clear_flags: dict[str, Any] | Unset = UNSET
        if not isinstance(self.clear_flags, Unset):
            clear_flags = self.clear_flags.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if clear_flags is not UNSET:
            field_dict["clearFlags"] = clear_flags

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.book_metadata import BookMetadata
        from ..models.metadata_clear_flags import MetadataClearFlags

        d = dict(src_dict)
        _metadata = d.pop("metadata", UNSET)
        metadata: BookMetadata | Unset
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = BookMetadata.from_dict(_metadata)

        _clear_flags = d.pop("clearFlags", UNSET)
        clear_flags: MetadataClearFlags | Unset
        if isinstance(_clear_flags, Unset):
            clear_flags = UNSET
        else:
            clear_flags = MetadataClearFlags.from_dict(_clear_flags)

        metadata_update_wrapper = cls(
            metadata=metadata,
            clear_flags=clear_flags,
        )

        metadata_update_wrapper.additional_properties = d
        return metadata_update_wrapper

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
