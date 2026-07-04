from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AttachBookFileRequest")


@_attrs_define
class AttachBookFileRequest:
    """Request containing source book IDs and delete option

    Attributes:
        source_book_ids (list[int]):
        move_files (bool | Unset):
    """

    source_book_ids: list[int]
    move_files: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        source_book_ids = self.source_book_ids

        move_files = self.move_files

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "sourceBookIds": source_book_ids,
            }
        )
        if move_files is not UNSET:
            field_dict["moveFiles"] = move_files

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        source_book_ids = cast(list[int], d.pop("sourceBookIds"))

        move_files = d.pop("moveFiles", UNSET)

        attach_book_file_request = cls(
            source_book_ids=source_book_ids,
            move_files=move_files,
        )

        attach_book_file_request.additional_properties = d
        return attach_book_file_request

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
