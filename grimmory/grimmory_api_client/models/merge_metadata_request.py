from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.merge_metadata_request_metadata_type import MergeMetadataRequestMetadataType
from ..types import UNSET, Unset

T = TypeVar("T", bound="MergeMetadataRequest")


@_attrs_define
class MergeMetadataRequest:
    """Merge metadata request

    Attributes:
        metadata_type (MergeMetadataRequestMetadataType | Unset):
        target_values (list[str] | Unset):
        values_to_merge (list[str] | Unset):
    """

    metadata_type: MergeMetadataRequestMetadataType | Unset = UNSET
    target_values: list[str] | Unset = UNSET
    values_to_merge: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        metadata_type: str | Unset = UNSET
        if not isinstance(self.metadata_type, Unset):
            metadata_type = self.metadata_type.value

        target_values: list[str] | Unset = UNSET
        if not isinstance(self.target_values, Unset):
            target_values = self.target_values

        values_to_merge: list[str] | Unset = UNSET
        if not isinstance(self.values_to_merge, Unset):
            values_to_merge = self.values_to_merge

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if metadata_type is not UNSET:
            field_dict["metadataType"] = metadata_type
        if target_values is not UNSET:
            field_dict["targetValues"] = target_values
        if values_to_merge is not UNSET:
            field_dict["valuesToMerge"] = values_to_merge

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _metadata_type = d.pop("metadataType", UNSET)
        metadata_type: MergeMetadataRequestMetadataType | Unset
        if isinstance(_metadata_type, Unset):
            metadata_type = UNSET
        else:
            metadata_type = MergeMetadataRequestMetadataType(_metadata_type)

        target_values = cast(list[str], d.pop("targetValues", UNSET))

        values_to_merge = cast(list[str], d.pop("valuesToMerge", UNSET))

        merge_metadata_request = cls(
            metadata_type=metadata_type,
            target_values=target_values,
            values_to_merge=values_to_merge,
        )

        merge_metadata_request.additional_properties = d
        return merge_metadata_request

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
