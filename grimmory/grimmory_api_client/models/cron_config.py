from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.cron_config_task_type import CronConfigTaskType
from ..types import UNSET, Unset

T = TypeVar("T", bound="CronConfig")


@_attrs_define
class CronConfig:
    """
    Attributes:
        id (int | Unset):
        task_type (CronConfigTaskType | Unset):
        cron_expression (str | Unset):
        enabled (bool | Unset):
        created_at (datetime.datetime | Unset):
        updated_at (datetime.datetime | Unset):
    """

    id: int | Unset = UNSET
    task_type: CronConfigTaskType | Unset = UNSET
    cron_expression: str | Unset = UNSET
    enabled: bool | Unset = UNSET
    created_at: datetime.datetime | Unset = UNSET
    updated_at: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        task_type: str | Unset = UNSET
        if not isinstance(self.task_type, Unset):
            task_type = self.task_type.value

        cron_expression = self.cron_expression

        enabled = self.enabled

        created_at: str | Unset = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        updated_at: str | Unset = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if task_type is not UNSET:
            field_dict["taskType"] = task_type
        if cron_expression is not UNSET:
            field_dict["cronExpression"] = cron_expression
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if updated_at is not UNSET:
            field_dict["updatedAt"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        _task_type = d.pop("taskType", UNSET)
        task_type: CronConfigTaskType | Unset
        if isinstance(_task_type, Unset):
            task_type = UNSET
        else:
            task_type = CronConfigTaskType(_task_type)

        cron_expression = d.pop("cronExpression", UNSET)

        enabled = d.pop("enabled", UNSET)

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

        cron_config = cls(
            id=id,
            task_type=task_type,
            cron_expression=cron_expression,
            enabled=enabled,
            created_at=created_at,
            updated_at=updated_at,
        )

        cron_config.additional_properties = d
        return cron_config

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
