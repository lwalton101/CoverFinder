from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="KoreaderUser")


@_attrs_define
class KoreaderUser:
    """
    Attributes:
        id (int | Unset):
        username (str | Unset):
        password (str | Unset):
        password_md5 (str | Unset):
        sync_enabled (bool | Unset):
        sync_with_web_reader (bool | Unset):
    """

    id: int | Unset = UNSET
    username: str | Unset = UNSET
    password: str | Unset = UNSET
    password_md5: str | Unset = UNSET
    sync_enabled: bool | Unset = UNSET
    sync_with_web_reader: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        username = self.username

        password = self.password

        password_md5 = self.password_md5

        sync_enabled = self.sync_enabled

        sync_with_web_reader = self.sync_with_web_reader

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if username is not UNSET:
            field_dict["username"] = username
        if password is not UNSET:
            field_dict["password"] = password
        if password_md5 is not UNSET:
            field_dict["passwordMD5"] = password_md5
        if sync_enabled is not UNSET:
            field_dict["syncEnabled"] = sync_enabled
        if sync_with_web_reader is not UNSET:
            field_dict["syncWithWebReader"] = sync_with_web_reader

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        username = d.pop("username", UNSET)

        password = d.pop("password", UNSET)

        password_md5 = d.pop("passwordMD5", UNSET)

        sync_enabled = d.pop("syncEnabled", UNSET)

        sync_with_web_reader = d.pop("syncWithWebReader", UNSET)

        koreader_user = cls(
            id=id,
            username=username,
            password=password,
            password_md5=password_md5,
            sync_enabled=sync_enabled,
            sync_with_web_reader=sync_with_web_reader,
        )

        koreader_user.additional_properties = d
        return koreader_user

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
