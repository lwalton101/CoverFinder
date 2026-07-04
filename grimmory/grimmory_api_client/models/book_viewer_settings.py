from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cbx_viewer_preferences import CbxViewerPreferences
    from ..models.ebook_viewer_preferences import EbookViewerPreferences
    from ..models.new_pdf_viewer_preferences import NewPdfViewerPreferences
    from ..models.pdf_viewer_preferences import PdfViewerPreferences


T = TypeVar("T", bound="BookViewerSettings")


@_attrs_define
class BookViewerSettings:
    """Viewer settings to update

    Attributes:
        pdf_settings (PdfViewerPreferences | Unset):
        new_pdf_settings (NewPdfViewerPreferences | Unset):
        ebook_settings (EbookViewerPreferences | Unset):
        cbx_settings (CbxViewerPreferences | Unset):
    """

    pdf_settings: PdfViewerPreferences | Unset = UNSET
    new_pdf_settings: NewPdfViewerPreferences | Unset = UNSET
    ebook_settings: EbookViewerPreferences | Unset = UNSET
    cbx_settings: CbxViewerPreferences | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        pdf_settings: dict[str, Any] | Unset = UNSET
        if not isinstance(self.pdf_settings, Unset):
            pdf_settings = self.pdf_settings.to_dict()

        new_pdf_settings: dict[str, Any] | Unset = UNSET
        if not isinstance(self.new_pdf_settings, Unset):
            new_pdf_settings = self.new_pdf_settings.to_dict()

        ebook_settings: dict[str, Any] | Unset = UNSET
        if not isinstance(self.ebook_settings, Unset):
            ebook_settings = self.ebook_settings.to_dict()

        cbx_settings: dict[str, Any] | Unset = UNSET
        if not isinstance(self.cbx_settings, Unset):
            cbx_settings = self.cbx_settings.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if pdf_settings is not UNSET:
            field_dict["pdfSettings"] = pdf_settings
        if new_pdf_settings is not UNSET:
            field_dict["newPdfSettings"] = new_pdf_settings
        if ebook_settings is not UNSET:
            field_dict["ebookSettings"] = ebook_settings
        if cbx_settings is not UNSET:
            field_dict["cbxSettings"] = cbx_settings

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cbx_viewer_preferences import CbxViewerPreferences
        from ..models.ebook_viewer_preferences import EbookViewerPreferences
        from ..models.new_pdf_viewer_preferences import NewPdfViewerPreferences
        from ..models.pdf_viewer_preferences import PdfViewerPreferences

        d = dict(src_dict)
        _pdf_settings = d.pop("pdfSettings", UNSET)
        pdf_settings: PdfViewerPreferences | Unset
        if isinstance(_pdf_settings, Unset):
            pdf_settings = UNSET
        else:
            pdf_settings = PdfViewerPreferences.from_dict(_pdf_settings)

        _new_pdf_settings = d.pop("newPdfSettings", UNSET)
        new_pdf_settings: NewPdfViewerPreferences | Unset
        if isinstance(_new_pdf_settings, Unset):
            new_pdf_settings = UNSET
        else:
            new_pdf_settings = NewPdfViewerPreferences.from_dict(_new_pdf_settings)

        _ebook_settings = d.pop("ebookSettings", UNSET)
        ebook_settings: EbookViewerPreferences | Unset
        if isinstance(_ebook_settings, Unset):
            ebook_settings = UNSET
        else:
            ebook_settings = EbookViewerPreferences.from_dict(_ebook_settings)

        _cbx_settings = d.pop("cbxSettings", UNSET)
        cbx_settings: CbxViewerPreferences | Unset
        if isinstance(_cbx_settings, Unset):
            cbx_settings = UNSET
        else:
            cbx_settings = CbxViewerPreferences.from_dict(_cbx_settings)

        book_viewer_settings = cls(
            pdf_settings=pdf_settings,
            new_pdf_settings=new_pdf_settings,
            ebook_settings=ebook_settings,
            cbx_settings=cbx_settings,
        )

        book_viewer_settings.additional_properties = d
        return book_viewer_settings

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
