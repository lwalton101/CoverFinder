"""Contains all the data models used in inputs/outputs"""

from .access_token_dto import AccessTokenDto
from .additional_file_upload_additional_file_body import AdditionalFileUploadAdditionalFileBody
from .additional_file_upload_additional_file_book_type import AdditionalFileUploadAdditionalFileBookType
from .amazon import Amazon
from .annotation import Annotation
from .app_author_detail import AppAuthorDetail
from .app_author_summary import AppAuthorSummary
from .app_book_detail import AppBookDetail
from .app_book_file import AppBookFile
from .app_book_progress_response import AppBookProgressResponse
from .app_book_summary import AppBookSummary
from .app_filter_options import AppFilterOptions
from .app_library_summary import AppLibrarySummary
from .app_library_summary_allowed_formats_item import AppLibrarySummaryAllowedFormatsItem
from .app_magic_shelf_summary import AppMagicShelfSummary
from .app_notebook_book_summary import AppNotebookBookSummary
from .app_notebook_entry import AppNotebookEntry
from .app_notebook_update_request import AppNotebookUpdateRequest
from .app_page_response_app_author_summary import AppPageResponseAppAuthorSummary
from .app_page_response_app_book_summary import AppPageResponseAppBookSummary
from .app_page_response_app_notebook_book_summary import AppPageResponseAppNotebookBookSummary
from .app_page_response_app_notebook_entry import AppPageResponseAppNotebookEntry
from .app_page_response_app_series_summary import AppPageResponseAppSeriesSummary
from .app_series_summary import AppSeriesSummary
from .app_settings import AppSettings
from .app_shelf_summary import AppShelfSummary
from .app_user_info import AppUserInfo
from .attach_book_file_request import AttachBookFileRequest
from .attach_book_file_response import AttachBookFileResponse
from .audible import Audible
from .audiobook_chapter import AudiobookChapter
from .audiobook_completion_entry import AudiobookCompletionEntry
from .audiobook_info import AudiobookInfo
from .audiobook_metadata import AudiobookMetadata
from .audiobook_progress import AudiobookProgress
from .audiobook_track import AudiobookTrack
from .audit_log_dto import AuditLogDto
from .audit_log_dto_action import AuditLogDtoAction
from .author_details import AuthorDetails
from .author_match_request import AuthorMatchRequest
from .author_match_request_source import AuthorMatchRequestSource
from .author_search_result import AuthorSearchResult
from .author_search_result_source import AuthorSearchResultSource
from .author_summary import AuthorSummary
from .author_update_request import AuthorUpdateRequest
from .book import Book
from .book_completion_heatmap_response import BookCompletionHeatmapResponse
from .book_deletion_response import BookDeletionResponse
from .book_distributions_response import BookDistributionsResponse
from .book_file import BookFile
from .book_file_archive_type import BookFileArchiveType
from .book_file_book_type import BookFileBookType
from .book_file_progress import BookFileProgress
from .book_list_request import BookListRequest
from .book_lore_user import BookLoreUser
from .book_lore_user_provisioning_method import BookLoreUserProvisioningMethod
from .book_mark import BookMark
from .book_metadata import BookMetadata
from .book_metadata_provider import BookMetadataProvider
from .book_note import BookNote
from .book_note_v2 import BookNoteV2
from .book_recommendation import BookRecommendation
from .book_review import BookReview
from .book_review_metadata_provider import BookReviewMetadataProvider
from .book_status_update_response import BookStatusUpdateResponse
from .book_status_update_response_read_status import BookStatusUpdateResponseReadStatus
from .book_timeline_response import BookTimelineResponse
from .book_viewer_settings import BookViewerSettings
from .bookdrop_bulk_edit_request import BookdropBulkEditRequest
from .bookdrop_bulk_edit_result import BookdropBulkEditResult
from .bookdrop_file import BookdropFile
from .bookdrop_file_notification import BookdropFileNotification
from .bookdrop_file_result import BookdropFileResult
from .bookdrop_file_status import BookdropFileStatus
from .bookdrop_finalize_file import BookdropFinalizeFile
from .bookdrop_finalize_request import BookdropFinalizeRequest
from .bookdrop_finalize_result import BookdropFinalizeResult
from .bookdrop_pattern_extract_request import BookdropPatternExtractRequest
from .bookdrop_pattern_extract_result import BookdropPatternExtractResult
from .bookdrop_selection_request import BookdropSelectionRequest
from .bulk_book_ids_request import BulkBookIdsRequest
from .bulk_metadata_update_request import BulkMetadataUpdateRequest
from .bulk_upload_cover_body import BulkUploadCoverBody
from .catch_all_1_body import CatchAll1Body
from .catch_all_2_body import CatchAll2Body
from .catch_all_3_body import CatchAll3Body
from .catch_all_4_body import CatchAll4Body
from .catch_all_body import CatchAllBody
from .cbx_page_dimension import CbxPageDimension
from .cbx_page_info import CbxPageInfo
from .cbx_progress import CbxProgress
from .cbx_reader_setting import CbxReaderSetting
from .cbx_reader_setting_background_color import CbxReaderSettingBackgroundColor
from .cbx_reader_setting_fit_mode import CbxReaderSettingFitMode
from .cbx_reader_setting_page_spread import CbxReaderSettingPageSpread
from .cbx_reader_setting_page_view_mode import CbxReaderSettingPageViewMode
from .cbx_reader_setting_scroll_mode import CbxReaderSettingScrollMode
from .cbx_viewer_preferences import CbxViewerPreferences
from .cbx_viewer_preferences_background_color import CbxViewerPreferencesBackgroundColor
from .cbx_viewer_preferences_fit_mode import CbxViewerPreferencesFitMode
from .cbx_viewer_preferences_page_spread import CbxViewerPreferencesPageSpread
from .cbx_viewer_preferences_page_view_mode import CbxViewerPreferencesPageViewMode
from .cbx_viewer_preferences_scroll_mode import CbxViewerPreferencesScrollMode
from .change_password_request import ChangePasswordRequest
from .change_user_password_request import ChangeUserPasswordRequest
from .chapter_info import ChapterInfo
from .claim_mapping import ClaimMapping
from .comic_metadata import ComicMetadata
from .comicvine import Comicvine
from .completion_race_response import CompletionRaceResponse
from .completion_timeline_response import CompletionTimelineResponse
from .completion_timeline_response_status_breakdown import CompletionTimelineResponseStatusBreakdown
from .content_disposition import ContentDisposition
from .content_restriction import ContentRestriction
from .content_restriction_mode import ContentRestrictionMode
from .content_restriction_restriction_type import ContentRestrictionRestrictionType
from .counted_option import CountedOption
from .cover_cropping_settings import CoverCroppingSettings
from .cover_fetch_request import CoverFetchRequest
from .cover_image import CoverImage
from .create_annotation_request import CreateAnnotationRequest
from .create_book_mark_request import CreateBookMarkRequest
from .create_book_note_request import CreateBookNoteRequest
from .create_book_note_v2_request import CreateBookNoteV2Request
from .create_email_provider_request import CreateEmailProviderRequest
from .create_email_recipient_request import CreateEmailRecipientRequest
from .create_library_request import CreateLibraryRequest
from .create_library_request_allowed_formats_item import CreateLibraryRequestAllowedFormatsItem
from .create_library_request_format_priority_item import CreateLibraryRequestFormatPriorityItem
from .create_library_request_icon_type import CreateLibraryRequestIconType
from .create_library_request_metadata_source import CreateLibraryRequestMetadataSource
from .create_library_request_organization_mode import CreateLibraryRequestOrganizationMode
from .create_physical_book_request import CreatePhysicalBookRequest
from .create_user_1_body import CreateUser1Body
from .cron_config import CronConfig
from .cron_config_task_type import CronConfigTaskType
from .current_bookmark import CurrentBookmark
from .custom_font_dto import CustomFontDto
from .custom_font_dto_format import CustomFontDtoFormat
from .dashboard_config import DashboardConfig
from .delete_metadata_request import DeleteMetadataRequest
from .delete_metadata_request_metadata_type import DeleteMetadataRequestMetadataType
from .detach_book_file_request import DetachBookFileRequest
from .detach_book_file_response import DetachBookFileResponse
from .douban import Douban
from .duplicate_detection_request import DuplicateDetectionRequest
from .duplicate_group import DuplicateGroup
from .ebook_reader_setting import EbookReaderSetting
from .ebook_viewer_preferences import EbookViewerPreferences
from .email_provider_v2 import EmailProviderV2
from .email_recipient_v2 import EmailRecipientV2
from .enabled_fields import EnabledFields
from .entity_view_preferences import EntityViewPreferences
from .epub_book_info import EpubBookInfo
from .epub_book_info_metadata import EpubBookInfoMetadata
from .epub_manifest_item import EpubManifestItem
from .epub_progress import EpubProgress
from .epub_reader_setting import EpubReaderSetting
from .epub_spine_item import EpubSpineItem
from .epub_toc_item import EpubTocItem
from .favorite_reading_days_response import FavoriteReadingDaysResponse
from .fetch_metadata_request import FetchMetadataRequest
from .fetch_metadata_request_providers_item import FetchMetadataRequestProvidersItem
from .fetched_proposal import FetchedProposal
from .fetched_proposal_status import FetchedProposalStatus
from .field_options import FieldOptions
from .field_provider import FieldProvider
from .field_provider_p1 import FieldProviderP1
from .field_provider_p2 import FieldProviderP2
from .field_provider_p3 import FieldProviderP3
from .field_provider_p4 import FieldProviderP4
from .file_extraction_result import FileExtractionResult
from .file_move_request import FileMoveRequest
from .format_settings import FormatSettings
from .genre_statistics_response import GenreStatisticsResponse
from .get_audit_logs_action import GetAuditLogsAction
from .get_detailed_provider_metadata_provider import GetDetailedProviderMetadataProvider
from .get_tests_body import GetTestsBody
from .global_preferences import GlobalPreferences
from .goodreads import Goodreads
from .google import Google
from .hardcover import Hardcover
from .hardcover_sync_settings import HardcoverSyncSettings
from .healthcheck_response import HealthcheckResponse
from .http_headers import HttpHeaders
from .http_headers_accept_language_item import HttpHeadersAcceptLanguageItem
from .http_headers_all import HttpHeadersAll
from .http_headers_host import HttpHeadersHost
from .http_headers_host_address import HttpHeadersHostAddress
from .icon_save_result import IconSaveResult
from .initial_user_request import InitialUserRequest
from .isbn_lookup_request import IsbnLookupRequest
from .json_node import JsonNode
from .json_node_node_type import JsonNodeNodeType
from .ko_progress import KoProgress
from .kobo_progress import KoboProgress
from .kobo_reading_state import KoboReadingState
from .kobo_reading_state_request import KoboReadingStateRequest
from .kobo_resources import KoboResources
from .kobo_settings import KoboSettings
from .kobo_sync_settings import KoboSyncSettings
from .koreader_progress import KoreaderProgress
from .koreader_user import KoreaderUser
from .language_option import LanguageOption
from .library import Library
from .library_allowed_formats_item import LibraryAllowedFormatsItem
from .library_format_priority_item import LibraryFormatPriorityItem
from .library_icon_type import LibraryIconType
from .library_metadata_source import LibraryMetadataSource
from .library_organization_mode import LibraryOrganizationMode
from .library_path import LibraryPath
from .listening_author_response import ListeningAuthorResponse
from .listening_completion_response import ListeningCompletionResponse
from .listening_finish_funnel_response import ListeningFinishFunnelResponse
from .listening_heatmap_response import ListeningHeatmapResponse
from .location import Location
from .logout_request import LogoutRequest
from .logout_response import LogoutResponse
from .longest_audiobook_response import LongestAudiobookResponse
from .lubimyczytac import Lubimyczytac
from .magic_shelf import MagicShelf
from .magic_shelf_icon_type import MagicShelfIconType
from .media_type import MediaType
from .media_type_parameters import MediaTypeParameters
from .merge_metadata_request import MergeMetadataRequest
from .merge_metadata_request_metadata_type import MergeMetadataRequestMetadataType
from .metadata_batch_progress_notification import MetadataBatchProgressNotification
from .metadata_clear_flags import MetadataClearFlags
from .metadata_fetch_task import MetadataFetchTask
from .metadata_fetch_task_status import MetadataFetchTaskStatus
from .metadata_match_weights import MetadataMatchWeights
from .metadata_persistence_settings import MetadataPersistenceSettings
from .metadata_provider_settings import MetadataProviderSettings
from .metadata_provider_specific_fields import MetadataProviderSpecificFields
from .metadata_public_reviews_settings import MetadataPublicReviewsSettings
from .metadata_refresh_options import MetadataRefreshOptions
from .metadata_refresh_options_replace_mode import MetadataRefreshOptionsReplaceMode
from .metadata_task_details_response import MetadataTaskDetailsResponse
from .metadata_update_wrapper import MetadataUpdateWrapper
from .monthly_pace_response import MonthlyPaceResponse
from .move import Move
from .new_pdf_reader_setting import NewPdfReaderSetting
from .new_pdf_reader_setting_background_color import NewPdfReaderSettingBackgroundColor
from .new_pdf_reader_setting_fit_mode import NewPdfReaderSettingFitMode
from .new_pdf_reader_setting_page_spread import NewPdfReaderSettingPageSpread
from .new_pdf_reader_setting_page_view_mode import NewPdfReaderSettingPageViewMode
from .new_pdf_reader_setting_scroll_mode import NewPdfReaderSettingScrollMode
from .new_pdf_viewer_preferences import NewPdfViewerPreferences
from .new_pdf_viewer_preferences_background_color import NewPdfViewerPreferencesBackgroundColor
from .new_pdf_viewer_preferences_fit_mode import NewPdfViewerPreferencesFitMode
from .new_pdf_viewer_preferences_page_spread import NewPdfViewerPreferencesPageSpread
from .new_pdf_viewer_preferences_page_view_mode import NewPdfViewerPreferencesPageViewMode
from .new_pdf_viewer_preferences_scroll_mode import NewPdfViewerPreferencesScrollMode
from .notebook_book_option import NotebookBookOption
from .notebook_entry import NotebookEntry
from .oidc_auto_provision_details import OidcAutoProvisionDetails
from .oidc_backchannel_logout_body import OidcBackchannelLogoutBody
from .oidc_callback_request import OidcCallbackRequest
from .oidc_group_mapping import OidcGroupMapping
from .oidc_provider_details import OidcProviderDetails
from .oidc_test_check import OidcTestCheck
from .oidc_test_check_status import OidcTestCheckStatus
from .oidc_test_result import OidcTestResult
from .opds_user_v2 import OpdsUserV2
from .opds_user_v2_create_request import OpdsUserV2CreateRequest
from .opds_user_v2_create_request_sort_order import OpdsUserV2CreateRequestSortOrder
from .opds_user_v2_sort_order import OpdsUserV2SortOrder
from .opds_user_v2_update_request import OpdsUserV2UpdateRequest
from .opds_user_v2_update_request_sort_order import OpdsUserV2UpdateRequestSortOrder
from .override_details import OverrideDetails
from .override_preference import OverridePreference
from .page_metadata import PageMetadata
from .page_turner_score_response import PageTurnerScoreResponse
from .pageable import Pageable
from .paged_model_audit_log_dto import PagedModelAuditLogDto
from .paged_model_book import PagedModelBook
from .paged_model_bookdrop_file import PagedModelBookdropFile
from .paged_model_notebook_entry import PagedModelNotebookEntry
from .paged_model_reading_session_response import PagedModelReadingSessionResponse
from .paged_model_string import PagedModelString
from .path_summary import PathSummary
from .pdf_book_info import PdfBookInfo
from .pdf_outline_item import PdfOutlineItem
from .pdf_progress import PdfProgress
from .pdf_reader_setting import PdfReaderSetting
from .pdf_viewer_preferences import PdfViewerPreferences
from .peak_hours_response import PeakHoursResponse
from .per_book_setting import PerBookSetting
from .per_book_setting_cbx import PerBookSettingCbx
from .per_book_setting_epub import PerBookSettingEpub
from .per_book_setting_new_pdf import PerBookSettingNewPdf
from .per_book_setting_pdf import PerBookSettingPdf
from .permissions import Permissions
from .personal_rating_update_request import PersonalRatingUpdateRequest
from .personal_rating_update_response import PersonalRatingUpdateResponse
from .progress_bucket import ProgressBucket
from .public_app_setting import PublicAppSetting
from .ranobedb import Ranobedb
from .rating_bucket import RatingBucket
from .read_progress_request import ReadProgressRequest
from .read_status_update_request import ReadStatusUpdateRequest
from .reading_session_heatmap_response import ReadingSessionHeatmapResponse
from .reading_session_request import ReadingSessionRequest
from .reading_session_request_book_type import ReadingSessionRequestBookType
from .reading_session_response import ReadingSessionResponse
from .reading_session_response_book_type import ReadingSessionResponseBookType
from .reading_session_timeline_response import ReadingSessionTimelineResponse
from .reading_session_timeline_response_book_type import ReadingSessionTimelineResponseBookType
from .reading_speed_response import ReadingSpeedResponse
from .reading_streak_day import ReadingStreakDay
from .reading_streak_response import ReadingStreakResponse
from .refresh_token_request import RefreshTokenRequest
from .release_note import ReleaseNote
from .reset_progress_type import ResetProgressType
from .review_provider_config import ReviewProviderConfig
from .review_provider_config_provider import ReviewProviderConfigProvider
from .save_annotations_body import SaveAnnotationsBody
from .save_to_original_file import SaveToOriginalFile
from .scroller_config import ScrollerConfig
from .send_book_by_email_request import SendBookByEmailRequest
from .series_cover_book import SeriesCoverBook
from .session_scatter_response import SessionScatterResponse
from .set_file_naming_pattern_body import SetFileNamingPatternBody
from .setting_request import SettingRequest
from .shelf import Shelf
from .shelf_create_request import ShelfCreateRequest
from .shelf_create_request_icon_type import ShelfCreateRequestIconType
from .shelf_icon_type import ShelfIconType
from .shelves_assignment_request import ShelvesAssignmentRequest
from .sidebar_sort_option import SidebarSortOption
from .sidecar_book_metadata import SidecarBookMetadata
from .sidecar_cover_info import SidecarCoverInfo
from .sidecar_identifiers import SidecarIdentifiers
from .sidecar_metadata import SidecarMetadata
from .sidecar_rating import SidecarRating
from .sidecar_ratings import SidecarRatings
from .sidecar_series import SidecarSeries
from .sidecar_settings import SidecarSettings
from .sort import Sort
from .sort_criterion import SortCriterion
from .sort_direction import SortDirection
from .statistics import Statistics
from .status_bucket import StatusBucket
from .status_info import StatusInfo
from .status_info_status import StatusInfoStatus
from .success_response_healthcheck_response import SuccessResponseHealthcheckResponse
from .svg_icon_batch_request import SvgIconBatchRequest
from .svg_icon_batch_response import SvgIconBatchResponse
from .svg_icon_create_request import SvgIconCreateRequest
from .table_column_preference import TableColumnPreference
from .task_cancel_response import TaskCancelResponse
from .task_create_request import TaskCreateRequest
from .task_create_request_task_type import TaskCreateRequestTaskType
from .task_create_response import TaskCreateResponse
from .task_create_response_status import TaskCreateResponseStatus
from .task_create_response_task_type import TaskCreateResponseTaskType
from .task_cron_config_request import TaskCronConfigRequest
from .task_history import TaskHistory
from .task_history_status import TaskHistoryStatus
from .task_history_type import TaskHistoryType
from .task_info import TaskInfo
from .task_info_task_type import TaskInfoTaskType
from .task_patch_cron_config_task_type import TaskPatchCronConfigTaskType
from .tasks_history_response import TasksHistoryResponse
from .toggle_all_lock_request import ToggleAllLockRequest
from .toggle_all_lock_request_lock import ToggleAllLockRequestLock
from .toggle_field_locks_request import ToggleFieldLocksRequest
from .toggle_field_locks_request_field_actions import ToggleFieldLocksRequestFieldActions
from .update_annotation_request import UpdateAnnotationRequest
from .update_book_mark_request import UpdateBookMarkRequest
from .update_book_note_v2_request import UpdateBookNoteV2Request
from .update_metadata_replace_mode import UpdateMetadataReplaceMode
from .update_progress_request import UpdateProgressRequest
from .update_rating_request import UpdateRatingRequest
from .update_status_request import UpdateStatusRequest
from .update_status_request_status import UpdateStatusRequestStatus
from .update_user_setting_request import UpdateUserSettingRequest
from .upload_audiobook_cover_from_file_body import UploadAudiobookCoverFromFileBody
from .upload_audiobook_cover_from_url_body import UploadAudiobookCoverFromUrlBody
from .upload_author_photo_body import UploadAuthorPhotoBody
from .upload_cover_from_file_body import UploadCoverFromFileBody
from .upload_cover_from_url_body import UploadCoverFromUrlBody
from .upload_file_1_body import UploadFile1Body
from .upload_file_body import UploadFileBody
from .upload_font_body import UploadFontBody
from .upsert_current_user_body import UpsertCurrentUserBody
from .user_create_request import UserCreateRequest
from .user_login_request import UserLoginRequest
from .user_permissions import UserPermissions
from .user_profile_update_request import UserProfileUpdateRequest
from .user_settings import UserSettings
from .user_update_request import UserUpdateRequest
from .version_info import VersionInfo
from .weekly_listening_trend_response import WeeklyListeningTrendResponse

