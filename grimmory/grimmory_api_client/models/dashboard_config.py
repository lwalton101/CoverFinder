from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.scroller_config import ScrollerConfig


T = TypeVar("T", bound="DashboardConfig")


@_attrs_define
class DashboardConfig:
    """
    Attributes:
        scrollers (list[ScrollerConfig] | Unset):
    """

    scrollers: list[ScrollerConfig] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        scrollers: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.scrollers, Unset):
            scrollers = []
            for scrollers_item_data in self.scrollers:
                scrollers_item = scrollers_item_data.to_dict()
                scrollers.append(scrollers_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if scrollers is not UNSET:
            field_dict["scrollers"] = scrollers

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.scroller_config import ScrollerConfig

        d = dict(src_dict)
        _scrollers = d.pop("scrollers", UNSET)
        scrollers: list[ScrollerConfig] | Unset = UNSET
        if _scrollers is not UNSET:
            scrollers = []
            for scrollers_item_data in _scrollers:
                scrollers_item = ScrollerConfig.from_dict(scrollers_item_data)

                scrollers.append(scrollers_item)

        dashboard_config = cls(
            scrollers=scrollers,
        )

        dashboard_config.additional_properties = d
        return dashboard_config

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
