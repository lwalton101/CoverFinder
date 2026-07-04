from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.book_metadata import BookMetadata


T = TypeVar("T", bound="BookdropFinalizeFile")


@_attrs_define
class BookdropFinalizeFile:
    """
    Attributes:
        file_id (int | Unset):
        library_id (int | Unset):
        path_id (int | Unset):
        metadata (BookMetadata | Unset):
    """

    file_id: int | Unset = UNSET
    library_id: int | Unset = UNSET
    path_id: int | Unset = UNSET
    metadata: BookMetadata | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        file_id = self.file_id

        library_id = self.library_id

        path_id = self.path_id

        metadata: dict[str, Any] | Unset = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if file_id is not UNSET:
            field_dict["fileId"] = file_id
        if library_id is not UNSET:
            field_dict["libraryId"] = library_id
        if path_id is not UNSET:
            field_dict["pathId"] = path_id
        if metadata is not UNSET:
            field_dict["metadata"] = metadata

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.book_metadata import BookMetadata

        d = dict(src_dict)
        file_id = d.pop("fileId", UNSET)

        library_id = d.pop("libraryId", UNSET)

        path_id = d.pop("pathId", UNSET)

        _metadata = d.pop("metadata", UNSET)
        metadata: BookMetadata | Unset
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = BookMetadata.from_dict(_metadata)

        bookdrop_finalize_file = cls(
            file_id=file_id,
            library_id=library_id,
            path_id=path_id,
            metadata=metadata,
        )

        bookdrop_finalize_file.additional_properties = d
        return bookdrop_finalize_file

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
