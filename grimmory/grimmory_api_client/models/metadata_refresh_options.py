from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.metadata_refresh_options_replace_mode import MetadataRefreshOptionsReplaceMode
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.enabled_fields import EnabledFields
    from ..models.field_options import FieldOptions


T = TypeVar("T", bound="MetadataRefreshOptions")


@_attrs_define
class MetadataRefreshOptions:
    """
    Attributes:
        field_options (FieldOptions):
        enabled_fields (EnabledFields):
        library_id (int | Unset):
        refresh_covers (bool | Unset):
        merge_categories (bool | Unset):
        review_before_apply (bool | Unset):
        replace_mode (MetadataRefreshOptionsReplaceMode | Unset):
    """

    field_options: FieldOptions
    enabled_fields: EnabledFields
    library_id: int | Unset = UNSET
    refresh_covers: bool | Unset = UNSET
    merge_categories: bool | Unset = UNSET
    review_before_apply: bool | Unset = UNSET
    replace_mode: MetadataRefreshOptionsReplaceMode | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        field_options = self.field_options.to_dict()

        enabled_fields = self.enabled_fields.to_dict()

        library_id = self.library_id

        refresh_covers = self.refresh_covers

        merge_categories = self.merge_categories

        review_before_apply = self.review_before_apply

        replace_mode: str | Unset = UNSET
        if not isinstance(self.replace_mode, Unset):
            replace_mode = self.replace_mode.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "fieldOptions": field_options,
                "enabledFields": enabled_fields,
            }
        )
        if library_id is not UNSET:
            field_dict["libraryId"] = library_id
        if refresh_covers is not UNSET:
            field_dict["refreshCovers"] = refresh_covers
        if merge_categories is not UNSET:
            field_dict["mergeCategories"] = merge_categories
        if review_before_apply is not UNSET:
            field_dict["reviewBeforeApply"] = review_before_apply
        if replace_mode is not UNSET:
            field_dict["replaceMode"] = replace_mode

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.enabled_fields import EnabledFields
        from ..models.field_options import FieldOptions

        d = dict(src_dict)
        field_options = FieldOptions.from_dict(d.pop("fieldOptions"))

        enabled_fields = EnabledFields.from_dict(d.pop("enabledFields"))

        library_id = d.pop("libraryId", UNSET)

        refresh_covers = d.pop("refreshCovers", UNSET)

        merge_categories = d.pop("mergeCategories", UNSET)

        review_before_apply = d.pop("reviewBeforeApply", UNSET)

        _replace_mode = d.pop("replaceMode", UNSET)
        replace_mode: MetadataRefreshOptionsReplaceMode | Unset
        if isinstance(_replace_mode, Unset):
            replace_mode = UNSET
        else:
            replace_mode = MetadataRefreshOptionsReplaceMode(_replace_mode)

        metadata_refresh_options = cls(
            field_options=field_options,
            enabled_fields=enabled_fields,
            library_id=library_id,
            refresh_covers=refresh_covers,
            merge_categories=merge_categories,
            review_before_apply=review_before_apply,
            replace_mode=replace_mode,
        )

        metadata_refresh_options.additional_properties = d
        return metadata_refresh_options

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
