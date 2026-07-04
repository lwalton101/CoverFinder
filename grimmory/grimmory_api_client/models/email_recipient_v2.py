from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="EmailRecipientV2")


@_attrs_define
class EmailRecipientV2:
    """
    Attributes:
        id (int | Unset):
        user_id (int | Unset):
        email (str | Unset):
        name (str | Unset):
        default_recipient (bool | Unset):
    """

    id: int | Unset = UNSET
    user_id: int | Unset = UNSET
    email: str | Unset = UNSET
    name: str | Unset = UNSET
    default_recipient: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        user_id = self.user_id

        email = self.email

        name = self.name

        default_recipient = self.default_recipient

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if user_id is not UNSET:
            field_dict["userId"] = user_id
        if email is not UNSET:
            field_dict["email"] = email
        if name is not UNSET:
            field_dict["name"] = name
        if default_recipient is not UNSET:
            field_dict["defaultRecipient"] = default_recipient

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        user_id = d.pop("userId", UNSET)

        email = d.pop("email", UNSET)

        name = d.pop("name", UNSET)

        default_recipient = d.pop("defaultRecipient", UNSET)

        email_recipient_v2 = cls(
            id=id,
            user_id=user_id,
            email=email,
            name=name,
            default_recipient=default_recipient,
        )

        email_recipient_v2.additional_properties = d
        return email_recipient_v2

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
