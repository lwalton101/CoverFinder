from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.content_restriction_mode import ContentRestrictionMode
from ..models.content_restriction_restriction_type import ContentRestrictionRestrictionType
from ..types import UNSET, Unset

T = TypeVar("T", bound="ContentRestriction")


@_attrs_define
class ContentRestriction:
    """Content restriction to add

    Attributes:
        id (int | Unset):
        user_id (int | Unset):
        restriction_type (ContentRestrictionRestrictionType | Unset):
        mode (ContentRestrictionMode | Unset):
        value (str | Unset):
        created_at (datetime.datetime | Unset):
    """

    id: int | Unset = UNSET
    user_id: int | Unset = UNSET
    restriction_type: ContentRestrictionRestrictionType | Unset = UNSET
    mode: ContentRestrictionMode | Unset = UNSET
    value: str | Unset = UNSET
    created_at: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        user_id = self.user_id

        restriction_type: str | Unset = UNSET
        if not isinstance(self.restriction_type, Unset):
            restriction_type = self.restriction_type.value

        mode: str | Unset = UNSET
        if not isinstance(self.mode, Unset):
            mode = self.mode.value

        value = self.value

        created_at: str | Unset = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if user_id is not UNSET:
            field_dict["userId"] = user_id
        if restriction_type is not UNSET:
            field_dict["restrictionType"] = restriction_type
        if mode is not UNSET:
            field_dict["mode"] = mode
        if value is not UNSET:
            field_dict["value"] = value
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        user_id = d.pop("userId", UNSET)

        _restriction_type = d.pop("restrictionType", UNSET)
        restriction_type: ContentRestrictionRestrictionType | Unset
        if isinstance(_restriction_type, Unset):
            restriction_type = UNSET
        else:
            restriction_type = ContentRestrictionRestrictionType(_restriction_type)

        _mode = d.pop("mode", UNSET)
        mode: ContentRestrictionMode | Unset
        if isinstance(_mode, Unset):
            mode = UNSET
        else:
            mode = ContentRestrictionMode(_mode)

        value = d.pop("value", UNSET)

        _created_at = d.pop("createdAt", UNSET)
        created_at: datetime.datetime | Unset
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = datetime.datetime.fromisoformat(_created_at)

        content_restriction = cls(
            id=id,
            user_id=user_id,
            restriction_type=restriction_type,
            mode=mode,
            value=value,
            created_at=created_at,
        )

        content_restriction.additional_properties = d
        return content_restriction

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
