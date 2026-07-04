from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.global_preferences import GlobalPreferences
    from ..models.override_preference import OverridePreference


T = TypeVar("T", bound="EntityViewPreferences")


@_attrs_define
class EntityViewPreferences:
    """
    Attributes:
        global_ (GlobalPreferences | Unset):
        overrides (list[OverridePreference] | Unset):
    """

    global_: GlobalPreferences | Unset = UNSET
    overrides: list[OverridePreference] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        global_: dict[str, Any] | Unset = UNSET
        if not isinstance(self.global_, Unset):
            global_ = self.global_.to_dict()

        overrides: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.overrides, Unset):
            overrides = []
            for overrides_item_data in self.overrides:
                overrides_item = overrides_item_data.to_dict()
                overrides.append(overrides_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if global_ is not UNSET:
            field_dict["global"] = global_
        if overrides is not UNSET:
            field_dict["overrides"] = overrides

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.global_preferences import GlobalPreferences
        from ..models.override_preference import OverridePreference

        d = dict(src_dict)
        _global_ = d.pop("global", UNSET)
        global_: GlobalPreferences | Unset
        if isinstance(_global_, Unset):
            global_ = UNSET
        else:
            global_ = GlobalPreferences.from_dict(_global_)

        _overrides = d.pop("overrides", UNSET)
        overrides: list[OverridePreference] | Unset = UNSET
        if _overrides is not UNSET:
            overrides = []
            for overrides_item_data in _overrides:
                overrides_item = OverridePreference.from_dict(overrides_item_data)

                overrides.append(overrides_item)

        entity_view_preferences = cls(
            global_=global_,
            overrides=overrides,
        )

        entity_view_preferences.additional_properties = d
        return entity_view_preferences

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
