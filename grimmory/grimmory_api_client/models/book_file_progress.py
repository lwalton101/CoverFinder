from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BookFileProgress")


@_attrs_define
class BookFileProgress:
    """
    Attributes:
        book_file_id (int):
        progress_percent (float):
        position_data (str | Unset):
        position_href (str | Unset):
        tts_position_cfi (str | Unset):
        content_source_progress_percent (float | Unset):
    """

    book_file_id: int
    progress_percent: float
    position_data: str | Unset = UNSET
    position_href: str | Unset = UNSET
    tts_position_cfi: str | Unset = UNSET
    content_source_progress_percent: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        book_file_id = self.book_file_id

        progress_percent = self.progress_percent

        position_data = self.position_data

        position_href = self.position_href

        tts_position_cfi = self.tts_position_cfi

        content_source_progress_percent = self.content_source_progress_percent

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "bookFileId": book_file_id,
                "progressPercent": progress_percent,
            }
        )
        if position_data is not UNSET:
            field_dict["positionData"] = position_data
        if position_href is not UNSET:
            field_dict["positionHref"] = position_href
        if tts_position_cfi is not UNSET:
            field_dict["ttsPositionCfi"] = tts_position_cfi
        if content_source_progress_percent is not UNSET:
            field_dict["contentSourceProgressPercent"] = content_source_progress_percent

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        book_file_id = d.pop("bookFileId")

        progress_percent = d.pop("progressPercent")

        position_data = d.pop("positionData", UNSET)

        position_href = d.pop("positionHref", UNSET)

        tts_position_cfi = d.pop("ttsPositionCfi", UNSET)

        content_source_progress_percent = d.pop("contentSourceProgressPercent", UNSET)

        book_file_progress = cls(
            book_file_id=book_file_id,
            progress_percent=progress_percent,
            position_data=position_data,
            position_href=position_href,
            tts_position_cfi=tts_position_cfi,
            content_source_progress_percent=content_source_progress_percent,
        )

        book_file_progress.additional_properties = d
        return book_file_progress

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
