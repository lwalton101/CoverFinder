from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TaskCancelResponse")


@_attrs_define
class TaskCancelResponse:
    """
    Attributes:
        task_id (str | Unset):
        cancelled (bool | Unset):
        message (str | Unset):
    """

    task_id: str | Unset = UNSET
    cancelled: bool | Unset = UNSET
    message: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        task_id = self.task_id

        cancelled = self.cancelled

        message = self.message

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if task_id is not UNSET:
            field_dict["taskId"] = task_id
        if cancelled is not UNSET:
            field_dict["cancelled"] = cancelled
        if message is not UNSET:
            field_dict["message"] = message

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        task_id = d.pop("taskId", UNSET)

        cancelled = d.pop("cancelled", UNSET)

        message = d.pop("message", UNSET)

        task_cancel_response = cls(
            task_id=task_id,
            cancelled=cancelled,
            message=message,
        )

        task_cancel_response.additional_properties = d
        return task_cancel_response

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
