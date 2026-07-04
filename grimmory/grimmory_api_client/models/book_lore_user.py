from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.book_lore_user_provisioning_method import BookLoreUserProvisioningMethod
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.library import Library
    from ..models.user_permissions import UserPermissions
    from ..models.user_settings import UserSettings


T = TypeVar("T", bound="BookLoreUser")


@_attrs_define
class BookLoreUser:
    """
    Attributes:
        id (int | Unset):
        username (str | Unset):
        name (str | Unset):
        email (str | Unset):
        locale (str | Unset):
        theme (str | Unset):
        theme_accent (str | Unset):
        theme_sync_enabled (bool | Unset):
        ui_font (str | Unset):
        provisioning_method (BookLoreUserProvisioningMethod | Unset):
        assigned_libraries (list[Library] | Unset):
        permissions (UserPermissions | Unset):
        user_settings (UserSettings | Unset):
        default_password (bool | Unset):
    """

    id: int | Unset = UNSET
    username: str | Unset = UNSET
    name: str | Unset = UNSET
    email: str | Unset = UNSET
    locale: str | Unset = UNSET
    theme: str | Unset = UNSET
    theme_accent: str | Unset = UNSET
    theme_sync_enabled: bool | Unset = UNSET
    ui_font: str | Unset = UNSET
    provisioning_method: BookLoreUserProvisioningMethod | Unset = UNSET
    assigned_libraries: list[Library] | Unset = UNSET
    permissions: UserPermissions | Unset = UNSET
    user_settings: UserSettings | Unset = UNSET
    default_password: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        username = self.username

        name = self.name

        email = self.email

        locale = self.locale

        theme = self.theme

        theme_accent = self.theme_accent

        theme_sync_enabled = self.theme_sync_enabled

        ui_font = self.ui_font

        provisioning_method: str | Unset = UNSET
        if not isinstance(self.provisioning_method, Unset):
            provisioning_method = self.provisioning_method.value

        assigned_libraries: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.assigned_libraries, Unset):
            assigned_libraries = []
            for assigned_libraries_item_data in self.assigned_libraries:
                assigned_libraries_item = assigned_libraries_item_data.to_dict()
                assigned_libraries.append(assigned_libraries_item)

        permissions: dict[str, Any] | Unset = UNSET
        if not isinstance(self.permissions, Unset):
            permissions = self.permissions.to_dict()

        user_settings: dict[str, Any] | Unset = UNSET
        if not isinstance(self.user_settings, Unset):
            user_settings = self.user_settings.to_dict()

        default_password = self.default_password

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if username is not UNSET:
            field_dict["username"] = username
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
        if provisioning_method is not UNSET:
            field_dict["provisioningMethod"] = provisioning_method
        if assigned_libraries is not UNSET:
            field_dict["assignedLibraries"] = assigned_libraries
        if permissions is not UNSET:
            field_dict["permissions"] = permissions
        if user_settings is not UNSET:
            field_dict["userSettings"] = user_settings
        if default_password is not UNSET:
            field_dict["defaultPassword"] = default_password

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.library import Library
        from ..models.user_permissions import UserPermissions
        from ..models.user_settings import UserSettings

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        username = d.pop("username", UNSET)

        name = d.pop("name", UNSET)

        email = d.pop("email", UNSET)

        locale = d.pop("locale", UNSET)

        theme = d.pop("theme", UNSET)

        theme_accent = d.pop("themeAccent", UNSET)

        theme_sync_enabled = d.pop("themeSyncEnabled", UNSET)

        ui_font = d.pop("uiFont", UNSET)

        _provisioning_method = d.pop("provisioningMethod", UNSET)
        provisioning_method: BookLoreUserProvisioningMethod | Unset
        if isinstance(_provisioning_method, Unset):
            provisioning_method = UNSET
        else:
            provisioning_method = BookLoreUserProvisioningMethod(_provisioning_method)

        _assigned_libraries = d.pop("assignedLibraries", UNSET)
        assigned_libraries: list[Library] | Unset = UNSET
        if _assigned_libraries is not UNSET:
            assigned_libraries = []
            for assigned_libraries_item_data in _assigned_libraries:
                assigned_libraries_item = Library.from_dict(assigned_libraries_item_data)

                assigned_libraries.append(assigned_libraries_item)

        _permissions = d.pop("permissions", UNSET)
        permissions: UserPermissions | Unset
        if isinstance(_permissions, Unset):
            permissions = UNSET
        else:
            permissions = UserPermissions.from_dict(_permissions)

        _user_settings = d.pop("userSettings", UNSET)
        user_settings: UserSettings | Unset
        if isinstance(_user_settings, Unset):
            user_settings = UNSET
        else:
            user_settings = UserSettings.from_dict(_user_settings)

        default_password = d.pop("defaultPassword", UNSET)

        book_lore_user = cls(
            id=id,
            username=username,
            name=name,
            email=email,
            locale=locale,
            theme=theme,
            theme_accent=theme_accent,
            theme_sync_enabled=theme_sync_enabled,
            ui_font=ui_font,
            provisioning_method=provisioning_method,
            assigned_libraries=assigned_libraries,
            permissions=permissions,
            user_settings=user_settings,
            default_password=default_password,
        )

        book_lore_user.additional_properties = d
        return book_lore_user

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
