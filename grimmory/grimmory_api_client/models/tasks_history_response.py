from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.task_history import TaskHistory


T = TypeVar("T", bound="TasksHistoryResponse")


@_attrs_define
class TasksHistoryResponse:
    """
    Attributes:
        task_histories (list[TaskHistory] | Unset):
    """

    task_histories: list[TaskHistory] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        task_histories: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.task_histories, Unset):
            task_histories = []
            for task_histories_item_data in self.task_histories:
                task_histories_item = task_histories_item_data.to_dict()
                task_histories.append(task_histories_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if task_histories is not UNSET:
            field_dict["taskHistories"] = task_histories

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.task_history import TaskHistory

        d = dict(src_dict)
        _task_histories = d.pop("taskHistories", UNSET)
        task_histories: list[TaskHistory] | Unset = UNSET
        if _task_histories is not UNSET:
            task_histories = []
            for task_histories_item_data in _task_histories:
                task_histories_item = TaskHistory.from_dict(task_histories_item_data)

                task_histories.append(task_histories_item)

        tasks_history_response = cls(
            task_histories=task_histories,
        )

        tasks_history_response.additional_properties = d
        return tasks_history_response

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
