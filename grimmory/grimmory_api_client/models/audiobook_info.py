from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.audiobook_chapter import AudiobookChapter
    from ..models.audiobook_track import AudiobookTrack


T = TypeVar("T", bound="AudiobookInfo")


@_attrs_define
class AudiobookInfo:
    """
    Attributes:
        book_id (int | Unset):
        book_file_id (int | Unset):
        title (str | Unset):
        author (str | Unset):
        narrator (str | Unset):
        duration_ms (int | Unset):
        bitrate (int | Unset):
        codec (str | Unset):
        sample_rate (int | Unset):
        channels (int | Unset):
        total_size_bytes (int | Unset):
        folder_based (bool | Unset):
        chapters (list[AudiobookChapter] | Unset):
        tracks (list[AudiobookTrack] | Unset):
    """

    book_id: int | Unset = UNSET
    book_file_id: int | Unset = UNSET
    title: str | Unset = UNSET
    author: str | Unset = UNSET
    narrator: str | Unset = UNSET
    duration_ms: int | Unset = UNSET
    bitrate: int | Unset = UNSET
    codec: str | Unset = UNSET
    sample_rate: int | Unset = UNSET
    channels: int | Unset = UNSET
    total_size_bytes: int | Unset = UNSET
    folder_based: bool | Unset = UNSET
    chapters: list[AudiobookChapter] | Unset = UNSET
    tracks: list[AudiobookTrack] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        book_id = self.book_id

        book_file_id = self.book_file_id

        title = self.title

        author = self.author

        narrator = self.narrator

        duration_ms = self.duration_ms

        bitrate = self.bitrate

        codec = self.codec

        sample_rate = self.sample_rate

        channels = self.channels

        total_size_bytes = self.total_size_bytes

        folder_based = self.folder_based

        chapters: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.chapters, Unset):
            chapters = []
            for chapters_item_data in self.chapters:
                chapters_item = chapters_item_data.to_dict()
                chapters.append(chapters_item)

        tracks: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.tracks, Unset):
            tracks = []
            for tracks_item_data in self.tracks:
                tracks_item = tracks_item_data.to_dict()
                tracks.append(tracks_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if book_id is not UNSET:
            field_dict["bookId"] = book_id
        if book_file_id is not UNSET:
            field_dict["bookFileId"] = book_file_id
        if title is not UNSET:
            field_dict["title"] = title
        if author is not UNSET:
            field_dict["author"] = author
        if narrator is not UNSET:
            field_dict["narrator"] = narrator
        if duration_ms is not UNSET:
            field_dict["durationMs"] = duration_ms
        if bitrate is not UNSET:
            field_dict["bitrate"] = bitrate
        if codec is not UNSET:
            field_dict["codec"] = codec
        if sample_rate is not UNSET:
            field_dict["sampleRate"] = sample_rate
        if channels is not UNSET:
            field_dict["channels"] = channels
        if total_size_bytes is not UNSET:
            field_dict["totalSizeBytes"] = total_size_bytes
        if folder_based is not UNSET:
            field_dict["folderBased"] = folder_based
        if chapters is not UNSET:
            field_dict["chapters"] = chapters
        if tracks is not UNSET:
            field_dict["tracks"] = tracks

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.audiobook_chapter import AudiobookChapter
        from ..models.audiobook_track import AudiobookTrack

        d = dict(src_dict)
        book_id = d.pop("bookId", UNSET)

        book_file_id = d.pop("bookFileId", UNSET)

        title = d.pop("title", UNSET)

        author = d.pop("author", UNSET)

        narrator = d.pop("narrator", UNSET)

        duration_ms = d.pop("durationMs", UNSET)

        bitrate = d.pop("bitrate", UNSET)

        codec = d.pop("codec", UNSET)

        sample_rate = d.pop("sampleRate", UNSET)

        channels = d.pop("channels", UNSET)

        total_size_bytes = d.pop("totalSizeBytes", UNSET)

        folder_based = d.pop("folderBased", UNSET)

        _chapters = d.pop("chapters", UNSET)
        chapters: list[AudiobookChapter] | Unset = UNSET
        if _chapters is not UNSET:
            chapters = []
            for chapters_item_data in _chapters:
                chapters_item = AudiobookChapter.from_dict(chapters_item_data)

                chapters.append(chapters_item)

        _tracks = d.pop("tracks", UNSET)
        tracks: list[AudiobookTrack] | Unset = UNSET
        if _tracks is not UNSET:
            tracks = []
            for tracks_item_data in _tracks:
                tracks_item = AudiobookTrack.from_dict(tracks_item_data)

                tracks.append(tracks_item)

        audiobook_info = cls(
            book_id=book_id,
            book_file_id=book_file_id,
            title=title,
            author=author,
            narrator=narrator,
            duration_ms=duration_ms,
            bitrate=bitrate,
            codec=codec,
            sample_rate=sample_rate,
            channels=channels,
            total_size_bytes=total_size_bytes,
            folder_based=folder_based,
            chapters=chapters,
            tracks=tracks,
        )

        audiobook_info.additional_properties = d
        return audiobook_info

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
