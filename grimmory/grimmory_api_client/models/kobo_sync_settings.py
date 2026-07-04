from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="KoboSyncSettings")


@_attrs_define
class KoboSyncSettings:
    """
    Attributes:
        id (int | Unset):
        user_id (str | Unset):
        token (str | Unset):
        sync_enabled (bool | Unset):
        progress_mark_as_reading_threshold (float | Unset):
        progress_mark_as_finished_threshold (float | Unset):
        auto_add_to_shelf (bool | Unset):
        hardcover_api_key (str | Unset):
        hardcover_sync_enabled (bool | Unset):
        two_way_progress_sync (bool | Unset):
    """

    id: int | Unset = UNSET
    user_id: str | Unset = UNSET
    token: str | Unset = UNSET
    sync_enabled: bool | Unset = UNSET
    progress_mark_as_reading_threshold: float | Unset = UNSET
    progress_mark_as_finished_threshold: float | Unset = UNSET
    auto_add_to_shelf: bool | Unset = UNSET
    hardcover_api_key: str | Unset = UNSET
    hardcover_sync_enabled: bool | Unset = UNSET
    two_way_progress_sync: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        user_id = self.user_id

        token = self.token

        sync_enabled = self.sync_enabled

        progress_mark_as_reading_threshold = self.progress_mark_as_reading_threshold

        progress_mark_as_finished_threshold = self.progress_mark_as_finished_threshold

        auto_add_to_shelf = self.auto_add_to_shelf

        hardcover_api_key = self.hardcover_api_key

        hardcover_sync_enabled = self.hardcover_sync_enabled

        two_way_progress_sync = self.two_way_progress_sync

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if user_id is not UNSET:
            field_dict["userId"] = user_id
        if token is not UNSET:
            field_dict["token"] = token
        if sync_enabled is not UNSET:
            field_dict["syncEnabled"] = sync_enabled
        if progress_mark_as_reading_threshold is not UNSET:
            field_dict["progressMarkAsReadingThreshold"] = progress_mark_as_reading_threshold
        if progress_mark_as_finished_threshold is not UNSET:
            field_dict["progressMarkAsFinishedThreshold"] = progress_mark_as_finished_threshold
        if auto_add_to_shelf is not UNSET:
            field_dict["autoAddToShelf"] = auto_add_to_shelf
        if hardcover_api_key is not UNSET:
            field_dict["hardcoverApiKey"] = hardcover_api_key
        if hardcover_sync_enabled is not UNSET:
            field_dict["hardcoverSyncEnabled"] = hardcover_sync_enabled
        if two_way_progress_sync is not UNSET:
            field_dict["twoWayProgressSync"] = two_way_progress_sync

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        user_id = d.pop("userId", UNSET)

        token = d.pop("token", UNSET)

        sync_enabled = d.pop("syncEnabled", UNSET)

        progress_mark_as_reading_threshold = d.pop("progressMarkAsReadingThreshold", UNSET)

        progress_mark_as_finished_threshold = d.pop("progressMarkAsFinishedThreshold", UNSET)

        auto_add_to_shelf = d.pop("autoAddToShelf", UNSET)

        hardcover_api_key = d.pop("hardcoverApiKey", UNSET)

        hardcover_sync_enabled = d.pop("hardcoverSyncEnabled", UNSET)

        two_way_progress_sync = d.pop("twoWayProgressSync", UNSET)

        kobo_sync_settings = cls(
            id=id,
            user_id=user_id,
            token=token,
            sync_enabled=sync_enabled,
            progress_mark_as_reading_threshold=progress_mark_as_reading_threshold,
            progress_mark_as_finished_threshold=progress_mark_as_finished_threshold,
            auto_add_to_shelf=auto_add_to_shelf,
            hardcover_api_key=hardcover_api_key,
            hardcover_sync_enabled=hardcover_sync_enabled,
            two_way_progress_sync=two_way_progress_sync,
        )

        kobo_sync_settings.additional_properties = d
        return kobo_sync_settings

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
