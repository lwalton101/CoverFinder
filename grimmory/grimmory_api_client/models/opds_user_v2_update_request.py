from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.opds_user_v2_update_request_sort_order import OpdsUserV2UpdateRequestSortOrder

T = TypeVar("T", bound="OpdsUserV2UpdateRequest")


@_attrs_define
class OpdsUserV2UpdateRequest:
    """OPDS user update request

    Attributes:
        sort_order (OpdsUserV2UpdateRequestSortOrder):
    """

    sort_order: OpdsUserV2UpdateRequestSortOrder
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        sort_order = self.sort_order.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "sortOrder": sort_order,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        sort_order = OpdsUserV2UpdateRequestSortOrder(d.pop("sortOrder"))

        opds_user_v2_update_request = cls(
            sort_order=sort_order,
        )

        opds_user_v2_update_request.additional_properties = d
        return opds_user_v2_update_request

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
