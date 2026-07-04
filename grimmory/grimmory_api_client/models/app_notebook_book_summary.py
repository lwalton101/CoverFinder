from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AppNotebookBookSummary")


@_attrs_define
class AppNotebookBookSummary:
    """
    Attributes:
        book_id (int | Unset):
        book_title (str | Unset):
        note_count (int | Unset):
        authors (list[str] | Unset):
        cover_updated_on (datetime.datetime | Unset):
    """

    book_id: int | Unset = UNSET
    book_title: str | Unset = UNSET
    note_count: int | Unset = UNSET
    authors: list[str] | Unset = UNSET
    cover_updated_on: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        book_id = self.book_id

        book_title = self.book_title

        note_count = self.note_count

        authors: list[str] | Unset = UNSET
        if not isinstance(self.authors, Unset):
            authors = self.authors

        cover_updated_on: str | Unset = UNSET
        if not isinstance(self.cover_updated_on, Unset):
            cover_updated_on = self.cover_updated_on.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if book_id is not UNSET:
            field_dict["bookId"] = book_id
        if book_title is not UNSET:
            field_dict["bookTitle"] = book_title
        if note_count is not UNSET:
            field_dict["noteCount"] = note_count
        if authors is not UNSET:
            field_dict["authors"] = authors
        if cover_updated_on is not UNSET:
            field_dict["coverUpdatedOn"] = cover_updated_on

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        book_id = d.pop("bookId", UNSET)

        book_title = d.pop("bookTitle", UNSET)

        note_count = d.pop("noteCount", UNSET)

        authors = cast(list[str], d.pop("authors", UNSET))

        _cover_updated_on = d.pop("coverUpdatedOn", UNSET)
        cover_updated_on: datetime.datetime | Unset
        if isinstance(_cover_updated_on, Unset):
            cover_updated_on = UNSET
        else:
            cover_updated_on = datetime.datetime.fromisoformat(_cover_updated_on)

        app_notebook_book_summary = cls(
            book_id=book_id,
            book_title=book_title,
            note_count=note_count,
            authors=authors,
            cover_updated_on=cover_updated_on,
        )

        app_notebook_book_summary.additional_properties = d
        return app_notebook_book_summary

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
