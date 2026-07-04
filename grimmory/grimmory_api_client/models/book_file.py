from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.book_file_archive_type import BookFileArchiveType
from ..models.book_file_book_type import BookFileBookType
from ..types import UNSET, Unset

T = TypeVar("T", bound="BookFile")


@_attrs_define
class BookFile:
    """
    Attributes:
        id (int | Unset):
        book_id (int | Unset):
        file_name (str | Unset):
        file_path (str | Unset):
        file_sub_path (str | Unset):
        folder_based (bool | Unset):
        book_type (BookFileBookType | Unset):
        archive_type (BookFileArchiveType | Unset):
        file_size_kb (int | Unset):
        extension (str | Unset):
        description (str | Unset):
        added_on (datetime.datetime | Unset):
        book (bool | Unset):
    """

    id: int | Unset = UNSET
    book_id: int | Unset = UNSET
    file_name: str | Unset = UNSET
    file_path: str | Unset = UNSET
    file_sub_path: str | Unset = UNSET
    folder_based: bool | Unset = UNSET
    book_type: BookFileBookType | Unset = UNSET
    archive_type: BookFileArchiveType | Unset = UNSET
    file_size_kb: int | Unset = UNSET
    extension: str | Unset = UNSET
    description: str | Unset = UNSET
    added_on: datetime.datetime | Unset = UNSET
    book: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        book_id = self.book_id

        file_name = self.file_name

        file_path = self.file_path

        file_sub_path = self.file_sub_path

        folder_based = self.folder_based

        book_type: str | Unset = UNSET
        if not isinstance(self.book_type, Unset):
            book_type = self.book_type.value

        archive_type: str | Unset = UNSET
        if not isinstance(self.archive_type, Unset):
            archive_type = self.archive_type.value

        file_size_kb = self.file_size_kb

        extension = self.extension

        description = self.description

        added_on: str | Unset = UNSET
        if not isinstance(self.added_on, Unset):
            added_on = self.added_on.isoformat()

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
        if file_path is not UNSET:
            field_dict["filePath"] = file_path
        if file_sub_path is not UNSET:
            field_dict["fileSubPath"] = file_sub_path
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
        if description is not UNSET:
            field_dict["description"] = description
        if added_on is not UNSET:
            field_dict["addedOn"] = added_on
        if book is not UNSET:
            field_dict["book"] = book

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        book_id = d.pop("bookId", UNSET)

        file_name = d.pop("fileName", UNSET)

        file_path = d.pop("filePath", UNSET)

        file_sub_path = d.pop("fileSubPath", UNSET)

        folder_based = d.pop("folderBased", UNSET)

        _book_type = d.pop("bookType", UNSET)
        book_type: BookFileBookType | Unset
        if isinstance(_book_type, Unset):
            book_type = UNSET
        else:
            book_type = BookFileBookType(_book_type)

        _archive_type = d.pop("archiveType", UNSET)
        archive_type: BookFileArchiveType | Unset
        if isinstance(_archive_type, Unset):
            archive_type = UNSET
        else:
            archive_type = BookFileArchiveType(_archive_type)

        file_size_kb = d.pop("fileSizeKb", UNSET)

        extension = d.pop("extension", UNSET)

        description = d.pop("description", UNSET)

        _added_on = d.pop("addedOn", UNSET)
        added_on: datetime.datetime | Unset
        if isinstance(_added_on, Unset):
            added_on = UNSET
        else:
            added_on = datetime.datetime.fromisoformat(_added_on)

        book = d.pop("book", UNSET)

        book_file = cls(
            id=id,
            book_id=book_id,
            file_name=file_name,
            file_path=file_path,
            file_sub_path=file_sub_path,
            folder_based=folder_based,
            book_type=book_type,
            archive_type=archive_type,
            file_size_kb=file_size_kb,
            extension=extension,
            description=description,
            added_on=added_on,
            book=book,
        )

        book_file.additional_properties = d
        return book_file

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
