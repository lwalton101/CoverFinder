from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.audiobook_progress import AudiobookProgress
    from ..models.book_file import BookFile
    from ..models.book_metadata import BookMetadata
    from ..models.cbx_progress import CbxProgress
    from ..models.epub_progress import EpubProgress
    from ..models.ko_progress import KoProgress
    from ..models.kobo_progress import KoboProgress
    from ..models.library_path import LibraryPath
    from ..models.pdf_progress import PdfProgress
    from ..models.shelf import Shelf


T = TypeVar("T", bound="Book")


@_attrs_define
class Book:
    """
    Attributes:
        id (int | Unset):
        library_id (int | Unset):
        library_name (str | Unset):
        primary_file (BookFile | Unset):
        title (str | Unset):
        last_read_time (datetime.datetime | Unset):
        added_on (datetime.datetime | Unset):
        metadata (BookMetadata | Unset):
        metadata_match_score (float | Unset):
        pdf_progress (PdfProgress | Unset):
        epub_progress (EpubProgress | Unset):
        cbx_progress (CbxProgress | Unset):
        audiobook_progress (AudiobookProgress | Unset):
        koreader_progress (KoProgress | Unset):
        kobo_progress (KoboProgress | Unset):
        personal_rating (int | Unset):
        shelves (list[Shelf] | Unset):
        read_status (str | Unset):
        date_finished (datetime.datetime | Unset):
        library_path (LibraryPath | Unset):
        alternative_formats (list[BookFile] | Unset):
        supplementary_files (list[BookFile] | Unset):
        is_physical (bool | Unset):
    """

    id: int | Unset = UNSET
    library_id: int | Unset = UNSET
    library_name: str | Unset = UNSET
    primary_file: BookFile | Unset = UNSET
    title: str | Unset = UNSET
    last_read_time: datetime.datetime | Unset = UNSET
    added_on: datetime.datetime | Unset = UNSET
    metadata: BookMetadata | Unset = UNSET
    metadata_match_score: float | Unset = UNSET
    pdf_progress: PdfProgress | Unset = UNSET
    epub_progress: EpubProgress | Unset = UNSET
    cbx_progress: CbxProgress | Unset = UNSET
    audiobook_progress: AudiobookProgress | Unset = UNSET
    koreader_progress: KoProgress | Unset = UNSET
    kobo_progress: KoboProgress | Unset = UNSET
    personal_rating: int | Unset = UNSET
    shelves: list[Shelf] | Unset = UNSET
    read_status: str | Unset = UNSET
    date_finished: datetime.datetime | Unset = UNSET
    library_path: LibraryPath | Unset = UNSET
    alternative_formats: list[BookFile] | Unset = UNSET
    supplementary_files: list[BookFile] | Unset = UNSET
    is_physical: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        library_id = self.library_id

        library_name = self.library_name

        primary_file: dict[str, Any] | Unset = UNSET
        if not isinstance(self.primary_file, Unset):
            primary_file = self.primary_file.to_dict()

        title = self.title

        last_read_time: str | Unset = UNSET
        if not isinstance(self.last_read_time, Unset):
            last_read_time = self.last_read_time.isoformat()

        added_on: str | Unset = UNSET
        if not isinstance(self.added_on, Unset):
            added_on = self.added_on.isoformat()

        metadata: dict[str, Any] | Unset = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        metadata_match_score = self.metadata_match_score

        pdf_progress: dict[str, Any] | Unset = UNSET
        if not isinstance(self.pdf_progress, Unset):
            pdf_progress = self.pdf_progress.to_dict()

        epub_progress: dict[str, Any] | Unset = UNSET
        if not isinstance(self.epub_progress, Unset):
            epub_progress = self.epub_progress.to_dict()

        cbx_progress: dict[str, Any] | Unset = UNSET
        if not isinstance(self.cbx_progress, Unset):
            cbx_progress = self.cbx_progress.to_dict()

        audiobook_progress: dict[str, Any] | Unset = UNSET
        if not isinstance(self.audiobook_progress, Unset):
            audiobook_progress = self.audiobook_progress.to_dict()

        koreader_progress: dict[str, Any] | Unset = UNSET
        if not isinstance(self.koreader_progress, Unset):
            koreader_progress = self.koreader_progress.to_dict()

        kobo_progress: dict[str, Any] | Unset = UNSET
        if not isinstance(self.kobo_progress, Unset):
            kobo_progress = self.kobo_progress.to_dict()

        personal_rating = self.personal_rating

        shelves: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.shelves, Unset):
            shelves = []
            for shelves_item_data in self.shelves:
                shelves_item = shelves_item_data.to_dict()
                shelves.append(shelves_item)

        read_status = self.read_status

        date_finished: str | Unset = UNSET
        if not isinstance(self.date_finished, Unset):
            date_finished = self.date_finished.isoformat()

        library_path: dict[str, Any] | Unset = UNSET
        if not isinstance(self.library_path, Unset):
            library_path = self.library_path.to_dict()

        alternative_formats: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.alternative_formats, Unset):
            alternative_formats = []
            for alternative_formats_item_data in self.alternative_formats:
                alternative_formats_item = alternative_formats_item_data.to_dict()
                alternative_formats.append(alternative_formats_item)

        supplementary_files: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.supplementary_files, Unset):
            supplementary_files = []
            for supplementary_files_item_data in self.supplementary_files:
                supplementary_files_item = supplementary_files_item_data.to_dict()
                supplementary_files.append(supplementary_files_item)

        is_physical = self.is_physical

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if library_id is not UNSET:
            field_dict["libraryId"] = library_id
        if library_name is not UNSET:
            field_dict["libraryName"] = library_name
        if primary_file is not UNSET:
            field_dict["primaryFile"] = primary_file
        if title is not UNSET:
            field_dict["title"] = title
        if last_read_time is not UNSET:
            field_dict["lastReadTime"] = last_read_time
        if added_on is not UNSET:
            field_dict["addedOn"] = added_on
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if metadata_match_score is not UNSET:
            field_dict["metadataMatchScore"] = metadata_match_score
        if pdf_progress is not UNSET:
            field_dict["pdfProgress"] = pdf_progress
        if epub_progress is not UNSET:
            field_dict["epubProgress"] = epub_progress
        if cbx_progress is not UNSET:
            field_dict["cbxProgress"] = cbx_progress
        if audiobook_progress is not UNSET:
            field_dict["audiobookProgress"] = audiobook_progress
        if koreader_progress is not UNSET:
            field_dict["koreaderProgress"] = koreader_progress
        if kobo_progress is not UNSET:
            field_dict["koboProgress"] = kobo_progress
        if personal_rating is not UNSET:
            field_dict["personalRating"] = personal_rating
        if shelves is not UNSET:
            field_dict["shelves"] = shelves
        if read_status is not UNSET:
            field_dict["readStatus"] = read_status
        if date_finished is not UNSET:
            field_dict["dateFinished"] = date_finished
        if library_path is not UNSET:
            field_dict["libraryPath"] = library_path
        if alternative_formats is not UNSET:
            field_dict["alternativeFormats"] = alternative_formats
        if supplementary_files is not UNSET:
            field_dict["supplementaryFiles"] = supplementary_files
        if is_physical is not UNSET:
            field_dict["isPhysical"] = is_physical

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.audiobook_progress import AudiobookProgress
        from ..models.book_file import BookFile
        from ..models.book_metadata import BookMetadata
        from ..models.cbx_progress import CbxProgress
        from ..models.epub_progress import EpubProgress
        from ..models.ko_progress import KoProgress
        from ..models.kobo_progress import KoboProgress
        from ..models.library_path import LibraryPath
        from ..models.pdf_progress import PdfProgress
        from ..models.shelf import Shelf

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        library_id = d.pop("libraryId", UNSET)

        library_name = d.pop("libraryName", UNSET)

        _primary_file = d.pop("primaryFile", UNSET)
        primary_file: BookFile | Unset
        if isinstance(_primary_file, Unset):
            primary_file = UNSET
        else:
            primary_file = BookFile.from_dict(_primary_file)

        title = d.pop("title", UNSET)

        _last_read_time = d.pop("lastReadTime", UNSET)
        last_read_time: datetime.datetime | Unset
        if isinstance(_last_read_time, Unset):
            last_read_time = UNSET
        else:
            last_read_time = datetime.datetime.fromisoformat(_last_read_time)

        _added_on = d.pop("addedOn", UNSET)
        added_on: datetime.datetime | Unset
        if isinstance(_added_on, Unset):
            added_on = UNSET
        else:
            added_on = datetime.datetime.fromisoformat(_added_on)

        _metadata = d.pop("metadata", UNSET)
        metadata: BookMetadata | Unset
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = BookMetadata.from_dict(_metadata)

        metadata_match_score = d.pop("metadataMatchScore", UNSET)

        _pdf_progress = d.pop("pdfProgress", UNSET)
        pdf_progress: PdfProgress | Unset
        if isinstance(_pdf_progress, Unset):
            pdf_progress = UNSET
        else:
            pdf_progress = PdfProgress.from_dict(_pdf_progress)

        _epub_progress = d.pop("epubProgress", UNSET)
        epub_progress: EpubProgress | Unset
        if isinstance(_epub_progress, Unset):
            epub_progress = UNSET
        else:
            epub_progress = EpubProgress.from_dict(_epub_progress)

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
        koreader_progress: KoProgress | Unset
        if isinstance(_koreader_progress, Unset):
            koreader_progress = UNSET
        else:
            koreader_progress = KoProgress.from_dict(_koreader_progress)

        _kobo_progress = d.pop("koboProgress", UNSET)
        kobo_progress: KoboProgress | Unset
        if isinstance(_kobo_progress, Unset):
            kobo_progress = UNSET
        else:
            kobo_progress = KoboProgress.from_dict(_kobo_progress)

        personal_rating = d.pop("personalRating", UNSET)

        _shelves = d.pop("shelves", UNSET)
        shelves: list[Shelf] | Unset = UNSET
        if _shelves is not UNSET:
            shelves = []
            for shelves_item_data in _shelves:
                shelves_item = Shelf.from_dict(shelves_item_data)

                shelves.append(shelves_item)

        read_status = d.pop("readStatus", UNSET)

        _date_finished = d.pop("dateFinished", UNSET)
        date_finished: datetime.datetime | Unset
        if isinstance(_date_finished, Unset):
            date_finished = UNSET
        else:
            date_finished = datetime.datetime.fromisoformat(_date_finished)

        _library_path = d.pop("libraryPath", UNSET)
        library_path: LibraryPath | Unset
        if isinstance(_library_path, Unset):
            library_path = UNSET
        else:
            library_path = LibraryPath.from_dict(_library_path)

        _alternative_formats = d.pop("alternativeFormats", UNSET)
        alternative_formats: list[BookFile] | Unset = UNSET
        if _alternative_formats is not UNSET:
            alternative_formats = []
            for alternative_formats_item_data in _alternative_formats:
                alternative_formats_item = BookFile.from_dict(alternative_formats_item_data)

                alternative_formats.append(alternative_formats_item)

        _supplementary_files = d.pop("supplementaryFiles", UNSET)
        supplementary_files: list[BookFile] | Unset = UNSET
        if _supplementary_files is not UNSET:
            supplementary_files = []
            for supplementary_files_item_data in _supplementary_files:
                supplementary_files_item = BookFile.from_dict(supplementary_files_item_data)

                supplementary_files.append(supplementary_files_item)

        is_physical = d.pop("isPhysical", UNSET)

        book = cls(
            id=id,
            library_id=library_id,
            library_name=library_name,
            primary_file=primary_file,
            title=title,
            last_read_time=last_read_time,
            added_on=added_on,
            metadata=metadata,
            metadata_match_score=metadata_match_score,
            pdf_progress=pdf_progress,
            epub_progress=epub_progress,
            cbx_progress=cbx_progress,
            audiobook_progress=audiobook_progress,
            koreader_progress=koreader_progress,
            kobo_progress=kobo_progress,
            personal_rating=personal_rating,
            shelves=shelves,
            read_status=read_status,
            date_finished=date_finished,
            library_path=library_path,
            alternative_formats=alternative_formats,
            supplementary_files=supplementary_files,
            is_physical=is_physical,
        )

        book.additional_properties = d
        return book

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
