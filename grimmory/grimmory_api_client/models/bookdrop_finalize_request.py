from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bookdrop_finalize_file import BookdropFinalizeFile


T = TypeVar("T", bound="BookdropFinalizeRequest")


@_attrs_define
class BookdropFinalizeRequest:
    """Finalize import request

    Attributes:
        select_all (bool | Unset):
        excluded_ids (list[int] | Unset):
        files (list[BookdropFinalizeFile] | Unset):
        default_library_id (int | Unset):
        default_path_id (int | Unset):
    """

    select_all: bool | Unset = UNSET
    excluded_ids: list[int] | Unset = UNSET
    files: list[BookdropFinalizeFile] | Unset = UNSET
    default_library_id: int | Unset = UNSET
    default_path_id: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        select_all = self.select_all

        excluded_ids: list[int] | Unset = UNSET
        if not isinstance(self.excluded_ids, Unset):
            excluded_ids = self.excluded_ids

        files: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.files, Unset):
            files = []
            for files_item_data in self.files:
                files_item = files_item_data.to_dict()
                files.append(files_item)

        default_library_id = self.default_library_id

        default_path_id = self.default_path_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if select_all is not UNSET:
            field_dict["selectAll"] = select_all
        if excluded_ids is not UNSET:
            field_dict["excludedIds"] = excluded_ids
        if files is not UNSET:
            field_dict["files"] = files
        if default_library_id is not UNSET:
            field_dict["defaultLibraryId"] = default_library_id
        if default_path_id is not UNSET:
            field_dict["defaultPathId"] = default_path_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bookdrop_finalize_file import BookdropFinalizeFile

        d = dict(src_dict)
        select_all = d.pop("selectAll", UNSET)

        excluded_ids = cast(list[int], d.pop("excludedIds", UNSET))

        _files = d.pop("files", UNSET)
        files: list[BookdropFinalizeFile] | Unset = UNSET
        if _files is not UNSET:
            files = []
            for files_item_data in _files:
                files_item = BookdropFinalizeFile.from_dict(files_item_data)

                files.append(files_item)

        default_library_id = d.pop("defaultLibraryId", UNSET)

        default_path_id = d.pop("defaultPathId", UNSET)

        bookdrop_finalize_request = cls(
            select_all=select_all,
            excluded_ids=excluded_ids,
            files=files,
            default_library_id=default_library_id,
            default_path_id=default_path_id,
        )

        bookdrop_finalize_request.additional_properties = d
        return bookdrop_finalize_request

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
