from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.audiobook_completion_entry import AudiobookCompletionEntry


T = TypeVar("T", bound="ListeningCompletionResponse")


@_attrs_define
class ListeningCompletionResponse:
    """
    Attributes:
        total_audiobooks (int | Unset):
        completed (int | Unset):
        in_progress_count (int | Unset):
        in_progress (list[AudiobookCompletionEntry] | Unset):
    """

    total_audiobooks: int | Unset = UNSET
    completed: int | Unset = UNSET
    in_progress_count: int | Unset = UNSET
    in_progress: list[AudiobookCompletionEntry] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        total_audiobooks = self.total_audiobooks

        completed = self.completed

        in_progress_count = self.in_progress_count

        in_progress: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.in_progress, Unset):
            in_progress = []
            for in_progress_item_data in self.in_progress:
                in_progress_item = in_progress_item_data.to_dict()
                in_progress.append(in_progress_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if total_audiobooks is not UNSET:
            field_dict["totalAudiobooks"] = total_audiobooks
        if completed is not UNSET:
            field_dict["completed"] = completed
        if in_progress_count is not UNSET:
            field_dict["inProgressCount"] = in_progress_count
        if in_progress is not UNSET:
            field_dict["inProgress"] = in_progress

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.audiobook_completion_entry import AudiobookCompletionEntry

        d = dict(src_dict)
        total_audiobooks = d.pop("totalAudiobooks", UNSET)

        completed = d.pop("completed", UNSET)

        in_progress_count = d.pop("inProgressCount", UNSET)

        _in_progress = d.pop("inProgress", UNSET)
        in_progress: list[AudiobookCompletionEntry] | Unset = UNSET
        if _in_progress is not UNSET:
            in_progress = []
            for in_progress_item_data in _in_progress:
                in_progress_item = AudiobookCompletionEntry.from_dict(in_progress_item_data)

                in_progress.append(in_progress_item)

        listening_completion_response = cls(
            total_audiobooks=total_audiobooks,
            completed=completed,
            in_progress_count=in_progress_count,
            in_progress=in_progress,
        )

        listening_completion_response.additional_properties = d
        return listening_completion_response

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
