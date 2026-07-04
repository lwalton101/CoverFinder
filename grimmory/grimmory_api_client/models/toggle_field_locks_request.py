from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.toggle_field_locks_request_field_actions import ToggleFieldLocksRequestFieldActions


T = TypeVar("T", bound="ToggleFieldLocksRequest")


@_attrs_define
class ToggleFieldLocksRequest:
    """Toggle field locks request

    Attributes:
        book_ids (list[int] | Unset):
        field_actions (ToggleFieldLocksRequestFieldActions | Unset):
    """

    book_ids: list[int] | Unset = UNSET
    field_actions: ToggleFieldLocksRequestFieldActions | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        book_ids: list[int] | Unset = UNSET
        if not isinstance(self.book_ids, Unset):
            book_ids = self.book_ids

        field_actions: dict[str, Any] | Unset = UNSET
        if not isinstance(self.field_actions, Unset):
            field_actions = self.field_actions.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if book_ids is not UNSET:
            field_dict["bookIds"] = book_ids
        if field_actions is not UNSET:
            field_dict["fieldActions"] = field_actions

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.toggle_field_locks_request_field_actions import ToggleFieldLocksRequestFieldActions

        d = dict(src_dict)
        book_ids = cast(list[int], d.pop("bookIds", UNSET))

        _field_actions = d.pop("fieldActions", UNSET)
        field_actions: ToggleFieldLocksRequestFieldActions | Unset
        if isinstance(_field_actions, Unset):
            field_actions = UNSET
        else:
            field_actions = ToggleFieldLocksRequestFieldActions.from_dict(_field_actions)

        toggle_field_locks_request = cls(
            book_ids=book_ids,
            field_actions=field_actions,
        )

        toggle_field_locks_request.additional_properties = d
        return toggle_field_locks_request

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
