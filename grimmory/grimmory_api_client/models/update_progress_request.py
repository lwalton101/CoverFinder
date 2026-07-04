from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.audiobook_progress import AudiobookProgress
    from ..models.book_file_progress import BookFileProgress
    from ..models.cbx_progress import CbxProgress
    from ..models.epub_progress import EpubProgress
    from ..models.pdf_progress import PdfProgress


T = TypeVar("T", bound="UpdateProgressRequest")


@_attrs_define
class UpdateProgressRequest:
    """
    Attributes:
        file_progress (BookFileProgress | Unset):
        epub_progress (EpubProgress | Unset):
        pdf_progress (PdfProgress | Unset):
        cbx_progress (CbxProgress | Unset):
        audiobook_progress (AudiobookProgress | Unset):
        date_finished (datetime.datetime | Unset):
        progress_valid (bool | Unset):
    """

    file_progress: BookFileProgress | Unset = UNSET
    epub_progress: EpubProgress | Unset = UNSET
    pdf_progress: PdfProgress | Unset = UNSET
    cbx_progress: CbxProgress | Unset = UNSET
    audiobook_progress: AudiobookProgress | Unset = UNSET
    date_finished: datetime.datetime | Unset = UNSET
    progress_valid: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        file_progress: dict[str, Any] | Unset = UNSET
        if not isinstance(self.file_progress, Unset):
            file_progress = self.file_progress.to_dict()

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

        date_finished: str | Unset = UNSET
        if not isinstance(self.date_finished, Unset):
            date_finished = self.date_finished.isoformat()

        progress_valid = self.progress_valid

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if file_progress is not UNSET:
            field_dict["fileProgress"] = file_progress
        if epub_progress is not UNSET:
            field_dict["epubProgress"] = epub_progress
        if pdf_progress is not UNSET:
            field_dict["pdfProgress"] = pdf_progress
        if cbx_progress is not UNSET:
            field_dict["cbxProgress"] = cbx_progress
        if audiobook_progress is not UNSET:
            field_dict["audiobookProgress"] = audiobook_progress
        if date_finished is not UNSET:
            field_dict["dateFinished"] = date_finished
        if progress_valid is not UNSET:
            field_dict["progressValid"] = progress_valid

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.audiobook_progress import AudiobookProgress
        from ..models.book_file_progress import BookFileProgress
        from ..models.cbx_progress import CbxProgress
        from ..models.epub_progress import EpubProgress
        from ..models.pdf_progress import PdfProgress

        d = dict(src_dict)
        _file_progress = d.pop("fileProgress", UNSET)
        file_progress: BookFileProgress | Unset
        if isinstance(_file_progress, Unset):
            file_progress = UNSET
        else:
            file_progress = BookFileProgress.from_dict(_file_progress)

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

        _date_finished = d.pop("dateFinished", UNSET)
        date_finished: datetime.datetime | Unset
        if isinstance(_date_finished, Unset):
            date_finished = UNSET
        else:
            date_finished = datetime.datetime.fromisoformat(_date_finished)

        progress_valid = d.pop("progressValid", UNSET)

        update_progress_request = cls(
            file_progress=file_progress,
            epub_progress=epub_progress,
            pdf_progress=pdf_progress,
            cbx_progress=cbx_progress,
            audiobook_progress=audiobook_progress,
            date_finished=date_finished,
            progress_valid=progress_valid,
        )

        update_progress_request.additional_properties = d
        return update_progress_request

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
