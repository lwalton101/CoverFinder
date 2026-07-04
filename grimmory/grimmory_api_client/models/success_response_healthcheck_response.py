from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.healthcheck_response import HealthcheckResponse


T = TypeVar("T", bound="SuccessResponseHealthcheckResponse")


@_attrs_define
class SuccessResponseHealthcheckResponse:
    """
    Attributes:
        status (int | Unset):
        message (str | Unset):
        data (HealthcheckResponse | Unset):
        timestamp (datetime.datetime | Unset):
    """

    status: int | Unset = UNSET
    message: str | Unset = UNSET
    data: HealthcheckResponse | Unset = UNSET
    timestamp: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        status = self.status

        message = self.message

        data: dict[str, Any] | Unset = UNSET
        if not isinstance(self.data, Unset):
            data = self.data.to_dict()

        timestamp: str | Unset = UNSET
        if not isinstance(self.timestamp, Unset):
            timestamp = self.timestamp.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if status is not UNSET:
            field_dict["status"] = status
        if message is not UNSET:
            field_dict["message"] = message
        if data is not UNSET:
            field_dict["data"] = data
        if timestamp is not UNSET:
            field_dict["timestamp"] = timestamp

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.healthcheck_response import HealthcheckResponse

        d = dict(src_dict)
        status = d.pop("status", UNSET)

        message = d.pop("message", UNSET)

        _data = d.pop("data", UNSET)
        data: HealthcheckResponse | Unset
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = HealthcheckResponse.from_dict(_data)

        _timestamp = d.pop("timestamp", UNSET)
        timestamp: datetime.datetime | Unset
        if isinstance(_timestamp, Unset):
            timestamp = UNSET
        else:
            timestamp = datetime.datetime.fromisoformat(_timestamp)

        success_response_healthcheck_response = cls(
            status=status,
            message=message,
            data=data,
            timestamp=timestamp,
        )

        success_response_healthcheck_response.additional_properties = d
        return success_response_healthcheck_response

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
