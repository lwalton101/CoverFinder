from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cover_cropping_settings import CoverCroppingSettings
    from ..models.kobo_settings import KoboSettings
    from ..models.metadata_match_weights import MetadataMatchWeights
    from ..models.metadata_persistence_settings import MetadataPersistenceSettings
    from ..models.metadata_provider_settings import MetadataProviderSettings
    from ..models.metadata_provider_specific_fields import MetadataProviderSpecificFields
    from ..models.metadata_public_reviews_settings import MetadataPublicReviewsSettings
    from ..models.metadata_refresh_options import MetadataRefreshOptions
    from ..models.oidc_auto_provision_details import OidcAutoProvisionDetails
    from ..models.oidc_provider_details import OidcProviderDetails


T = TypeVar("T", bound="AppSettings")


@_attrs_define
class AppSettings:
    """
    Attributes:
        default_metadata_refresh_options (MetadataRefreshOptions | Unset):
        library_metadata_refresh_options (list[MetadataRefreshOptions] | Unset):
        auto_book_search (bool | Unset):
        similar_book_recommendation (bool | Unset):
        opds_server_enabled (bool | Unset):
        komga_api_enabled (bool | Unset):
        komga_group_unknown (bool | Unset):
        upload_pattern (str | Unset):
        pdf_cache_size_in_mb (int | Unset):
        max_file_upload_size_in_mb (int | Unset):
        remote_auth_enabled (bool | Unset):
        metadata_download_on_bookdrop (bool | Unset):
        oidc_enabled (bool | Unset):
        oidc_provider_details (OidcProviderDetails | Unset):
        oidc_redirect_uris (list[str] | Unset):
        oidc_auto_provision_details (OidcAutoProvisionDetails | Unset):
        metadata_provider_settings (MetadataProviderSettings | Unset):
        metadata_match_weights (MetadataMatchWeights | Unset):
        metadata_persistence_settings (MetadataPersistenceSettings | Unset):
        metadata_public_reviews_settings (MetadataPublicReviewsSettings | Unset):
        kobo_settings (KoboSettings | Unset):
        cover_cropping_settings (CoverCroppingSettings | Unset):
        metadata_provider_specific_fields (MetadataProviderSpecificFields | Unset):
        oidc_session_duration_hours (int | Unset):
        oidc_group_sync_mode (str | Unset):
        oidc_force_only_mode (bool | Unset):
        disk_type (str | Unset):
    """

    default_metadata_refresh_options: MetadataRefreshOptions | Unset = UNSET
    library_metadata_refresh_options: list[MetadataRefreshOptions] | Unset = UNSET
    auto_book_search: bool | Unset = UNSET
    similar_book_recommendation: bool | Unset = UNSET
    opds_server_enabled: bool | Unset = UNSET
    komga_api_enabled: bool | Unset = UNSET
    komga_group_unknown: bool | Unset = UNSET
    upload_pattern: str | Unset = UNSET
    pdf_cache_size_in_mb: int | Unset = UNSET
    max_file_upload_size_in_mb: int | Unset = UNSET
    remote_auth_enabled: bool | Unset = UNSET
    metadata_download_on_bookdrop: bool | Unset = UNSET
    oidc_enabled: bool | Unset = UNSET
    oidc_provider_details: OidcProviderDetails | Unset = UNSET
    oidc_redirect_uris: list[str] | Unset = UNSET
    oidc_auto_provision_details: OidcAutoProvisionDetails | Unset = UNSET
    metadata_provider_settings: MetadataProviderSettings | Unset = UNSET
    metadata_match_weights: MetadataMatchWeights | Unset = UNSET
    metadata_persistence_settings: MetadataPersistenceSettings | Unset = UNSET
    metadata_public_reviews_settings: MetadataPublicReviewsSettings | Unset = UNSET
    kobo_settings: KoboSettings | Unset = UNSET
    cover_cropping_settings: CoverCroppingSettings | Unset = UNSET
    metadata_provider_specific_fields: MetadataProviderSpecificFields | Unset = UNSET
    oidc_session_duration_hours: int | Unset = UNSET
    oidc_group_sync_mode: str | Unset = UNSET
    oidc_force_only_mode: bool | Unset = UNSET
    disk_type: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        default_metadata_refresh_options: dict[str, Any] | Unset = UNSET
        if not isinstance(self.default_metadata_refresh_options, Unset):
            default_metadata_refresh_options = self.default_metadata_refresh_options.to_dict()

        library_metadata_refresh_options: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.library_metadata_refresh_options, Unset):
            library_metadata_refresh_options = []
            for library_metadata_refresh_options_item_data in self.library_metadata_refresh_options:
                library_metadata_refresh_options_item = library_metadata_refresh_options_item_data.to_dict()
                library_metadata_refresh_options.append(library_metadata_refresh_options_item)

        auto_book_search = self.auto_book_search

        similar_book_recommendation = self.similar_book_recommendation

        opds_server_enabled = self.opds_server_enabled

        komga_api_enabled = self.komga_api_enabled

        komga_group_unknown = self.komga_group_unknown

        upload_pattern = self.upload_pattern

        pdf_cache_size_in_mb = self.pdf_cache_size_in_mb

        max_file_upload_size_in_mb = self.max_file_upload_size_in_mb

        remote_auth_enabled = self.remote_auth_enabled

        metadata_download_on_bookdrop = self.metadata_download_on_bookdrop

        oidc_enabled = self.oidc_enabled

        oidc_provider_details: dict[str, Any] | Unset = UNSET
        if not isinstance(self.oidc_provider_details, Unset):
            oidc_provider_details = self.oidc_provider_details.to_dict()

        oidc_redirect_uris: list[str] | Unset = UNSET
        if not isinstance(self.oidc_redirect_uris, Unset):
            oidc_redirect_uris = self.oidc_redirect_uris

        oidc_auto_provision_details: dict[str, Any] | Unset = UNSET
        if not isinstance(self.oidc_auto_provision_details, Unset):
            oidc_auto_provision_details = self.oidc_auto_provision_details.to_dict()

        metadata_provider_settings: dict[str, Any] | Unset = UNSET
        if not isinstance(self.metadata_provider_settings, Unset):
            metadata_provider_settings = self.metadata_provider_settings.to_dict()

        metadata_match_weights: dict[str, Any] | Unset = UNSET
        if not isinstance(self.metadata_match_weights, Unset):
            metadata_match_weights = self.metadata_match_weights.to_dict()

        metadata_persistence_settings: dict[str, Any] | Unset = UNSET
        if not isinstance(self.metadata_persistence_settings, Unset):
            metadata_persistence_settings = self.metadata_persistence_settings.to_dict()

        metadata_public_reviews_settings: dict[str, Any] | Unset = UNSET
        if not isinstance(self.metadata_public_reviews_settings, Unset):
            metadata_public_reviews_settings = self.metadata_public_reviews_settings.to_dict()

        kobo_settings: dict[str, Any] | Unset = UNSET
        if not isinstance(self.kobo_settings, Unset):
            kobo_settings = self.kobo_settings.to_dict()

        cover_cropping_settings: dict[str, Any] | Unset = UNSET
        if not isinstance(self.cover_cropping_settings, Unset):
            cover_cropping_settings = self.cover_cropping_settings.to_dict()

        metadata_provider_specific_fields: dict[str, Any] | Unset = UNSET
        if not isinstance(self.metadata_provider_specific_fields, Unset):
            metadata_provider_specific_fields = self.metadata_provider_specific_fields.to_dict()

        oidc_session_duration_hours = self.oidc_session_duration_hours

        oidc_group_sync_mode = self.oidc_group_sync_mode

        oidc_force_only_mode = self.oidc_force_only_mode

        disk_type = self.disk_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if default_metadata_refresh_options is not UNSET:
            field_dict["defaultMetadataRefreshOptions"] = default_metadata_refresh_options
        if library_metadata_refresh_options is not UNSET:
            field_dict["libraryMetadataRefreshOptions"] = library_metadata_refresh_options
        if auto_book_search is not UNSET:
            field_dict["autoBookSearch"] = auto_book_search
        if similar_book_recommendation is not UNSET:
            field_dict["similarBookRecommendation"] = similar_book_recommendation
        if opds_server_enabled is not UNSET:
            field_dict["opdsServerEnabled"] = opds_server_enabled
        if komga_api_enabled is not UNSET:
            field_dict["komgaApiEnabled"] = komga_api_enabled
        if komga_group_unknown is not UNSET:
            field_dict["komgaGroupUnknown"] = komga_group_unknown
        if upload_pattern is not UNSET:
            field_dict["uploadPattern"] = upload_pattern
        if pdf_cache_size_in_mb is not UNSET:
            field_dict["pdfCacheSizeInMb"] = pdf_cache_size_in_mb
        if max_file_upload_size_in_mb is not UNSET:
            field_dict["maxFileUploadSizeInMb"] = max_file_upload_size_in_mb
        if remote_auth_enabled is not UNSET:
            field_dict["remoteAuthEnabled"] = remote_auth_enabled
        if metadata_download_on_bookdrop is not UNSET:
            field_dict["metadataDownloadOnBookdrop"] = metadata_download_on_bookdrop
        if oidc_enabled is not UNSET:
            field_dict["oidcEnabled"] = oidc_enabled
        if oidc_provider_details is not UNSET:
            field_dict["oidcProviderDetails"] = oidc_provider_details
        if oidc_redirect_uris is not UNSET:
            field_dict["oidcRedirectUris"] = oidc_redirect_uris
        if oidc_auto_provision_details is not UNSET:
            field_dict["oidcAutoProvisionDetails"] = oidc_auto_provision_details
        if metadata_provider_settings is not UNSET:
            field_dict["metadataProviderSettings"] = metadata_provider_settings
        if metadata_match_weights is not UNSET:
            field_dict["metadataMatchWeights"] = metadata_match_weights
        if metadata_persistence_settings is not UNSET:
            field_dict["metadataPersistenceSettings"] = metadata_persistence_settings
        if metadata_public_reviews_settings is not UNSET:
            field_dict["metadataPublicReviewsSettings"] = metadata_public_reviews_settings
        if kobo_settings is not UNSET:
            field_dict["koboSettings"] = kobo_settings
        if cover_cropping_settings is not UNSET:
            field_dict["coverCroppingSettings"] = cover_cropping_settings
        if metadata_provider_specific_fields is not UNSET:
            field_dict["metadataProviderSpecificFields"] = metadata_provider_specific_fields
        if oidc_session_duration_hours is not UNSET:
            field_dict["oidcSessionDurationHours"] = oidc_session_duration_hours
        if oidc_group_sync_mode is not UNSET:
            field_dict["oidcGroupSyncMode"] = oidc_group_sync_mode
        if oidc_force_only_mode is not UNSET:
            field_dict["oidcForceOnlyMode"] = oidc_force_only_mode
        if disk_type is not UNSET:
            field_dict["diskType"] = disk_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cover_cropping_settings import CoverCroppingSettings
        from ..models.kobo_settings import KoboSettings
        from ..models.metadata_match_weights import MetadataMatchWeights
        from ..models.metadata_persistence_settings import MetadataPersistenceSettings
        from ..models.metadata_provider_settings import MetadataProviderSettings
        from ..models.metadata_provider_specific_fields import MetadataProviderSpecificFields
        from ..models.metadata_public_reviews_settings import MetadataPublicReviewsSettings
        from ..models.metadata_refresh_options import MetadataRefreshOptions
        from ..models.oidc_auto_provision_details import OidcAutoProvisionDetails
        from ..models.oidc_provider_details import OidcProviderDetails

        d = dict(src_dict)
        _default_metadata_refresh_options = d.pop("defaultMetadataRefreshOptions", UNSET)
        default_metadata_refresh_options: MetadataRefreshOptions | Unset
        if isinstance(_default_metadata_refresh_options, Unset):
            default_metadata_refresh_options = UNSET
        else:
            default_metadata_refresh_options = MetadataRefreshOptions.from_dict(_default_metadata_refresh_options)

        _library_metadata_refresh_options = d.pop("libraryMetadataRefreshOptions", UNSET)
        library_metadata_refresh_options: list[MetadataRefreshOptions] | Unset = UNSET
        if _library_metadata_refresh_options is not UNSET:
            library_metadata_refresh_options = []
            for library_metadata_refresh_options_item_data in _library_metadata_refresh_options:
                library_metadata_refresh_options_item = MetadataRefreshOptions.from_dict(
                    library_metadata_refresh_options_item_data
                )

                library_metadata_refresh_options.append(library_metadata_refresh_options_item)

        auto_book_search = d.pop("autoBookSearch", UNSET)

        similar_book_recommendation = d.pop("similarBookRecommendation", UNSET)

        opds_server_enabled = d.pop("opdsServerEnabled", UNSET)

        komga_api_enabled = d.pop("komgaApiEnabled", UNSET)

        komga_group_unknown = d.pop("komgaGroupUnknown", UNSET)

        upload_pattern = d.pop("uploadPattern", UNSET)

        pdf_cache_size_in_mb = d.pop("pdfCacheSizeInMb", UNSET)

        max_file_upload_size_in_mb = d.pop("maxFileUploadSizeInMb", UNSET)

        remote_auth_enabled = d.pop("remoteAuthEnabled", UNSET)

        metadata_download_on_bookdrop = d.pop("metadataDownloadOnBookdrop", UNSET)

        oidc_enabled = d.pop("oidcEnabled", UNSET)

        _oidc_provider_details = d.pop("oidcProviderDetails", UNSET)
        oidc_provider_details: OidcProviderDetails | Unset
        if isinstance(_oidc_provider_details, Unset):
            oidc_provider_details = UNSET
        else:
            oidc_provider_details = OidcProviderDetails.from_dict(_oidc_provider_details)

        oidc_redirect_uris = cast(list[str], d.pop("oidcRedirectUris", UNSET))

        _oidc_auto_provision_details = d.pop("oidcAutoProvisionDetails", UNSET)
        oidc_auto_provision_details: OidcAutoProvisionDetails | Unset
        if isinstance(_oidc_auto_provision_details, Unset):
            oidc_auto_provision_details = UNSET
        else:
            oidc_auto_provision_details = OidcAutoProvisionDetails.from_dict(_oidc_auto_provision_details)

        _metadata_provider_settings = d.pop("metadataProviderSettings", UNSET)
        metadata_provider_settings: MetadataProviderSettings | Unset
        if isinstance(_metadata_provider_settings, Unset):
            metadata_provider_settings = UNSET
        else:
            metadata_provider_settings = MetadataProviderSettings.from_dict(_metadata_provider_settings)

        _metadata_match_weights = d.pop("metadataMatchWeights", UNSET)
        metadata_match_weights: MetadataMatchWeights | Unset
        if isinstance(_metadata_match_weights, Unset):
            metadata_match_weights = UNSET
        else:
            metadata_match_weights = MetadataMatchWeights.from_dict(_metadata_match_weights)

        _metadata_persistence_settings = d.pop("metadataPersistenceSettings", UNSET)
        metadata_persistence_settings: MetadataPersistenceSettings | Unset
        if isinstance(_metadata_persistence_settings, Unset):
            metadata_persistence_settings = UNSET
        else:
            metadata_persistence_settings = MetadataPersistenceSettings.from_dict(_metadata_persistence_settings)

        _metadata_public_reviews_settings = d.pop("metadataPublicReviewsSettings", UNSET)
        metadata_public_reviews_settings: MetadataPublicReviewsSettings | Unset
        if isinstance(_metadata_public_reviews_settings, Unset):
            metadata_public_reviews_settings = UNSET
        else:
            metadata_public_reviews_settings = MetadataPublicReviewsSettings.from_dict(
                _metadata_public_reviews_settings
            )

        _kobo_settings = d.pop("koboSettings", UNSET)
        kobo_settings: KoboSettings | Unset
        if isinstance(_kobo_settings, Unset):
            kobo_settings = UNSET
        else:
            kobo_settings = KoboSettings.from_dict(_kobo_settings)

        _cover_cropping_settings = d.pop("coverCroppingSettings", UNSET)
        cover_cropping_settings: CoverCroppingSettings | Unset
        if isinstance(_cover_cropping_settings, Unset):
            cover_cropping_settings = UNSET
        else:
            cover_cropping_settings = CoverCroppingSettings.from_dict(_cover_cropping_settings)

        _metadata_provider_specific_fields = d.pop("metadataProviderSpecificFields", UNSET)
        metadata_provider_specific_fields: MetadataProviderSpecificFields | Unset
        if isinstance(_metadata_provider_specific_fields, Unset):
            metadata_provider_specific_fields = UNSET
        else:
            metadata_provider_specific_fields = MetadataProviderSpecificFields.from_dict(
                _metadata_provider_specific_fields
            )

        oidc_session_duration_hours = d.pop("oidcSessionDurationHours", UNSET)

        oidc_group_sync_mode = d.pop("oidcGroupSyncMode", UNSET)

        oidc_force_only_mode = d.pop("oidcForceOnlyMode", UNSET)

        disk_type = d.pop("diskType", UNSET)

        app_settings = cls(
            default_metadata_refresh_options=default_metadata_refresh_options,
            library_metadata_refresh_options=library_metadata_refresh_options,
            auto_book_search=auto_book_search,
            similar_book_recommendation=similar_book_recommendation,
            opds_server_enabled=opds_server_enabled,
            komga_api_enabled=komga_api_enabled,
            komga_group_unknown=komga_group_unknown,
            upload_pattern=upload_pattern,
            pdf_cache_size_in_mb=pdf_cache_size_in_mb,
            max_file_upload_size_in_mb=max_file_upload_size_in_mb,
            remote_auth_enabled=remote_auth_enabled,
            metadata_download_on_bookdrop=metadata_download_on_bookdrop,
            oidc_enabled=oidc_enabled,
            oidc_provider_details=oidc_provider_details,
            oidc_redirect_uris=oidc_redirect_uris,
            oidc_auto_provision_details=oidc_auto_provision_details,
            metadata_provider_settings=metadata_provider_settings,
            metadata_match_weights=metadata_match_weights,
            metadata_persistence_settings=metadata_persistence_settings,
            metadata_public_reviews_settings=metadata_public_reviews_settings,
            kobo_settings=kobo_settings,
            cover_cropping_settings=cover_cropping_settings,
            metadata_provider_specific_fields=metadata_provider_specific_fields,
            oidc_session_duration_hours=oidc_session_duration_hours,
            oidc_group_sync_mode=oidc_group_sync_mode,
            oidc_force_only_mode=oidc_force_only_mode,
            disk_type=disk_type,
        )

        app_settings.additional_properties = d
        return app_settings

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
