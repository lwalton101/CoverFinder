from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.amazon import Amazon
    from ..models.audible import Audible
    from ..models.comicvine import Comicvine
    from ..models.douban import Douban
    from ..models.goodreads import Goodreads
    from ..models.google import Google
    from ..models.hardcover import Hardcover
    from ..models.lubimyczytac import Lubimyczytac
    from ..models.ranobedb import Ranobedb


T = TypeVar("T", bound="MetadataProviderSettings")


@_attrs_define
class MetadataProviderSettings:
    """
    Attributes:
        amazon (Amazon | Unset):
        google (Google | Unset):
        good_reads (Goodreads | Unset):
        hardcover (Hardcover | Unset):
        comicvine (Comicvine | Unset):
        ranobedb (Ranobedb | Unset):
        douban (Douban | Unset):
        audible (Audible | Unset):
        lubimyczytac (Lubimyczytac | Unset):
    """

    amazon: Amazon | Unset = UNSET
    google: Google | Unset = UNSET
    good_reads: Goodreads | Unset = UNSET
    hardcover: Hardcover | Unset = UNSET
    comicvine: Comicvine | Unset = UNSET
    ranobedb: Ranobedb | Unset = UNSET
    douban: Douban | Unset = UNSET
    audible: Audible | Unset = UNSET
    lubimyczytac: Lubimyczytac | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        amazon: dict[str, Any] | Unset = UNSET
        if not isinstance(self.amazon, Unset):
            amazon = self.amazon.to_dict()

        google: dict[str, Any] | Unset = UNSET
        if not isinstance(self.google, Unset):
            google = self.google.to_dict()

        good_reads: dict[str, Any] | Unset = UNSET
        if not isinstance(self.good_reads, Unset):
            good_reads = self.good_reads.to_dict()

        hardcover: dict[str, Any] | Unset = UNSET
        if not isinstance(self.hardcover, Unset):
            hardcover = self.hardcover.to_dict()

        comicvine: dict[str, Any] | Unset = UNSET
        if not isinstance(self.comicvine, Unset):
            comicvine = self.comicvine.to_dict()

        ranobedb: dict[str, Any] | Unset = UNSET
        if not isinstance(self.ranobedb, Unset):
            ranobedb = self.ranobedb.to_dict()

        douban: dict[str, Any] | Unset = UNSET
        if not isinstance(self.douban, Unset):
            douban = self.douban.to_dict()

        audible: dict[str, Any] | Unset = UNSET
        if not isinstance(self.audible, Unset):
            audible = self.audible.to_dict()

        lubimyczytac: dict[str, Any] | Unset = UNSET
        if not isinstance(self.lubimyczytac, Unset):
            lubimyczytac = self.lubimyczytac.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if amazon is not UNSET:
            field_dict["amazon"] = amazon
        if google is not UNSET:
            field_dict["google"] = google
        if good_reads is not UNSET:
            field_dict["goodReads"] = good_reads
        if hardcover is not UNSET:
            field_dict["hardcover"] = hardcover
        if comicvine is not UNSET:
            field_dict["comicvine"] = comicvine
        if ranobedb is not UNSET:
            field_dict["ranobedb"] = ranobedb
        if douban is not UNSET:
            field_dict["douban"] = douban
        if audible is not UNSET:
            field_dict["audible"] = audible
        if lubimyczytac is not UNSET:
            field_dict["lubimyczytac"] = lubimyczytac

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.amazon import Amazon
        from ..models.audible import Audible
        from ..models.comicvine import Comicvine
        from ..models.douban import Douban
        from ..models.goodreads import Goodreads
        from ..models.google import Google
        from ..models.hardcover import Hardcover
        from ..models.lubimyczytac import Lubimyczytac
        from ..models.ranobedb import Ranobedb

        d = dict(src_dict)
        _amazon = d.pop("amazon", UNSET)
        amazon: Amazon | Unset
        if isinstance(_amazon, Unset):
            amazon = UNSET
        else:
            amazon = Amazon.from_dict(_amazon)

        _google = d.pop("google", UNSET)
        google: Google | Unset
        if isinstance(_google, Unset):
            google = UNSET
        else:
            google = Google.from_dict(_google)

        _good_reads = d.pop("goodReads", UNSET)
        good_reads: Goodreads | Unset
        if isinstance(_good_reads, Unset):
            good_reads = UNSET
        else:
            good_reads = Goodreads.from_dict(_good_reads)

        _hardcover = d.pop("hardcover", UNSET)
        hardcover: Hardcover | Unset
        if isinstance(_hardcover, Unset):
            hardcover = UNSET
        else:
            hardcover = Hardcover.from_dict(_hardcover)

        _comicvine = d.pop("comicvine", UNSET)
        comicvine: Comicvine | Unset
        if isinstance(_comicvine, Unset):
            comicvine = UNSET
        else:
            comicvine = Comicvine.from_dict(_comicvine)

        _ranobedb = d.pop("ranobedb", UNSET)
        ranobedb: Ranobedb | Unset
        if isinstance(_ranobedb, Unset):
            ranobedb = UNSET
        else:
            ranobedb = Ranobedb.from_dict(_ranobedb)

        _douban = d.pop("douban", UNSET)
        douban: Douban | Unset
        if isinstance(_douban, Unset):
            douban = UNSET
        else:
            douban = Douban.from_dict(_douban)

        _audible = d.pop("audible", UNSET)
        audible: Audible | Unset
        if isinstance(_audible, Unset):
            audible = UNSET
        else:
            audible = Audible.from_dict(_audible)

        _lubimyczytac = d.pop("lubimyczytac", UNSET)
        lubimyczytac: Lubimyczytac | Unset
        if isinstance(_lubimyczytac, Unset):
            lubimyczytac = UNSET
        else:
            lubimyczytac = Lubimyczytac.from_dict(_lubimyczytac)

        metadata_provider_settings = cls(
            amazon=amazon,
            google=google,
            good_reads=good_reads,
            hardcover=hardcover,
            comicvine=comicvine,
            ranobedb=ranobedb,
            douban=douban,
            audible=audible,
            lubimyczytac=lubimyczytac,
        )

        metadata_provider_settings.additional_properties = d
        return metadata_provider_settings

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
