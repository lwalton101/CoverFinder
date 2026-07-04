from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BookListRequest")


@_attrs_define
class BookListRequest:
    """
    Attributes:
        page (int | Unset):
        size (int | Unset):
        sort (str | Unset):
        dir_ (str | Unset):
        library_id (int | Unset):
        shelf_id (int | Unset):
        status (list[str] | Unset):
        search (str | Unset):
        file_type (list[str] | Unset):
        min_rating (int | Unset):
        max_rating (int | Unset):
        authors (list[str] | Unset):
        language (list[str] | Unset):
        series (list[str] | Unset):
        category (list[str] | Unset):
        publisher (list[str] | Unset):
        tag (list[str] | Unset):
        mood (list[str] | Unset):
        narrator (list[str] | Unset):
        age_rating (list[str] | Unset):
        content_rating (list[str] | Unset):
        match_score (list[str] | Unset):
        published_date (list[str] | Unset):
        file_size (list[str] | Unset):
        personal_rating (list[str] | Unset):
        amazon_rating (list[str] | Unset):
        goodreads_rating (list[str] | Unset):
        hardcover_rating (list[str] | Unset):
        lubimyczytac_rating (list[str] | Unset):
        ranobedb_rating (list[str] | Unset):
        audible_rating (list[str] | Unset):
        page_count (list[str] | Unset):
        shelf_status (list[str] | Unset):
        comic_character (list[str] | Unset):
        comic_team (list[str] | Unset):
        comic_location (list[str] | Unset):
        comic_creator (list[str] | Unset):
        shelves (list[str] | Unset):
        libraries (list[str] | Unset):
        magic_shelf_id (int | Unset):
        unshelved (bool | Unset):
        filter_mode (str | Unset):
    """

    page: int | Unset = UNSET
    size: int | Unset = UNSET
    sort: str | Unset = UNSET
    dir_: str | Unset = UNSET
    library_id: int | Unset = UNSET
    shelf_id: int | Unset = UNSET
    status: list[str] | Unset = UNSET
    search: str | Unset = UNSET
    file_type: list[str] | Unset = UNSET
    min_rating: int | Unset = UNSET
    max_rating: int | Unset = UNSET
    authors: list[str] | Unset = UNSET
    language: list[str] | Unset = UNSET
    series: list[str] | Unset = UNSET
    category: list[str] | Unset = UNSET
    publisher: list[str] | Unset = UNSET
    tag: list[str] | Unset = UNSET
    mood: list[str] | Unset = UNSET
    narrator: list[str] | Unset = UNSET
    age_rating: list[str] | Unset = UNSET
    content_rating: list[str] | Unset = UNSET
    match_score: list[str] | Unset = UNSET
    published_date: list[str] | Unset = UNSET
    file_size: list[str] | Unset = UNSET
    personal_rating: list[str] | Unset = UNSET
    amazon_rating: list[str] | Unset = UNSET
    goodreads_rating: list[str] | Unset = UNSET
    hardcover_rating: list[str] | Unset = UNSET
    lubimyczytac_rating: list[str] | Unset = UNSET
    ranobedb_rating: list[str] | Unset = UNSET
    audible_rating: list[str] | Unset = UNSET
    page_count: list[str] | Unset = UNSET
    shelf_status: list[str] | Unset = UNSET
    comic_character: list[str] | Unset = UNSET
    comic_team: list[str] | Unset = UNSET
    comic_location: list[str] | Unset = UNSET
    comic_creator: list[str] | Unset = UNSET
    shelves: list[str] | Unset = UNSET
    libraries: list[str] | Unset = UNSET
    magic_shelf_id: int | Unset = UNSET
    unshelved: bool | Unset = UNSET
    filter_mode: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        page = self.page

        size = self.size

        sort = self.sort

        dir_ = self.dir_

        library_id = self.library_id

        shelf_id = self.shelf_id

        status: list[str] | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status

        search = self.search

        file_type: list[str] | Unset = UNSET
        if not isinstance(self.file_type, Unset):
            file_type = self.file_type

        min_rating = self.min_rating

        max_rating = self.max_rating

        authors: list[str] | Unset = UNSET
        if not isinstance(self.authors, Unset):
            authors = self.authors

        language: list[str] | Unset = UNSET
        if not isinstance(self.language, Unset):
            language = self.language

        series: list[str] | Unset = UNSET
        if not isinstance(self.series, Unset):
            series = self.series

        category: list[str] | Unset = UNSET
        if not isinstance(self.category, Unset):
            category = self.category

        publisher: list[str] | Unset = UNSET
        if not isinstance(self.publisher, Unset):
            publisher = self.publisher

        tag: list[str] | Unset = UNSET
        if not isinstance(self.tag, Unset):
            tag = self.tag

        mood: list[str] | Unset = UNSET
        if not isinstance(self.mood, Unset):
            mood = self.mood

        narrator: list[str] | Unset = UNSET
        if not isinstance(self.narrator, Unset):
            narrator = self.narrator

        age_rating: list[str] | Unset = UNSET
        if not isinstance(self.age_rating, Unset):
            age_rating = self.age_rating

        content_rating: list[str] | Unset = UNSET
        if not isinstance(self.content_rating, Unset):
            content_rating = self.content_rating

        match_score: list[str] | Unset = UNSET
        if not isinstance(self.match_score, Unset):
            match_score = self.match_score

        published_date: list[str] | Unset = UNSET
        if not isinstance(self.published_date, Unset):
            published_date = self.published_date

        file_size: list[str] | Unset = UNSET
        if not isinstance(self.file_size, Unset):
            file_size = self.file_size

        personal_rating: list[str] | Unset = UNSET
        if not isinstance(self.personal_rating, Unset):
            personal_rating = self.personal_rating

        amazon_rating: list[str] | Unset = UNSET
        if not isinstance(self.amazon_rating, Unset):
            amazon_rating = self.amazon_rating

        goodreads_rating: list[str] | Unset = UNSET
        if not isinstance(self.goodreads_rating, Unset):
            goodreads_rating = self.goodreads_rating

        hardcover_rating: list[str] | Unset = UNSET
        if not isinstance(self.hardcover_rating, Unset):
            hardcover_rating = self.hardcover_rating

        lubimyczytac_rating: list[str] | Unset = UNSET
        if not isinstance(self.lubimyczytac_rating, Unset):
            lubimyczytac_rating = self.lubimyczytac_rating

        ranobedb_rating: list[str] | Unset = UNSET
        if not isinstance(self.ranobedb_rating, Unset):
            ranobedb_rating = self.ranobedb_rating

        audible_rating: list[str] | Unset = UNSET
        if not isinstance(self.audible_rating, Unset):
            audible_rating = self.audible_rating

        page_count: list[str] | Unset = UNSET
        if not isinstance(self.page_count, Unset):
            page_count = self.page_count

        shelf_status: list[str] | Unset = UNSET
        if not isinstance(self.shelf_status, Unset):
            shelf_status = self.shelf_status

        comic_character: list[str] | Unset = UNSET
        if not isinstance(self.comic_character, Unset):
            comic_character = self.comic_character

        comic_team: list[str] | Unset = UNSET
        if not isinstance(self.comic_team, Unset):
            comic_team = self.comic_team

        comic_location: list[str] | Unset = UNSET
        if not isinstance(self.comic_location, Unset):
            comic_location = self.comic_location

        comic_creator: list[str] | Unset = UNSET
        if not isinstance(self.comic_creator, Unset):
            comic_creator = self.comic_creator

        shelves: list[str] | Unset = UNSET
        if not isinstance(self.shelves, Unset):
            shelves = self.shelves

        libraries: list[str] | Unset = UNSET
        if not isinstance(self.libraries, Unset):
            libraries = self.libraries

        magic_shelf_id = self.magic_shelf_id

        unshelved = self.unshelved

        filter_mode = self.filter_mode

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if page is not UNSET:
            field_dict["page"] = page
        if size is not UNSET:
            field_dict["size"] = size
        if sort is not UNSET:
            field_dict["sort"] = sort
        if dir_ is not UNSET:
            field_dict["dir"] = dir_
        if library_id is not UNSET:
            field_dict["libraryId"] = library_id
        if shelf_id is not UNSET:
            field_dict["shelfId"] = shelf_id
        if status is not UNSET:
            field_dict["status"] = status
        if search is not UNSET:
            field_dict["search"] = search
        if file_type is not UNSET:
            field_dict["fileType"] = file_type
        if min_rating is not UNSET:
            field_dict["minRating"] = min_rating
        if max_rating is not UNSET:
            field_dict["maxRating"] = max_rating
        if authors is not UNSET:
            field_dict["authors"] = authors
        if language is not UNSET:
            field_dict["language"] = language
        if series is not UNSET:
            field_dict["series"] = series
        if category is not UNSET:
            field_dict["category"] = category
        if publisher is not UNSET:
            field_dict["publisher"] = publisher
        if tag is not UNSET:
            field_dict["tag"] = tag
        if mood is not UNSET:
            field_dict["mood"] = mood
        if narrator is not UNSET:
            field_dict["narrator"] = narrator
        if age_rating is not UNSET:
            field_dict["ageRating"] = age_rating
        if content_rating is not UNSET:
            field_dict["contentRating"] = content_rating
        if match_score is not UNSET:
            field_dict["matchScore"] = match_score
        if published_date is not UNSET:
            field_dict["publishedDate"] = published_date
        if file_size is not UNSET:
            field_dict["fileSize"] = file_size
        if personal_rating is not UNSET:
            field_dict["personalRating"] = personal_rating
        if amazon_rating is not UNSET:
            field_dict["amazonRating"] = amazon_rating
        if goodreads_rating is not UNSET:
            field_dict["goodreadsRating"] = goodreads_rating
        if hardcover_rating is not UNSET:
            field_dict["hardcoverRating"] = hardcover_rating
        if lubimyczytac_rating is not UNSET:
            field_dict["lubimyczytacRating"] = lubimyczytac_rating
        if ranobedb_rating is not UNSET:
            field_dict["ranobedbRating"] = ranobedb_rating
        if audible_rating is not UNSET:
            field_dict["audibleRating"] = audible_rating
        if page_count is not UNSET:
            field_dict["pageCount"] = page_count
        if shelf_status is not UNSET:
            field_dict["shelfStatus"] = shelf_status
        if comic_character is not UNSET:
            field_dict["comicCharacter"] = comic_character
        if comic_team is not UNSET:
            field_dict["comicTeam"] = comic_team
        if comic_location is not UNSET:
            field_dict["comicLocation"] = comic_location
        if comic_creator is not UNSET:
            field_dict["comicCreator"] = comic_creator
        if shelves is not UNSET:
            field_dict["shelves"] = shelves
        if libraries is not UNSET:
            field_dict["libraries"] = libraries
        if magic_shelf_id is not UNSET:
            field_dict["magicShelfId"] = magic_shelf_id
        if unshelved is not UNSET:
            field_dict["unshelved"] = unshelved
        if filter_mode is not UNSET:
            field_dict["filterMode"] = filter_mode

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        page = d.pop("page", UNSET)

        size = d.pop("size", UNSET)

        sort = d.pop("sort", UNSET)

        dir_ = d.pop("dir", UNSET)

        library_id = d.pop("libraryId", UNSET)

        shelf_id = d.pop("shelfId", UNSET)

        status = cast(list[str], d.pop("status", UNSET))

        search = d.pop("search", UNSET)

        file_type = cast(list[str], d.pop("fileType", UNSET))

        min_rating = d.pop("minRating", UNSET)

        max_rating = d.pop("maxRating", UNSET)

        authors = cast(list[str], d.pop("authors", UNSET))

        language = cast(list[str], d.pop("language", UNSET))

        series = cast(list[str], d.pop("series", UNSET))

        category = cast(list[str], d.pop("category", UNSET))

        publisher = cast(list[str], d.pop("publisher", UNSET))

        tag = cast(list[str], d.pop("tag", UNSET))

        mood = cast(list[str], d.pop("mood", UNSET))

        narrator = cast(list[str], d.pop("narrator", UNSET))

        age_rating = cast(list[str], d.pop("ageRating", UNSET))

        content_rating = cast(list[str], d.pop("contentRating", UNSET))

        match_score = cast(list[str], d.pop("matchScore", UNSET))

        published_date = cast(list[str], d.pop("publishedDate", UNSET))

        file_size = cast(list[str], d.pop("fileSize", UNSET))

        personal_rating = cast(list[str], d.pop("personalRating", UNSET))

        amazon_rating = cast(list[str], d.pop("amazonRating", UNSET))

        goodreads_rating = cast(list[str], d.pop("goodreadsRating", UNSET))

        hardcover_rating = cast(list[str], d.pop("hardcoverRating", UNSET))

        lubimyczytac_rating = cast(list[str], d.pop("lubimyczytacRating", UNSET))

        ranobedb_rating = cast(list[str], d.pop("ranobedbRating", UNSET))

        audible_rating = cast(list[str], d.pop("audibleRating", UNSET))

        page_count = cast(list[str], d.pop("pageCount", UNSET))

        shelf_status = cast(list[str], d.pop("shelfStatus", UNSET))

        comic_character = cast(list[str], d.pop("comicCharacter", UNSET))

        comic_team = cast(list[str], d.pop("comicTeam", UNSET))

        comic_location = cast(list[str], d.pop("comicLocation", UNSET))

        comic_creator = cast(list[str], d.pop("comicCreator", UNSET))

        shelves = cast(list[str], d.pop("shelves", UNSET))

        libraries = cast(list[str], d.pop("libraries", UNSET))

        magic_shelf_id = d.pop("magicShelfId", UNSET)

        unshelved = d.pop("unshelved", UNSET)

        filter_mode = d.pop("filterMode", UNSET)

        book_list_request = cls(
            page=page,
            size=size,
            sort=sort,
            dir_=dir_,
            library_id=library_id,
            shelf_id=shelf_id,
            status=status,
            search=search,
            file_type=file_type,
            min_rating=min_rating,
            max_rating=max_rating,
            authors=authors,
            language=language,
            series=series,
            category=category,
            publisher=publisher,
            tag=tag,
            mood=mood,
            narrator=narrator,
            age_rating=age_rating,
            content_rating=content_rating,
            match_score=match_score,
            published_date=published_date,
            file_size=file_size,
            personal_rating=personal_rating,
            amazon_rating=amazon_rating,
            goodreads_rating=goodreads_rating,
            hardcover_rating=hardcover_rating,
            lubimyczytac_rating=lubimyczytac_rating,
            ranobedb_rating=ranobedb_rating,
            audible_rating=audible_rating,
            page_count=page_count,
            shelf_status=shelf_status,
            comic_character=comic_character,
            comic_team=comic_team,
            comic_location=comic_location,
            comic_creator=comic_creator,
            shelves=shelves,
            libraries=libraries,
            magic_shelf_id=magic_shelf_id,
            unshelved=unshelved,
            filter_mode=filter_mode,
        )

        book_list_request.additional_properties = d
        return book_list_request

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