__all__ = (
    "AccessTokenDto",
    "AdditionalFileUploadAdditionalFileBody",
    "AdditionalFileUploadAdditionalFileBookType",
    "Amazon",
    "Annotation",
    "AppAuthorDetail",
    "AppAuthorSummary",
    "AppBookDetail",
    "AppBookFile",
    "AppBookProgressResponse",
    "AppBookSummary",
    "AppFilterOptions",
    "AppLibrarySummary",
    "AppLibrarySummaryAllowedFormatsItem",
    "AppMagicShelfSummary",
    "AppNotebookBookSummary",
    "AppNotebookEntry",
    "AppNotebookUpdateRequest",
    "AppPageResponseAppAuthorSummary",
    "AppPageResponseAppBookSummary",
    "AppPageResponseAppNotebookBookSummary",
    "AppPageResponseAppNotebookEntry",
    "AppPageResponseAppSeriesSummary",
    "AppSeriesSummary",
    "AppSettings",
    "AppShelfSummary",
    "AppUserInfo",
    "AttachBookFileRequest",
    "AttachBookFileResponse",
    "Audible",
    "AudiobookChapter",
    "AudiobookCompletionEntry",
    "AudiobookInfo",
    "AudiobookMetadata",
    "AudiobookProgress",
    "AudiobookTrack",
    "AuditLogDto",
    "AuditLogDtoAction",
    "AuthorDetails",
    "AuthorMatchRequest",
    "AuthorMatchRequestSource",
    "AuthorSearchResult",
    "AuthorSearchResultSource",
    "AuthorSummary",
    "AuthorUpdateRequest",
    "Book",
    "BookCompletionHeatmapResponse",
    "BookDeletionResponse",
    "BookDistributionsResponse",
    "BookdropBulkEditRequest",
    "BookdropBulkEditResult",
    "BookdropFile",
    "BookdropFileNotification",
    "BookdropFileResult",
    "BookdropFileStatus",
    "BookdropFinalizeFile",
    "BookdropFinalizeRequest",
    "BookdropFinalizeResult",
    "BookdropPatternExtractRequest",
    "BookdropPatternExtractResult",
    "BookdropSelectionRequest",
    "BookFile",
    "BookFileArchiveType",
    "BookFileBookType",
    "BookFileProgress",
    "BookListRequest",
    "BookLoreUser",
    "BookLoreUserProvisioningMethod",
    "BookMark",
    "BookMetadata",
    "BookMetadataProvider",
    "BookNote",
    "BookNoteV2",
    "BookRecommendation",
    "BookReview",
    "BookReviewMetadataProvider",
    "BookStatusUpdateResponse",
    "BookStatusUpdateResponseReadStatus",
    "BookTimelineResponse",
    "BookViewerSettings",
    "BulkBookIdsRequest",
    "BulkMetadataUpdateRequest",
    "BulkUploadCoverBody",
    "CatchAll1Body",
    "CatchAll2Body",
    "CatchAll3Body",
    "CatchAll4Body",
    "CatchAllBody",
    "CbxPageDimension",
    "CbxPageInfo",
    "CbxProgress",
    "CbxReaderSetting",
    "CbxReaderSettingBackgroundColor",
    "CbxReaderSettingFitMode",
    "CbxReaderSettingPageSpread",
    "CbxReaderSettingPageViewMode",
    "CbxReaderSettingScrollMode",
    "CbxViewerPreferences",
    "CbxViewerPreferencesBackgroundColor",
    "CbxViewerPreferencesFitMode",
    "CbxViewerPreferencesPageSpread",
    "CbxViewerPreferencesPageViewMode",
    "CbxViewerPreferencesScrollMode",
    "ChangePasswordRequest",
    "ChangeUserPasswordRequest",
    "ChapterInfo",
    "ClaimMapping",
    "ComicMetadata",
    "Comicvine",
    "CompletionRaceResponse",
    "CompletionTimelineResponse",
    "CompletionTimelineResponseStatusBreakdown",
    "ContentDisposition",
    "ContentRestriction",
    "ContentRestrictionMode",
    "ContentRestrictionRestrictionType",
    "CountedOption",
    "CoverCroppingSettings",
    "CoverFetchRequest",
    "CoverImage",
    "CreateAnnotationRequest",
    "CreateBookMarkRequest",
    "CreateBookNoteRequest",
    "CreateBookNoteV2Request",
    "CreateEmailProviderRequest",
    "CreateEmailRecipientRequest",
    "CreateLibraryRequest",
    "CreateLibraryRequestAllowedFormatsItem",
    "CreateLibraryRequestFormatPriorityItem",
    "CreateLibraryRequestIconType",
    "CreateLibraryRequestMetadataSource",
    "CreateLibraryRequestOrganizationMode",
    "CreatePhysicalBookRequest",
    "CreateUser1Body",
    "CronConfig",
    "CronConfigTaskType",
    "CurrentBookmark",
    "CustomFontDto",
    "CustomFontDtoFormat",
    "DashboardConfig",
    "DeleteMetadataRequest",
    "DeleteMetadataRequestMetadataType",
    "DetachBookFileRequest",
    "DetachBookFileResponse",
    "Douban",
    "DuplicateDetectionRequest",
    "DuplicateGroup",
    "EbookReaderSetting",
    "EbookViewerPreferences",
    "EmailProviderV2",
    "EmailRecipientV2",
    "EnabledFields",
    "EntityViewPreferences",
    "EpubBookInfo",
    "EpubBookInfoMetadata",
    "EpubManifestItem",
    "EpubProgress",
    "EpubReaderSetting",
    "EpubSpineItem",
    "EpubTocItem",
    "FavoriteReadingDaysResponse",
    "FetchedProposal",
    "FetchedProposalStatus",
    "FetchMetadataRequest",
    "FetchMetadataRequestProvidersItem",
    "FieldOptions",
    "FieldProvider",
    "FieldProviderP1",
    "FieldProviderP2",
    "FieldProviderP3",
    "FieldProviderP4",
    "FileExtractionResult",
    "FileMoveRequest",
    "FormatSettings",
    "GenreStatisticsResponse",
    "GetAuditLogsAction",
    "GetDetailedProviderMetadataProvider",
    "GetTestsBody",
    "GlobalPreferences",
    "Goodreads",
    "Google",
    "Hardcover",
    "HardcoverSyncSettings",
    "HealthcheckResponse",
    "HttpHeaders",
    "HttpHeadersAcceptLanguageItem",
    "HttpHeadersAll",
    "HttpHeadersHost",
    "HttpHeadersHostAddress",
    "IconSaveResult",
    "InitialUserRequest",
    "IsbnLookupRequest",
    "JsonNode",
    "JsonNodeNodeType",
    "KoboProgress",
    "KoboReadingState",
    "KoboReadingStateRequest",
    "KoboResources",
    "KoboSettings",
    "KoboSyncSettings",
    "KoProgress",
    "KoreaderProgress",
    "KoreaderUser",
    "LanguageOption",
    "Library",
    "LibraryAllowedFormatsItem",
    "LibraryFormatPriorityItem",
    "LibraryIconType",
    "LibraryMetadataSource",
    "LibraryOrganizationMode",
    "LibraryPath",
    "ListeningAuthorResponse",
    "ListeningCompletionResponse",
    "ListeningFinishFunnelResponse",
    "ListeningHeatmapResponse",
    "Location",
    "LogoutRequest",
    "LogoutResponse",
    "LongestAudiobookResponse",
    "Lubimyczytac",
    "MagicShelf",
    "MagicShelfIconType",
    "MediaType",
    "MediaTypeParameters",
    "MergeMetadataRequest",
    "MergeMetadataRequestMetadataType",
    "MetadataBatchProgressNotification",
    "MetadataClearFlags",
    "MetadataFetchTask",
    "MetadataFetchTaskStatus",
    "MetadataMatchWeights",
    "MetadataPersistenceSettings",
    "MetadataProviderSettings",
    "MetadataProviderSpecificFields",
    "MetadataPublicReviewsSettings",
    "MetadataRefreshOptions",
    "MetadataRefreshOptionsReplaceMode",
    "MetadataTaskDetailsResponse",
    "MetadataUpdateWrapper",
    "MonthlyPaceResponse",
    "Move",
    "NewPdfReaderSetting",
    "NewPdfReaderSettingBackgroundColor",
    "NewPdfReaderSettingFitMode",
    "NewPdfReaderSettingPageSpread",
    "NewPdfReaderSettingPageViewMode",
    "NewPdfReaderSettingScrollMode",
    "NewPdfViewerPreferences",
    "NewPdfViewerPreferencesBackgroundColor",
    "NewPdfViewerPreferencesFitMode",
    "NewPdfViewerPreferencesPageSpread",
    "NewPdfViewerPreferencesPageViewMode",
    "NewPdfViewerPreferencesScrollMode",
    "NotebookBookOption",
    "NotebookEntry",
    "OidcAutoProvisionDetails",
    "OidcBackchannelLogoutBody",
    "OidcCallbackRequest",
    "OidcGroupMapping",
    "OidcProviderDetails",
    "OidcTestCheck",
    "OidcTestCheckStatus",
    "OidcTestResult",
    "OpdsUserV2",
    "OpdsUserV2CreateRequest",
    "OpdsUserV2CreateRequestSortOrder",
    "OpdsUserV2SortOrder",
    "OpdsUserV2UpdateRequest",
    "OpdsUserV2UpdateRequestSortOrder",
    "OverrideDetails",
    "OverridePreference",
    "Pageable",
    "PagedModelAuditLogDto",
    "PagedModelBook",
    "PagedModelBookdropFile",
    "PagedModelNotebookEntry",
    "PagedModelReadingSessionResponse",
    "PagedModelString",
    "PageMetadata",
    "PageTurnerScoreResponse",
    "PathSummary",
    "PdfBookInfo",
    "PdfOutlineItem",
    "PdfProgress",
    "PdfReaderSetting",
    "PdfViewerPreferences",
    "PeakHoursResponse",
    "PerBookSetting",
    "PerBookSettingCbx",
    "PerBookSettingEpub",
    "PerBookSettingNewPdf",
    "PerBookSettingPdf",
    "Permissions",
    "PersonalRatingUpdateRequest",
    "PersonalRatingUpdateResponse",
    "ProgressBucket",
    "PublicAppSetting",
    "Ranobedb",
    "RatingBucket",
    "ReadingSessionHeatmapResponse",
    "ReadingSessionRequest",
    "ReadingSessionRequestBookType",
    "ReadingSessionResponse",
    "ReadingSessionResponseBookType",
    "ReadingSessionTimelineResponse",
    "ReadingSessionTimelineResponseBookType",
    "ReadingSpeedResponse",
    "ReadingStreakDay",
    "ReadingStreakResponse",
    "ReadProgressRequest",
    "ReadStatusUpdateRequest",
    "RefreshTokenRequest",
    "ReleaseNote",
    "ResetProgressType",
    "ReviewProviderConfig",
    "ReviewProviderConfigProvider",
    "SaveAnnotationsBody",
    "SaveToOriginalFile",
    "ScrollerConfig",
    "SendBookByEmailRequest",
    "SeriesCoverBook",
    "SessionScatterResponse",
    "SetFileNamingPatternBody",
    "SettingRequest",
    "Shelf",
    "ShelfCreateRequest",
    "ShelfCreateRequestIconType",
    "ShelfIconType",
    "ShelvesAssignmentRequest",
    "SidebarSortOption",
    "SidecarBookMetadata",
    "SidecarCoverInfo",
    "SidecarIdentifiers",
    "SidecarMetadata",
    "SidecarRating",
    "SidecarRatings",
    "SidecarSeries",
    "SidecarSettings",
    "Sort",
    "SortCriterion",
    "SortDirection",
    "Statistics",
    "StatusBucket",
    "StatusInfo",
    "StatusInfoStatus",
    "SuccessResponseHealthcheckResponse",
    "SvgIconBatchRequest",
    "SvgIconBatchResponse",
    "SvgIconCreateRequest",
    "TableColumnPreference",
    "TaskCancelResponse",
    "TaskCreateRequest",
    "TaskCreateRequestTaskType",
    "TaskCreateResponse",
    "TaskCreateResponseStatus",
    "TaskCreateResponseTaskType",
    "TaskCronConfigRequest",
    "TaskHistory",
    "TaskHistoryStatus",
    "TaskHistoryType",
    "TaskInfo",
    "TaskInfoTaskType",
    "TaskPatchCronConfigTaskType",
    "TasksHistoryResponse",
    "ToggleAllLockRequest",
    "ToggleAllLockRequestLock",
    "ToggleFieldLocksRequest",
    "ToggleFieldLocksRequestFieldActions",
    "UpdateAnnotationRequest",
    "UpdateBookMarkRequest",
    "UpdateBookNoteV2Request",
    "UpdateMetadataReplaceMode",
    "UpdateProgressRequest",
    "UpdateRatingRequest",
    "UpdateStatusRequest",
    "UpdateStatusRequestStatus",
    "UpdateUserSettingRequest",
    "UploadAudiobookCoverFromFileBody",
    "UploadAudiobookCoverFromUrlBody",
    "UploadAuthorPhotoBody",
    "UploadCoverFromFileBody",
    "UploadCoverFromUrlBody",
    "UploadFile1Body",
    "UploadFileBody",
    "UploadFontBody",
    "UpsertCurrentUserBody",
    "UserCreateRequest",
    "UserLoginRequest",
    "UserPermissions",
    "UserProfileUpdateRequest",
    "UserSettings",
    "UserUpdateRequest",
    "VersionInfo",
    "WeeklyListeningTrendResponse",
)
