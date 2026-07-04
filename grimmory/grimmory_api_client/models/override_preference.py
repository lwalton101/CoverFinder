from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.override_details import OverrideDetails


T = TypeVar("T", bound="OverridePreference")


@_attrs_define
class OverridePreference:
    """
    Attributes:
        entity_type (str | Unset):
        entity_id (int | Unset):
        preferences (OverrideDetails | Unset):
    """

    entity_type: str | Unset = UNSET
    entity_id: int | Unset = UNSET
    preferences: OverrideDetails | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        entity_type = self.entity_type

        entity_id = self.entity_id

        preferences: dict[str, Any] | Unset = UNSET
        if not isinstance(self.preferences, Unset):
            preferences = self.preferences.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if entity_type is not UNSET:
            field_dict["entityType"] = entity_type
        if entity_id is not UNSET:
            field_dict["entityId"] = entity_id
        if preferences is not UNSET:
            field_dict["preferences"] = preferences

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.override_details import OverrideDetails

        d = dict(src_dict)
        entity_type = d.pop("entityType", UNSET)

        entity_id = d.pop("entityId", UNSET)

        _preferences = d.pop("preferences", UNSET)
        preferences: OverrideDetails | Unset
        if isinstance(_preferences, Unset):
            preferences = UNSET
        else:
            preferences = OverrideDetails.from_dict(_preferences)

        override_preference = cls(
            entity_type=entity_type,
            entity_id=entity_id,
            preferences=preferences,
        )

        override_preference.additional_properties = d
        return override_preference

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
