from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AppUserInfo")


@_attrs_define
class AppUserInfo:
    """
    Attributes:
        can_upload (bool | Unset):
        can_download (bool | Unset):
        can_access_bookdrop (bool | Unset):
        max_file_upload_size_mb (int | Unset):
        admin (bool | Unset):
    """

    can_upload: bool | Unset = UNSET
    can_download: bool | Unset = UNSET
    can_access_bookdrop: bool | Unset = UNSET
    max_file_upload_size_mb: int | Unset = UNSET
    admin: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        can_upload = self.can_upload

        can_download = self.can_download

        can_access_bookdrop = self.can_access_bookdrop

        max_file_upload_size_mb = self.max_file_upload_size_mb

        admin = self.admin

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if can_upload is not UNSET:
            field_dict["canUpload"] = can_upload
        if can_download is not UNSET:
            field_dict["canDownload"] = can_download
        if can_access_bookdrop is not UNSET:
            field_dict["canAccessBookdrop"] = can_access_bookdrop
        if max_file_upload_size_mb is not UNSET:
            field_dict["maxFileUploadSizeMb"] = max_file_upload_size_mb
        if admin is not UNSET:
            field_dict["admin"] = admin

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        can_upload = d.pop("canUpload", UNSET)

        can_download = d.pop("canDownload", UNSET)

        can_access_bookdrop = d.pop("canAccessBookdrop", UNSET)

        max_file_upload_size_mb = d.pop("maxFileUploadSizeMb", UNSET)

        admin = d.pop("admin", UNSET)

        app_user_info = cls(
            can_upload=can_upload,
            can_download=can_download,
            can_access_bookdrop=can_access_bookdrop,
            max_file_upload_size_mb=max_file_upload_size_mb,
            admin=admin,
        )

        app_user_info.additional_properties = d
        return app_user_info

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
