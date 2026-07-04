from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="EpubProgress")


@_attrs_define
class EpubProgress:
    """
    Attributes:
        percentage (float):
        cfi (str | Unset):
        href (str | Unset):
        content_source_progress_percent (float | Unset):
        tts_position_cfi (str | Unset):
    """

    percentage: float
    cfi: str | Unset = UNSET
    href: str | Unset = UNSET
    content_source_progress_percent: float | Unset = UNSET
    tts_position_cfi: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        percentage = self.percentage

        cfi = self.cfi

        href = self.href

        content_source_progress_percent = self.content_source_progress_percent

        tts_position_cfi = self.tts_position_cfi

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "percentage": percentage,
            }
        )
        if cfi is not UNSET:
            field_dict["cfi"] = cfi
        if href is not UNSET:
            field_dict["href"] = href
        if content_source_progress_percent is not UNSET:
            field_dict["contentSourceProgressPercent"] = content_source_progress_percent
        if tts_position_cfi is not UNSET:
            field_dict["ttsPositionCfi"] = tts_position_cfi

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        percentage = d.pop("percentage")

        cfi = d.pop("cfi", UNSET)

        href = d.pop("href", UNSET)

        content_source_progress_percent = d.pop("contentSourceProgressPercent", UNSET)

        tts_position_cfi = d.pop("ttsPositionCfi", UNSET)

        epub_progress = cls(
            percentage=percentage,
            cfi=cfi,
            href=href,
            content_source_progress_percent=content_source_progress_percent,
            tts_position_cfi=tts_position_cfi,
        )

        epub_progress.additional_properties = d
        return epub_progress

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
