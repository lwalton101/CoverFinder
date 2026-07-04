from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.task_history_status import TaskHistoryStatus
from ..models.task_history_type import TaskHistoryType
from ..types import UNSET, Unset

T = TypeVar("T", bound="TaskHistory")


@_attrs_define
class TaskHistory:
    """
    Attributes:
        id (str | Unset):
        type_ (TaskHistoryType | Unset):
        status (TaskHistoryStatus | Unset):
        progress_percentage (int | Unset):
        message (str | Unset):
        created_at (datetime.datetime | Unset):
        updated_at (datetime.datetime | Unset):
        completed_at (datetime.datetime | Unset):
    """

    id: str | Unset = UNSET
    type_: TaskHistoryType | Unset = UNSET
    status: TaskHistoryStatus | Unset = UNSET
    progress_percentage: int | Unset = UNSET
    message: str | Unset = UNSET
    created_at: datetime.datetime | Unset = UNSET
    updated_at: datetime.datetime | Unset = UNSET
    completed_at: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        progress_percentage = self.progress_percentage

        message = self.message

        created_at: str | Unset = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        updated_at: str | Unset = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        completed_at: str | Unset = UNSET
        if not isinstance(self.completed_at, Unset):
            completed_at = self.completed_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if type_ is not UNSET:
            field_dict["type"] = type_
        if status is not UNSET:
            field_dict["status"] = status
        if progress_percentage is not UNSET:
            field_dict["progressPercentage"] = progress_percentage
        if message is not UNSET:
            field_dict["message"] = message
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if updated_at is not UNSET:
            field_dict["updatedAt"] = updated_at
        if completed_at is not UNSET:
            field_dict["completedAt"] = completed_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: TaskHistoryType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = TaskHistoryType(_type_)

        _status = d.pop("status", UNSET)
        status: TaskHistoryStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = TaskHistoryStatus(_status)

        progress_percentage = d.pop("progressPercentage", UNSET)

        message = d.pop("message", UNSET)

        _created_at = d.pop("createdAt", UNSET)
        created_at: datetime.datetime | Unset
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = datetime.datetime.fromisoformat(_created_at)

        _updated_at = d.pop("updatedAt", UNSET)
        updated_at: datetime.datetime | Unset
        if isinstance(_updated_at, Unset):
            updated_at = UNSET
        else:
            updated_at = datetime.datetime.fromisoformat(_updated_at)

        _completed_at = d.pop("completedAt", UNSET)
        completed_at: datetime.datetime | Unset
        if isinstance(_completed_at, Unset):
            completed_at = UNSET
        else:
            completed_at = datetime.datetime.fromisoformat(_completed_at)

        task_history = cls(
            id=id,
            type_=type_,
            status=status,
            progress_percentage=progress_percentage,
            message=message,
            created_at=created_at,
            updated_at=updated_at,
            completed_at=completed_at,
        )

        task_history.additional_properties = d
        return task_history

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
