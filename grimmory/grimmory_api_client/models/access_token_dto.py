from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AccessTokenDto")


@_attrs_define
class AccessTokenDto:
    """
    Attributes:
        access_token (str | Unset):
        refresh_token (str | Unset):
        expires (int | Unset):
        is_default_password (bool | Unset):
    """

    access_token: str | Unset = UNSET
    refresh_token: str | Unset = UNSET
    expires: int | Unset = UNSET
    is_default_password: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        access_token = self.access_token

        refresh_token = self.refresh_token

        expires = self.expires

        is_default_password = self.is_default_password

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if access_token is not UNSET:
            field_dict["accessToken"] = access_token
        if refresh_token is not UNSET:
            field_dict["refreshToken"] = refresh_token
        if expires is not UNSET:
            field_dict["expires"] = expires
        if is_default_password is not UNSET:
            field_dict["isDefaultPassword"] = is_default_password

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        access_token = d.pop("accessToken", UNSET)

        refresh_token = d.pop("refreshToken", UNSET)

        expires = d.pop("expires", UNSET)

        is_default_password = d.pop("isDefaultPassword", UNSET)

        access_token_dto = cls(
            access_token=access_token,
            refresh_token=refresh_token,
            expires=expires,
            is_default_password=is_default_password,
        )

        access_token_dto.additional_properties = d
        return access_token_dto

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
