from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.bookdrop_file_status import BookdropFileStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.book_metadata import BookMetadata


T = TypeVar("T", bound="BookdropFile")


@_attrs_define
class BookdropFile:
    """
    Attributes:
        id (int | Unset):
        file_name (str | Unset):
        file_path (str | Unset):
        file_size (int | Unset):
        original_metadata (BookMetadata | Unset):
        fetched_metadata (BookMetadata | Unset):
        created_at (str | Unset):
        updated_at (str | Unset):
        status (BookdropFileStatus | Unset):
    """

    id: int | Unset = UNSET
    file_name: str | Unset = UNSET
    file_path: str | Unset = UNSET
    file_size: int | Unset = UNSET
    original_metadata: BookMetadata | Unset = UNSET
    fetched_metadata: BookMetadata | Unset = UNSET
    created_at: str | Unset = UNSET
    updated_at: str | Unset = UNSET
    status: BookdropFileStatus | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        file_name = self.file_name

        file_path = self.file_path

        file_size = self.file_size

        original_metadata: dict[str, Any] | Unset = UNSET
        if not isinstance(self.original_metadata, Unset):
            original_metadata = self.original_metadata.to_dict()

        fetched_metadata: dict[str, Any] | Unset = UNSET
        if not isinstance(self.fetched_metadata, Unset):
            fetched_metadata = self.fetched_metadata.to_dict()

        created_at = self.created_at

        updated_at = self.updated_at

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if file_name is not UNSET:
            field_dict["fileName"] = file_name
        if file_path is not UNSET:
            field_dict["filePath"] = file_path
        if file_size is not UNSET:
            field_dict["fileSize"] = file_size
        if original_metadata is not UNSET:
            field_dict["originalMetadata"] = original_metadata
        if fetched_metadata is not UNSET:
            field_dict["fetchedMetadata"] = fetched_metadata
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if updated_at is not UNSET:
            field_dict["updatedAt"] = updated_at
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.book_metadata import BookMetadata

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        file_name = d.pop("fileName", UNSET)

        file_path = d.pop("filePath", UNSET)

        file_size = d.pop("fileSize", UNSET)

        _original_metadata = d.pop("originalMetadata", UNSET)
        original_metadata: BookMetadata | Unset
        if isinstance(_original_metadata, Unset):
            original_metadata = UNSET
        else:
            original_metadata = BookMetadata.from_dict(_original_metadata)

        _fetched_metadata = d.pop("fetchedMetadata", UNSET)
        fetched_metadata: BookMetadata | Unset
        if isinstance(_fetched_metadata, Unset):
            fetched_metadata = UNSET
        else:
            fetched_metadata = BookMetadata.from_dict(_fetched_metadata)

        created_at = d.pop("createdAt", UNSET)

        updated_at = d.pop("updatedAt", UNSET)

        _status = d.pop("status", UNSET)
        status: BookdropFileStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = BookdropFileStatus(_status)

        bookdrop_file = cls(
            id=id,
            file_name=file_name,
            file_path=file_path,
            file_size=file_size,
            original_metadata=original_metadata,
            fetched_metadata=fetched_metadata,
            created_at=created_at,
            updated_at=updated_at,
            status=status,
        )

        bookdrop_file.additional_properties = d
        return bookdrop_file

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
