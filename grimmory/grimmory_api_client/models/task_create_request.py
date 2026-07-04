from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.task_create_request_task_type import TaskCreateRequestTaskType
from ..types import UNSET, Unset

T = TypeVar("T", bound="TaskCreateRequest")


@_attrs_define
class TaskCreateRequest:
    """
    Attributes:
        task_id (str | Unset):
        task_type (TaskCreateRequestTaskType | Unset):
        triggered_by_cron (bool | Unset):
        options (Any | Unset):
    """

    task_id: str | Unset = UNSET
    task_type: TaskCreateRequestTaskType | Unset = UNSET
    triggered_by_cron: bool | Unset = UNSET
    options: Any | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        task_id = self.task_id

        task_type: str | Unset = UNSET
        if not isinstance(self.task_type, Unset):
            task_type = self.task_type.value

        triggered_by_cron = self.triggered_by_cron

        options = self.options

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if task_id is not UNSET:
            field_dict["taskId"] = task_id
        if task_type is not UNSET:
            field_dict["taskType"] = task_type
        if triggered_by_cron is not UNSET:
            field_dict["triggeredByCron"] = triggered_by_cron
        if options is not UNSET:
            field_dict["options"] = options

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        task_id = d.pop("taskId", UNSET)

        _task_type = d.pop("taskType", UNSET)
        task_type: TaskCreateRequestTaskType | Unset
        if isinstance(_task_type, Unset):
            task_type = UNSET
        else:
            task_type = TaskCreateRequestTaskType(_task_type)

        triggered_by_cron = d.pop("triggeredByCron", UNSET)

        options = d.pop("options", UNSET)

        task_create_request = cls(
            task_id=task_id,
            task_type=task_type,
            triggered_by_cron=triggered_by_cron,
            options=options,
        )

        task_create_request.additional_properties = d
        return task_create_request

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
