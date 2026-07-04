from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.book_metadata import BookMetadata


T = TypeVar("T", bound="BookdropBulkEditRequest")


@_attrs_define
class BookdropBulkEditRequest:
    """Bulk edit request

    Attributes:
        fields (BookMetadata):
        enabled_fields (list[str]):
        merge_arrays (bool | Unset):
        select_all (bool | Unset):
        excluded_ids (list[int] | Unset):
        selected_ids (list[int] | Unset):
    """

    fields: BookMetadata
    enabled_fields: list[str]
    merge_arrays: bool | Unset = UNSET
    select_all: bool | Unset = UNSET
    excluded_ids: list[int] | Unset = UNSET
    selected_ids: list[int] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        fields = self.fields.to_dict()

        enabled_fields = self.enabled_fields

        merge_arrays = self.merge_arrays

        select_all = self.select_all

        excluded_ids: list[int] | Unset = UNSET
        if not isinstance(self.excluded_ids, Unset):
            excluded_ids = self.excluded_ids

        selected_ids: list[int] | Unset = UNSET
        if not isinstance(self.selected_ids, Unset):
            selected_ids = self.selected_ids

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "fields": fields,
                "enabledFields": enabled_fields,
            }
        )
        if merge_arrays is not UNSET:
            field_dict["mergeArrays"] = merge_arrays
        if select_all is not UNSET:
            field_dict["selectAll"] = select_all
        if excluded_ids is not UNSET:
            field_dict["excludedIds"] = excluded_ids
        if selected_ids is not UNSET:
            field_dict["selectedIds"] = selected_ids

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.book_metadata import BookMetadata

        d = dict(src_dict)
        fields = BookMetadata.from_dict(d.pop("fields"))

        enabled_fields = cast(list[str], d.pop("enabledFields"))

        merge_arrays = d.pop("mergeArrays", UNSET)

        select_all = d.pop("selectAll", UNSET)

        excluded_ids = cast(list[int], d.pop("excludedIds", UNSET))

        selected_ids = cast(list[int], d.pop("selectedIds", UNSET))

        bookdrop_bulk_edit_request = cls(
            fields=fields,
            enabled_fields=enabled_fields,
            merge_arrays=merge_arrays,
            select_all=select_all,
            excluded_ids=excluded_ids,
            selected_ids=selected_ids,
        )

        bookdrop_bulk_edit_request.additional_properties = d
        return bookdrop_bulk_edit_request

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
