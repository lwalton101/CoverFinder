from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.audiobook_progress import AudiobookProgress
    from ..models.cbx_progress import CbxProgress
    from ..models.epub_progress import EpubProgress
    from ..models.koreader_progress import KoreaderProgress
    from ..models.pdf_progress import PdfProgress


T = TypeVar("T", bound="AppBookProgressResponse")


@_attrs_define
class AppBookProgressResponse:
    """
    Attributes:
        read_progress (float | Unset):
        read_status (str | Unset):
        last_read_time (datetime.datetime | Unset):
        epub_progress (EpubProgress | Unset):
        pdf_progress (PdfProgress | Unset):
        cbx_progress (CbxProgress | Unset):
        audiobook_progress (AudiobookProgress | Unset):
        koreader_progress (KoreaderProgress | Unset): KoReader progress object
    """

    read_progress: float | Unset = UNSET
    read_status: str | Unset = UNSET
    last_read_time: datetime.datetime | Unset = UNSET
    epub_progress: EpubProgress | Unset = UNSET
    pdf_progress: PdfProgress | Unset = UNSET
    cbx_progress: CbxProgress | Unset = UNSET
    audiobook_progress: AudiobookProgress | Unset = UNSET
    koreader_progress: KoreaderProgress | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        read_progress = self.read_progress

        read_status = self.read_status

        last_read_time: str | Unset = UNSET
        if not isinstance(self.last_read_time, Unset):
            last_read_time = self.last_read_time.isoformat()

        epub_progress: dict[str, Any] | Unset = UNSET
        if not isinstance(self.epub_progress, Unset):
            epub_progress = self.epub_progress.to_dict()

        pdf_progress: dict[str, Any] | Unset = UNSET
        if not isinstance(self.pdf_progress, Unset):
            pdf_progress = self.pdf_progress.to_dict()

        cbx_progress: dict[str, Any] | Unset = UNSET
        if not isinstance(self.cbx_progress, Unset):
            cbx_progress = self.cbx_progress.to_dict()

        audiobook_progress: dict[str, Any] | Unset = UNSET
        if not isinstance(self.audiobook_progress, Unset):
            audiobook_progress = self.audiobook_progress.to_dict()

        koreader_progress: dict[str, Any] | Unset = UNSET
        if not isinstance(self.koreader_progress, Unset):
            koreader_progress = self.koreader_progress.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if read_progress is not UNSET:
            field_dict["readProgress"] = read_progress
        if read_status is not UNSET:
            field_dict["readStatus"] = read_status
        if last_read_time is not UNSET:
            field_dict["lastReadTime"] = last_read_time
        if epub_progress is not UNSET:
            field_dict["epubProgress"] = epub_progress
        if pdf_progress is not UNSET:
            field_dict["pdfProgress"] = pdf_progress
        if cbx_progress is not UNSET:
            field_dict["cbxProgress"] = cbx_progress
        if audiobook_progress is not UNSET:
            field_dict["audiobookProgress"] = audiobook_progress
        if koreader_progress is not UNSET:
            field_dict["koreaderProgress"] = koreader_progress

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.audiobook_progress import AudiobookProgress
        from ..models.cbx_progress import CbxProgress
        from ..models.epub_progress import EpubProgress
        from ..models.koreader_progress import KoreaderProgress
        from ..models.pdf_progress import PdfProgress

        d = dict(src_dict)
        read_progress = d.pop("readProgress", UNSET)

        read_status = d.pop("readStatus", UNSET)

        _last_read_time = d.pop("lastReadTime", UNSET)
        last_read_time: datetime.datetime | Unset
        if isinstance(_last_read_time, Unset):
            last_read_time = UNSET
        else:
            last_read_time = datetime.datetime.fromisoformat(_last_read_time)

        _epub_progress = d.pop("epubProgress", UNSET)
        epub_progress: EpubProgress | Unset
        if isinstance(_epub_progress, Unset):
            epub_progress = UNSET
        else:
            epub_progress = EpubProgress.from_dict(_epub_progress)

        _pdf_progress = d.pop("pdfProgress", UNSET)
        pdf_progress: PdfProgress | Unset
        if isinstance(_pdf_progress, Unset):
            pdf_progress = UNSET
        else:
            pdf_progress = PdfProgress.from_dict(_pdf_progress)

        _cbx_progress = d.pop("cbxProgress", UNSET)
        cbx_progress: CbxProgress | Unset
        if isinstance(_cbx_progress, Unset):
            cbx_progress = UNSET
        else:
            cbx_progress = CbxProgress.from_dict(_cbx_progress)

        _audiobook_progress = d.pop("audiobookProgress", UNSET)
        audiobook_progress: AudiobookProgress | Unset
        if isinstance(_audiobook_progress, Unset):
            audiobook_progress = UNSET
        else:
            audiobook_progress = AudiobookProgress.from_dict(_audiobook_progress)

        _koreader_progress = d.pop("koreaderProgress", UNSET)
        koreader_progress: KoreaderProgress | Unset
        if isinstance(_koreader_progress, Unset):
            koreader_progress = UNSET
        else:
            koreader_progress = KoreaderProgress.from_dict(_koreader_progress)

        app_book_progress_response = cls(
            read_progress=read_progress,
            read_status=read_status,
            last_read_time=last_read_time,
            epub_progress=epub_progress,
            pdf_progress=pdf_progress,
            cbx_progress=cbx_progress,
            audiobook_progress=audiobook_progress,
            koreader_progress=koreader_progress,
        )

        app_book_progress_response.additional_properties = d
        return app_book_progress_response

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
