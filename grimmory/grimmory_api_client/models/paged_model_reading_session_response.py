from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.page_metadata import PageMetadata
    from ..models.reading_session_response import ReadingSessionResponse


T = TypeVar("T", bound="PagedModelReadingSessionResponse")


@_attrs_define
class PagedModelReadingSessionResponse:
    """
    Attributes:
        content (list[ReadingSessionResponse] | Unset):
        page (PageMetadata | Unset):
    """

    content: list[ReadingSessionResponse] | Unset = UNSET
    page: PageMetadata | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        content: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.content, Unset):
            content = []
            for content_item_data in self.content:
                content_item = content_item_data.to_dict()
                content.append(content_item)

        page: dict[str, Any] | Unset = UNSET
        if not isinstance(self.page, Unset):
            page = self.page.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if content is not UNSET:
            field_dict["content"] = content
        if page is not UNSET:
            field_dict["page"] = page

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.page_metadata import PageMetadata
        from ..models.reading_session_response import ReadingSessionResponse

        d = dict(src_dict)
        _content = d.pop("content", UNSET)
        content: list[ReadingSessionResponse] | Unset = UNSET
        if _content is not UNSET:
            content = []
            for content_item_data in _content:
                content_item = ReadingSessionResponse.from_dict(content_item_data)

                content.append(content_item)

        _page = d.pop("page", UNSET)
        page: PageMetadata | Unset
        if isinstance(_page, Unset):
            page = UNSET
        else:
            page = PageMetadata.from_dict(_page)

        paged_model_reading_session_response = cls(
            content=content,
            page=page,
        )

        paged_model_reading_session_response.additional_properties = d
        return paged_model_reading_session_response

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
