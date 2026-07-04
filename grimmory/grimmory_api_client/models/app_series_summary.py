from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.series_cover_book import SeriesCoverBook


T = TypeVar("T", bound="AppSeriesSummary")


@_attrs_define
class AppSeriesSummary:
    """
    Attributes:
        series_name (str | Unset):
        book_count (int | Unset):
        series_total (int | Unset):
        authors (list[str] | Unset):
        books_read (int | Unset):
        latest_added_on (datetime.datetime | Unset):
        cover_books (list[SeriesCoverBook] | Unset):
    """

    series_name: str | Unset = UNSET
    book_count: int | Unset = UNSET
    series_total: int | Unset = UNSET
    authors: list[str] | Unset = UNSET
    books_read: int | Unset = UNSET
    latest_added_on: datetime.datetime | Unset = UNSET
    cover_books: list[SeriesCoverBook] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        series_name = self.series_name

        book_count = self.book_count

        series_total = self.series_total

        authors: list[str] | Unset = UNSET
        if not isinstance(self.authors, Unset):
            authors = self.authors

        books_read = self.books_read

        latest_added_on: str | Unset = UNSET
        if not isinstance(self.latest_added_on, Unset):
            latest_added_on = self.latest_added_on.isoformat()

        cover_books: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.cover_books, Unset):
            cover_books = []
            for cover_books_item_data in self.cover_books:
                cover_books_item = cover_books_item_data.to_dict()
                cover_books.append(cover_books_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if series_name is not UNSET:
            field_dict["seriesName"] = series_name
        if book_count is not UNSET:
            field_dict["bookCount"] = book_count
        if series_total is not UNSET:
            field_dict["seriesTotal"] = series_total
        if authors is not UNSET:
            field_dict["authors"] = authors
        if books_read is not UNSET:
            field_dict["booksRead"] = books_read
        if latest_added_on is not UNSET:
            field_dict["latestAddedOn"] = latest_added_on
        if cover_books is not UNSET:
            field_dict["coverBooks"] = cover_books

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.series_cover_book import SeriesCoverBook

        d = dict(src_dict)
        series_name = d.pop("seriesName", UNSET)

        book_count = d.pop("bookCount", UNSET)

        series_total = d.pop("seriesTotal", UNSET)

        authors = cast(list[str], d.pop("authors", UNSET))

        books_read = d.pop("booksRead", UNSET)

        _latest_added_on = d.pop("latestAddedOn", UNSET)
        latest_added_on: datetime.datetime | Unset
        if isinstance(_latest_added_on, Unset):
            latest_added_on = UNSET
        else:
            latest_added_on = datetime.datetime.fromisoformat(_latest_added_on)

        _cover_books = d.pop("coverBooks", UNSET)
        cover_books: list[SeriesCoverBook] | Unset = UNSET
        if _cover_books is not UNSET:
            cover_books = []
            for cover_books_item_data in _cover_books:
                cover_books_item = SeriesCoverBook.from_dict(cover_books_item_data)

                cover_books.append(cover_books_item)

        app_series_summary = cls(
            series_name=series_name,
            book_count=book_count,
            series_total=series_total,
            authors=authors,
            books_read=books_read,
            latest_added_on=latest_added_on,
            cover_books=cover_books,
        )

        app_series_summary.additional_properties = d
        return app_series_summary

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
