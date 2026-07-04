from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.svg_icon_create_request import SvgIconCreateRequest


T = TypeVar("T", bound="SvgIconBatchRequest")


@_attrs_define
class SvgIconBatchRequest:
    """
    Attributes:
        icons (list[SvgIconCreateRequest]):
    """

    icons: list[SvgIconCreateRequest]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        icons = []
        for icons_item_data in self.icons:
            icons_item = icons_item_data.to_dict()
            icons.append(icons_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "icons": icons,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.svg_icon_create_request import SvgIconCreateRequest

        d = dict(src_dict)
        icons = []
        _icons = d.pop("icons")
        for icons_item_data in _icons:
            icons_item = SvgIconCreateRequest.from_dict(icons_item_data)

            icons.append(icons_item)

        svg_icon_batch_request = cls(
            icons=icons,
        )

        svg_icon_batch_request.additional_properties = d
        return svg_icon_batch_request

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
