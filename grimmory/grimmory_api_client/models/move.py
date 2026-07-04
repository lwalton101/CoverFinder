from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Move")


@_attrs_define
class Move:
    """
    Attributes:
        book_id (int | Unset):
        target_library_id (int | Unset):
        target_library_path_id (int | Unset):
    """

    book_id: int | Unset = UNSET
    target_library_id: int | Unset = UNSET
    target_library_path_id: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        book_id = self.book_id

        target_library_id = self.target_library_id

        target_library_path_id = self.target_library_path_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if book_id is not UNSET:
            field_dict["bookId"] = book_id
        if target_library_id is not UNSET:
            field_dict["targetLibraryId"] = target_library_id
        if target_library_path_id is not UNSET:
            field_dict["targetLibraryPathId"] = target_library_path_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        book_id = d.pop("bookId", UNSET)

        target_library_id = d.pop("targetLibraryId", UNSET)

        target_library_path_id = d.pop("targetLibraryPathId", UNSET)

        move = cls(
            book_id=book_id,
            target_library_id=target_library_id,
            target_library_path_id=target_library_path_id,
        )

        move.additional_properties = d
        return move

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
