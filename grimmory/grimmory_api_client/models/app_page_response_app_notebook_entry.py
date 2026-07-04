from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.app_notebook_entry import AppNotebookEntry


T = TypeVar("T", bound="AppPageResponseAppNotebookEntry")


@_attrs_define
class AppPageResponseAppNotebookEntry:
    """
    Attributes:
        content (list[AppNotebookEntry] | Unset):
        page (int | Unset):
        size (int | Unset):
        total_elements (int | Unset):
        total_pages (int | Unset):
        has_next (bool | Unset):
        has_previous (bool | Unset):
    """

    content: list[AppNotebookEntry] | Unset = UNSET
    page: int | Unset = UNSET
    size: int | Unset = UNSET
    total_elements: int | Unset = UNSET
    total_pages: int | Unset = UNSET
    has_next: bool | Unset = UNSET
    has_previous: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        content: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.content, Unset):
            content = []
            for content_item_data in self.content:
                content_item = content_item_data.to_dict()
                content.append(content_item)

        page = self.page

        size = self.size

        total_elements = self.total_elements

        total_pages = self.total_pages

        has_next = self.has_next

        has_previous = self.has_previous

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if content is not UNSET:
            field_dict["content"] = content
        if page is not UNSET:
            field_dict["page"] = page
        if size is not UNSET:
            field_dict["size"] = size
        if total_elements is not UNSET:
            field_dict["totalElements"] = total_elements
        if total_pages is not UNSET:
            field_dict["totalPages"] = total_pages
        if has_next is not UNSET:
            field_dict["hasNext"] = has_next
        if has_previous is not UNSET:
            field_dict["hasPrevious"] = has_previous

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.app_notebook_entry import AppNotebookEntry

        d = dict(src_dict)
        _content = d.pop("content", UNSET)
        content: list[AppNotebookEntry] | Unset = UNSET
        if _content is not UNSET:
            content = []
            for content_item_data in _content:
                content_item = AppNotebookEntry.from_dict(content_item_data)

                content.append(content_item)

        page = d.pop("page", UNSET)

        size = d.pop("size", UNSET)

        total_elements = d.pop("totalElements", UNSET)

        total_pages = d.pop("totalPages", UNSET)

        has_next = d.pop("hasNext", UNSET)

        has_previous = d.pop("hasPrevious", UNSET)

        app_page_response_app_notebook_entry = cls(
            content=content,
            page=page,
            size=size,
            total_elements=total_elements,
            total_pages=total_pages,
            has_next=has_next,
            has_previous=has_previous,
        )

        app_page_response_app_notebook_entry.additional_properties = d
        return app_page_response_app_notebook_entry

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
