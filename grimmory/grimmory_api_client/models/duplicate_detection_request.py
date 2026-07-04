from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DuplicateDetectionRequest")


@_attrs_define
class DuplicateDetectionRequest:
    """Duplicate detection configuration

    Attributes:
        library_id (int):
        match_by_isbn (bool | Unset):
        match_by_external_id (bool | Unset):
        match_by_title_author (bool | Unset):
        match_by_directory (bool | Unset):
        match_by_filename (bool | Unset):
    """

    library_id: int
    match_by_isbn: bool | Unset = UNSET
    match_by_external_id: bool | Unset = UNSET
    match_by_title_author: bool | Unset = UNSET
    match_by_directory: bool | Unset = UNSET
    match_by_filename: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        library_id = self.library_id

        match_by_isbn = self.match_by_isbn

        match_by_external_id = self.match_by_external_id

        match_by_title_author = self.match_by_title_author

        match_by_directory = self.match_by_directory

        match_by_filename = self.match_by_filename

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "libraryId": library_id,
            }
        )
        if match_by_isbn is not UNSET:
            field_dict["matchByIsbn"] = match_by_isbn
        if match_by_external_id is not UNSET:
            field_dict["matchByExternalId"] = match_by_external_id
        if match_by_title_author is not UNSET:
            field_dict["matchByTitleAuthor"] = match_by_title_author
        if match_by_directory is not UNSET:
            field_dict["matchByDirectory"] = match_by_directory
        if match_by_filename is not UNSET:
            field_dict["matchByFilename"] = match_by_filename

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        library_id = d.pop("libraryId")

        match_by_isbn = d.pop("matchByIsbn", UNSET)

        match_by_external_id = d.pop("matchByExternalId", UNSET)

        match_by_title_author = d.pop("matchByTitleAuthor", UNSET)

        match_by_directory = d.pop("matchByDirectory", UNSET)

        match_by_filename = d.pop("matchByFilename", UNSET)

        duplicate_detection_request = cls(
            library_id=library_id,
            match_by_isbn=match_by_isbn,
            match_by_external_id=match_by_external_id,
            match_by_title_author=match_by_title_author,
            match_by_directory=match_by_directory,
            match_by_filename=match_by_filename,
        )

        duplicate_detection_request.additional_properties = d
        return duplicate_detection_request

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
