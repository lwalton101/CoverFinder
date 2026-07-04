from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AppBookFile")


@_attrs_define
class AppBookFile:
    """
    Attributes:
        id (int | Unset):
        book_id (int | Unset):
        file_name (str | Unset):
        folder_based (bool | Unset):
        book_type (str | Unset):
        archive_type (str | Unset):
        file_size_kb (int | Unset):
        extension (str | Unset):
        added_on (datetime.datetime | Unset):
        primary (bool | Unset):
        book (bool | Unset):
    """

    id: int | Unset = UNSET
    book_id: int | Unset = UNSET
    file_name: str | Unset = UNSET
    folder_based: bool | Unset = UNSET
    book_type: str | Unset = UNSET
    archive_type: str | Unset = UNSET
    file_size_kb: int | Unset = UNSET
    extension: str | Unset = UNSET
    added_on: datetime.datetime | Unset = UNSET
    primary: bool | Unset = UNSET
    book: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        book_id = self.book_id

        file_name = self.file_name

        folder_based = self.folder_based

        book_type = self.book_type

        archive_type = self.archive_type

        file_size_kb = self.file_size_kb

        extension = self.extension

        added_on: str | Unset = UNSET
        if not isinstance(self.added_on, Unset):
            added_on = self.added_on.isoformat()

        primary = self.primary

        book = self.book

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if book_id is not UNSET:
            field_dict["bookId"] = book_id
        if file_name is not UNSET:
            field_dict["fileName"] = file_name
        if folder_based is not UNSET:
            field_dict["folderBased"] = folder_based
        if book_type is not UNSET:
            field_dict["bookType"] = book_type
        if archive_type is not UNSET:
            field_dict["archiveType"] = archive_type
        if file_size_kb is not UNSET:
            field_dict["fileSizeKb"] = file_size_kb
        if extension is not UNSET:
            field_dict["extension"] = extension
        if added_on is not UNSET:
            field_dict["addedOn"] = added_on
        if primary is not UNSET:
            field_dict["primary"] = primary
        if book is not UNSET:
            field_dict["book"] = book

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        book_id = d.pop("bookId", UNSET)

        file_name = d.pop("fileName", UNSET)

        folder_based = d.pop("folderBased", UNSET)

        book_type = d.pop("bookType", UNSET)

        archive_type = d.pop("archiveType", UNSET)

        file_size_kb = d.pop("fileSizeKb", UNSET)

        extension = d.pop("extension", UNSET)

        _added_on = d.pop("addedOn", UNSET)
        added_on: datetime.datetime | Unset
        if isinstance(_added_on, Unset):
            added_on = UNSET
        else:
            added_on = datetime.datetime.fromisoformat(_added_on)

        primary = d.pop("primary", UNSET)

        book = d.pop("book", UNSET)

        app_book_file = cls(
            id=id,
            book_id=book_id,
            file_name=file_name,
            folder_based=folder_based,
            book_type=book_type,
            archive_type=archive_type,
            file_size_kb=file_size_kb,
            extension=extension,
            added_on=added_on,
            primary=primary,
            book=book,
        )

        app_book_file.additional_properties = d
        return app_book_file

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
