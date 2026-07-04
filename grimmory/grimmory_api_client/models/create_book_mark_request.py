from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateBookMarkRequest")


@_attrs_define
class CreateBookMarkRequest:
    """Bookmark creation request

    Attributes:
        book_id (int):
        cfi (str | Unset):
        position_ms (int | Unset):
        track_index (int | Unset):
        page_number (int | Unset):
        title (str | Unset):
        audiobook_bookmark (bool | Unset):
        pdf_bookmark (bool | Unset):
    """

    book_id: int
    cfi: str | Unset = UNSET
    position_ms: int | Unset = UNSET
    track_index: int | Unset = UNSET
    page_number: int | Unset = UNSET
    title: str | Unset = UNSET
    audiobook_bookmark: bool | Unset = UNSET
    pdf_bookmark: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        book_id = self.book_id

        cfi = self.cfi

        position_ms = self.position_ms

        track_index = self.track_index

        page_number = self.page_number

        title = self.title

        audiobook_bookmark = self.audiobook_bookmark

        pdf_bookmark = self.pdf_bookmark

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "bookId": book_id,
            }
        )
        if cfi is not UNSET:
            field_dict["cfi"] = cfi
        if position_ms is not UNSET:
            field_dict["positionMs"] = position_ms
        if track_index is not UNSET:
            field_dict["trackIndex"] = track_index
        if page_number is not UNSET:
            field_dict["pageNumber"] = page_number
        if title is not UNSET:
            field_dict["title"] = title
        if audiobook_bookmark is not UNSET:
            field_dict["audiobookBookmark"] = audiobook_bookmark
        if pdf_bookmark is not UNSET:
            field_dict["pdfBookmark"] = pdf_bookmark

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        book_id = d.pop("bookId")

        cfi = d.pop("cfi", UNSET)

        position_ms = d.pop("positionMs", UNSET)

        track_index = d.pop("trackIndex", UNSET)

        page_number = d.pop("pageNumber", UNSET)

        title = d.pop("title", UNSET)

        audiobook_bookmark = d.pop("audiobookBookmark", UNSET)

        pdf_bookmark = d.pop("pdfBookmark", UNSET)

        create_book_mark_request = cls(
            book_id=book_id,
            cfi=cfi,
            position_ms=position_ms,
            track_index=track_index,
            page_number=page_number,
            title=title,
            audiobook_bookmark=audiobook_bookmark,
            pdf_bookmark=pdf_bookmark,
        )

        create_book_mark_request.additional_properties = d
        return create_book_mark_request

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
