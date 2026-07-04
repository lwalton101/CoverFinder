from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cbx_reader_setting import CbxReaderSetting
    from ..models.dashboard_config import DashboardConfig
    from ..models.ebook_reader_setting import EbookReaderSetting
    from ..models.entity_view_preferences import EntityViewPreferences
    from ..models.epub_reader_setting import EpubReaderSetting
    from ..models.new_pdf_reader_setting import NewPdfReaderSetting
    from ..models.pdf_reader_setting import PdfReaderSetting
    from ..models.per_book_setting import PerBookSetting
    from ..models.sidebar_sort_option import SidebarSortOption
    from ..models.table_column_preference import TableColumnPreference


T = TypeVar("T", bound="UserSettings")


@_attrs_define
class UserSettings:
    """
    Attributes:
        per_book_setting (PerBookSetting | Unset):
        pdf_reader_setting (PdfReaderSetting | Unset):
        new_pdf_reader_setting (NewPdfReaderSetting | Unset):
        epub_reader_setting (EpubReaderSetting | Unset):
        ebook_reader_setting (EbookReaderSetting | Unset):
        cbx_reader_setting (CbxReaderSetting | Unset):
        sidebar_library_sorting (SidebarSortOption | Unset):
        sidebar_shelf_sorting (SidebarSortOption | Unset):
        sidebar_magic_shelf_sorting (SidebarSortOption | Unset):
        entity_view_preferences (EntityViewPreferences | Unset):
        table_column_preference (list[TableColumnPreference] | Unset):
        filter_mode (str | Unset):
        filter_sorting_mode (str | Unset):
        metadata_center_view_mode (str | Unset):
        ko_reader_enabled (bool | Unset):
        enable_series_view (bool | Unset):
        auto_save_metadata (bool | Unset):
        visible_filters (list[str] | Unset):
        visible_sort_fields (list[str] | Unset):
        dashboard_config (DashboardConfig | Unset):
    """

    per_book_setting: PerBookSetting | Unset = UNSET
    pdf_reader_setting: PdfReaderSetting | Unset = UNSET
    new_pdf_reader_setting: NewPdfReaderSetting | Unset = UNSET
    epub_reader_setting: EpubReaderSetting | Unset = UNSET
    ebook_reader_setting: EbookReaderSetting | Unset = UNSET
    cbx_reader_setting: CbxReaderSetting | Unset = UNSET
    sidebar_library_sorting: SidebarSortOption | Unset = UNSET
    sidebar_shelf_sorting: SidebarSortOption | Unset = UNSET
    sidebar_magic_shelf_sorting: SidebarSortOption | Unset = UNSET
    entity_view_preferences: EntityViewPreferences | Unset = UNSET
    table_column_preference: list[TableColumnPreference] | Unset = UNSET
    filter_mode: str | Unset = UNSET
    filter_sorting_mode: str | Unset = UNSET
    metadata_center_view_mode: str | Unset = UNSET
    ko_reader_enabled: bool | Unset = UNSET
    enable_series_view: bool | Unset = UNSET
    auto_save_metadata: bool | Unset = UNSET
    visible_filters: list[str] | Unset = UNSET
    visible_sort_fields: list[str] | Unset = UNSET
    dashboard_config: DashboardConfig | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        per_book_setting: dict[str, Any] | Unset = UNSET
        if not isinstance(self.per_book_setting, Unset):
            per_book_setting = self.per_book_setting.to_dict()

        pdf_reader_setting: dict[str, Any] | Unset = UNSET
        if not isinstance(self.pdf_reader_setting, Unset):
            pdf_reader_setting = self.pdf_reader_setting.to_dict()

        new_pdf_reader_setting: dict[str, Any] | Unset = UNSET
        if not isinstance(self.new_pdf_reader_setting, Unset):
            new_pdf_reader_setting = self.new_pdf_reader_setting.to_dict()

        epub_reader_setting: dict[str, Any] | Unset = UNSET
        if not isinstance(self.epub_reader_setting, Unset):
            epub_reader_setting = self.epub_reader_setting.to_dict()

        ebook_reader_setting: dict[str, Any] | Unset = UNSET
        if not isinstance(self.ebook_reader_setting, Unset):
            ebook_reader_setting = self.ebook_reader_setting.to_dict()

        cbx_reader_setting: dict[str, Any] | Unset = UNSET
        if not isinstance(self.cbx_reader_setting, Unset):
            cbx_reader_setting = self.cbx_reader_setting.to_dict()

        sidebar_library_sorting: dict[str, Any] | Unset = UNSET
        if not isinstance(self.sidebar_library_sorting, Unset):
            sidebar_library_sorting = self.sidebar_library_sorting.to_dict()

        sidebar_shelf_sorting: dict[str, Any] | Unset = UNSET
        if not isinstance(self.sidebar_shelf_sorting, Unset):
            sidebar_shelf_sorting = self.sidebar_shelf_sorting.to_dict()

        sidebar_magic_shelf_sorting: dict[str, Any] | Unset = UNSET
        if not isinstance(self.sidebar_magic_shelf_sorting, Unset):
            sidebar_magic_shelf_sorting = self.sidebar_magic_shelf_sorting.to_dict()

        entity_view_preferences: dict[str, Any] | Unset = UNSET
        if not isinstance(self.entity_view_preferences, Unset):
            entity_view_preferences = self.entity_view_preferences.to_dict()

        table_column_preference: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.table_column_preference, Unset):
            table_column_preference = []
            for table_column_preference_item_data in self.table_column_preference:
                table_column_preference_item = table_column_preference_item_data.to_dict()
                table_column_preference.append(table_column_preference_item)

        filter_mode = self.filter_mode

        filter_sorting_mode = self.filter_sorting_mode

        metadata_center_view_mode = self.metadata_center_view_mode

        ko_reader_enabled = self.ko_reader_enabled

        enable_series_view = self.enable_series_view

        auto_save_metadata = self.auto_save_metadata

        visible_filters: list[str] | Unset = UNSET
        if not isinstance(self.visible_filters, Unset):
            visible_filters = self.visible_filters

        visible_sort_fields: list[str] | Unset = UNSET
        if not isinstance(self.visible_sort_fields, Unset):
            visible_sort_fields = self.visible_sort_fields

        dashboard_config: dict[str, Any] | Unset = UNSET
        if not isinstance(self.dashboard_config, Unset):
            dashboard_config = self.dashboard_config.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if per_book_setting is not UNSET:
            field_dict["perBookSetting"] = per_book_setting
        if pdf_reader_setting is not UNSET:
            field_dict["pdfReaderSetting"] = pdf_reader_setting
        if new_pdf_reader_setting is not UNSET:
            field_dict["newPdfReaderSetting"] = new_pdf_reader_setting
        if epub_reader_setting is not UNSET:
            field_dict["epubReaderSetting"] = epub_reader_setting
        if ebook_reader_setting is not UNSET:
            field_dict["ebookReaderSetting"] = ebook_reader_setting
        if cbx_reader_setting is not UNSET:
            field_dict["cbxReaderSetting"] = cbx_reader_setting
        if sidebar_library_sorting is not UNSET:
            field_dict["sidebarLibrarySorting"] = sidebar_library_sorting
        if sidebar_shelf_sorting is not UNSET:
            field_dict["sidebarShelfSorting"] = sidebar_shelf_sorting
        if sidebar_magic_shelf_sorting is not UNSET:
            field_dict["sidebarMagicShelfSorting"] = sidebar_magic_shelf_sorting
        if entity_view_preferences is not UNSET:
            field_dict["entityViewPreferences"] = entity_view_preferences
        if table_column_preference is not UNSET:
            field_dict["tableColumnPreference"] = table_column_preference
        if filter_mode is not UNSET:
            field_dict["filterMode"] = filter_mode
        if filter_sorting_mode is not UNSET:
            field_dict["filterSortingMode"] = filter_sorting_mode
        if metadata_center_view_mode is not UNSET:
            field_dict["metadataCenterViewMode"] = metadata_center_view_mode
        if ko_reader_enabled is not UNSET:
            field_dict["koReaderEnabled"] = ko_reader_enabled
        if enable_series_view is not UNSET:
            field_dict["enableSeriesView"] = enable_series_view
        if auto_save_metadata is not UNSET:
            field_dict["autoSaveMetadata"] = auto_save_metadata
        if visible_filters is not UNSET:
            field_dict["visibleFilters"] = visible_filters
        if visible_sort_fields is not UNSET:
            field_dict["visibleSortFields"] = visible_sort_fields
        if dashboard_config is not UNSET:
            field_dict["dashboardConfig"] = dashboard_config

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cbx_reader_setting import CbxReaderSetting
        from ..models.dashboard_config import DashboardConfig
        from ..models.ebook_reader_setting import EbookReaderSetting
        from ..models.entity_view_preferences import EntityViewPreferences
        from ..models.epub_reader_setting import EpubReaderSetting
        from ..models.new_pdf_reader_setting import NewPdfReaderSetting
        from ..models.pdf_reader_setting import PdfReaderSetting
        from ..models.per_book_setting import PerBookSetting
        from ..models.sidebar_sort_option import SidebarSortOption
        from ..models.table_column_preference import TableColumnPreference

        d = dict(src_dict)
        _per_book_setting = d.pop("perBookSetting", UNSET)
        per_book_setting: PerBookSetting | Unset
        if isinstance(_per_book_setting, Unset):
            per_book_setting = UNSET
        else:
            per_book_setting = PerBookSetting.from_dict(_per_book_setting)

        _pdf_reader_setting = d.pop("pdfReaderSetting", UNSET)
        pdf_reader_setting: PdfReaderSetting | Unset
        if isinstance(_pdf_reader_setting, Unset):
            pdf_reader_setting = UNSET
        else:
            pdf_reader_setting = PdfReaderSetting.from_dict(_pdf_reader_setting)

        _new_pdf_reader_setting = d.pop("newPdfReaderSetting", UNSET)
        new_pdf_reader_setting: NewPdfReaderSetting | Unset
        if isinstance(_new_pdf_reader_setting, Unset):
            new_pdf_reader_setting = UNSET
        else:
            new_pdf_reader_setting = NewPdfReaderSetting.from_dict(_new_pdf_reader_setting)

        _epub_reader_setting = d.pop("epubReaderSetting", UNSET)
        epub_reader_setting: EpubReaderSetting | Unset
        if isinstance(_epub_reader_setting, Unset):
            epub_reader_setting = UNSET
        else:
            epub_reader_setting = EpubReaderSetting.from_dict(_epub_reader_setting)

        _ebook_reader_setting = d.pop("ebookReaderSetting", UNSET)
        ebook_reader_setting: EbookReaderSetting | Unset
        if isinstance(_ebook_reader_setting, Unset):
            ebook_reader_setting = UNSET
        else:
            ebook_reader_setting = EbookReaderSetting.from_dict(_ebook_reader_setting)

        _cbx_reader_setting = d.pop("cbxReaderSetting", UNSET)
        cbx_reader_setting: CbxReaderSetting | Unset
        if isinstance(_cbx_reader_setting, Unset):
            cbx_reader_setting = UNSET
        else:
            cbx_reader_setting = CbxReaderSetting.from_dict(_cbx_reader_setting)

        _sidebar_library_sorting = d.pop("sidebarLibrarySorting", UNSET)
        sidebar_library_sorting: SidebarSortOption | Unset
        if isinstance(_sidebar_library_sorting, Unset):
            sidebar_library_sorting = UNSET
        else:
            sidebar_library_sorting = SidebarSortOption.from_dict(_sidebar_library_sorting)

        _sidebar_shelf_sorting = d.pop("sidebarShelfSorting", UNSET)
        sidebar_shelf_sorting: SidebarSortOption | Unset
        if isinstance(_sidebar_shelf_sorting, Unset):
            sidebar_shelf_sorting = UNSET
        else:
            sidebar_shelf_sorting = SidebarSortOption.from_dict(_sidebar_shelf_sorting)

        _sidebar_magic_shelf_sorting = d.pop("sidebarMagicShelfSorting", UNSET)
        sidebar_magic_shelf_sorting: SidebarSortOption | Unset
        if isinstance(_sidebar_magic_shelf_sorting, Unset):
            sidebar_magic_shelf_sorting = UNSET
        else:
            sidebar_magic_shelf_sorting = SidebarSortOption.from_dict(_sidebar_magic_shelf_sorting)

        _entity_view_preferences = d.pop("entityViewPreferences", UNSET)
        entity_view_preferences: EntityViewPreferences | Unset
        if isinstance(_entity_view_preferences, Unset):
            entity_view_preferences = UNSET
        else:
            entity_view_preferences = EntityViewPreferences.from_dict(_entity_view_preferences)

        _table_column_preference = d.pop("tableColumnPreference", UNSET)
        table_column_preference: list[TableColumnPreference] | Unset = UNSET
        if _table_column_preference is not UNSET:
            table_column_preference = []
            for table_column_preference_item_data in _table_column_preference:
                table_column_preference_item = TableColumnPreference.from_dict(table_column_preference_item_data)

                table_column_preference.append(table_column_preference_item)

        filter_mode = d.pop("filterMode", UNSET)

        filter_sorting_mode = d.pop("filterSortingMode", UNSET)

        metadata_center_view_mode = d.pop("metadataCenterViewMode", UNSET)

        ko_reader_enabled = d.pop("koReaderEnabled", UNSET)

        enable_series_view = d.pop("enableSeriesView", UNSET)

        auto_save_metadata = d.pop("autoSaveMetadata", UNSET)

        visible_filters = cast(list[str], d.pop("visibleFilters", UNSET))

        visible_sort_fields = cast(list[str], d.pop("visibleSortFields", UNSET))

        _dashboard_config = d.pop("dashboardConfig", UNSET)
        dashboard_config: DashboardConfig | Unset
        if isinstance(_dashboard_config, Unset):
            dashboard_config = UNSET
        else:
            dashboard_config = DashboardConfig.from_dict(_dashboard_config)

        user_settings = cls(
            per_book_setting=per_book_setting,
            pdf_reader_setting=pdf_reader_setting,
            new_pdf_reader_setting=new_pdf_reader_setting,
            epub_reader_setting=epub_reader_setting,
            ebook_reader_setting=ebook_reader_setting,
            cbx_reader_setting=cbx_reader_setting,
            sidebar_library_sorting=sidebar_library_sorting,
            sidebar_shelf_sorting=sidebar_shelf_sorting,
            sidebar_magic_shelf_sorting=sidebar_magic_shelf_sorting,
            entity_view_preferences=entity_view_preferences,
            table_column_preference=table_column_preference,
            filter_mode=filter_mode,
            filter_sorting_mode=filter_sorting_mode,
            metadata_center_view_mode=metadata_center_view_mode,
            ko_reader_enabled=ko_reader_enabled,
            enable_series_view=enable_series_view,
            auto_save_metadata=auto_save_metadata,
            visible_filters=visible_filters,
            visible_sort_fields=visible_sort_fields,
            dashboard_config=dashboard_config,
        )

        user_settings.additional_properties = d
        return user_settings

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
