from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="KoboSettings")


@_attrs_define
class KoboSettings:
    """
    Attributes:
        convert_to_kepub (bool | Unset):
        conversion_limit_in_mb (int | Unset):
        convert_cbx_to_epub (bool | Unset):
        conversion_limit_in_mb_for_cbx (int | Unset):
        force_enable_hyphenation (bool | Unset):
        conversion_image_compression_percentage (int | Unset):
        forward_to_kobo_store (bool | Unset):
    """

    convert_to_kepub: bool | Unset = UNSET
    conversion_limit_in_mb: int | Unset = UNSET
    convert_cbx_to_epub: bool | Unset = UNSET
    conversion_limit_in_mb_for_cbx: int | Unset = UNSET
    force_enable_hyphenation: bool | Unset = UNSET
    conversion_image_compression_percentage: int | Unset = UNSET
    forward_to_kobo_store: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        convert_to_kepub = self.convert_to_kepub

        conversion_limit_in_mb = self.conversion_limit_in_mb

        convert_cbx_to_epub = self.convert_cbx_to_epub

        conversion_limit_in_mb_for_cbx = self.conversion_limit_in_mb_for_cbx

        force_enable_hyphenation = self.force_enable_hyphenation

        conversion_image_compression_percentage = self.conversion_image_compression_percentage

        forward_to_kobo_store = self.forward_to_kobo_store

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if convert_to_kepub is not UNSET:
            field_dict["convertToKepub"] = convert_to_kepub
        if conversion_limit_in_mb is not UNSET:
            field_dict["conversionLimitInMb"] = conversion_limit_in_mb
        if convert_cbx_to_epub is not UNSET:
            field_dict["convertCbxToEpub"] = convert_cbx_to_epub
        if conversion_limit_in_mb_for_cbx is not UNSET:
            field_dict["conversionLimitInMbForCbx"] = conversion_limit_in_mb_for_cbx
        if force_enable_hyphenation is not UNSET:
            field_dict["forceEnableHyphenation"] = force_enable_hyphenation
        if conversion_image_compression_percentage is not UNSET:
            field_dict["conversionImageCompressionPercentage"] = conversion_image_compression_percentage
        if forward_to_kobo_store is not UNSET:
            field_dict["forwardToKoboStore"] = forward_to_kobo_store

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        convert_to_kepub = d.pop("convertToKepub", UNSET)

        conversion_limit_in_mb = d.pop("conversionLimitInMb", UNSET)

        convert_cbx_to_epub = d.pop("convertCbxToEpub", UNSET)

        conversion_limit_in_mb_for_cbx = d.pop("conversionLimitInMbForCbx", UNSET)

        force_enable_hyphenation = d.pop("forceEnableHyphenation", UNSET)

        conversion_image_compression_percentage = d.pop("conversionImageCompressionPercentage", UNSET)

        forward_to_kobo_store = d.pop("forwardToKoboStore", UNSET)

        kobo_settings = cls(
            convert_to_kepub=convert_to_kepub,
            conversion_limit_in_mb=conversion_limit_in_mb,
            convert_cbx_to_epub=convert_cbx_to_epub,
            conversion_limit_in_mb_for_cbx=conversion_limit_in_mb_for_cbx,
            force_enable_hyphenation=force_enable_hyphenation,
            conversion_image_compression_percentage=conversion_image_compression_percentage,
            forward_to_kobo_store=forward_to_kobo_store,
        )

        kobo_settings.additional_properties = d
        return kobo_settings

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
