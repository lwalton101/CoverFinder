from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UserProfileUpdateRequest")


@_attrs_define
class UserProfileUpdateRequest:
    """User profile update request

    Attributes:
        name (str | Unset):
        email (str | Unset):
        locale (str | Unset):
        theme (str | Unset):
        theme_accent (str | Unset):
        theme_sync_enabled (bool | Unset):
        ui_font (str | Unset):
    """

    name: str | Unset = UNSET
    email: str | Unset = UNSET
    locale: str | Unset = UNSET
    theme: str | Unset = UNSET
    theme_accent: str | Unset = UNSET
    theme_sync_enabled: bool | Unset = UNSET
    ui_font: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        email = self.email

        locale = self.locale

        theme = self.theme

        theme_accent = self.theme_accent

        theme_sync_enabled = self.theme_sync_enabled

        ui_font = self.ui_font

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if email is not UNSET:
            field_dict["email"] = email
        if locale is not UNSET:
            field_dict["locale"] = locale
        if theme is not UNSET:
            field_dict["theme"] = theme
        if theme_accent is not UNSET:
            field_dict["themeAccent"] = theme_accent
        if theme_sync_enabled is not UNSET:
            field_dict["themeSyncEnabled"] = theme_sync_enabled
        if ui_font is not UNSET:
            field_dict["uiFont"] = ui_font

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name", UNSET)

        email = d.pop("email", UNSET)

        locale = d.pop("locale", UNSET)

        theme = d.pop("theme", UNSET)

        theme_accent = d.pop("themeAccent", UNSET)

        theme_sync_enabled = d.pop("themeSyncEnabled", UNSET)

        ui_font = d.pop("uiFont", UNSET)

        user_profile_update_request = cls(
            name=name,
            email=email,
            locale=locale,
            theme=theme,
            theme_accent=theme_accent,
            theme_sync_enabled=theme_sync_enabled,
            ui_font=ui_font,
        )

        user_profile_update_request.additional_properties = d
        return user_profile_update_request

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
