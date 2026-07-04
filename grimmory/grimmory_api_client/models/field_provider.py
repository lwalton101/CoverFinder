from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.field_provider_p1 import FieldProviderP1
from ..models.field_provider_p2 import FieldProviderP2
from ..models.field_provider_p3 import FieldProviderP3
from ..models.field_provider_p4 import FieldProviderP4
from ..types import UNSET, Unset

T = TypeVar("T", bound="FieldProvider")


@_attrs_define
class FieldProvider:
    """
    Attributes:
        p1 (FieldProviderP1 | Unset):
        p2 (FieldProviderP2 | Unset):
        p3 (FieldProviderP3 | Unset):
        p4 (FieldProviderP4 | Unset):
    """

    p1: FieldProviderP1 | Unset = UNSET
    p2: FieldProviderP2 | Unset = UNSET
    p3: FieldProviderP3 | Unset = UNSET
    p4: FieldProviderP4 | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        p1: str | Unset = UNSET
        if not isinstance(self.p1, Unset):
            p1 = self.p1.value

        p2: str | Unset = UNSET
        if not isinstance(self.p2, Unset):
            p2 = self.p2.value

        p3: str | Unset = UNSET
        if not isinstance(self.p3, Unset):
            p3 = self.p3.value

        p4: str | Unset = UNSET
        if not isinstance(self.p4, Unset):
            p4 = self.p4.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if p1 is not UNSET:
            field_dict["p1"] = p1
        if p2 is not UNSET:
            field_dict["p2"] = p2
        if p3 is not UNSET:
            field_dict["p3"] = p3
        if p4 is not UNSET:
            field_dict["p4"] = p4

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _p1 = d.pop("p1", UNSET)
        p1: FieldProviderP1 | Unset
        if isinstance(_p1, Unset):
            p1 = UNSET
        else:
            p1 = FieldProviderP1(_p1)

        _p2 = d.pop("p2", UNSET)
        p2: FieldProviderP2 | Unset
        if isinstance(_p2, Unset):
            p2 = UNSET
        else:
            p2 = FieldProviderP2(_p2)

        _p3 = d.pop("p3", UNSET)
        p3: FieldProviderP3 | Unset
        if isinstance(_p3, Unset):
            p3 = UNSET
        else:
            p3 = FieldProviderP3(_p3)

        _p4 = d.pop("p4", UNSET)
        p4: FieldProviderP4 | Unset
        if isinstance(_p4, Unset):
            p4 = UNSET
        else:
            p4 = FieldProviderP4(_p4)

        field_provider = cls(
            p1=p1,
            p2=p2,
            p3=p3,
            p4=p4,
        )

        field_provider.additional_properties = d
        return field_provider

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
