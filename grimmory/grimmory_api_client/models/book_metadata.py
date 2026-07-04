from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.book_metadata_provider import BookMetadataProvider
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.audiobook_metadata import AudiobookMetadata
    from ..models.book_review import BookReview
    from ..models.comic_metadata import ComicMetadata


T = TypeVar("T", bound="BookMetadata")


@_attrs_define
class BookMetadata:
    """
    Attributes:
        book_id (int | Unset):
        title (str | Unset):
        subtitle (str | Unset):
        publisher (str | Unset):
        published_date (datetime.date | Unset):
        description (str | Unset):
        series_name (str | Unset):
        series_number (float | Unset):
        series_total (int | Unset):
        isbn13 (str | Unset):
        isbn10 (str | Unset):
        page_count (int | Unset):
        language (str | Unset):
        narrator (str | Unset):
        abridged (bool | Unset):
        audiobook_metadata (AudiobookMetadata | Unset):
        comic_metadata (ComicMetadata | Unset):
        asin (str | Unset):
        amazon_rating (float | Unset):
        amazon_review_count (int | Unset):
        goodreads_id (str | Unset):
        comicvine_id (str | Unset):
        goodreads_rating (float | Unset):
        goodreads_review_count (int | Unset):
        hardcover_id (str | Unset):
        hardcover_book_id (str | Unset):
        hardcover_rating (float | Unset):
        hardcover_review_count (int | Unset):
        douban_id (str | Unset):
        douban_rating (float | Unset):
        douban_review_count (int | Unset):
        lubimyczytac_rating (float | Unset):
        google_id (str | Unset):
        lubimyczytac_id (str | Unset):
        ranobedb_id (str | Unset):
        ranobedb_rating (float | Unset):
        audible_id (str | Unset):
        audible_rating (float | Unset):
        audible_review_count (int | Unset):
        external_url (str | Unset):
        cover_updated_on (datetime.datetime | Unset):
        audiobook_cover_updated_on (datetime.datetime | Unset):
        authors (list[str] | Unset):
        categories (list[str] | Unset):
        moods (list[str] | Unset):
        tags (list[str] | Unset):
        provider (BookMetadataProvider | Unset):
        thumbnail_url (str | Unset):
        book_reviews (list[BookReview] | Unset):
        rating (float | Unset):
        is_fixed_layout (bool | Unset):
        all_metadata_locked (bool | Unset):
        title_locked (bool | Unset):
        subtitle_locked (bool | Unset):
        publisher_locked (bool | Unset):
        published_date_locked (bool | Unset):
        description_locked (bool | Unset):
        series_name_locked (bool | Unset):
        series_number_locked (bool | Unset):
        series_total_locked (bool | Unset):
        isbn_13_locked (bool | Unset):
        isbn_10_locked (bool | Unset):
        asin_locked (bool | Unset):
        goodreads_id_locked (bool | Unset):
        comicvine_id_locked (bool | Unset):
        hardcover_id_locked (bool | Unset):
        hardcover_book_id_locked (bool | Unset):
        douban_id_locked (bool | Unset):
        google_id_locked (bool | Unset):
        page_count_locked (bool | Unset):
        language_locked (bool | Unset):
        amazon_rating_locked (bool | Unset):
        amazon_review_count_locked (bool | Unset):
        goodreads_rating_locked (bool | Unset):
        goodreads_review_count_locked (bool | Unset):
        hardcover_rating_locked (bool | Unset):
        hardcover_review_count_locked (bool | Unset):
        douban_rating_locked (bool | Unset):
        douban_review_count_locked (bool | Unset):
        lubimyczytac_id_locked (bool | Unset):
        lubimyczytac_rating_locked (bool | Unset):
        ranobedb_id_locked (bool | Unset):
        ranobedb_rating_locked (bool | Unset):
        audible_id_locked (bool | Unset):
        audible_rating_locked (bool | Unset):
        audible_review_count_locked (bool | Unset):
        external_url_locked (bool | Unset):
        cover_locked (bool | Unset):
        audiobook_cover_locked (bool | Unset):
        authors_locked (bool | Unset):
        categories_locked (bool | Unset):
        moods_locked (bool | Unset):
        tags_locked (bool | Unset):
        reviews_locked (bool | Unset):
        narrator_locked (bool | Unset):
        abridged_locked (bool | Unset):
        age_rating (int | Unset):
        content_rating (str | Unset):
        age_rating_locked (bool | Unset):
        content_rating_locked (bool | Unset):
    """

    book_id: int | Unset = UNSET
    title: str | Unset = UNSET
    subtitle: str | Unset = UNSET
    publisher: str | Unset = UNSET
    published_date: datetime.date | Unset = UNSET
    description: str | Unset = UNSET
    series_name: str | Unset = UNSET
    series_number: float | Unset = UNSET
    series_total: int | Unset = UNSET
    isbn13: str | Unset = UNSET
    isbn10: str | Unset = UNSET
    page_count: int | Unset = UNSET
    language: str | Unset = UNSET
    narrator: str | Unset = UNSET
    abridged: bool | Unset = UNSET
    audiobook_metadata: AudiobookMetadata | Unset = UNSET
    comic_metadata: ComicMetadata | Unset = UNSET
    asin: str | Unset = UNSET
    amazon_rating: float | Unset = UNSET
    amazon_review_count: int | Unset = UNSET
    goodreads_id: str | Unset = UNSET
    comicvine_id: str | Unset = UNSET
    goodreads_rating: float | Unset = UNSET
    goodreads_review_count: int | Unset = UNSET
    hardcover_id: str | Unset = UNSET
    hardcover_book_id: str | Unset = UNSET
    hardcover_rating: float | Unset = UNSET
    hardcover_review_count: int | Unset = UNSET
    douban_id: str | Unset = UNSET
    douban_rating: float | Unset = UNSET
    douban_review_count: int | Unset = UNSET
    lubimyczytac_rating: float | Unset = UNSET
    google_id: str | Unset = UNSET
    lubimyczytac_id: str | Unset = UNSET
    ranobedb_id: str | Unset = UNSET
    ranobedb_rating: float | Unset = UNSET
    audible_id: str | Unset = UNSET
    audible_rating: float | Unset = UNSET
    audible_review_count: int | Unset = UNSET
    external_url: str | Unset = UNSET
    cover_updated_on: datetime.datetime | Unset = UNSET
    audiobook_cover_updated_on: datetime.datetime | Unset = UNSET
    authors: list[str] | Unset = UNSET
    categories: list[str] | Unset = UNSET
    moods: list[str] | Unset = UNSET
    tags: list[str] | Unset = UNSET
    provider: BookMetadataProvider | Unset = UNSET
    thumbnail_url: str | Unset = UNSET
    book_reviews: list[BookReview] | Unset = UNSET
    rating: float | Unset = UNSET
    is_fixed_layout: bool | Unset = UNSET
    all_metadata_locked: bool | Unset = UNSET
    title_locked: bool | Unset = UNSET
    subtitle_locked: bool | Unset = UNSET
    publisher_locked: bool | Unset = UNSET
    published_date_locked: bool | Unset = UNSET
    description_locked: bool | Unset = UNSET
    series_name_locked: bool | Unset = UNSET
    series_number_locked: bool | Unset = UNSET
    series_total_locked: bool | Unset = UNSET
    isbn_13_locked: bool | Unset = UNSET
    isbn_10_locked: bool | Unset = UNSET
    asin_locked: bool | Unset = UNSET
    goodreads_id_locked: bool | Unset = UNSET
    comicvine_id_locked: bool | Unset = UNSET
    hardcover_id_locked: bool | Unset = UNSET
    hardcover_book_id_locked: bool | Unset = UNSET
    douban_id_locked: bool | Unset = UNSET
    google_id_locked: bool | Unset = UNSET
    page_count_locked: bool | Unset = UNSET
    language_locked: bool | Unset = UNSET
    amazon_rating_locked: bool | Unset = UNSET
    amazon_review_count_locked: bool | Unset = UNSET
    goodreads_rating_locked: bool | Unset = UNSET
    goodreads_review_count_locked: bool | Unset = UNSET
    hardcover_rating_locked: bool | Unset = UNSET
    hardcover_review_count_locked: bool | Unset = UNSET
    douban_rating_locked: bool | Unset = UNSET
    douban_review_count_locked: bool | Unset = UNSET
    lubimyczytac_id_locked: bool | Unset = UNSET
    lubimyczytac_rating_locked: bool | Unset = UNSET
    ranobedb_id_locked: bool | Unset = UNSET
    ranobedb_rating_locked: bool | Unset = UNSET
    audible_id_locked: bool | Unset = UNSET
    audible_rating_locked: bool | Unset = UNSET
    audible_review_count_locked: bool | Unset = UNSET
    external_url_locked: bool | Unset = UNSET
    cover_locked: bool | Unset = UNSET
    audiobook_cover_locked: bool | Unset = UNSET
    authors_locked: bool | Unset = UNSET
    categories_locked: bool | Unset = UNSET
    moods_locked: bool | Unset = UNSET
    tags_locked: bool | Unset = UNSET
    reviews_locked: bool | Unset = UNSET
    narrator_locked: bool | Unset = UNSET
    abridged_locked: bool | Unset = UNSET
    age_rating: int | Unset = UNSET
    content_rating: str | Unset = UNSET
    age_rating_locked: bool | Unset = UNSET
    content_rating_locked: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        book_id = self.book_id

        title = self.title

        subtitle = self.subtitle

        publisher = self.publisher

        published_date: str | Unset = UNSET
        if not isinstance(self.published_date, Unset):
            published_date = self.published_date.isoformat()

        description = self.description

        series_name = self.series_name

        series_number = self.series_number

        series_total = self.series_total

        isbn13 = self.isbn13

        isbn10 = self.isbn10

        page_count = self.page_count

        language = self.language

        narrator = self.narrator

        abridged = self.abridged

        audiobook_metadata: dict[str, Any] | Unset = UNSET
        if not isinstance(self.audiobook_metadata, Unset):
            audiobook_metadata = self.audiobook_metadata.to_dict()

        comic_metadata: dict[str, Any] | Unset = UNSET
        if not isinstance(self.comic_metadata, Unset):
            comic_metadata = self.comic_metadata.to_dict()

        asin = self.asin

        amazon_rating = self.amazon_rating

        amazon_review_count = self.amazon_review_count

        goodreads_id = self.goodreads_id

        comicvine_id = self.comicvine_id

        goodreads_rating = self.goodreads_rating

        goodreads_review_count = self.goodreads_review_count

        hardcover_id = self.hardcover_id

        hardcover_book_id = self.hardcover_book_id

        hardcover_rating = self.hardcover_rating

        hardcover_review_count = self.hardcover_review_count

        douban_id = self.douban_id

        douban_rating = self.douban_rating

        douban_review_count = self.douban_review_count

        lubimyczytac_rating = self.lubimyczytac_rating

        google_id = self.google_id

        lubimyczytac_id = self.lubimyczytac_id

        ranobedb_id = self.ranobedb_id

        ranobedb_rating = self.ranobedb_rating

        audible_id = self.audible_id

        audible_rating = self.audible_rating

        audible_review_count = self.audible_review_count

        external_url = self.external_url

        cover_updated_on: str | Unset = UNSET
        if not isinstance(self.cover_updated_on, Unset):
            cover_updated_on = self.cover_updated_on.isoformat()

        audiobook_cover_updated_on: str | Unset = UNSET
        if not isinstance(self.audiobook_cover_updated_on, Unset):
            audiobook_cover_updated_on = self.audiobook_cover_updated_on.isoformat()

        authors: list[str] | Unset = UNSET
        if not isinstance(self.authors, Unset):
            authors = self.authors

        categories: list[str] | Unset = UNSET
        if not isinstance(self.categories, Unset):
            categories = self.categories

        moods: list[str] | Unset = UNSET
        if not isinstance(self.moods, Unset):
            moods = self.moods

        tags: list[str] | Unset = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags

        provider: str | Unset = UNSET
        if not isinstance(self.provider, Unset):
            provider = self.provider.value

        thumbnail_url = self.thumbnail_url

        book_reviews: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.book_reviews, Unset):
            book_reviews = []
            for book_reviews_item_data in self.book_reviews:
                book_reviews_item = book_reviews_item_data.to_dict()
                book_reviews.append(book_reviews_item)

        rating = self.rating

        is_fixed_layout = self.is_fixed_layout

        all_metadata_locked = self.all_metadata_locked

        title_locked = self.title_locked

        subtitle_locked = self.subtitle_locked

        publisher_locked = self.publisher_locked

        published_date_locked = self.published_date_locked

        description_locked = self.description_locked

        series_name_locked = self.series_name_locked

        series_number_locked = self.series_number_locked

        series_total_locked = self.series_total_locked

        isbn_13_locked = self.isbn_13_locked

        isbn_10_locked = self.isbn_10_locked

        asin_locked = self.asin_locked

        goodreads_id_locked = self.goodreads_id_locked

        comicvine_id_locked = self.comicvine_id_locked

        hardcover_id_locked = self.hardcover_id_locked

        hardcover_book_id_locked = self.hardcover_book_id_locked

        douban_id_locked = self.douban_id_locked

        google_id_locked = self.google_id_locked

        page_count_locked = self.page_count_locked

        language_locked = self.language_locked

        amazon_rating_locked = self.amazon_rating_locked

        amazon_review_count_locked = self.amazon_review_count_locked

        goodreads_rating_locked = self.goodreads_rating_locked

        goodreads_review_count_locked = self.goodreads_review_count_locked

        hardcover_rating_locked = self.hardcover_rating_locked

        hardcover_review_count_locked = self.hardcover_review_count_locked

        douban_rating_locked = self.douban_rating_locked

        douban_review_count_locked = self.douban_review_count_locked

        lubimyczytac_id_locked = self.lubimyczytac_id_locked

        lubimyczytac_rating_locked = self.lubimyczytac_rating_locked

        ranobedb_id_locked = self.ranobedb_id_locked

        ranobedb_rating_locked = self.ranobedb_rating_locked

        audible_id_locked = self.audible_id_locked

        audible_rating_locked = self.audible_rating_locked

        audible_review_count_locked = self.audible_review_count_locked

        external_url_locked = self.external_url_locked

        cover_locked = self.cover_locked

        audiobook_cover_locked = self.audiobook_cover_locked

        authors_locked = self.authors_locked

        categories_locked = self.categories_locked

        moods_locked = self.moods_locked

        tags_locked = self.tags_locked

        reviews_locked = self.reviews_locked

        narrator_locked = self.narrator_locked

        abridged_locked = self.abridged_locked

        age_rating = self.age_rating

        content_rating = self.content_rating

        age_rating_locked = self.age_rating_locked

        content_rating_locked = self.content_rating_locked

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if book_id is not UNSET:
            field_dict["bookId"] = book_id
        if title is not UNSET:
            field_dict["title"] = title
        if subtitle is not UNSET:
            field_dict["subtitle"] = subtitle
        if publisher is not UNSET:
            field_dict["publisher"] = publisher
        if published_date is not UNSET:
            field_dict["publishedDate"] = published_date
        if description is not UNSET:
            field_dict["description"] = description
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
        if page_count is not UNSET:
            field_dict["pageCount"] = page_count
        if language is not UNSET:
            field_dict["language"] = language
        if narrator is not UNSET:
            field_dict["narrator"] = narrator
        if abridged is not UNSET:
            field_dict["abridged"] = abridged
        if audiobook_metadata is not UNSET:
            field_dict["audiobookMetadata"] = audiobook_metadata
        if comic_metadata is not UNSET:
            field_dict["comicMetadata"] = comic_metadata
        if asin is not UNSET:
            field_dict["asin"] = asin
        if amazon_rating is not UNSET:
            field_dict["amazonRating"] = amazon_rating
        if amazon_review_count is not UNSET:
            field_dict["amazonReviewCount"] = amazon_review_count
        if goodreads_id is not UNSET:
            field_dict["goodreadsId"] = goodreads_id
        if comicvine_id is not UNSET:
            field_dict["comicvineId"] = comicvine_id
        if goodreads_rating is not UNSET:
            field_dict["goodreadsRating"] = goodreads_rating
        if goodreads_review_count is not UNSET:
            field_dict["goodreadsReviewCount"] = goodreads_review_count
        if hardcover_id is not UNSET:
            field_dict["hardcoverId"] = hardcover_id
        if hardcover_book_id is not UNSET:
            field_dict["hardcoverBookId"] = hardcover_book_id
        if hardcover_rating is not UNSET:
            field_dict["hardcoverRating"] = hardcover_rating
        if hardcover_review_count is not UNSET:
            field_dict["hardcoverReviewCount"] = hardcover_review_count
        if douban_id is not UNSET:
            field_dict["doubanId"] = douban_id
        if douban_rating is not UNSET:
            field_dict["doubanRating"] = douban_rating
        if douban_review_count is not UNSET:
            field_dict["doubanReviewCount"] = douban_review_count
        if lubimyczytac_rating is not UNSET:
            field_dict["lubimyczytacRating"] = lubimyczytac_rating
        if google_id is not UNSET:
            field_dict["googleId"] = google_id
        if lubimyczytac_id is not UNSET:
            field_dict["lubimyczytacId"] = lubimyczytac_id
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
        if external_url is not UNSET:
            field_dict["externalUrl"] = external_url
        if cover_updated_on is not UNSET:
            field_dict["coverUpdatedOn"] = cover_updated_on
        if audiobook_cover_updated_on is not UNSET:
            field_dict["audiobookCoverUpdatedOn"] = audiobook_cover_updated_on
        if authors is not UNSET:
            field_dict["authors"] = authors
        if categories is not UNSET:
            field_dict["categories"] = categories
        if moods is not UNSET:
            field_dict["moods"] = moods
        if tags is not UNSET:
            field_dict["tags"] = tags
        if provider is not UNSET:
            field_dict["provider"] = provider
        if thumbnail_url is not UNSET:
            field_dict["thumbnailUrl"] = thumbnail_url
        if book_reviews is not UNSET:
            field_dict["bookReviews"] = book_reviews
        if rating is not UNSET:
            field_dict["rating"] = rating
        if is_fixed_layout is not UNSET:
            field_dict["isFixedLayout"] = is_fixed_layout
        if all_metadata_locked is not UNSET:
            field_dict["allMetadataLocked"] = all_metadata_locked
        if title_locked is not UNSET:
            field_dict["titleLocked"] = title_locked
        if subtitle_locked is not UNSET:
            field_dict["subtitleLocked"] = subtitle_locked
        if publisher_locked is not UNSET:
            field_dict["publisherLocked"] = publisher_locked
        if published_date_locked is not UNSET:
            field_dict["publishedDateLocked"] = published_date_locked
        if description_locked is not UNSET:
            field_dict["descriptionLocked"] = description_locked
        if series_name_locked is not UNSET:
            field_dict["seriesNameLocked"] = series_name_locked
        if series_number_locked is not UNSET:
            field_dict["seriesNumberLocked"] = series_number_locked
        if series_total_locked is not UNSET:
            field_dict["seriesTotalLocked"] = series_total_locked
        if isbn_13_locked is not UNSET:
            field_dict["isbn13Locked"] = isbn_13_locked
        if isbn_10_locked is not UNSET:
            field_dict["isbn10Locked"] = isbn_10_locked
        if asin_locked is not UNSET:
            field_dict["asinLocked"] = asin_locked
        if goodreads_id_locked is not UNSET:
            field_dict["goodreadsIdLocked"] = goodreads_id_locked
        if comicvine_id_locked is not UNSET:
            field_dict["comicvineIdLocked"] = comicvine_id_locked
        if hardcover_id_locked is not UNSET:
            field_dict["hardcoverIdLocked"] = hardcover_id_locked
        if hardcover_book_id_locked is not UNSET:
            field_dict["hardcoverBookIdLocked"] = hardcover_book_id_locked
        if douban_id_locked is not UNSET:
            field_dict["doubanIdLocked"] = douban_id_locked
        if google_id_locked is not UNSET:
            field_dict["googleIdLocked"] = google_id_locked
        if page_count_locked is not UNSET:
            field_dict["pageCountLocked"] = page_count_locked
        if language_locked is not UNSET:
            field_dict["languageLocked"] = language_locked
        if amazon_rating_locked is not UNSET:
            field_dict["amazonRatingLocked"] = amazon_rating_locked
        if amazon_review_count_locked is not UNSET:
            field_dict["amazonReviewCountLocked"] = amazon_review_count_locked
        if goodreads_rating_locked is not UNSET:
            field_dict["goodreadsRatingLocked"] = goodreads_rating_locked
        if goodreads_review_count_locked is not UNSET:
            field_dict["goodreadsReviewCountLocked"] = goodreads_review_count_locked
        if hardcover_rating_locked is not UNSET:
            field_dict["hardcoverRatingLocked"] = hardcover_rating_locked
        if hardcover_review_count_locked is not UNSET:
            field_dict["hardcoverReviewCountLocked"] = hardcover_review_count_locked
        if douban_rating_locked is not UNSET:
            field_dict["doubanRatingLocked"] = douban_rating_locked
        if douban_review_count_locked is not UNSET:
            field_dict["doubanReviewCountLocked"] = douban_review_count_locked
        if lubimyczytac_id_locked is not UNSET:
            field_dict["lubimyczytacIdLocked"] = lubimyczytac_id_locked
        if lubimyczytac_rating_locked is not UNSET:
            field_dict["lubimyczytacRatingLocked"] = lubimyczytac_rating_locked
        if ranobedb_id_locked is not UNSET:
            field_dict["ranobedbIdLocked"] = ranobedb_id_locked
        if ranobedb_rating_locked is not UNSET:
            field_dict["ranobedbRatingLocked"] = ranobedb_rating_locked
        if audible_id_locked is not UNSET:
            field_dict["audibleIdLocked"] = audible_id_locked
        if audible_rating_locked is not UNSET:
            field_dict["audibleRatingLocked"] = audible_rating_locked
        if audible_review_count_locked is not UNSET:
            field_dict["audibleReviewCountLocked"] = audible_review_count_locked
        if external_url_locked is not UNSET:
            field_dict["externalUrlLocked"] = external_url_locked
        if cover_locked is not UNSET:
            field_dict["coverLocked"] = cover_locked
        if audiobook_cover_locked is not UNSET:
            field_dict["audiobookCoverLocked"] = audiobook_cover_locked
        if authors_locked is not UNSET:
            field_dict["authorsLocked"] = authors_locked
        if categories_locked is not UNSET:
            field_dict["categoriesLocked"] = categories_locked
        if moods_locked is not UNSET:
            field_dict["moodsLocked"] = moods_locked
        if tags_locked is not UNSET:
            field_dict["tagsLocked"] = tags_locked
        if reviews_locked is not UNSET:
            field_dict["reviewsLocked"] = reviews_locked
        if narrator_locked is not UNSET:
            field_dict["narratorLocked"] = narrator_locked
        if abridged_locked is not UNSET:
            field_dict["abridgedLocked"] = abridged_locked
        if age_rating is not UNSET:
            field_dict["ageRating"] = age_rating
        if content_rating is not UNSET:
            field_dict["contentRating"] = content_rating
        if age_rating_locked is not UNSET:
            field_dict["ageRatingLocked"] = age_rating_locked
        if content_rating_locked is not UNSET:
            field_dict["contentRatingLocked"] = content_rating_locked

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.audiobook_metadata import AudiobookMetadata
        from ..models.book_review import BookReview
        from ..models.comic_metadata import ComicMetadata

        d = dict(src_dict)
        book_id = d.pop("bookId", UNSET)

        title = d.pop("title", UNSET)

        subtitle = d.pop("subtitle", UNSET)

        publisher = d.pop("publisher", UNSET)

        _published_date = d.pop("publishedDate", UNSET)
        published_date: datetime.date | Unset
        if isinstance(_published_date, Unset):
            published_date = UNSET
        else:
            published_date = datetime.date.fromisoformat(_published_date)

        description = d.pop("description", UNSET)

        series_name = d.pop("seriesName", UNSET)

        series_number = d.pop("seriesNumber", UNSET)

        series_total = d.pop("seriesTotal", UNSET)

        isbn13 = d.pop("isbn13", UNSET)

        isbn10 = d.pop("isbn10", UNSET)

        page_count = d.pop("pageCount", UNSET)

        language = d.pop("language", UNSET)

        narrator = d.pop("narrator", UNSET)

        abridged = d.pop("abridged", UNSET)

        _audiobook_metadata = d.pop("audiobookMetadata", UNSET)
        audiobook_metadata: AudiobookMetadata | Unset
        if isinstance(_audiobook_metadata, Unset):
            audiobook_metadata = UNSET
        else:
            audiobook_metadata = AudiobookMetadata.from_dict(_audiobook_metadata)

        _comic_metadata = d.pop("comicMetadata", UNSET)
        comic_metadata: ComicMetadata | Unset
        if isinstance(_comic_metadata, Unset):
            comic_metadata = UNSET
        else:
            comic_metadata = ComicMetadata.from_dict(_comic_metadata)

        asin = d.pop("asin", UNSET)

        amazon_rating = d.pop("amazonRating", UNSET)

        amazon_review_count = d.pop("amazonReviewCount", UNSET)

        goodreads_id = d.pop("goodreadsId", UNSET)

        comicvine_id = d.pop("comicvineId", UNSET)

        goodreads_rating = d.pop("goodreadsRating", UNSET)

        goodreads_review_count = d.pop("goodreadsReviewCount", UNSET)

        hardcover_id = d.pop("hardcoverId", UNSET)

        hardcover_book_id = d.pop("hardcoverBookId", UNSET)

        hardcover_rating = d.pop("hardcoverRating", UNSET)

        hardcover_review_count = d.pop("hardcoverReviewCount", UNSET)

        douban_id = d.pop("doubanId", UNSET)

        douban_rating = d.pop("doubanRating", UNSET)

        douban_review_count = d.pop("doubanReviewCount", UNSET)

        lubimyczytac_rating = d.pop("lubimyczytacRating", UNSET)

        google_id = d.pop("googleId", UNSET)

        lubimyczytac_id = d.pop("lubimyczytacId", UNSET)

        ranobedb_id = d.pop("ranobedbId", UNSET)

        ranobedb_rating = d.pop("ranobedbRating", UNSET)

        audible_id = d.pop("audibleId", UNSET)

        audible_rating = d.pop("audibleRating", UNSET)

        audible_review_count = d.pop("audibleReviewCount", UNSET)

        external_url = d.pop("externalUrl", UNSET)

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

        authors = cast(list[str], d.pop("authors", UNSET))

        categories = cast(list[str], d.pop("categories", UNSET))

        moods = cast(list[str], d.pop("moods", UNSET))

        tags = cast(list[str], d.pop("tags", UNSET))

        _provider = d.pop("provider", UNSET)
        provider: BookMetadataProvider | Unset
        if isinstance(_provider, Unset):
            provider = UNSET
        else:
            provider = BookMetadataProvider(_provider)

        thumbnail_url = d.pop("thumbnailUrl", UNSET)

        _book_reviews = d.pop("bookReviews", UNSET)
        book_reviews: list[BookReview] | Unset = UNSET
        if _book_reviews is not UNSET:
            book_reviews = []
            for book_reviews_item_data in _book_reviews:
                book_reviews_item = BookReview.from_dict(book_reviews_item_data)

                book_reviews.append(book_reviews_item)

        rating = d.pop("rating", UNSET)

        is_fixed_layout = d.pop("isFixedLayout", UNSET)

        all_metadata_locked = d.pop("allMetadataLocked", UNSET)

        title_locked = d.pop("titleLocked", UNSET)

        subtitle_locked = d.pop("subtitleLocked", UNSET)

        publisher_locked = d.pop("publisherLocked", UNSET)

        published_date_locked = d.pop("publishedDateLocked", UNSET)

        description_locked = d.pop("descriptionLocked", UNSET)

        series_name_locked = d.pop("seriesNameLocked", UNSET)

        series_number_locked = d.pop("seriesNumberLocked", UNSET)

        series_total_locked = d.pop("seriesTotalLocked", UNSET)

        isbn_13_locked = d.pop("isbn13Locked", UNSET)

        isbn_10_locked = d.pop("isbn10Locked", UNSET)

        asin_locked = d.pop("asinLocked", UNSET)

        goodreads_id_locked = d.pop("goodreadsIdLocked", UNSET)

        comicvine_id_locked = d.pop("comicvineIdLocked", UNSET)

        hardcover_id_locked = d.pop("hardcoverIdLocked", UNSET)

        hardcover_book_id_locked = d.pop("hardcoverBookIdLocked", UNSET)

        douban_id_locked = d.pop("doubanIdLocked", UNSET)

        google_id_locked = d.pop("googleIdLocked", UNSET)

        page_count_locked = d.pop("pageCountLocked", UNSET)

        language_locked = d.pop("languageLocked", UNSET)

        amazon_rating_locked = d.pop("amazonRatingLocked", UNSET)

        amazon_review_count_locked = d.pop("amazonReviewCountLocked", UNSET)

        goodreads_rating_locked = d.pop("goodreadsRatingLocked", UNSET)

        goodreads_review_count_locked = d.pop("goodreadsReviewCountLocked", UNSET)

        hardcover_rating_locked = d.pop("hardcoverRatingLocked", UNSET)

        hardcover_review_count_locked = d.pop("hardcoverReviewCountLocked", UNSET)

        douban_rating_locked = d.pop("doubanRatingLocked", UNSET)

        douban_review_count_locked = d.pop("doubanReviewCountLocked", UNSET)

        lubimyczytac_id_locked = d.pop("lubimyczytacIdLocked", UNSET)

        lubimyczytac_rating_locked = d.pop("lubimyczytacRatingLocked", UNSET)

        ranobedb_id_locked = d.pop("ranobedbIdLocked", UNSET)

        ranobedb_rating_locked = d.pop("ranobedbRatingLocked", UNSET)

        audible_id_locked = d.pop("audibleIdLocked", UNSET)

        audible_rating_locked = d.pop("audibleRatingLocked", UNSET)

        audible_review_count_locked = d.pop("audibleReviewCountLocked", UNSET)

        external_url_locked = d.pop("externalUrlLocked", UNSET)

        cover_locked = d.pop("coverLocked", UNSET)

        audiobook_cover_locked = d.pop("audiobookCoverLocked", UNSET)

        authors_locked = d.pop("authorsLocked", UNSET)

        categories_locked = d.pop("categoriesLocked", UNSET)

        moods_locked = d.pop("moodsLocked", UNSET)

        tags_locked = d.pop("tagsLocked", UNSET)

        reviews_locked = d.pop("reviewsLocked", UNSET)

        narrator_locked = d.pop("narratorLocked", UNSET)

        abridged_locked = d.pop("abridgedLocked", UNSET)

        age_rating = d.pop("ageRating", UNSET)

        content_rating = d.pop("contentRating", UNSET)

        age_rating_locked = d.pop("ageRatingLocked", UNSET)

        content_rating_locked = d.pop("contentRatingLocked", UNSET)

        book_metadata = cls(
            book_id=book_id,
            title=title,
            subtitle=subtitle,
            publisher=publisher,
            published_date=published_date,
            description=description,
            series_name=series_name,
            series_number=series_number,
            series_total=series_total,
            isbn13=isbn13,
            isbn10=isbn10,
            page_count=page_count,
            language=language,
            narrator=narrator,
            abridged=abridged,
            audiobook_metadata=audiobook_metadata,
            comic_metadata=comic_metadata,
            asin=asin,
            amazon_rating=amazon_rating,
            amazon_review_count=amazon_review_count,
            goodreads_id=goodreads_id,
            comicvine_id=comicvine_id,
            goodreads_rating=goodreads_rating,
            goodreads_review_count=goodreads_review_count,
            hardcover_id=hardcover_id,
            hardcover_book_id=hardcover_book_id,
            hardcover_rating=hardcover_rating,
            hardcover_review_count=hardcover_review_count,
            douban_id=douban_id,
            douban_rating=douban_rating,
            douban_review_count=douban_review_count,
            lubimyczytac_rating=lubimyczytac_rating,
            google_id=google_id,
            lubimyczytac_id=lubimyczytac_id,
            ranobedb_id=ranobedb_id,
            ranobedb_rating=ranobedb_rating,
            audible_id=audible_id,
            audible_rating=audible_rating,
            audible_review_count=audible_review_count,
            external_url=external_url,
            cover_updated_on=cover_updated_on,
            audiobook_cover_updated_on=audiobook_cover_updated_on,
            authors=authors,
            categories=categories,
            moods=moods,
            tags=tags,
            provider=provider,
            thumbnail_url=thumbnail_url,
            book_reviews=book_reviews,
            rating=rating,
            is_fixed_layout=is_fixed_layout,
            all_metadata_locked=all_metadata_locked,
            title_locked=title_locked,
            subtitle_locked=subtitle_locked,
            publisher_locked=publisher_locked,
            published_date_locked=published_date_locked,
            description_locked=description_locked,
            series_name_locked=series_name_locked,
            series_number_locked=series_number_locked,
            series_total_locked=series_total_locked,
            isbn_13_locked=isbn_13_locked,
            isbn_10_locked=isbn_10_locked,
            asin_locked=asin_locked,
            goodreads_id_locked=goodreads_id_locked,
            comicvine_id_locked=comicvine_id_locked,
            hardcover_id_locked=hardcover_id_locked,
            hardcover_book_id_locked=hardcover_book_id_locked,
            douban_id_locked=douban_id_locked,
            google_id_locked=google_id_locked,
            page_count_locked=page_count_locked,
            language_locked=language_locked,
            amazon_rating_locked=amazon_rating_locked,
            amazon_review_count_locked=amazon_review_count_locked,
            goodreads_rating_locked=goodreads_rating_locked,
            goodreads_review_count_locked=goodreads_review_count_locked,
            hardcover_rating_locked=hardcover_rating_locked,
            hardcover_review_count_locked=hardcover_review_count_locked,
            douban_rating_locked=douban_rating_locked,
            douban_review_count_locked=douban_review_count_locked,
            lubimyczytac_id_locked=lubimyczytac_id_locked,
            lubimyczytac_rating_locked=lubimyczytac_rating_locked,
            ranobedb_id_locked=ranobedb_id_locked,
            ranobedb_rating_locked=ranobedb_rating_locked,
            audible_id_locked=audible_id_locked,
            audible_rating_locked=audible_rating_locked,
            audible_review_count_locked=audible_review_count_locked,
            external_url_locked=external_url_locked,
            cover_locked=cover_locked,
            audiobook_cover_locked=audiobook_cover_locked,
            authors_locked=authors_locked,
            categories_locked=categories_locked,
            moods_locked=moods_locked,
            tags_locked=tags_locked,
            reviews_locked=reviews_locked,
            narrator_locked=narrator_locked,
            abridged_locked=abridged_locked,
            age_rating=age_rating,
            content_rating=content_rating,
            age_rating_locked=age_rating_locked,
            content_rating_locked=content_rating_locked,
        )

        book_metadata.additional_properties = d
        return book_metadata

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
