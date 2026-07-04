from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.delete_metadata_request_metadata_type import DeleteMetadataRequestMetadataType

T = TypeVar("T", bound="DeleteMetadataRequest")


@_attrs_define
class DeleteMetadataRequest:
    """Delete metadata request

    Attributes:
        metadata_type (DeleteMetadataRequestMetadataType):
        values_to_delete (list[str]):
    """

    metadata_type: DeleteMetadataRequestMetadataType
    values_to_delete: list[str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        metadata_type = self.metadata_type.value

        values_to_delete = self.values_to_delete

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "metadataType": metadata_type,
                "valuesToDelete": values_to_delete,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        metadata_type = DeleteMetadataRequestMetadataType(d.pop("metadataType"))

        values_to_delete = cast(list[str], d.pop("valuesToDelete"))

        delete_metadata_request = cls(
            metadata_type=metadata_type,
            values_to_delete=values_to_delete,
        )

        delete_metadata_request.additional_properties = d
        return delete_metadata_request

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
