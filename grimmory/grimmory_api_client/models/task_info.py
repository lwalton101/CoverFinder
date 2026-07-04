from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.task_info_task_type import TaskInfoTaskType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cron_config import CronConfig


T = TypeVar("T", bound="TaskInfo")


@_attrs_define
class TaskInfo:
    """
    Attributes:
        task_type (TaskInfoTaskType | Unset):
        name (str | Unset):
        description (str | Unset):
        parallel (bool | Unset):
        async_ (bool | Unset):
        cron_supported (bool | Unset):
        cron_config (CronConfig | Unset):
        metadata (str | Unset):
    """

    task_type: TaskInfoTaskType | Unset = UNSET
    name: str | Unset = UNSET
    description: str | Unset = UNSET
    parallel: bool | Unset = UNSET
    async_: bool | Unset = UNSET
    cron_supported: bool | Unset = UNSET
    cron_config: CronConfig | Unset = UNSET
    metadata: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        task_type: str | Unset = UNSET
        if not isinstance(self.task_type, Unset):
            task_type = self.task_type.value

        name = self.name

        description = self.description

        parallel = self.parallel

        async_ = self.async_

        cron_supported = self.cron_supported

        cron_config: dict[str, Any] | Unset = UNSET
        if not isinstance(self.cron_config, Unset):
            cron_config = self.cron_config.to_dict()

        metadata = self.metadata

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if task_type is not UNSET:
            field_dict["taskType"] = task_type
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if parallel is not UNSET:
            field_dict["parallel"] = parallel
        if async_ is not UNSET:
            field_dict["async"] = async_
        if cron_supported is not UNSET:
            field_dict["cronSupported"] = cron_supported
        if cron_config is not UNSET:
            field_dict["cronConfig"] = cron_config
        if metadata is not UNSET:
            field_dict["metadata"] = metadata

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cron_config import CronConfig

        d = dict(src_dict)
        _task_type = d.pop("taskType", UNSET)
        task_type: TaskInfoTaskType | Unset
        if isinstance(_task_type, Unset):
            task_type = UNSET
        else:
            task_type = TaskInfoTaskType(_task_type)

        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        parallel = d.pop("parallel", UNSET)

        async_ = d.pop("async", UNSET)

        cron_supported = d.pop("cronSupported", UNSET)

        _cron_config = d.pop("cronConfig", UNSET)
        cron_config: CronConfig | Unset
        if isinstance(_cron_config, Unset):
            cron_config = UNSET
        else:
            cron_config = CronConfig.from_dict(_cron_config)

        metadata = d.pop("metadata", UNSET)

        task_info = cls(
            task_type=task_type,
            name=name,
            description=description,
            parallel=parallel,
            async_=async_,
            cron_supported=cron_supported,
            cron_config=cron_config,
            metadata=metadata,
        )

        task_info.additional_properties = d
        return task_info

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
