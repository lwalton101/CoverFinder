from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateEmailRecipientRequest")


@_attrs_define
class CreateEmailRecipientRequest:
    """Email recipient creation request

    Attributes:
        email (str):
        name (str):
        default_recipient (bool | Unset):
    """

    email: str
    name: str
    default_recipient: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        email = self.email

        name = self.name

        default_recipient = self.default_recipient

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "email": email,
                "name": name,
            }
        )
        if default_recipient is not UNSET:
            field_dict["defaultRecipient"] = default_recipient

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        email = d.pop("email")

        name = d.pop("name")

        default_recipient = d.pop("defaultRecipient", UNSET)

        create_email_recipient_request = cls(
            email=email,
            name=name,
            default_recipient=default_recipient,
        )

        create_email_recipient_request.additional_properties = d
        return create_email_recipient_request

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
