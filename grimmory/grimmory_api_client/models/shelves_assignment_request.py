from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ShelvesAssignmentRequest")


@_attrs_define
class ShelvesAssignmentRequest:
    """Shelves assignment request

    Attributes:
        book_ids (list[int] | Unset):
        shelves_to_assign (list[int] | Unset):
        shelves_to_unassign (list[int] | Unset):
    """

    book_ids: list[int] | Unset = UNSET
    shelves_to_assign: list[int] | Unset = UNSET
    shelves_to_unassign: list[int] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        book_ids: list[int] | Unset = UNSET
        if not isinstance(self.book_ids, Unset):
            book_ids = self.book_ids

        shelves_to_assign: list[int] | Unset = UNSET
        if not isinstance(self.shelves_to_assign, Unset):
            shelves_to_assign = self.shelves_to_assign

        shelves_to_unassign: list[int] | Unset = UNSET
        if not isinstance(self.shelves_to_unassign, Unset):
            shelves_to_unassign = self.shelves_to_unassign

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if book_ids is not UNSET:
            field_dict["bookIds"] = book_ids
        if shelves_to_assign is not UNSET:
            field_dict["shelvesToAssign"] = shelves_to_assign
        if shelves_to_unassign is not UNSET:
            field_dict["shelvesToUnassign"] = shelves_to_unassign

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        book_ids = cast(list[int], d.pop("bookIds", UNSET))

        shelves_to_assign = cast(list[int], d.pop("shelvesToAssign", UNSET))

        shelves_to_unassign = cast(list[int], d.pop("shelvesToUnassign", UNSET))

        shelves_assignment_request = cls(
            book_ids=book_ids,
            shelves_to_assign=shelves_to_assign,
            shelves_to_unassign=shelves_to_unassign,
        )

        shelves_assignment_request.additional_properties = d
        return shelves_assignment_request

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
