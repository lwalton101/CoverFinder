from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.metadata_fetch_task_status import MetadataFetchTaskStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.fetched_proposal import FetchedProposal


T = TypeVar("T", bound="MetadataFetchTask")


@_attrs_define
class MetadataFetchTask:
    """
    Attributes:
        id (str | Unset):
        status (MetadataFetchTaskStatus | Unset):
        completed (int | Unset):
        total_books (int | Unset):
        started_at (datetime.datetime | Unset):
        completed_at (datetime.datetime | Unset):
        initiated_by (int | Unset):
        proposals (list[FetchedProposal] | Unset):
    """

    id: str | Unset = UNSET
    status: MetadataFetchTaskStatus | Unset = UNSET
    completed: int | Unset = UNSET
    total_books: int | Unset = UNSET
    started_at: datetime.datetime | Unset = UNSET
    completed_at: datetime.datetime | Unset = UNSET
    initiated_by: int | Unset = UNSET
    proposals: list[FetchedProposal] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        completed = self.completed

        total_books = self.total_books

        started_at: str | Unset = UNSET
        if not isinstance(self.started_at, Unset):
            started_at = self.started_at.isoformat()

        completed_at: str | Unset = UNSET
        if not isinstance(self.completed_at, Unset):
            completed_at = self.completed_at.isoformat()

        initiated_by = self.initiated_by

        proposals: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.proposals, Unset):
            proposals = []
            for proposals_item_data in self.proposals:
                proposals_item = proposals_item_data.to_dict()
                proposals.append(proposals_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if status is not UNSET:
            field_dict["status"] = status
        if completed is not UNSET:
            field_dict["completed"] = completed
        if total_books is not UNSET:
            field_dict["totalBooks"] = total_books
        if started_at is not UNSET:
            field_dict["startedAt"] = started_at
        if completed_at is not UNSET:
            field_dict["completedAt"] = completed_at
        if initiated_by is not UNSET:
            field_dict["initiatedBy"] = initiated_by
        if proposals is not UNSET:
            field_dict["proposals"] = proposals

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.fetched_proposal import FetchedProposal

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        _status = d.pop("status", UNSET)
        status: MetadataFetchTaskStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = MetadataFetchTaskStatus(_status)

        completed = d.pop("completed", UNSET)

        total_books = d.pop("totalBooks", UNSET)

        _started_at = d.pop("startedAt", UNSET)
        started_at: datetime.datetime | Unset
        if isinstance(_started_at, Unset):
            started_at = UNSET
        else:
            started_at = datetime.datetime.fromisoformat(_started_at)

        _completed_at = d.pop("completedAt", UNSET)
        completed_at: datetime.datetime | Unset
        if isinstance(_completed_at, Unset):
            completed_at = UNSET
        else:
            completed_at = datetime.datetime.fromisoformat(_completed_at)

        initiated_by = d.pop("initiatedBy", UNSET)

        _proposals = d.pop("proposals", UNSET)
        proposals: list[FetchedProposal] | Unset = UNSET
        if _proposals is not UNSET:
            proposals = []
            for proposals_item_data in _proposals:
                proposals_item = FetchedProposal.from_dict(proposals_item_data)

                proposals.append(proposals_item)

        metadata_fetch_task = cls(
            id=id,
            status=status,
            completed=completed,
            total_books=total_books,
            started_at=started_at,
            completed_at=completed_at,
            initiated_by=initiated_by,
            proposals=proposals,
        )

        metadata_fetch_task.additional_properties = d
        return metadata_fetch_task

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
