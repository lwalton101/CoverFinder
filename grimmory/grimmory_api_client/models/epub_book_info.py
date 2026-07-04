from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.epub_book_info_metadata import EpubBookInfoMetadata
    from ..models.epub_manifest_item import EpubManifestItem
    from ..models.epub_spine_item import EpubSpineItem
    from ..models.epub_toc_item import EpubTocItem


T = TypeVar("T", bound="EpubBookInfo")


@_attrs_define
class EpubBookInfo:
    """
    Attributes:
        container_path (str | Unset):
        root_path (str | Unset):
        spine (list[EpubSpineItem] | Unset):
        manifest (list[EpubManifestItem] | Unset):
        toc (EpubTocItem | Unset):
        metadata (EpubBookInfoMetadata | Unset):
        cover_path (str | Unset):
    """

    container_path: str | Unset = UNSET
    root_path: str | Unset = UNSET
    spine: list[EpubSpineItem] | Unset = UNSET
    manifest: list[EpubManifestItem] | Unset = UNSET
    toc: EpubTocItem | Unset = UNSET
    metadata: EpubBookInfoMetadata | Unset = UNSET
    cover_path: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        container_path = self.container_path

        root_path = self.root_path

        spine: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.spine, Unset):
            spine = []
            for spine_item_data in self.spine:
                spine_item = spine_item_data.to_dict()
                spine.append(spine_item)

        manifest: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.manifest, Unset):
            manifest = []
            for manifest_item_data in self.manifest:
                manifest_item = manifest_item_data.to_dict()
                manifest.append(manifest_item)

        toc: dict[str, Any] | Unset = UNSET
        if not isinstance(self.toc, Unset):
            toc = self.toc.to_dict()

        metadata: dict[str, Any] | Unset = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        cover_path = self.cover_path

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if container_path is not UNSET:
            field_dict["containerPath"] = container_path
        if root_path is not UNSET:
            field_dict["rootPath"] = root_path
        if spine is not UNSET:
            field_dict["spine"] = spine
        if manifest is not UNSET:
            field_dict["manifest"] = manifest
        if toc is not UNSET:
            field_dict["toc"] = toc
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if cover_path is not UNSET:
            field_dict["coverPath"] = cover_path

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.epub_book_info_metadata import EpubBookInfoMetadata
        from ..models.epub_manifest_item import EpubManifestItem
        from ..models.epub_spine_item import EpubSpineItem
        from ..models.epub_toc_item import EpubTocItem

        d = dict(src_dict)
        container_path = d.pop("containerPath", UNSET)

        root_path = d.pop("rootPath", UNSET)

        _spine = d.pop("spine", UNSET)
        spine: list[EpubSpineItem] | Unset = UNSET
        if _spine is not UNSET:
            spine = []
            for spine_item_data in _spine:
                spine_item = EpubSpineItem.from_dict(spine_item_data)

                spine.append(spine_item)

        _manifest = d.pop("manifest", UNSET)
        manifest: list[EpubManifestItem] | Unset = UNSET
        if _manifest is not UNSET:
            manifest = []
            for manifest_item_data in _manifest:
                manifest_item = EpubManifestItem.from_dict(manifest_item_data)

                manifest.append(manifest_item)

        _toc = d.pop("toc", UNSET)
        toc: EpubTocItem | Unset
        if isinstance(_toc, Unset):
            toc = UNSET
        else:
            toc = EpubTocItem.from_dict(_toc)

        _metadata = d.pop("metadata", UNSET)
        metadata: EpubBookInfoMetadata | Unset
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = EpubBookInfoMetadata.from_dict(_metadata)

        cover_path = d.pop("coverPath", UNSET)

        epub_book_info = cls(
            container_path=container_path,
            root_path=root_path,
            spine=spine,
            manifest=manifest,
            toc=toc,
            metadata=metadata,
            cover_path=cover_path,
        )

        epub_book_info.additional_properties = d
        return epub_book_info

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
