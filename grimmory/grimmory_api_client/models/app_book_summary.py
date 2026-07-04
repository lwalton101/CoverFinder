from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AppBookSummary")


@_attrs_define
class AppBookSummary:
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
        read_progress (float | Unset):
        primary_file_id (int | Unset):
        primary_file_type (str | Unset):
        primary_file_name (str | Unset):
        cover_updated_on (datetime.datetime | Unset):
        audiobook_cover_updated_on (datetime.datetime | Unset):
        is_physical (bool | Unset):
        publisher (str | Unset):
        categories (list[str] | Unset):
        tags (list[str] | Unset):
        moods (list[str] | Unset):
        language (str | Unset):
        narrator (str | Unset):
        isbn13 (str | Unset):
        isbn10 (str | Unset):
        published_date (datetime.date | Unset):
        page_count (int | Unset):
        age_rating (int | Unset):
        content_rating (str | Unset):
        metadata_match_score (float | Unset):
        file_size_kb (int | Unset):
        amazon_rating (float | Unset):
        amazon_review_count (int | Unset):
        goodreads_rating (float | Unset):
        goodreads_review_count (int | Unset):
        hardcover_rating (float | Unset):
        hardcover_review_count (int | Unset):
        ranobedb_rating (float | Unset):
        lubimyczytac_rating (float | Unset):
        audible_rating (float | Unset):
        audible_review_count (int | Unset):
        all_metadata_locked (bool | Unset):
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
    read_progress: float | Unset = UNSET
    primary_file_id: int | Unset = UNSET
    primary_file_type: str | Unset = UNSET
    primary_file_name: str | Unset = UNSET
    cover_updated_on: datetime.datetime | Unset = UNSET
    audiobook_cover_updated_on: datetime.datetime | Unset = UNSET
    is_physical: bool | Unset = UNSET
    publisher: str | Unset = UNSET
    categories: list[str] | Unset = UNSET
    tags: list[str] | Unset = UNSET
    moods: list[str] | Unset = UNSET
    language: str | Unset = UNSET
    narrator: str | Unset = UNSET
    isbn13: str | Unset = UNSET
    isbn10: str | Unset = UNSET
    published_date: datetime.date | Unset = UNSET
    page_count: int | Unset = UNSET
    age_rating: int | Unset = UNSET
    content_rating: str | Unset = UNSET
    metadata_match_score: float | Unset = UNSET
    file_size_kb: int | Unset = UNSET
    amazon_rating: float | Unset = UNSET
    amazon_review_count: int | Unset = UNSET
    goodreads_rating: float | Unset = UNSET
    goodreads_review_count: int | Unset = UNSET
    hardcover_rating: float | Unset = UNSET
    hardcover_review_count: int | Unset = UNSET
    ranobedb_rating: float | Unset = UNSET
    lubimyczytac_rating: float | Unset = UNSET
    audible_rating: float | Unset = UNSET
    audible_review_count: int | Unset = UNSET
    all_metadata_locked: bool | Unset = UNSET
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

        read_progress = self.read_progress

        primary_file_id = self.primary_file_id

        primary_file_type = self.primary_file_type

        primary_file_name = self.primary_file_name

        cover_updated_on: str | Unset = UNSET
        if not isinstance(self.cover_updated_on, Unset):
            cover_updated_on = self.cover_updated_on.isoformat()

        audiobook_cover_updated_on: str | Unset = UNSET
        if not isinstance(self.audiobook_cover_updated_on, Unset):
            audiobook_cover_updated_on = self.audiobook_cover_updated_on.isoformat()

        is_physical = self.is_physical

        publisher = self.publisher

        categories: list[str] | Unset = UNSET
        if not isinstance(self.categories, Unset):
            categories = self.categories

        tags: list[str] | Unset = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags

        moods: list[str] | Unset = UNSET
        if not isinstance(self.moods, Unset):
            moods = self.moods

        language = self.language

        narrator = self.narrator

        isbn13 = self.isbn13

        isbn10 = self.isbn10

        published_date: str | Unset = UNSET
        if not isinstance(self.published_date, Unset):
            published_date = self.published_date.isoformat()

        page_count = self.page_count

        age_rating = self.age_rating

        content_rating = self.content_rating

        metadata_match_score = self.metadata_match_score

        file_size_kb = self.file_size_kb

        amazon_rating = self.amazon_rating

        amazon_review_count = self.amazon_review_count

        goodreads_rating = self.goodreads_rating

        goodreads_review_count = self.goodreads_review_count

        hardcover_rating = self.hardcover_rating

        hardcover_review_count = self.hardcover_review_count

        ranobedb_rating = self.ranobedb_rating

        lubimyczytac_rating = self.lubimyczytac_rating

        audible_rating = self.audible_rating

        audible_review_count = self.audible_review_count

        all_metadata_locked = self.all_metadata_locked

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
        if read_progress is not UNSET:
            field_dict["readProgress"] = read_progress
        if primary_file_id is not UNSET:
            field_dict["primaryFileId"] = primary_file_id
        if primary_file_type is not UNSET:
            field_dict["primaryFileType"] = primary_file_type
        if primary_file_name is not UNSET:
            field_dict["primaryFileName"] = primary_file_name
        if cover_updated_on is not UNSET:
            field_dict["coverUpdatedOn"] = cover_updated_on
        if audiobook_cover_updated_on is not UNSET:
            field_dict["audiobookCoverUpdatedOn"] = audiobook_cover_updated_on
        if is_physical is not UNSET:
            field_dict["isPhysical"] = is_physical
        if publisher is not UNSET:
            field_dict["publisher"] = publisher
        if categories is not UNSET:
            field_dict["categories"] = categories
        if tags is not UNSET:
            field_dict["tags"] = tags
        if moods is not UNSET:
            field_dict["moods"] = moods
        if language is not UNSET:
            field_dict["language"] = language
        if narrator is not UNSET:
            field_dict["narrator"] = narrator
        if isbn13 is not UNSET:
            field_dict["isbn13"] = isbn13
        if isbn10 is not UNSET:
            field_dict["isbn10"] = isbn10
        if published_date is not UNSET:
            field_dict["publishedDate"] = published_date
        if page_count is not UNSET:
            field_dict["pageCount"] = page_count
        if age_rating is not UNSET:
            field_dict["ageRating"] = age_rating
        if content_rating is not UNSET:
            field_dict["contentRating"] = content_rating
        if metadata_match_score is not UNSET:
            field_dict["metadataMatchScore"] = metadata_match_score
        if file_size_kb is not UNSET:
            field_dict["fileSizeKb"] = file_size_kb
        if amazon_rating is not UNSET:
            field_dict["amazonRating"] = amazon_rating
        if amazon_review_count is not UNSET:
            field_dict["amazonReviewCount"] = amazon_review_count
        if goodreads_rating is not UNSET:
            field_dict["goodreadsRating"] = goodreads_rating
        if goodreads_review_count is not UNSET:
            field_dict["goodreadsReviewCount"] = goodreads_review_count
        if hardcover_rating is not UNSET:
            field_dict["hardcoverRating"] = hardcover_rating
        if hardcover_review_count is not UNSET:
            field_dict["hardcoverReviewCount"] = hardcover_review_count
        if ranobedb_rating is not UNSET:
            field_dict["ranobedbRating"] = ranobedb_rating
        if lubimyczytac_rating is not UNSET:
            field_dict["lubimyczytacRating"] = lubimyczytac_rating
        if audible_rating is not UNSET:
            field_dict["audibleRating"] = audible_rating
        if audible_review_count is not UNSET:
            field_dict["audibleReviewCount"] = audible_review_count
        if all_metadata_locked is not UNSET:
            field_dict["allMetadataLocked"] = all_metadata_locked

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
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

        read_progress = d.pop("readProgress", UNSET)

        primary_file_id = d.pop("primaryFileId", UNSET)

        primary_file_type = d.pop("primaryFileType", UNSET)

        primary_file_name = d.pop("primaryFileName", UNSET)

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

        publisher = d.pop("publisher", UNSET)

        categories = cast(list[str], d.pop("categories", UNSET))

        tags = cast(list[str], d.pop("tags", UNSET))

        moods = cast(list[str], d.pop("moods", UNSET))

        language = d.pop("language", UNSET)

        narrator = d.pop("narrator", UNSET)

        isbn13 = d.pop("isbn13", UNSET)

        isbn10 = d.pop("isbn10", UNSET)

        _published_date = d.pop("publishedDate", UNSET)
        published_date: datetime.date | Unset
        if isinstance(_published_date, Unset):
            published_date = UNSET
        else:
            published_date = datetime.date.fromisoformat(_published_date)

        page_count = d.pop("pageCount", UNSET)

        age_rating = d.pop("ageRating", UNSET)

        content_rating = d.pop("contentRating", UNSET)

        metadata_match_score = d.pop("metadataMatchScore", UNSET)

        file_size_kb = d.pop("fileSizeKb", UNSET)

        amazon_rating = d.pop("amazonRating", UNSET)

        amazon_review_count = d.pop("amazonReviewCount", UNSET)

        goodreads_rating = d.pop("goodreadsRating", UNSET)

        goodreads_review_count = d.pop("goodreadsReviewCount", UNSET)

        hardcover_rating = d.pop("hardcoverRating", UNSET)

        hardcover_review_count = d.pop("hardcoverReviewCount", UNSET)

        ranobedb_rating = d.pop("ranobedbRating", UNSET)

        lubimyczytac_rating = d.pop("lubimyczytacRating", UNSET)

        audible_rating = d.pop("audibleRating", UNSET)

        audible_review_count = d.pop("audibleReviewCount", UNSET)

        all_metadata_locked = d.pop("allMetadataLocked", UNSET)

        app_book_summary = cls(
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
            read_progress=read_progress,
            primary_file_id=primary_file_id,
            primary_file_type=primary_file_type,
            primary_file_name=primary_file_name,
            cover_updated_on=cover_updated_on,
            audiobook_cover_updated_on=audiobook_cover_updated_on,
            is_physical=is_physical,
            publisher=publisher,
            categories=categories,
            tags=tags,
            moods=moods,
            language=language,
            narrator=narrator,
            isbn13=isbn13,
            isbn10=isbn10,
            published_date=published_date,
            page_count=page_count,
            age_rating=age_rating,
            content_rating=content_rating,
            metadata_match_score=metadata_match_score,
            file_size_kb=file_size_kb,
            amazon_rating=amazon_rating,
            amazon_review_count=amazon_review_count,
            goodreads_rating=goodreads_rating,
            goodreads_review_count=goodreads_review_count,
            hardcover_rating=hardcover_rating,
            hardcover_review_count=hardcover_review_count,
            ranobedb_rating=ranobedb_rating,
            lubimyczytac_rating=lubimyczytac_rating,
            audible_rating=audible_rating,
            audible_review_count=audible_review_count,
            all_metadata_locked=all_metadata_locked,
        )

        app_book_summary.additional_properties = d
        return app_book_summary

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
