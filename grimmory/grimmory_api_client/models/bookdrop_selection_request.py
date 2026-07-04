from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BookdropSelectionRequest")


@_attrs_define
class BookdropSelectionRequest:
    """Selection request for files to discard

    Attributes:
        select_all (bool | Unset):
        excluded_ids (list[int] | Unset):
        selected_ids (list[int] | Unset):
    """

    select_all: bool | Unset = UNSET
    excluded_ids: list[int] | Unset = UNSET
    selected_ids: list[int] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        select_all = self.select_all

        excluded_ids: list[int] | Unset = UNSET
        if not isinstance(self.excluded_ids, Unset):
            excluded_ids = self.excluded_ids

        selected_ids: list[int] | Unset = UNSET
        if not isinstance(self.selected_ids, Unset):
            selected_ids = self.selected_ids

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if select_all is not UNSET:
            field_dict["selectAll"] = select_all
        if excluded_ids is not UNSET:
            field_dict["excludedIds"] = excluded_ids
        if selected_ids is not UNSET:
            field_dict["selectedIds"] = selected_ids

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        select_all = d.pop("selectAll", UNSET)

        excluded_ids = cast(list[int], d.pop("excludedIds", UNSET))

        selected_ids = cast(list[int], d.pop("selectedIds", UNSET))

        bookdrop_selection_request = cls(
            select_all=select_all,
            excluded_ids=excluded_ids,
            selected_ids=selected_ids,
        )

        bookdrop_selection_request.additional_properties = d
        return bookdrop_selection_request

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
