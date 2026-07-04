from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.task_create_response_status import TaskCreateResponseStatus
from ..models.task_create_response_task_type import TaskCreateResponseTaskType
from ..types import UNSET, Unset

T = TypeVar("T", bound="TaskCreateResponse")


@_attrs_define
class TaskCreateResponse:
    """
    Attributes:
        task_id (str | Unset):
        task_type (TaskCreateResponseTaskType | Unset):
        status (TaskCreateResponseStatus | Unset):
    """

    task_id: str | Unset = UNSET
    task_type: TaskCreateResponseTaskType | Unset = UNSET
    status: TaskCreateResponseStatus | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        task_id = self.task_id

        task_type: str | Unset = UNSET
        if not isinstance(self.task_type, Unset):
            task_type = self.task_type.value

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if task_id is not UNSET:
            field_dict["taskId"] = task_id
        if task_type is not UNSET:
            field_dict["taskType"] = task_type
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        task_id = d.pop("taskId", UNSET)

        _task_type = d.pop("taskType", UNSET)
        task_type: TaskCreateResponseTaskType | Unset
        if isinstance(_task_type, Unset):
            task_type = UNSET
        else:
            task_type = TaskCreateResponseTaskType(_task_type)

        _status = d.pop("status", UNSET)
        status: TaskCreateResponseStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = TaskCreateResponseStatus(_status)

        task_create_response = cls(
            task_id=task_id,
            task_type=task_type,
            status=status,
        )

        task_create_response.additional_properties = d
        return task_create_response

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
