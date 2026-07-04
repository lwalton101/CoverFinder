from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.opds_user_v2_create_request_sort_order import OpdsUserV2CreateRequestSortOrder
from ..types import UNSET, Unset

T = TypeVar("T", bound="OpdsUserV2CreateRequest")


@_attrs_define
class OpdsUserV2CreateRequest:
    """OPDS user creation request

    Attributes:
        username (str | Unset):
        password (str | Unset):
        sort_order (OpdsUserV2CreateRequestSortOrder | Unset):
    """

    username: str | Unset = UNSET
    password: str | Unset = UNSET
    sort_order: OpdsUserV2CreateRequestSortOrder | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        username = self.username

        password = self.password

        sort_order: str | Unset = UNSET
        if not isinstance(self.sort_order, Unset):
            sort_order = self.sort_order.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if username is not UNSET:
            field_dict["username"] = username
        if password is not UNSET:
            field_dict["password"] = password
        if sort_order is not UNSET:
            field_dict["sortOrder"] = sort_order

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        username = d.pop("username", UNSET)

        password = d.pop("password", UNSET)

        _sort_order = d.pop("sortOrder", UNSET)
        sort_order: OpdsUserV2CreateRequestSortOrder | Unset
        if isinstance(_sort_order, Unset):
            sort_order = UNSET
        else:
            sort_order = OpdsUserV2CreateRequestSortOrder(_sort_order)

        opds_user_v2_create_request = cls(
            username=username,
            password=password,
            sort_order=sort_order,
        )

        opds_user_v2_create_request.additional_properties = d
        return opds_user_v2_create_request

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
