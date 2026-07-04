from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.kobo_reading_state import KoboReadingState


T = TypeVar("T", bound="KoboReadingStateRequest")


@_attrs_define
class KoboReadingStateRequest:
    """Reading state update body

    Attributes:
        reading_states (list[KoboReadingState] | Unset):
    """

    reading_states: list[KoboReadingState] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        reading_states: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.reading_states, Unset):
            reading_states = []
            for reading_states_item_data in self.reading_states:
                reading_states_item = reading_states_item_data.to_dict()
                reading_states.append(reading_states_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if reading_states is not UNSET:
            field_dict["readingStates"] = reading_states

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.kobo_reading_state import KoboReadingState

        d = dict(src_dict)
        _reading_states = d.pop("readingStates", UNSET)
        reading_states: list[KoboReadingState] | Unset = UNSET
        if _reading_states is not UNSET:
            reading_states = []
            for reading_states_item_data in _reading_states:
                reading_states_item = KoboReadingState.from_dict(reading_states_item_data)

                reading_states.append(reading_states_item)

        kobo_reading_state_request = cls(
            reading_states=reading_states,
        )

        kobo_reading_state_request.additional_properties = d
        return kobo_reading_state_request

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
