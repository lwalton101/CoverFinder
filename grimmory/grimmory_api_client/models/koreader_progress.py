from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="KoreaderProgress")


@_attrs_define
class KoreaderProgress:
    """KoReader progress object

    Attributes:
        timestamp (int | Unset):
        document (str | Unset):
        percentage (float | Unset):
        progress (str | Unset):
        device (str | Unset):
        device_id (str | Unset):
    """

    timestamp: int | Unset = UNSET
    document: str | Unset = UNSET
    percentage: float | Unset = UNSET
    progress: str | Unset = UNSET
    device: str | Unset = UNSET
    device_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        timestamp = self.timestamp

        document = self.document

        percentage = self.percentage

        progress = self.progress

        device = self.device

        device_id = self.device_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if timestamp is not UNSET:
            field_dict["timestamp"] = timestamp
        if document is not UNSET:
            field_dict["document"] = document
        if percentage is not UNSET:
            field_dict["percentage"] = percentage
        if progress is not UNSET:
            field_dict["progress"] = progress
        if device is not UNSET:
            field_dict["device"] = device
        if device_id is not UNSET:
            field_dict["device_id"] = device_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        timestamp = d.pop("timestamp", UNSET)

        document = d.pop("document", UNSET)

        percentage = d.pop("percentage", UNSET)

        progress = d.pop("progress", UNSET)

        device = d.pop("device", UNSET)

        device_id = d.pop("device_id", UNSET)

        koreader_progress = cls(
            timestamp=timestamp,
            document=document,
            percentage=percentage,
            progress=progress,
            device=device,
            device_id=device_id,
        )

        koreader_progress.additional_properties = d
        return koreader_progress

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
