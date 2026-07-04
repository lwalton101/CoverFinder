from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ProgressBucket")


@_attrs_define
class ProgressBucket:
    """
    Attributes:
        range_ (str | Unset):
        min_ (int | Unset):
        max_ (int | Unset):
        count (int | Unset):
    """

    range_: str | Unset = UNSET
    min_: int | Unset = UNSET
    max_: int | Unset = UNSET
    count: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        range_ = self.range_

        min_ = self.min_

        max_ = self.max_

        count = self.count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if range_ is not UNSET:
            field_dict["range"] = range_
        if min_ is not UNSET:
            field_dict["min"] = min_
        if max_ is not UNSET:
            field_dict["max"] = max_
        if count is not UNSET:
            field_dict["count"] = count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        range_ = d.pop("range", UNSET)

        min_ = d.pop("min", UNSET)

        max_ = d.pop("max", UNSET)

        count = d.pop("count", UNSET)

        progress_bucket = cls(
            range_=range_,
            min_=min_,
            max_=max_,
            count=count,
        )

        progress_bucket.additional_properties = d
        return progress_bucket

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
