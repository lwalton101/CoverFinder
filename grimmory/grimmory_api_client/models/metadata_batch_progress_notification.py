from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="MetadataBatchProgressNotification")


@_attrs_define
class MetadataBatchProgressNotification:
    """
    Attributes:
        task_id (str | Unset):
        completed (int | Unset):
        total (int | Unset):
        message (str | Unset):
        status (str | Unset):
        review (bool | Unset):
    """

    task_id: str | Unset = UNSET
    completed: int | Unset = UNSET
    total: int | Unset = UNSET
    message: str | Unset = UNSET
    status: str | Unset = UNSET
    review: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        task_id = self.task_id

        completed = self.completed

        total = self.total

        message = self.message

        status = self.status

        review = self.review

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if task_id is not UNSET:
            field_dict["taskId"] = task_id
        if completed is not UNSET:
            field_dict["completed"] = completed
        if total is not UNSET:
            field_dict["total"] = total
        if message is not UNSET:
            field_dict["message"] = message
        if status is not UNSET:
            field_dict["status"] = status
        if review is not UNSET:
            field_dict["review"] = review

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        task_id = d.pop("taskId", UNSET)

        completed = d.pop("completed", UNSET)

        total = d.pop("total", UNSET)

        message = d.pop("message", UNSET)

        status = d.pop("status", UNSET)

        review = d.pop("review", UNSET)

        metadata_batch_progress_notification = cls(
            task_id=task_id,
            completed=completed,
            total=total,
            message=message,
            status=status,
            review=review,
        )

        metadata_batch_progress_notification.additional_properties = d
        return metadata_batch_progress_notification

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
