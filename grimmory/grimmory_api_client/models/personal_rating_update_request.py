from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PersonalRatingUpdateRequest")


@_attrs_define
class PersonalRatingUpdateRequest:
    """Personal rating update request

    Attributes:
        ids (list[int] | Unset):
        rating (int | Unset):
    """

    ids: list[int] | Unset = UNSET
    rating: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ids: list[int] | Unset = UNSET
        if not isinstance(self.ids, Unset):
            ids = self.ids

        rating = self.rating

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ids is not UNSET:
            field_dict["ids"] = ids
        if rating is not UNSET:
            field_dict["rating"] = rating

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        ids = cast(list[int], d.pop("ids", UNSET))

        rating = d.pop("rating", UNSET)

        personal_rating_update_request = cls(
            ids=ids,
            rating=rating,
        )

        personal_rating_update_request.additional_properties = d
        return personal_rating_update_request

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
