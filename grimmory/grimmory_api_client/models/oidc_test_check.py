from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.oidc_test_check_status import OidcTestCheckStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="OidcTestCheck")


@_attrs_define
class OidcTestCheck:
    """
    Attributes:
        name (str | Unset):
        status (OidcTestCheckStatus | Unset):
        message (str | Unset):
    """

    name: str | Unset = UNSET
    status: OidcTestCheckStatus | Unset = UNSET
    message: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        message = self.message

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if status is not UNSET:
            field_dict["status"] = status
        if message is not UNSET:
            field_dict["message"] = message

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name", UNSET)

        _status = d.pop("status", UNSET)
        status: OidcTestCheckStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = OidcTestCheckStatus(_status)

        message = d.pop("message", UNSET)

        oidc_test_check = cls(
            name=name,
            status=status,
            message=message,
        )

        oidc_test_check.additional_properties = d
        return oidc_test_check

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
