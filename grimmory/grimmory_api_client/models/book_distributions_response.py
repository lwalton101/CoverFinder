from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.progress_bucket import ProgressBucket
    from ..models.rating_bucket import RatingBucket
    from ..models.status_bucket import StatusBucket


T = TypeVar("T", bound="BookDistributionsResponse")


@_attrs_define
class BookDistributionsResponse:
    """
    Attributes:
        rating_distribution (list[RatingBucket] | Unset):
        progress_distribution (list[ProgressBucket] | Unset):
        status_distribution (list[StatusBucket] | Unset):
    """

    rating_distribution: list[RatingBucket] | Unset = UNSET
    progress_distribution: list[ProgressBucket] | Unset = UNSET
    status_distribution: list[StatusBucket] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        rating_distribution: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.rating_distribution, Unset):
            rating_distribution = []
            for rating_distribution_item_data in self.rating_distribution:
                rating_distribution_item = rating_distribution_item_data.to_dict()
                rating_distribution.append(rating_distribution_item)

        progress_distribution: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.progress_distribution, Unset):
            progress_distribution = []
            for progress_distribution_item_data in self.progress_distribution:
                progress_distribution_item = progress_distribution_item_data.to_dict()
                progress_distribution.append(progress_distribution_item)

        status_distribution: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.status_distribution, Unset):
            status_distribution = []
            for status_distribution_item_data in self.status_distribution:
                status_distribution_item = status_distribution_item_data.to_dict()
                status_distribution.append(status_distribution_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if rating_distribution is not UNSET:
            field_dict["ratingDistribution"] = rating_distribution
        if progress_distribution is not UNSET:
            field_dict["progressDistribution"] = progress_distribution
        if status_distribution is not UNSET:
            field_dict["statusDistribution"] = status_distribution

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.progress_bucket import ProgressBucket
        from ..models.rating_bucket import RatingBucket
        from ..models.status_bucket import StatusBucket

        d = dict(src_dict)
        _rating_distribution = d.pop("ratingDistribution", UNSET)
        rating_distribution: list[RatingBucket] | Unset = UNSET
        if _rating_distribution is not UNSET:
            rating_distribution = []
            for rating_distribution_item_data in _rating_distribution:
                rating_distribution_item = RatingBucket.from_dict(rating_distribution_item_data)

                rating_distribution.append(rating_distribution_item)

        _progress_distribution = d.pop("progressDistribution", UNSET)
        progress_distribution: list[ProgressBucket] | Unset = UNSET
        if _progress_distribution is not UNSET:
            progress_distribution = []
            for progress_distribution_item_data in _progress_distribution:
                progress_distribution_item = ProgressBucket.from_dict(progress_distribution_item_data)

                progress_distribution.append(progress_distribution_item)

        _status_distribution = d.pop("statusDistribution", UNSET)
        status_distribution: list[StatusBucket] | Unset = UNSET
        if _status_distribution is not UNSET:
            status_distribution = []
            for status_distribution_item_data in _status_distribution:
                status_distribution_item = StatusBucket.from_dict(status_distribution_item_data)

                status_distribution.append(status_distribution_item)

        book_distributions_response = cls(
            rating_distribution=rating_distribution,
            progress_distribution=progress_distribution,
            status_distribution=status_distribution,
        )

        book_distributions_response.additional_properties = d
        return book_distributions_response

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
