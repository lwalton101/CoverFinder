from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.save_to_original_file import SaveToOriginalFile
    from ..models.sidecar_settings import SidecarSettings


T = TypeVar("T", bound="MetadataPersistenceSettings")


@_attrs_define
class MetadataPersistenceSettings:
    """
    Attributes:
        save_to_original_file (SaveToOriginalFile | Unset):
        convert_cbr_cb_7_to_cbz (bool | Unset):
        move_files_to_library_pattern (bool | Unset):
        sidecar_settings (SidecarSettings | Unset):
    """

    save_to_original_file: SaveToOriginalFile | Unset = UNSET
    convert_cbr_cb_7_to_cbz: bool | Unset = UNSET
    move_files_to_library_pattern: bool | Unset = UNSET
    sidecar_settings: SidecarSettings | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        save_to_original_file: dict[str, Any] | Unset = UNSET
        if not isinstance(self.save_to_original_file, Unset):
            save_to_original_file = self.save_to_original_file.to_dict()

        convert_cbr_cb_7_to_cbz = self.convert_cbr_cb_7_to_cbz

        move_files_to_library_pattern = self.move_files_to_library_pattern

        sidecar_settings: dict[str, Any] | Unset = UNSET
        if not isinstance(self.sidecar_settings, Unset):
            sidecar_settings = self.sidecar_settings.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if save_to_original_file is not UNSET:
            field_dict["saveToOriginalFile"] = save_to_original_file
        if convert_cbr_cb_7_to_cbz is not UNSET:
            field_dict["convertCbrCb7ToCbz"] = convert_cbr_cb_7_to_cbz
        if move_files_to_library_pattern is not UNSET:
            field_dict["moveFilesToLibraryPattern"] = move_files_to_library_pattern
        if sidecar_settings is not UNSET:
            field_dict["sidecarSettings"] = sidecar_settings

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.save_to_original_file import SaveToOriginalFile
        from ..models.sidecar_settings import SidecarSettings

        d = dict(src_dict)
        _save_to_original_file = d.pop("saveToOriginalFile", UNSET)
        save_to_original_file: SaveToOriginalFile | Unset
        if isinstance(_save_to_original_file, Unset):
            save_to_original_file = UNSET
        else:
            save_to_original_file = SaveToOriginalFile.from_dict(_save_to_original_file)

        convert_cbr_cb_7_to_cbz = d.pop("convertCbrCb7ToCbz", UNSET)

        move_files_to_library_pattern = d.pop("moveFilesToLibraryPattern", UNSET)

        _sidecar_settings = d.pop("sidecarSettings", UNSET)
        sidecar_settings: SidecarSettings | Unset
        if isinstance(_sidecar_settings, Unset):
            sidecar_settings = UNSET
        else:
            sidecar_settings = SidecarSettings.from_dict(_sidecar_settings)

        metadata_persistence_settings = cls(
            save_to_original_file=save_to_original_file,
            convert_cbr_cb_7_to_cbz=convert_cbr_cb_7_to_cbz,
            move_files_to_library_pattern=move_files_to_library_pattern,
            sidecar_settings=sidecar_settings,
        )

        metadata_persistence_settings.additional_properties = d
        return metadata_persistence_settings

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
