from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.app_book_file import AppBookFile
    from ..models.app_shelf_summary import AppShelfSummary
    from ..models.audiobook_progress import AudiobookProgress
    from ..models.cbx_progress import CbxProgress
    from ..models.epub_progress import EpubProgress
    from ..models.koreader_progress import KoreaderProgress
    from ..models.pdf_progress import PdfProgress


T = TypeVar("T", bound="AppBookDetail")


@_attrs_define
class AppBookDetail:
    """
    Attributes:
        id (int | Unset):
        title (str | Unset):
        authors (list[str] | Unset):
        thumbnail_url (str | Unset):
        read_status (str | Unset):
        personal_rating (int | Unset):
        series_name (str | Unset):
        series_number (float | Unset):
        library_id (int | Unset):
        added_on (datetime.datetime | Unset):
        last_read_time (datetime.datetime | Unset):
        subtitle (str | Unset):
        description (str | Unset):
        categories (list[str] | Unset):
        publisher (str | Unset):
        published_date (datetime.date | Unset):
        page_count (int | Unset):
        isbn13 (str | Unset):
        language (str | Unset):
        goodreads_rating (float | Unset):
        goodreads_review_count (int | Unset):
        library_name (str | Unset):
        shelves (list[AppShelfSummary] | Unset):
        read_progress (float | Unset):
        primary_file_type (str | Unset):
        file_types (list[str] | Unset):
        files (list[AppBookFile] | Unset):
        cover_updated_on (datetime.datetime | Unset):
        audiobook_cover_updated_on (datetime.datetime | Unset):
        is_physical (bool | Unset):
        epub_progress (EpubProgress | Unset):
        pdf_progress (PdfProgress | Unset):
        cbx_progress (CbxProgress | Unset):
        audiobook_progress (AudiobookProgress | Unset):
        koreader_progress (KoreaderProgress | Unset): KoReader progress object
    """

    id: int | Unset = UNSET
    title: str | Unset = UNSET
    authors: list[str] | Unset = UNSET
    thumbnail_url: str | Unset = UNSET
    read_status: str | Unset = UNSET
    personal_rating: int | Unset = UNSET
    series_name: str | Unset = UNSET
    series_number: float | Unset = UNSET
    library_id: int | Unset = UNSET
    added_on: datetime.datetime | Unset = UNSET
    last_read_time: datetime.datetime | Unset = UNSET
    subtitle: str | Unset = UNSET
    description: str | Unset = UNSET
    categories: list[str] | Unset = UNSET
    publisher: str | Unset = UNSET
    published_date: datetime.date | Unset = UNSET
    page_count: int | Unset = UNSET
    isbn13: str | Unset = UNSET
    language: str | Unset = UNSET
    goodreads_rating: float | Unset = UNSET
    goodreads_review_count: int | Unset = UNSET
    library_name: str | Unset = UNSET
    shelves: list[AppShelfSummary] | Unset = UNSET
    read_progress: float | Unset = UNSET
    primary_file_type: str | Unset = UNSET
    file_types: list[str] | Unset = UNSET
    files: list[AppBookFile] | Unset = UNSET
    cover_updated_on: datetime.datetime | Unset = UNSET
    audiobook_cover_updated_on: datetime.datetime | Unset = UNSET
    is_physical: bool | Unset = UNSET
    epub_progress: EpubProgress | Unset = UNSET
    pdf_progress: PdfProgress | Unset = UNSET
    cbx_progress: CbxProgress | Unset = UNSET
    audiobook_progress: AudiobookProgress | Unset = UNSET
    koreader_progress: KoreaderProgress | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        title = self.title

        authors: list[str] | Unset = UNSET
        if not isinstance(self.authors, Unset):
            authors = self.authors

        thumbnail_url = self.thumbnail_url

        read_status = self.read_status

        personal_rating = self.personal_rating

        series_name = self.series_name

        series_number = self.series_number

        library_id = self.library_id

        added_on: str | Unset = UNSET
        if not isinstance(self.added_on, Unset):
            added_on = self.added_on.isoformat()

        last_read_time: str | Unset = UNSET
        if not isinstance(self.last_read_time, Unset):
            last_read_time = self.last_read_time.isoformat()

        subtitle = self.subtitle

        description = self.description

        categories: list[str] | Unset = UNSET
        if not isinstance(self.categories, Unset):
            categories = self.categories

        publisher = self.publisher

        published_date: str | Unset = UNSET
        if not isinstance(self.published_date, Unset):
            published_date = self.published_date.isoformat()

        page_count = self.page_count

        isbn13 = self.isbn13

        language = self.language

        goodreads_rating = self.goodreads_rating

        goodreads_review_count = self.goodreads_review_count

        library_name = self.library_name

        shelves: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.shelves, Unset):
            shelves = []
            for shelves_item_data in self.shelves:
                shelves_item = shelves_item_data.to_dict()
                shelves.append(shelves_item)

        read_progress = self.read_progress

        primary_file_type = self.primary_file_type

        file_types: list[str] | Unset = UNSET
        if not isinstance(self.file_types, Unset):
            file_types = self.file_types

        files: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.files, Unset):
            files = []
            for files_item_data in self.files:
                files_item = files_item_data.to_dict()
                files.append(files_item)

        cover_updated_on: str | Unset = UNSET
        if not isinstance(self.cover_updated_on, Unset):
            cover_updated_on = self.cover_updated_on.isoformat()

        audiobook_cover_updated_on: str | Unset = UNSET
        if not isinstance(self.audiobook_cover_updated_on, Unset):
            audiobook_cover_updated_on = self.audiobook_cover_updated_on.isoformat()

        is_physical = self.is_physical

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
        if id is not UNSET:
            field_dict["id"] = id
        if title is not UNSET:
            field_dict["title"] = title
        if authors is not UNSET:
            field_dict["authors"] = authors
        if thumbnail_url is not UNSET:
            field_dict["thumbnailUrl"] = thumbnail_url
        if read_status is not UNSET:
            field_dict["readStatus"] = read_status
        if personal_rating is not UNSET:
            field_dict["personalRating"] = personal_rating
        if series_name is not UNSET:
            field_dict["seriesName"] = series_name
        if series_number is not UNSET:
            field_dict["seriesNumber"] = series_number
        if library_id is not UNSET:
            field_dict["libraryId"] = library_id
        if added_on is not UNSET:
            field_dict["addedOn"] = added_on
        if last_read_time is not UNSET:
            field_dict["lastReadTime"] = last_read_time
        if subtitle is not UNSET:
            field_dict["subtitle"] = subtitle
        if description is not UNSET:
            field_dict["description"] = description
        if categories is not UNSET:
            field_dict["categories"] = categories
        if publisher is not UNSET:
            field_dict["publisher"] = publisher
        if published_date is not UNSET:
            field_dict["publishedDate"] = published_date
        if page_count is not UNSET:
            field_dict["pageCount"] = page_count
        if isbn13 is not UNSET:
            field_dict["isbn13"] = isbn13
        if language is not UNSET:
            field_dict["language"] = language
        if goodreads_rating is not UNSET:
            field_dict["goodreadsRating"] = goodreads_rating
        if goodreads_review_count is not UNSET:
            field_dict["goodreadsReviewCount"] = goodreads_review_count
        if library_name is not UNSET:
            field_dict["libraryName"] = library_name
        if shelves is not UNSET:
            field_dict["shelves"] = shelves
        if read_progress is not UNSET:
            field_dict["readProgress"] = read_progress
        if primary_file_type is not UNSET:
            field_dict["primaryFileType"] = primary_file_type
        if file_types is not UNSET:
            field_dict["fileTypes"] = file_types
        if files is not UNSET:
            field_dict["files"] = files
        if cover_updated_on is not UNSET:
            field_dict["coverUpdatedOn"] = cover_updated_on
        if audiobook_cover_updated_on is not UNSET:
            field_dict["audiobookCoverUpdatedOn"] = audiobook_cover_updated_on
        if is_physical is not UNSET:
            field_dict["isPhysical"] = is_physical
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
        from ..models.app_book_file import AppBookFile
        from ..models.app_shelf_summary import AppShelfSummary
        from ..models.audiobook_progress import AudiobookProgress
        from ..models.cbx_progress import CbxProgress
        from ..models.epub_progress import EpubProgress
        from ..models.koreader_progress import KoreaderProgress
        from ..models.pdf_progress import PdfProgress

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        title = d.pop("title", UNSET)

        authors = cast(list[str], d.pop("authors", UNSET))

        thumbnail_url = d.pop("thumbnailUrl", UNSET)

        read_status = d.pop("readStatus", UNSET)

        personal_rating = d.pop("personalRating", UNSET)

        series_name = d.pop("seriesName", UNSET)

        series_number = d.pop("seriesNumber", UNSET)

        library_id = d.pop("libraryId", UNSET)

        _added_on = d.pop("addedOn", UNSET)
        added_on: datetime.datetime | Unset
        if isinstance(_added_on, Unset):
            added_on = UNSET
        else:
            added_on = datetime.datetime.fromisoformat(_added_on)

        _last_read_time = d.pop("lastReadTime", UNSET)
        last_read_time: datetime.datetime | Unset
        if isinstance(_last_read_time, Unset):
            last_read_time = UNSET
        else:
            last_read_time = datetime.datetime.fromisoformat(_last_read_time)

        subtitle = d.pop("subtitle", UNSET)

        description = d.pop("description", UNSET)

        categories = cast(list[str], d.pop("categories", UNSET))

        publisher = d.pop("publisher", UNSET)

        _published_date = d.pop("publishedDate", UNSET)
        published_date: datetime.date | Unset
        if isinstance(_published_date, Unset):
            published_date = UNSET
        else:
            published_date = datetime.date.fromisoformat(_published_date)

        page_count = d.pop("pageCount", UNSET)

        isbn13 = d.pop("isbn13", UNSET)

        language = d.pop("language", UNSET)

        goodreads_rating = d.pop("goodreadsRating", UNSET)

        goodreads_review_count = d.pop("goodreadsReviewCount", UNSET)

        library_name = d.pop("libraryName", UNSET)

        _shelves = d.pop("shelves", UNSET)
        shelves: list[AppShelfSummary] | Unset = UNSET
        if _shelves is not UNSET:
            shelves = []
            for shelves_item_data in _shelves:
                shelves_item = AppShelfSummary.from_dict(shelves_item_data)

                shelves.append(shelves_item)

        read_progress = d.pop("readProgress", UNSET)

        primary_file_type = d.pop("primaryFileType", UNSET)

        file_types = cast(list[str], d.pop("fileTypes", UNSET))

        _files = d.pop("files", UNSET)
        files: list[AppBookFile] | Unset = UNSET
        if _files is not UNSET:
            files = []
            for files_item_data in _files:
                files_item = AppBookFile.from_dict(files_item_data)

                files.append(files_item)

        _cover_updated_on = d.pop("coverUpdatedOn", UNSET)
        cover_updated_on: datetime.datetime | Unset
        if isinstance(_cover_updated_on, Unset):
            cover_updated_on = UNSET
        else:
            cover_updated_on = datetime.datetime.fromisoformat(_cover_updated_on)

        _audiobook_cover_updated_on = d.pop("audiobookCoverUpdatedOn", UNSET)
        audiobook_cover_updated_on: datetime.datetime | Unset
        if isinstance(_audiobook_cover_updated_on, Unset):
            audiobook_cover_updated_on = UNSET
        else:
            audiobook_cover_updated_on = datetime.datetime.fromisoformat(_audiobook_cover_updated_on)

        is_physical = d.pop("isPhysical", UNSET)

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

        app_book_detail = cls(
            id=id,
            title=title,
            authors=authors,
            thumbnail_url=thumbnail_url,
            read_status=read_status,
            personal_rating=personal_rating,
            series_name=series_name,
            series_number=series_number,
            library_id=library_id,
            added_on=added_on,
            last_read_time=last_read_time,
            subtitle=subtitle,
            description=description,
            categories=categories,
            publisher=publisher,
            published_date=published_date,
            page_count=page_count,
            isbn13=isbn13,
            language=language,
            goodreads_rating=goodreads_rating,
            goodreads_review_count=goodreads_review_count,
            library_name=library_name,
            shelves=shelves,
            read_progress=read_progress,
            primary_file_type=primary_file_type,
            file_types=file_types,
            files=files,
            cover_updated_on=cover_updated_on,
            audiobook_cover_updated_on=audiobook_cover_updated_on,
            is_physical=is_physical,
            epub_progress=epub_progress,
            pdf_progress=pdf_progress,
            cbx_progress=cbx_progress,
            audiobook_progress=audiobook_progress,
            koreader_progress=koreader_progress,
        )

        app_book_detail.additional_properties = d
        return app_book_detail

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
