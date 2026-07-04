from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.chapter_info import ChapterInfo


T = TypeVar("T", bound="AudiobookMetadata")


@_attrs_define
class AudiobookMetadata:
    """
    Attributes:
        duration_seconds (int | Unset):
        bitrate (int | Unset):
        sample_rate (int | Unset):
        channels (int | Unset):
        codec (str | Unset):
        chapter_count (int | Unset):
        chapters (list[ChapterInfo] | Unset):
    """

    duration_seconds: int | Unset = UNSET
    bitrate: int | Unset = UNSET
    sample_rate: int | Unset = UNSET
    channels: int | Unset = UNSET
    codec: str | Unset = UNSET
    chapter_count: int | Unset = UNSET
    chapters: list[ChapterInfo] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        duration_seconds = self.duration_seconds

        bitrate = self.bitrate

        sample_rate = self.sample_rate

        channels = self.channels

        codec = self.codec

        chapter_count = self.chapter_count

        chapters: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.chapters, Unset):
            chapters = []
            for chapters_item_data in self.chapters:
                chapters_item = chapters_item_data.to_dict()
                chapters.append(chapters_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if duration_seconds is not UNSET:
            field_dict["durationSeconds"] = duration_seconds
        if bitrate is not UNSET:
            field_dict["bitrate"] = bitrate
        if sample_rate is not UNSET:
            field_dict["sampleRate"] = sample_rate
        if channels is not UNSET:
            field_dict["channels"] = channels
        if codec is not UNSET:
            field_dict["codec"] = codec
        if chapter_count is not UNSET:
            field_dict["chapterCount"] = chapter_count
        if chapters is not UNSET:
            field_dict["chapters"] = chapters

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.chapter_info import ChapterInfo

        d = dict(src_dict)
        duration_seconds = d.pop("durationSeconds", UNSET)

        bitrate = d.pop("bitrate", UNSET)

        sample_rate = d.pop("sampleRate", UNSET)

        channels = d.pop("channels", UNSET)

        codec = d.pop("codec", UNSET)

        chapter_count = d.pop("chapterCount", UNSET)

        _chapters = d.pop("chapters", UNSET)
        chapters: list[ChapterInfo] | Unset = UNSET
        if _chapters is not UNSET:
            chapters = []
            for chapters_item_data in _chapters:
                chapters_item = ChapterInfo.from_dict(chapters_item_data)

                chapters.append(chapters_item)

        audiobook_metadata = cls(
            duration_seconds=duration_seconds,
            bitrate=bitrate,
            sample_rate=sample_rate,
            channels=channels,
            codec=codec,
            chapter_count=chapter_count,
            chapters=chapters,
        )

        audiobook_metadata.additional_properties = d
        return audiobook_metadata

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
