from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PersonalRatingUpdateResponse")


@_attrs_define
class PersonalRatingUpdateResponse:
    """
    Attributes:
        book_id (int | Unset):
        personal_rating (int | Unset):
    """

    book_id: int | Unset = UNSET
    personal_rating: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        book_id = self.book_id

        personal_rating = self.personal_rating

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if book_id is not UNSET:
            field_dict["bookId"] = book_id
        if personal_rating is not UNSET:
            field_dict["personalRating"] = personal_rating

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        book_id = d.pop("bookId", UNSET)

        personal_rating = d.pop("personalRating", UNSET)

        personal_rating_update_response = cls(
            book_id=book_id,
            personal_rating=personal_rating,
        )

        personal_rating_update_response.additional_properties = d
        return personal_rating_update_response

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
