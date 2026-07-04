from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.sidecar_rating import SidecarRating


T = TypeVar("T", bound="SidecarRatings")


@_attrs_define
class SidecarRatings:
    """
    Attributes:
        amazon (SidecarRating | Unset):
        goodreads (SidecarRating | Unset):
        hardcover (SidecarRating | Unset):
        lubimyczytac (SidecarRating | Unset):
        ranobedb (SidecarRating | Unset):
        audible (SidecarRating | Unset):
    """

    amazon: SidecarRating | Unset = UNSET
    goodreads: SidecarRating | Unset = UNSET
    hardcover: SidecarRating | Unset = UNSET
    lubimyczytac: SidecarRating | Unset = UNSET
    ranobedb: SidecarRating | Unset = UNSET
    audible: SidecarRating | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        amazon: dict[str, Any] | Unset = UNSET
        if not isinstance(self.amazon, Unset):
            amazon = self.amazon.to_dict()

        goodreads: dict[str, Any] | Unset = UNSET
        if not isinstance(self.goodreads, Unset):
            goodreads = self.goodreads.to_dict()

        hardcover: dict[str, Any] | Unset = UNSET
        if not isinstance(self.hardcover, Unset):
            hardcover = self.hardcover.to_dict()

        lubimyczytac: dict[str, Any] | Unset = UNSET
        if not isinstance(self.lubimyczytac, Unset):
            lubimyczytac = self.lubimyczytac.to_dict()

        ranobedb: dict[str, Any] | Unset = UNSET
        if not isinstance(self.ranobedb, Unset):
            ranobedb = self.ranobedb.to_dict()

        audible: dict[str, Any] | Unset = UNSET
        if not isinstance(self.audible, Unset):
            audible = self.audible.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if amazon is not UNSET:
            field_dict["amazon"] = amazon
        if goodreads is not UNSET:
            field_dict["goodreads"] = goodreads
        if hardcover is not UNSET:
            field_dict["hardcover"] = hardcover
        if lubimyczytac is not UNSET:
            field_dict["lubimyczytac"] = lubimyczytac
        if ranobedb is not UNSET:
            field_dict["ranobedb"] = ranobedb
        if audible is not UNSET:
            field_dict["audible"] = audible

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.sidecar_rating import SidecarRating

        d = dict(src_dict)
        _amazon = d.pop("amazon", UNSET)
        amazon: SidecarRating | Unset
        if isinstance(_amazon, Unset):
            amazon = UNSET
        else:
            amazon = SidecarRating.from_dict(_amazon)

        _goodreads = d.pop("goodreads", UNSET)
        goodreads: SidecarRating | Unset
        if isinstance(_goodreads, Unset):
            goodreads = UNSET
        else:
            goodreads = SidecarRating.from_dict(_goodreads)

        _hardcover = d.pop("hardcover", UNSET)
        hardcover: SidecarRating | Unset
        if isinstance(_hardcover, Unset):
            hardcover = UNSET
        else:
            hardcover = SidecarRating.from_dict(_hardcover)

        _lubimyczytac = d.pop("lubimyczytac", UNSET)
        lubimyczytac: SidecarRating | Unset
        if isinstance(_lubimyczytac, Unset):
            lubimyczytac = UNSET
        else:
            lubimyczytac = SidecarRating.from_dict(_lubimyczytac)

        _ranobedb = d.pop("ranobedb", UNSET)
        ranobedb: SidecarRating | Unset
        if isinstance(_ranobedb, Unset):
            ranobedb = UNSET
        else:
            ranobedb = SidecarRating.from_dict(_ranobedb)

        _audible = d.pop("audible", UNSET)
        audible: SidecarRating | Unset
        if isinstance(_audible, Unset):
            audible = UNSET
        else:
            audible = SidecarRating.from_dict(_audible)

        sidecar_ratings = cls(
            amazon=amazon,
            goodreads=goodreads,
            hardcover=hardcover,
            lubimyczytac=lubimyczytac,
            ranobedb=ranobedb,
            audible=audible,
        )

        sidecar_ratings.additional_properties = d
        return sidecar_ratings

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
