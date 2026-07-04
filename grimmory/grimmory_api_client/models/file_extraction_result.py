from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.book_metadata import BookMetadata


T = TypeVar("T", bound="FileExtractionResult")


@_attrs_define
class FileExtractionResult:
    """
    Attributes:
        file_id (int | Unset):
        file_name (str | Unset):
        success (bool | Unset):
        extracted_metadata (BookMetadata | Unset):
        error_message (str | Unset):
    """

    file_id: int | Unset = UNSET
    file_name: str | Unset = UNSET
    success: bool | Unset = UNSET
    extracted_metadata: BookMetadata | Unset = UNSET
    error_message: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        file_id = self.file_id

        file_name = self.file_name

        success = self.success

        extracted_metadata: dict[str, Any] | Unset = UNSET
        if not isinstance(self.extracted_metadata, Unset):
            extracted_metadata = self.extracted_metadata.to_dict()

        error_message = self.error_message

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if file_id is not UNSET:
            field_dict["fileId"] = file_id
        if file_name is not UNSET:
            field_dict["fileName"] = file_name
        if success is not UNSET:
            field_dict["success"] = success
        if extracted_metadata is not UNSET:
            field_dict["extractedMetadata"] = extracted_metadata
        if error_message is not UNSET:
            field_dict["errorMessage"] = error_message

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.book_metadata import BookMetadata

        d = dict(src_dict)
        file_id = d.pop("fileId", UNSET)

        file_name = d.pop("fileName", UNSET)

        success = d.pop("success", UNSET)

        _extracted_metadata = d.pop("extractedMetadata", UNSET)
        extracted_metadata: BookMetadata | Unset
        if isinstance(_extracted_metadata, Unset):
            extracted_metadata = UNSET
        else:
            extracted_metadata = BookMetadata.from_dict(_extracted_metadata)

        error_message = d.pop("errorMessage", UNSET)

        file_extraction_result = cls(
            file_id=file_id,
            file_name=file_name,
            success=success,
            extracted_metadata=extracted_metadata,
            error_message=error_message,
        )

        file_extraction_result.additional_properties = d
        return file_extraction_result

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
