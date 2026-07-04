from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.field_provider import FieldProvider


T = TypeVar("T", bound="FieldOptions")


@_attrs_define
class FieldOptions:
    """
    Attributes:
        title (FieldProvider | Unset):
        subtitle (FieldProvider | Unset):
        description (FieldProvider | Unset):
        authors (FieldProvider | Unset):
        publisher (FieldProvider | Unset):
        published_date (FieldProvider | Unset):
        series_name (FieldProvider | Unset):
        series_number (FieldProvider | Unset):
        series_total (FieldProvider | Unset):
        isbn13 (FieldProvider | Unset):
        isbn10 (FieldProvider | Unset):
        language (FieldProvider | Unset):
        categories (FieldProvider | Unset):
        cover (FieldProvider | Unset):
        page_count (FieldProvider | Unset):
        asin (FieldProvider | Unset):
        goodreads_id (FieldProvider | Unset):
        comicvine_id (FieldProvider | Unset):
        hardcover_id (FieldProvider | Unset):
        hardcover_book_id (FieldProvider | Unset):
        google_id (FieldProvider | Unset):
        lubimyczytac_id (FieldProvider | Unset):
        amazon_rating (FieldProvider | Unset):
        amazon_review_count (FieldProvider | Unset):
        goodreads_rating (FieldProvider | Unset):
        goodreads_review_count (FieldProvider | Unset):
        hardcover_rating (FieldProvider | Unset):
        hardcover_review_count (FieldProvider | Unset):
        lubimyczytac_rating (FieldProvider | Unset):
        ranobedb_id (FieldProvider | Unset):
        ranobedb_rating (FieldProvider | Unset):
        audible_id (FieldProvider | Unset):
        audible_rating (FieldProvider | Unset):
        audible_review_count (FieldProvider | Unset):
        moods (FieldProvider | Unset):
        tags (FieldProvider | Unset):
    """

    title: FieldProvider | Unset = UNSET
    subtitle: FieldProvider | Unset = UNSET
    description: FieldProvider | Unset = UNSET
    authors: FieldProvider | Unset = UNSET
    publisher: FieldProvider | Unset = UNSET
    published_date: FieldProvider | Unset = UNSET
    series_name: FieldProvider | Unset = UNSET
    series_number: FieldProvider | Unset = UNSET
    series_total: FieldProvider | Unset = UNSET
    isbn13: FieldProvider | Unset = UNSET
    isbn10: FieldProvider | Unset = UNSET
    language: FieldProvider | Unset = UNSET
    categories: FieldProvider | Unset = UNSET
    cover: FieldProvider | Unset = UNSET
    page_count: FieldProvider | Unset = UNSET
    asin: FieldProvider | Unset = UNSET
    goodreads_id: FieldProvider | Unset = UNSET
    comicvine_id: FieldProvider | Unset = UNSET
    hardcover_id: FieldProvider | Unset = UNSET
    hardcover_book_id: FieldProvider | Unset = UNSET
    google_id: FieldProvider | Unset = UNSET
    lubimyczytac_id: FieldProvider | Unset = UNSET
    amazon_rating: FieldProvider | Unset = UNSET
    amazon_review_count: FieldProvider | Unset = UNSET
    goodreads_rating: FieldProvider | Unset = UNSET
    goodreads_review_count: FieldProvider | Unset = UNSET
    hardcover_rating: FieldProvider | Unset = UNSET
    hardcover_review_count: FieldProvider | Unset = UNSET
    lubimyczytac_rating: FieldProvider | Unset = UNSET
    ranobedb_id: FieldProvider | Unset = UNSET
    ranobedb_rating: FieldProvider | Unset = UNSET
    audible_id: FieldProvider | Unset = UNSET
    audible_rating: FieldProvider | Unset = UNSET
    audible_review_count: FieldProvider | Unset = UNSET
    moods: FieldProvider | Unset = UNSET
    tags: FieldProvider | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        title: dict[str, Any] | Unset = UNSET
        if not isinstance(self.title, Unset):
            title = self.title.to_dict()

        subtitle: dict[str, Any] | Unset = UNSET
        if not isinstance(self.subtitle, Unset):
            subtitle = self.subtitle.to_dict()

        description: dict[str, Any] | Unset = UNSET
        if not isinstance(self.description, Unset):
            description = self.description.to_dict()

        authors: dict[str, Any] | Unset = UNSET
        if not isinstance(self.authors, Unset):
            authors = self.authors.to_dict()

        publisher: dict[str, Any] | Unset = UNSET
        if not isinstance(self.publisher, Unset):
            publisher = self.publisher.to_dict()

        published_date: dict[str, Any] | Unset = UNSET
        if not isinstance(self.published_date, Unset):
            published_date = self.published_date.to_dict()

        series_name: dict[str, Any] | Unset = UNSET
        if not isinstance(self.series_name, Unset):
            series_name = self.series_name.to_dict()

        series_number: dict[str, Any] | Unset = UNSET
        if not isinstance(self.series_number, Unset):
            series_number = self.series_number.to_dict()

        series_total: dict[str, Any] | Unset = UNSET
        if not isinstance(self.series_total, Unset):
            series_total = self.series_total.to_dict()

        isbn13: dict[str, Any] | Unset = UNSET
        if not isinstance(self.isbn13, Unset):
            isbn13 = self.isbn13.to_dict()

        isbn10: dict[str, Any] | Unset = UNSET
        if not isinstance(self.isbn10, Unset):
            isbn10 = self.isbn10.to_dict()

        language: dict[str, Any] | Unset = UNSET
        if not isinstance(self.language, Unset):
            language = self.language.to_dict()

        categories: dict[str, Any] | Unset = UNSET
        if not isinstance(self.categories, Unset):
            categories = self.categories.to_dict()

        cover: dict[str, Any] | Unset = UNSET
        if not isinstance(self.cover, Unset):
            cover = self.cover.to_dict()

        page_count: dict[str, Any] | Unset = UNSET
        if not isinstance(self.page_count, Unset):
            page_count = self.page_count.to_dict()

        asin: dict[str, Any] | Unset = UNSET
        if not isinstance(self.asin, Unset):
            asin = self.asin.to_dict()

        goodreads_id: dict[str, Any] | Unset = UNSET
        if not isinstance(self.goodreads_id, Unset):
            goodreads_id = self.goodreads_id.to_dict()

        comicvine_id: dict[str, Any] | Unset = UNSET
        if not isinstance(self.comicvine_id, Unset):
            comicvine_id = self.comicvine_id.to_dict()

        hardcover_id: dict[str, Any] | Unset = UNSET
        if not isinstance(self.hardcover_id, Unset):
            hardcover_id = self.hardcover_id.to_dict()

        hardcover_book_id: dict[str, Any] | Unset = UNSET
        if not isinstance(self.hardcover_book_id, Unset):
            hardcover_book_id = self.hardcover_book_id.to_dict()

        google_id: dict[str, Any] | Unset = UNSET
        if not isinstance(self.google_id, Unset):
            google_id = self.google_id.to_dict()

        lubimyczytac_id: dict[str, Any] | Unset = UNSET
        if not isinstance(self.lubimyczytac_id, Unset):
            lubimyczytac_id = self.lubimyczytac_id.to_dict()

        amazon_rating: dict[str, Any] | Unset = UNSET
        if not isinstance(self.amazon_rating, Unset):
            amazon_rating = self.amazon_rating.to_dict()

        amazon_review_count: dict[str, Any] | Unset = UNSET
        if not isinstance(self.amazon_review_count, Unset):
            amazon_review_count = self.amazon_review_count.to_dict()

        goodreads_rating: dict[str, Any] | Unset = UNSET
        if not isinstance(self.goodreads_rating, Unset):
            goodreads_rating = self.goodreads_rating.to_dict()

        goodreads_review_count: dict[str, Any] | Unset = UNSET
        if not isinstance(self.goodreads_review_count, Unset):
            goodreads_review_count = self.goodreads_review_count.to_dict()

        hardcover_rating: dict[str, Any] | Unset = UNSET
        if not isinstance(self.hardcover_rating, Unset):
            hardcover_rating = self.hardcover_rating.to_dict()

        hardcover_review_count: dict[str, Any] | Unset = UNSET
        if not isinstance(self.hardcover_review_count, Unset):
            hardcover_review_count = self.hardcover_review_count.to_dict()

        lubimyczytac_rating: dict[str, Any] | Unset = UNSET
        if not isinstance(self.lubimyczytac_rating, Unset):
            lubimyczytac_rating = self.lubimyczytac_rating.to_dict()

        ranobedb_id: dict[str, Any] | Unset = UNSET
        if not isinstance(self.ranobedb_id, Unset):
            ranobedb_id = self.ranobedb_id.to_dict()

        ranobedb_rating: dict[str, Any] | Unset = UNSET
        if not isinstance(self.ranobedb_rating, Unset):
            ranobedb_rating = self.ranobedb_rating.to_dict()

        audible_id: dict[str, Any] | Unset = UNSET
        if not isinstance(self.audible_id, Unset):
            audible_id = self.audible_id.to_dict()

        audible_rating: dict[str, Any] | Unset = UNSET
        if not isinstance(self.audible_rating, Unset):
            audible_rating = self.audible_rating.to_dict()

        audible_review_count: dict[str, Any] | Unset = UNSET
        if not isinstance(self.audible_review_count, Unset):
            audible_review_count = self.audible_review_count.to_dict()

        moods: dict[str, Any] | Unset = UNSET
        if not isinstance(self.moods, Unset):
            moods = self.moods.to_dict()

        tags: dict[str, Any] | Unset = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if title is not UNSET:
            field_dict["title"] = title
        if subtitle is not UNSET:
            field_dict["subtitle"] = subtitle
        if description is not UNSET:
            field_dict["description"] = description
        if authors is not UNSET:
            field_dict["authors"] = authors
        if publisher is not UNSET:
            field_dict["publisher"] = publisher
        if published_date is not UNSET:
            field_dict["publishedDate"] = published_date
        if series_name is not UNSET:
            field_dict["seriesName"] = series_name
        if series_number is not UNSET:
            field_dict["seriesNumber"] = series_number
        if series_total is not UNSET:
            field_dict["seriesTotal"] = series_total
        if isbn13 is not UNSET:
            field_dict["isbn13"] = isbn13
        if isbn10 is not UNSET:
            field_dict["isbn10"] = isbn10
        if language is not UNSET:
            field_dict["language"] = language
        if categories is not UNSET:
            field_dict["categories"] = categories
        if cover is not UNSET:
            field_dict["cover"] = cover
        if page_count is not UNSET:
            field_dict["pageCount"] = page_count
        if asin is not UNSET:
            field_dict["asin"] = asin
        if goodreads_id is not UNSET:
            field_dict["goodreadsId"] = goodreads_id
        if comicvine_id is not UNSET:
            field_dict["comicvineId"] = comicvine_id
        if hardcover_id is not UNSET:
            field_dict["hardcoverId"] = hardcover_id
        if hardcover_book_id is not UNSET:
            field_dict["hardcoverBookId"] = hardcover_book_id
        if google_id is not UNSET:
            field_dict["googleId"] = google_id
        if lubimyczytac_id is not UNSET:
            field_dict["lubimyczytacId"] = lubimyczytac_id
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
        if lubimyczytac_rating is not UNSET:
            field_dict["lubimyczytacRating"] = lubimyczytac_rating
        if ranobedb_id is not UNSET:
            field_dict["ranobedbId"] = ranobedb_id
        if ranobedb_rating is not UNSET:
            field_dict["ranobedbRating"] = ranobedb_rating
        if audible_id is not UNSET:
            field_dict["audibleId"] = audible_id
        if audible_rating is not UNSET:
            field_dict["audibleRating"] = audible_rating
        if audible_review_count is not UNSET:
            field_dict["audibleReviewCount"] = audible_review_count
        if moods is not UNSET:
            field_dict["moods"] = moods
        if tags is not UNSET:
            field_dict["tags"] = tags

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.field_provider import FieldProvider

        d = dict(src_dict)
        _title = d.pop("title", UNSET)
        title: FieldProvider | Unset
        if isinstance(_title, Unset):
            title = UNSET
        else:
            title = FieldProvider.from_dict(_title)

        _subtitle = d.pop("subtitle", UNSET)
        subtitle: FieldProvider | Unset
        if isinstance(_subtitle, Unset):
            subtitle = UNSET
        else:
            subtitle = FieldProvider.from_dict(_subtitle)

        _description = d.pop("description", UNSET)
        description: FieldProvider | Unset
        if isinstance(_description, Unset):
            description = UNSET
        else:
            description = FieldProvider.from_dict(_description)

        _authors = d.pop("authors", UNSET)
        authors: FieldProvider | Unset
        if isinstance(_authors, Unset):
            authors = UNSET
        else:
            authors = FieldProvider.from_dict(_authors)

        _publisher = d.pop("publisher", UNSET)
        publisher: FieldProvider | Unset
        if isinstance(_publisher, Unset):
            publisher = UNSET
        else:
            publisher = FieldProvider.from_dict(_publisher)

        _published_date = d.pop("publishedDate", UNSET)
        published_date: FieldProvider | Unset
        if isinstance(_published_date, Unset):
            published_date = UNSET
        else:
            published_date = FieldProvider.from_dict(_published_date)

        _series_name = d.pop("seriesName", UNSET)
        series_name: FieldProvider | Unset
        if isinstance(_series_name, Unset):
            series_name = UNSET
        else:
            series_name = FieldProvider.from_dict(_series_name)

        _series_number = d.pop("seriesNumber", UNSET)
        series_number: FieldProvider | Unset
        if isinstance(_series_number, Unset):
            series_number = UNSET
        else:
            series_number = FieldProvider.from_dict(_series_number)

        _series_total = d.pop("seriesTotal", UNSET)
        series_total: FieldProvider | Unset
        if isinstance(_series_total, Unset):
            series_total = UNSET
        else:
            series_total = FieldProvider.from_dict(_series_total)

        _isbn13 = d.pop("isbn13", UNSET)
        isbn13: FieldProvider | Unset
        if isinstance(_isbn13, Unset):
            isbn13 = UNSET
        else:
            isbn13 = FieldProvider.from_dict(_isbn13)

        _isbn10 = d.pop("isbn10", UNSET)
        isbn10: FieldProvider | Unset
        if isinstance(_isbn10, Unset):
            isbn10 = UNSET
        else:
            isbn10 = FieldProvider.from_dict(_isbn10)

        _language = d.pop("language", UNSET)
        language: FieldProvider | Unset
        if isinstance(_language, Unset):
            language = UNSET
        else:
            language = FieldProvider.from_dict(_language)

        _categories = d.pop("categories", UNSET)
        categories: FieldProvider | Unset
        if isinstance(_categories, Unset):
            categories = UNSET
        else:
            categories = FieldProvider.from_dict(_categories)

        _cover = d.pop("cover", UNSET)
        cover: FieldProvider | Unset
        if isinstance(_cover, Unset):
            cover = UNSET
        else:
            cover = FieldProvider.from_dict(_cover)

        _page_count = d.pop("pageCount", UNSET)
        page_count: FieldProvider | Unset
        if isinstance(_page_count, Unset):
            page_count = UNSET
        else:
            page_count = FieldProvider.from_dict(_page_count)

        _asin = d.pop("asin", UNSET)
        asin: FieldProvider | Unset
        if isinstance(_asin, Unset):
            asin = UNSET
        else:
            asin = FieldProvider.from_dict(_asin)

        _goodreads_id = d.pop("goodreadsId", UNSET)
        goodreads_id: FieldProvider | Unset
        if isinstance(_goodreads_id, Unset):
            goodreads_id = UNSET
        else:
            goodreads_id = FieldProvider.from_dict(_goodreads_id)

        _comicvine_id = d.pop("comicvineId", UNSET)
        comicvine_id: FieldProvider | Unset
        if isinstance(_comicvine_id, Unset):
            comicvine_id = UNSET
        else:
            comicvine_id = FieldProvider.from_dict(_comicvine_id)

        _hardcover_id = d.pop("hardcoverId", UNSET)
        hardcover_id: FieldProvider | Unset
        if isinstance(_hardcover_id, Unset):
            hardcover_id = UNSET
        else:
            hardcover_id = FieldProvider.from_dict(_hardcover_id)

        _hardcover_book_id = d.pop("hardcoverBookId", UNSET)
        hardcover_book_id: FieldProvider | Unset
        if isinstance(_hardcover_book_id, Unset):
            hardcover_book_id = UNSET
        else:
            hardcover_book_id = FieldProvider.from_dict(_hardcover_book_id)

        _google_id = d.pop("googleId", UNSET)
        google_id: FieldProvider | Unset
        if isinstance(_google_id, Unset):
            google_id = UNSET
        else:
            google_id = FieldProvider.from_dict(_google_id)

        _lubimyczytac_id = d.pop("lubimyczytacId", UNSET)
        lubimyczytac_id: FieldProvider | Unset
        if isinstance(_lubimyczytac_id, Unset):
            lubimyczytac_id = UNSET
        else:
            lubimyczytac_id = FieldProvider.from_dict(_lubimyczytac_id)

        _amazon_rating = d.pop("amazonRating", UNSET)
        amazon_rating: FieldProvider | Unset
        if isinstance(_amazon_rating, Unset):
            amazon_rating = UNSET
        else:
            amazon_rating = FieldProvider.from_dict(_amazon_rating)

        _amazon_review_count = d.pop("amazonReviewCount", UNSET)
        amazon_review_count: FieldProvider | Unset
        if isinstance(_amazon_review_count, Unset):
            amazon_review_count = UNSET
        else:
            amazon_review_count = FieldProvider.from_dict(_amazon_review_count)

        _goodreads_rating = d.pop("goodreadsRating", UNSET)
        goodreads_rating: FieldProvider | Unset
        if isinstance(_goodreads_rating, Unset):
            goodreads_rating = UNSET
        else:
            goodreads_rating = FieldProvider.from_dict(_goodreads_rating)

        _goodreads_review_count = d.pop("goodreadsReviewCount", UNSET)
        goodreads_review_count: FieldProvider | Unset
        if isinstance(_goodreads_review_count, Unset):
            goodreads_review_count = UNSET
        else:
            goodreads_review_count = FieldProvider.from_dict(_goodreads_review_count)

        _hardcover_rating = d.pop("hardcoverRating", UNSET)
        hardcover_rating: FieldProvider | Unset
        if isinstance(_hardcover_rating, Unset):
            hardcover_rating = UNSET
        else:
            hardcover_rating = FieldProvider.from_dict(_hardcover_rating)

        _hardcover_review_count = d.pop("hardcoverReviewCount", UNSET)
        hardcover_review_count: FieldProvider | Unset
        if isinstance(_hardcover_review_count, Unset):
            hardcover_review_count = UNSET
        else:
            hardcover_review_count = FieldProvider.from_dict(_hardcover_review_count)

        _lubimyczytac_rating = d.pop("lubimyczytacRating", UNSET)
        lubimyczytac_rating: FieldProvider | Unset
        if isinstance(_lubimyczytac_rating, Unset):
            lubimyczytac_rating = UNSET
        else:
            lubimyczytac_rating = FieldProvider.from_dict(_lubimyczytac_rating)

        _ranobedb_id = d.pop("ranobedbId", UNSET)
        ranobedb_id: FieldProvider | Unset
        if isinstance(_ranobedb_id, Unset):
            ranobedb_id = UNSET
        else:
            ranobedb_id = FieldProvider.from_dict(_ranobedb_id)

        _ranobedb_rating = d.pop("ranobedbRating", UNSET)
        ranobedb_rating: FieldProvider | Unset
        if isinstance(_ranobedb_rating, Unset):
            ranobedb_rating = UNSET
        else:
            ranobedb_rating = FieldProvider.from_dict(_ranobedb_rating)

        _audible_id = d.pop("audibleId", UNSET)
        audible_id: FieldProvider | Unset
        if isinstance(_audible_id, Unset):
            audible_id = UNSET
        else:
            audible_id = FieldProvider.from_dict(_audible_id)

        _audible_rating = d.pop("audibleRating", UNSET)
        audible_rating: FieldProvider | Unset
        if isinstance(_audible_rating, Unset):
            audible_rating = UNSET
        else:
            audible_rating = FieldProvider.from_dict(_audible_rating)

        _audible_review_count = d.pop("audibleReviewCount", UNSET)
        audible_review_count: FieldProvider | Unset
        if isinstance(_audible_review_count, Unset):
            audible_review_count = UNSET
        else:
            audible_review_count = FieldProvider.from_dict(_audible_review_count)

        _moods = d.pop("moods", UNSET)
        moods: FieldProvider | Unset
        if isinstance(_moods, Unset):
            moods = UNSET
        else:
            moods = FieldProvider.from_dict(_moods)

        _tags = d.pop("tags", UNSET)
        tags: FieldProvider | Unset
        if isinstance(_tags, Unset):
            tags = UNSET
        else:
            tags = FieldProvider.from_dict(_tags)

        field_options = cls(
            title=title,
            subtitle=subtitle,
            description=description,
            authors=authors,
            publisher=publisher,
            published_date=published_date,
            series_name=series_name,
            series_number=series_number,
            series_total=series_total,
            isbn13=isbn13,
            isbn10=isbn10,
            language=language,
            categories=categories,
            cover=cover,
            page_count=page_count,
            asin=asin,
            goodreads_id=goodreads_id,
            comicvine_id=comicvine_id,
            hardcover_id=hardcover_id,
            hardcover_book_id=hardcover_book_id,
            google_id=google_id,
            lubimyczytac_id=lubimyczytac_id,
            amazon_rating=amazon_rating,
            amazon_review_count=amazon_review_count,
            goodreads_rating=goodreads_rating,
            goodreads_review_count=goodreads_review_count,
            hardcover_rating=hardcover_rating,
            hardcover_review_count=hardcover_review_count,
            lubimyczytac_rating=lubimyczytac_rating,
            ranobedb_id=ranobedb_id,
            ranobedb_rating=ranobedb_rating,
            audible_id=audible_id,
            audible_rating=audible_rating,
            audible_review_count=audible_review_count,
            moods=moods,
            tags=tags,
        )

        field_options.additional_properties = d
        return field_options

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
