from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UserCreateRequest")


@_attrs_define
class UserCreateRequest:
    """User registration request

    Attributes:
        username (str):
        password (str):
        name (str):
        email (str):
        permission_upload (bool | Unset):
        permission_download (bool | Unset):
        permission_edit_metadata (bool | Unset):
        permission_manage_library (bool | Unset):
        permission_email_book (bool | Unset):
        permission_delete_book (bool | Unset):
        permission_access_opds (bool | Unset):
        permission_sync_koreader (bool | Unset):
        permission_sync_kobo (bool | Unset):
        permission_admin (bool | Unset):
        permission_manage_metadata_config (bool | Unset):
        permission_access_bookdrop (bool | Unset):
        permission_access_library_stats (bool | Unset):
        permission_access_user_stats (bool | Unset):
        permission_access_task_manager (bool | Unset):
        permission_manage_global_preferences (bool | Unset):
        permission_manage_icons (bool | Unset):
        permission_manage_fonts (bool | Unset):
        permission_bulk_auto_fetch_metadata (bool | Unset):
        permission_bulk_custom_fetch_metadata (bool | Unset):
        permission_bulk_edit_metadata (bool | Unset):
        permission_bulk_regenerate_cover (bool | Unset):
        permission_move_organize_files (bool | Unset):
        permission_bulk_lock_unlock_metadata (bool | Unset):
        permission_bulk_reset_booklore_read_progress (bool | Unset):
        permission_bulk_reset_ko_reader_read_progress (bool | Unset):
        permission_bulk_reset_book_read_status (bool | Unset):
        selected_libraries (list[int] | Unset):
    """

    username: str
    password: str
    name: str
    email: str
    permission_upload: bool | Unset = UNSET
    permission_download: bool | Unset = UNSET
    permission_edit_metadata: bool | Unset = UNSET
    permission_manage_library: bool | Unset = UNSET
    permission_email_book: bool | Unset = UNSET
    permission_delete_book: bool | Unset = UNSET
    permission_access_opds: bool | Unset = UNSET
    permission_sync_koreader: bool | Unset = UNSET
    permission_sync_kobo: bool | Unset = UNSET
    permission_admin: bool | Unset = UNSET
    permission_manage_metadata_config: bool | Unset = UNSET
    permission_access_bookdrop: bool | Unset = UNSET
    permission_access_library_stats: bool | Unset = UNSET
    permission_access_user_stats: bool | Unset = UNSET
    permission_access_task_manager: bool | Unset = UNSET
    permission_manage_global_preferences: bool | Unset = UNSET
    permission_manage_icons: bool | Unset = UNSET
    permission_manage_fonts: bool | Unset = UNSET
    permission_bulk_auto_fetch_metadata: bool | Unset = UNSET
    permission_bulk_custom_fetch_metadata: bool | Unset = UNSET
    permission_bulk_edit_metadata: bool | Unset = UNSET
    permission_bulk_regenerate_cover: bool | Unset = UNSET
    permission_move_organize_files: bool | Unset = UNSET
    permission_bulk_lock_unlock_metadata: bool | Unset = UNSET
    permission_bulk_reset_booklore_read_progress: bool | Unset = UNSET
    permission_bulk_reset_ko_reader_read_progress: bool | Unset = UNSET
    permission_bulk_reset_book_read_status: bool | Unset = UNSET
    selected_libraries: list[int] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        username = self.username

        password = self.password

        name = self.name

        email = self.email

        permission_upload = self.permission_upload

        permission_download = self.permission_download

        permission_edit_metadata = self.permission_edit_metadata

        permission_manage_library = self.permission_manage_library

        permission_email_book = self.permission_email_book

        permission_delete_book = self.permission_delete_book

        permission_access_opds = self.permission_access_opds

        permission_sync_koreader = self.permission_sync_koreader

        permission_sync_kobo = self.permission_sync_kobo

        permission_admin = self.permission_admin

        permission_manage_metadata_config = self.permission_manage_metadata_config

        permission_access_bookdrop = self.permission_access_bookdrop

        permission_access_library_stats = self.permission_access_library_stats

        permission_access_user_stats = self.permission_access_user_stats

        permission_access_task_manager = self.permission_access_task_manager

        permission_manage_global_preferences = self.permission_manage_global_preferences

        permission_manage_icons = self.permission_manage_icons

        permission_manage_fonts = self.permission_manage_fonts

        permission_bulk_auto_fetch_metadata = self.permission_bulk_auto_fetch_metadata

        permission_bulk_custom_fetch_metadata = self.permission_bulk_custom_fetch_metadata

        permission_bulk_edit_metadata = self.permission_bulk_edit_metadata

        permission_bulk_regenerate_cover = self.permission_bulk_regenerate_cover

        permission_move_organize_files = self.permission_move_organize_files

        permission_bulk_lock_unlock_metadata = self.permission_bulk_lock_unlock_metadata

        permission_bulk_reset_booklore_read_progress = self.permission_bulk_reset_booklore_read_progress

        permission_bulk_reset_ko_reader_read_progress = self.permission_bulk_reset_ko_reader_read_progress

        permission_bulk_reset_book_read_status = self.permission_bulk_reset_book_read_status

        selected_libraries: list[int] | Unset = UNSET
        if not isinstance(self.selected_libraries, Unset):
            selected_libraries = self.selected_libraries

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "username": username,
                "password": password,
                "name": name,
                "email": email,
            }
        )
        if permission_upload is not UNSET:
            field_dict["permissionUpload"] = permission_upload
        if permission_download is not UNSET:
            field_dict["permissionDownload"] = permission_download
        if permission_edit_metadata is not UNSET:
            field_dict["permissionEditMetadata"] = permission_edit_metadata
        if permission_manage_library is not UNSET:
            field_dict["permissionManageLibrary"] = permission_manage_library
        if permission_email_book is not UNSET:
            field_dict["permissionEmailBook"] = permission_email_book
        if permission_delete_book is not UNSET:
            field_dict["permissionDeleteBook"] = permission_delete_book
        if permission_access_opds is not UNSET:
            field_dict["permissionAccessOpds"] = permission_access_opds
        if permission_sync_koreader is not UNSET:
            field_dict["permissionSyncKoreader"] = permission_sync_koreader
        if permission_sync_kobo is not UNSET:
            field_dict["permissionSyncKobo"] = permission_sync_kobo
        if permission_admin is not UNSET:
            field_dict["permissionAdmin"] = permission_admin
        if permission_manage_metadata_config is not UNSET:
            field_dict["permissionManageMetadataConfig"] = permission_manage_metadata_config
        if permission_access_bookdrop is not UNSET:
            field_dict["permissionAccessBookdrop"] = permission_access_bookdrop
        if permission_access_library_stats is not UNSET:
            field_dict["permissionAccessLibraryStats"] = permission_access_library_stats
        if permission_access_user_stats is not UNSET:
            field_dict["permissionAccessUserStats"] = permission_access_user_stats
        if permission_access_task_manager is not UNSET:
            field_dict["permissionAccessTaskManager"] = permission_access_task_manager
        if permission_manage_global_preferences is not UNSET:
            field_dict["permissionManageGlobalPreferences"] = permission_manage_global_preferences
        if permission_manage_icons is not UNSET:
            field_dict["permissionManageIcons"] = permission_manage_icons
        if permission_manage_fonts is not UNSET:
            field_dict["permissionManageFonts"] = permission_manage_fonts
        if permission_bulk_auto_fetch_metadata is not UNSET:
            field_dict["permissionBulkAutoFetchMetadata"] = permission_bulk_auto_fetch_metadata
        if permission_bulk_custom_fetch_metadata is not UNSET:
            field_dict["permissionBulkCustomFetchMetadata"] = permission_bulk_custom_fetch_metadata
        if permission_bulk_edit_metadata is not UNSET:
            field_dict["permissionBulkEditMetadata"] = permission_bulk_edit_metadata
        if permission_bulk_regenerate_cover is not UNSET:
            field_dict["permissionBulkRegenerateCover"] = permission_bulk_regenerate_cover
        if permission_move_organize_files is not UNSET:
            field_dict["permissionMoveOrganizeFiles"] = permission_move_organize_files
        if permission_bulk_lock_unlock_metadata is not UNSET:
            field_dict["permissionBulkLockUnlockMetadata"] = permission_bulk_lock_unlock_metadata
        if permission_bulk_reset_booklore_read_progress is not UNSET:
            field_dict["permissionBulkResetBookloreReadProgress"] = permission_bulk_reset_booklore_read_progress
        if permission_bulk_reset_ko_reader_read_progress is not UNSET:
            field_dict["permissionBulkResetKoReaderReadProgress"] = permission_bulk_reset_ko_reader_read_progress
        if permission_bulk_reset_book_read_status is not UNSET:
            field_dict["permissionBulkResetBookReadStatus"] = permission_bulk_reset_book_read_status
        if selected_libraries is not UNSET:
            field_dict["selectedLibraries"] = selected_libraries

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        username = d.pop("username")

        password = d.pop("password")

        name = d.pop("name")

        email = d.pop("email")

        permission_upload = d.pop("permissionUpload", UNSET)

        permission_download = d.pop("permissionDownload", UNSET)

        permission_edit_metadata = d.pop("permissionEditMetadata", UNSET)

        permission_manage_library = d.pop("permissionManageLibrary", UNSET)

        permission_email_book = d.pop("permissionEmailBook", UNSET)

        permission_delete_book = d.pop("permissionDeleteBook", UNSET)

        permission_access_opds = d.pop("permissionAccessOpds", UNSET)

        permission_sync_koreader = d.pop("permissionSyncKoreader", UNSET)

        permission_sync_kobo = d.pop("permissionSyncKobo", UNSET)

        permission_admin = d.pop("permissionAdmin", UNSET)

        permission_manage_metadata_config = d.pop("permissionManageMetadataConfig", UNSET)

        permission_access_bookdrop = d.pop("permissionAccessBookdrop", UNSET)

        permission_access_library_stats = d.pop("permissionAccessLibraryStats", UNSET)

        permission_access_user_stats = d.pop("permissionAccessUserStats", UNSET)

        permission_access_task_manager = d.pop("permissionAccessTaskManager", UNSET)

        permission_manage_global_preferences = d.pop("permissionManageGlobalPreferences", UNSET)

        permission_manage_icons = d.pop("permissionManageIcons", UNSET)

        permission_manage_fonts = d.pop("permissionManageFonts", UNSET)

        permission_bulk_auto_fetch_metadata = d.pop("permissionBulkAutoFetchMetadata", UNSET)

        permission_bulk_custom_fetch_metadata = d.pop("permissionBulkCustomFetchMetadata", UNSET)

        permission_bulk_edit_metadata = d.pop("permissionBulkEditMetadata", UNSET)

        permission_bulk_regenerate_cover = d.pop("permissionBulkRegenerateCover", UNSET)

        permission_move_organize_files = d.pop("permissionMoveOrganizeFiles", UNSET)

        permission_bulk_lock_unlock_metadata = d.pop("permissionBulkLockUnlockMetadata", UNSET)

        permission_bulk_reset_booklore_read_progress = d.pop("permissionBulkResetBookloreReadProgress", UNSET)

        permission_bulk_reset_ko_reader_read_progress = d.pop("permissionBulkResetKoReaderReadProgress", UNSET)

        permission_bulk_reset_book_read_status = d.pop("permissionBulkResetBookReadStatus", UNSET)

        selected_libraries = cast(list[int], d.pop("selectedLibraries", UNSET))

        user_create_request = cls(
            username=username,
            password=password,
            name=name,
            email=email,
            permission_upload=permission_upload,
            permission_download=permission_download,
            permission_edit_metadata=permission_edit_metadata,
            permission_manage_library=permission_manage_library,
            permission_email_book=permission_email_book,
            permission_delete_book=permission_delete_book,
            permission_access_opds=permission_access_opds,
            permission_sync_koreader=permission_sync_koreader,
            permission_sync_kobo=permission_sync_kobo,
            permission_admin=permission_admin,
            permission_manage_metadata_config=permission_manage_metadata_config,
            permission_access_bookdrop=permission_access_bookdrop,
            permission_access_library_stats=permission_access_library_stats,
            permission_access_user_stats=permission_access_user_stats,
            permission_access_task_manager=permission_access_task_manager,
            permission_manage_global_preferences=permission_manage_global_preferences,
            permission_manage_icons=permission_manage_icons,
            permission_manage_fonts=permission_manage_fonts,
            permission_bulk_auto_fetch_metadata=permission_bulk_auto_fetch_metadata,
            permission_bulk_custom_fetch_metadata=permission_bulk_custom_fetch_metadata,
            permission_bulk_edit_metadata=permission_bulk_edit_metadata,
            permission_bulk_regenerate_cover=permission_bulk_regenerate_cover,
            permission_move_organize_files=permission_move_organize_files,
            permission_bulk_lock_unlock_metadata=permission_bulk_lock_unlock_metadata,
            permission_bulk_reset_booklore_read_progress=permission_bulk_reset_booklore_read_progress,
            permission_bulk_reset_ko_reader_read_progress=permission_bulk_reset_ko_reader_read_progress,
            permission_bulk_reset_book_read_status=permission_bulk_reset_book_read_status,
            selected_libraries=selected_libraries,
        )

        user_create_request.additional_properties = d
        return user_create_request

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
