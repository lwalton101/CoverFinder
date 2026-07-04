from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ListeningFinishFunnelResponse")


@_attrs_define
class ListeningFinishFunnelResponse:
    """
    Attributes:
        total_started (int | Unset):
        reached25 (int | Unset):
        reached50 (int | Unset):
        reached75 (int | Unset):
        completed (int | Unset):
    """

    total_started: int | Unset = UNSET
    reached25: int | Unset = UNSET
    reached50: int | Unset = UNSET
    reached75: int | Unset = UNSET
    completed: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        total_started = self.total_started

        reached25 = self.reached25

        reached50 = self.reached50

        reached75 = self.reached75

        completed = self.completed

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if total_started is not UNSET:
            field_dict["totalStarted"] = total_started
        if reached25 is not UNSET:
            field_dict["reached25"] = reached25
        if reached50 is not UNSET:
            field_dict["reached50"] = reached50
        if reached75 is not UNSET:
            field_dict["reached75"] = reached75
        if completed is not UNSET:
            field_dict["completed"] = completed

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        total_started = d.pop("totalStarted", UNSET)

        reached25 = d.pop("reached25", UNSET)

        reached50 = d.pop("reached50", UNSET)

        reached75 = d.pop("reached75", UNSET)

        completed = d.pop("completed", UNSET)

        listening_finish_funnel_response = cls(
            total_started=total_started,
            reached25=reached25,
            reached50=reached50,
            reached75=reached75,
            completed=completed,
        )

        listening_finish_funnel_response.additional_properties = d
        return listening_finish_funnel_response

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
