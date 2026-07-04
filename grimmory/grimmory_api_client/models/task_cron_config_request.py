from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TaskCronConfigRequest")


@_attrs_define
class TaskCronConfigRequest:
    """
    Attributes:
        cron_expression (str | Unset):
        enabled (bool | Unset):
    """

    cron_expression: str | Unset = UNSET
    enabled: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cron_expression = self.cron_expression

        enabled = self.enabled

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cron_expression is not UNSET:
            field_dict["cronExpression"] = cron_expression
        if enabled is not UNSET:
            field_dict["enabled"] = enabled

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        cron_expression = d.pop("cronExpression", UNSET)

        enabled = d.pop("enabled", UNSET)

        task_cron_config_request = cls(
            cron_expression=cron_expression,
            enabled=enabled,
        )

        task_cron_config_request.additional_properties = d
        return task_cron_config_request

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
