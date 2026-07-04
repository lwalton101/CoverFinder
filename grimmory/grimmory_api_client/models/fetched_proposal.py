from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.fetched_proposal_status import FetchedProposalStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.book_metadata import BookMetadata


T = TypeVar("T", bound="FetchedProposal")


@_attrs_define
class FetchedProposal:
    """
    Attributes:
        proposal_id (int | Unset):
        task_id (str | Unset):
        book_id (int | Unset):
        fetched_at (datetime.datetime | Unset):
        reviewed_at (datetime.datetime | Unset):
        reviewer_user_id (str | Unset):
        status (FetchedProposalStatus | Unset):
        metadata_json (BookMetadata | Unset):
    """

    proposal_id: int | Unset = UNSET
    task_id: str | Unset = UNSET
    book_id: int | Unset = UNSET
    fetched_at: datetime.datetime | Unset = UNSET
    reviewed_at: datetime.datetime | Unset = UNSET
    reviewer_user_id: str | Unset = UNSET
    status: FetchedProposalStatus | Unset = UNSET
    metadata_json: BookMetadata | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        proposal_id = self.proposal_id

        task_id = self.task_id

        book_id = self.book_id

        fetched_at: str | Unset = UNSET
        if not isinstance(self.fetched_at, Unset):
            fetched_at = self.fetched_at.isoformat()

        reviewed_at: str | Unset = UNSET
        if not isinstance(self.reviewed_at, Unset):
            reviewed_at = self.reviewed_at.isoformat()

        reviewer_user_id = self.reviewer_user_id

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        metadata_json: dict[str, Any] | Unset = UNSET
        if not isinstance(self.metadata_json, Unset):
            metadata_json = self.metadata_json.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if proposal_id is not UNSET:
            field_dict["proposalId"] = proposal_id
        if task_id is not UNSET:
            field_dict["taskId"] = task_id
        if book_id is not UNSET:
            field_dict["bookId"] = book_id
        if fetched_at is not UNSET:
            field_dict["fetchedAt"] = fetched_at
        if reviewed_at is not UNSET:
            field_dict["reviewedAt"] = reviewed_at
        if reviewer_user_id is not UNSET:
            field_dict["reviewerUserId"] = reviewer_user_id
        if status is not UNSET:
            field_dict["status"] = status
        if metadata_json is not UNSET:
            field_dict["metadataJson"] = metadata_json

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.book_metadata import BookMetadata

        d = dict(src_dict)
        proposal_id = d.pop("proposalId", UNSET)

        task_id = d.pop("taskId", UNSET)

        book_id = d.pop("bookId", UNSET)

        _fetched_at = d.pop("fetchedAt", UNSET)
        fetched_at: datetime.datetime | Unset
        if isinstance(_fetched_at, Unset):
            fetched_at = UNSET
        else:
            fetched_at = datetime.datetime.fromisoformat(_fetched_at)

        _reviewed_at = d.pop("reviewedAt", UNSET)
        reviewed_at: datetime.datetime | Unset
        if isinstance(_reviewed_at, Unset):
            reviewed_at = UNSET
        else:
            reviewed_at = datetime.datetime.fromisoformat(_reviewed_at)

        reviewer_user_id = d.pop("reviewerUserId", UNSET)

        _status = d.pop("status", UNSET)
        status: FetchedProposalStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = FetchedProposalStatus(_status)

        _metadata_json = d.pop("metadataJson", UNSET)
        metadata_json: BookMetadata | Unset
        if isinstance(_metadata_json, Unset):
            metadata_json = UNSET
        else:
            metadata_json = BookMetadata.from_dict(_metadata_json)

        fetched_proposal = cls(
            proposal_id=proposal_id,
            task_id=task_id,
            book_id=book_id,
            fetched_at=fetched_at,
            reviewed_at=reviewed_at,
            reviewer_user_id=reviewer_user_id,
            status=status,
            metadata_json=metadata_json,
        )

        fetched_proposal.additional_properties = d
        return fetched_proposal

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
