from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.opds_user_v2_sort_order import OpdsUserV2SortOrder
from ..types import UNSET, Unset

T = TypeVar("T", bound="OpdsUserV2")


@_attrs_define
class OpdsUserV2:
    """
    Attributes:
        id (int | Unset):
        user_id (int | Unset):
        username (str | Unset):
        sort_order (OpdsUserV2SortOrder | Unset):
    """

    id: int | Unset = UNSET
    user_id: int | Unset = UNSET
    username: str | Unset = UNSET
    sort_order: OpdsUserV2SortOrder | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        user_id = self.user_id

        username = self.username

        sort_order: str | Unset = UNSET
        if not isinstance(self.sort_order, Unset):
            sort_order = self.sort_order.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if user_id is not UNSET:
            field_dict["userId"] = user_id
        if username is not UNSET:
            field_dict["username"] = username
        if sort_order is not UNSET:
            field_dict["sortOrder"] = sort_order

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        user_id = d.pop("userId", UNSET)

        username = d.pop("username", UNSET)

        _sort_order = d.pop("sortOrder", UNSET)
        sort_order: OpdsUserV2SortOrder | Unset
        if isinstance(_sort_order, Unset):
            sort_order = UNSET
        else:
            sort_order = OpdsUserV2SortOrder(_sort_order)

        opds_user_v2 = cls(
            id=id,
            user_id=user_id,
            username=username,
            sort_order=sort_order,
        )

        opds_user_v2.additional_properties = d
        return opds_user_v2

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
