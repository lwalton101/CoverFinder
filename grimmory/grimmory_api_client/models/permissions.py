from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Permissions")


@_attrs_define
class Permissions:
    """
    Attributes:
        can_upload (bool | Unset):
        can_download (bool | Unset):
        can_edit_metadata (bool | Unset):
        can_manage_library (bool | Unset):
        can_email_book (bool | Unset):
        can_delete_book (bool | Unset):
        can_access_opds (bool | Unset):
        can_sync_ko_reader (bool | Unset):
        can_sync_kobo (bool | Unset):
        can_manage_metadata_config (bool | Unset):
        can_access_bookdrop (bool | Unset):
        can_access_library_stats (bool | Unset):
        can_access_user_stats (bool | Unset):
        can_access_task_manager (bool | Unset):
        can_manage_global_preferences (bool | Unset):
        can_manage_icons (bool | Unset):
        can_manage_fonts (bool | Unset):
        can_bulk_auto_fetch_metadata (bool | Unset):
        can_bulk_custom_fetch_metadata (bool | Unset):
        can_bulk_edit_metadata (bool | Unset):
        can_bulk_regenerate_cover (bool | Unset):
        can_move_organize_files (bool | Unset):
        can_bulk_lock_unlock_metadata (bool | Unset):
        can_bulk_reset_booklore_read_progress (bool | Unset):
        can_bulk_reset_ko_reader_read_progress (bool | Unset):
        can_bulk_reset_book_read_status (bool | Unset):
        admin (bool | Unset):
    """

    can_upload: bool | Unset = UNSET
    can_download: bool | Unset = UNSET
    can_edit_metadata: bool | Unset = UNSET
    can_manage_library: bool | Unset = UNSET
    can_email_book: bool | Unset = UNSET
    can_delete_book: bool | Unset = UNSET
    can_access_opds: bool | Unset = UNSET
    can_sync_ko_reader: bool | Unset = UNSET
    can_sync_kobo: bool | Unset = UNSET
    can_manage_metadata_config: bool | Unset = UNSET
    can_access_bookdrop: bool | Unset = UNSET
    can_access_library_stats: bool | Unset = UNSET
    can_access_user_stats: bool | Unset = UNSET
    can_access_task_manager: bool | Unset = UNSET
    can_manage_global_preferences: bool | Unset = UNSET
    can_manage_icons: bool | Unset = UNSET
    can_manage_fonts: bool | Unset = UNSET
    can_bulk_auto_fetch_metadata: bool | Unset = UNSET
    can_bulk_custom_fetch_metadata: bool | Unset = UNSET
    can_bulk_edit_metadata: bool | Unset = UNSET
    can_bulk_regenerate_cover: bool | Unset = UNSET
    can_move_organize_files: bool | Unset = UNSET
    can_bulk_lock_unlock_metadata: bool | Unset = UNSET
    can_bulk_reset_booklore_read_progress: bool | Unset = UNSET
    can_bulk_reset_ko_reader_read_progress: bool | Unset = UNSET
    can_bulk_reset_book_read_status: bool | Unset = UNSET
    admin: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        can_upload = self.can_upload

        can_download = self.can_download

        can_edit_metadata = self.can_edit_metadata

        can_manage_library = self.can_manage_library

        can_email_book = self.can_email_book

        can_delete_book = self.can_delete_book

        can_access_opds = self.can_access_opds

        can_sync_ko_reader = self.can_sync_ko_reader

        can_sync_kobo = self.can_sync_kobo

        can_manage_metadata_config = self.can_manage_metadata_config

        can_access_bookdrop = self.can_access_bookdrop

        can_access_library_stats = self.can_access_library_stats

        can_access_user_stats = self.can_access_user_stats

        can_access_task_manager = self.can_access_task_manager

        can_manage_global_preferences = self.can_manage_global_preferences

        can_manage_icons = self.can_manage_icons

        can_manage_fonts = self.can_manage_fonts

        can_bulk_auto_fetch_metadata = self.can_bulk_auto_fetch_metadata

        can_bulk_custom_fetch_metadata = self.can_bulk_custom_fetch_metadata

        can_bulk_edit_metadata = self.can_bulk_edit_metadata

        can_bulk_regenerate_cover = self.can_bulk_regenerate_cover

        can_move_organize_files = self.can_move_organize_files

        can_bulk_lock_unlock_metadata = self.can_bulk_lock_unlock_metadata

        can_bulk_reset_booklore_read_progress = self.can_bulk_reset_booklore_read_progress

        can_bulk_reset_ko_reader_read_progress = self.can_bulk_reset_ko_reader_read_progress

        can_bulk_reset_book_read_status = self.can_bulk_reset_book_read_status

        admin = self.admin

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if can_upload is not UNSET:
            field_dict["canUpload"] = can_upload
        if can_download is not UNSET:
            field_dict["canDownload"] = can_download
        if can_edit_metadata is not UNSET:
            field_dict["canEditMetadata"] = can_edit_metadata
        if can_manage_library is not UNSET:
            field_dict["canManageLibrary"] = can_manage_library
        if can_email_book is not UNSET:
            field_dict["canEmailBook"] = can_email_book
        if can_delete_book is not UNSET:
            field_dict["canDeleteBook"] = can_delete_book
        if can_access_opds is not UNSET:
            field_dict["canAccessOpds"] = can_access_opds
        if can_sync_ko_reader is not UNSET:
            field_dict["canSyncKoReader"] = can_sync_ko_reader
        if can_sync_kobo is not UNSET:
            field_dict["canSyncKobo"] = can_sync_kobo
        if can_manage_metadata_config is not UNSET:
            field_dict["canManageMetadataConfig"] = can_manage_metadata_config
        if can_access_bookdrop is not UNSET:
            field_dict["canAccessBookdrop"] = can_access_bookdrop
        if can_access_library_stats is not UNSET:
            field_dict["canAccessLibraryStats"] = can_access_library_stats
        if can_access_user_stats is not UNSET:
            field_dict["canAccessUserStats"] = can_access_user_stats
        if can_access_task_manager is not UNSET:
            field_dict["canAccessTaskManager"] = can_access_task_manager
        if can_manage_global_preferences is not UNSET:
            field_dict["canManageGlobalPreferences"] = can_manage_global_preferences
        if can_manage_icons is not UNSET:
            field_dict["canManageIcons"] = can_manage_icons
        if can_manage_fonts is not UNSET:
            field_dict["canManageFonts"] = can_manage_fonts
        if can_bulk_auto_fetch_metadata is not UNSET:
            field_dict["canBulkAutoFetchMetadata"] = can_bulk_auto_fetch_metadata
        if can_bulk_custom_fetch_metadata is not UNSET:
            field_dict["canBulkCustomFetchMetadata"] = can_bulk_custom_fetch_metadata
        if can_bulk_edit_metadata is not UNSET:
            field_dict["canBulkEditMetadata"] = can_bulk_edit_metadata
        if can_bulk_regenerate_cover is not UNSET:
            field_dict["canBulkRegenerateCover"] = can_bulk_regenerate_cover
        if can_move_organize_files is not UNSET:
            field_dict["canMoveOrganizeFiles"] = can_move_organize_files
        if can_bulk_lock_unlock_metadata is not UNSET:
            field_dict["canBulkLockUnlockMetadata"] = can_bulk_lock_unlock_metadata
        if can_bulk_reset_booklore_read_progress is not UNSET:
            field_dict["canBulkResetBookloreReadProgress"] = can_bulk_reset_booklore_read_progress
        if can_bulk_reset_ko_reader_read_progress is not UNSET:
            field_dict["canBulkResetKoReaderReadProgress"] = can_bulk_reset_ko_reader_read_progress
        if can_bulk_reset_book_read_status is not UNSET:
            field_dict["canBulkResetBookReadStatus"] = can_bulk_reset_book_read_status
        if admin is not UNSET:
            field_dict["admin"] = admin

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        can_upload = d.pop("canUpload", UNSET)

        can_download = d.pop("canDownload", UNSET)

        can_edit_metadata = d.pop("canEditMetadata", UNSET)

        can_manage_library = d.pop("canManageLibrary", UNSET)

        can_email_book = d.pop("canEmailBook", UNSET)

        can_delete_book = d.pop("canDeleteBook", UNSET)

        can_access_opds = d.pop("canAccessOpds", UNSET)

        can_sync_ko_reader = d.pop("canSyncKoReader", UNSET)

        can_sync_kobo = d.pop("canSyncKobo", UNSET)

        can_manage_metadata_config = d.pop("canManageMetadataConfig", UNSET)

        can_access_bookdrop = d.pop("canAccessBookdrop", UNSET)

        can_access_library_stats = d.pop("canAccessLibraryStats", UNSET)

        can_access_user_stats = d.pop("canAccessUserStats", UNSET)

        can_access_task_manager = d.pop("canAccessTaskManager", UNSET)

        can_manage_global_preferences = d.pop("canManageGlobalPreferences", UNSET)

        can_manage_icons = d.pop("canManageIcons", UNSET)

        can_manage_fonts = d.pop("canManageFonts", UNSET)

        can_bulk_auto_fetch_metadata = d.pop("canBulkAutoFetchMetadata", UNSET)

        can_bulk_custom_fetch_metadata = d.pop("canBulkCustomFetchMetadata", UNSET)

        can_bulk_edit_metadata = d.pop("canBulkEditMetadata", UNSET)

        can_bulk_regenerate_cover = d.pop("canBulkRegenerateCover", UNSET)

        can_move_organize_files = d.pop("canMoveOrganizeFiles", UNSET)

        can_bulk_lock_unlock_metadata = d.pop("canBulkLockUnlockMetadata", UNSET)

        can_bulk_reset_booklore_read_progress = d.pop("canBulkResetBookloreReadProgress", UNSET)

        can_bulk_reset_ko_reader_read_progress = d.pop("canBulkResetKoReaderReadProgress", UNSET)

        can_bulk_reset_book_read_status = d.pop("canBulkResetBookReadStatus", UNSET)

        admin = d.pop("admin", UNSET)

        permissions = cls(
            can_upload=can_upload,
            can_download=can_download,
            can_edit_metadata=can_edit_metadata,
            can_manage_library=can_manage_library,
            can_email_book=can_email_book,
            can_delete_book=can_delete_book,
            can_access_opds=can_access_opds,
            can_sync_ko_reader=can_sync_ko_reader,
            can_sync_kobo=can_sync_kobo,
            can_manage_metadata_config=can_manage_metadata_config,
            can_access_bookdrop=can_access_bookdrop,
            can_access_library_stats=can_access_library_stats,
            can_access_user_stats=can_access_user_stats,
            can_access_task_manager=can_access_task_manager,
            can_manage_global_preferences=can_manage_global_preferences,
            can_manage_icons=can_manage_icons,
            can_manage_fonts=can_manage_fonts,
            can_bulk_auto_fetch_metadata=can_bulk_auto_fetch_metadata,
            can_bulk_custom_fetch_metadata=can_bulk_custom_fetch_metadata,
            can_bulk_edit_metadata=can_bulk_edit_metadata,
            can_bulk_regenerate_cover=can_bulk_regenerate_cover,
            can_move_organize_files=can_move_organize_files,
            can_bulk_lock_unlock_metadata=can_bulk_lock_unlock_metadata,
            can_bulk_reset_booklore_read_progress=can_bulk_reset_booklore_read_progress,
            can_bulk_reset_ko_reader_read_progress=can_bulk_reset_ko_reader_read_progress,
            can_bulk_reset_book_read_status=can_bulk_reset_book_read_status,
            admin=admin,
        )

        permissions.additional_properties = d
        return permissions

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
