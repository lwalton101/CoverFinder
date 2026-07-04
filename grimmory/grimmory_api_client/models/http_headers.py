from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.content_disposition import ContentDisposition
    from ..models.http_headers_accept_language_item import HttpHeadersAcceptLanguageItem
    from ..models.http_headers_all import HttpHeadersAll
    from ..models.http_headers_host import HttpHeadersHost
    from ..models.media_type import MediaType


T = TypeVar("T", bound="HttpHeaders")


@_attrs_define
class HttpHeaders:
    """
    Attributes:
        empty (bool | Unset):
        location (str | Unset):
        host (HttpHeadersHost | Unset):
        all_ (HttpHeadersAll | Unset):
        last_modified (int | Unset):
        date (int | Unset):
        content_length (int | Unset):
        content_disposition (ContentDisposition | Unset):
        accept_charset (list[str] | Unset):
        content_language (str | Unset):
        connection (list[str] | Unset):
        if_modified_since (int | Unset):
        content_type (MediaType | Unset):
        origin (str | Unset):
        range_ (list[Any] | Unset):
        bearer_auth (str | Unset):
        cache_control (str | Unset):
        expires (int | Unset):
        allow (list[Any] | Unset):
        accept_language (list[HttpHeadersAcceptLanguageItem] | Unset):
        basic_auth (str | Unset):
        accept (list[MediaType] | Unset):
        accept_language_as_locales (list[str] | Unset):
        accept_patch (list[MediaType] | Unset):
        access_control_allow_credentials (bool | Unset):
        access_control_allow_headers (list[str] | Unset):
        access_control_allow_methods (list[Any] | Unset):
        access_control_allow_origin (str | Unset):
        access_control_expose_headers (list[str] | Unset):
        access_control_max_age (int | Unset):
        access_control_request_headers (list[str] | Unset):
        access_control_request_method (Any | Unset):
        etag (str | Unset):
        if_match (list[str] | Unset):
        if_none_match (list[str] | Unset):
        if_unmodified_since (int | Unset):
        pragma (str | Unset):
        upgrade (str | Unset):
        vary (list[str] | Unset):
    """

    empty: bool | Unset = UNSET
    location: str | Unset = UNSET
    host: HttpHeadersHost | Unset = UNSET
    all_: HttpHeadersAll | Unset = UNSET
    last_modified: int | Unset = UNSET
    date: int | Unset = UNSET
    content_length: int | Unset = UNSET
    content_disposition: ContentDisposition | Unset = UNSET
    accept_charset: list[str] | Unset = UNSET
    content_language: str | Unset = UNSET
    connection: list[str] | Unset = UNSET
    if_modified_since: int | Unset = UNSET
    content_type: MediaType | Unset = UNSET
    origin: str | Unset = UNSET
    range_: list[Any] | Unset = UNSET
    bearer_auth: str | Unset = UNSET
    cache_control: str | Unset = UNSET
    expires: int | Unset = UNSET
    allow: list[Any] | Unset = UNSET
    accept_language: list[HttpHeadersAcceptLanguageItem] | Unset = UNSET
    basic_auth: str | Unset = UNSET
    accept: list[MediaType] | Unset = UNSET
    accept_language_as_locales: list[str] | Unset = UNSET
    accept_patch: list[MediaType] | Unset = UNSET
    access_control_allow_credentials: bool | Unset = UNSET
    access_control_allow_headers: list[str] | Unset = UNSET
    access_control_allow_methods: list[Any] | Unset = UNSET
    access_control_allow_origin: str | Unset = UNSET
    access_control_expose_headers: list[str] | Unset = UNSET
    access_control_max_age: int | Unset = UNSET
    access_control_request_headers: list[str] | Unset = UNSET
    access_control_request_method: Any | Unset = UNSET
    etag: str | Unset = UNSET
    if_match: list[str] | Unset = UNSET
    if_none_match: list[str] | Unset = UNSET
    if_unmodified_since: int | Unset = UNSET
    pragma: str | Unset = UNSET
    upgrade: str | Unset = UNSET
    vary: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        empty = self.empty

        location = self.location

        host: dict[str, Any] | Unset = UNSET
        if not isinstance(self.host, Unset):
            host = self.host.to_dict()

        all_: dict[str, Any] | Unset = UNSET
        if not isinstance(self.all_, Unset):
            all_ = self.all_.to_dict()

        last_modified = self.last_modified

        date = self.date

        content_length = self.content_length

        content_disposition: dict[str, Any] | Unset = UNSET
        if not isinstance(self.content_disposition, Unset):
            content_disposition = self.content_disposition.to_dict()

        accept_charset: list[str] | Unset = UNSET
        if not isinstance(self.accept_charset, Unset):
            accept_charset = self.accept_charset

        content_language = self.content_language

        connection: list[str] | Unset = UNSET
        if not isinstance(self.connection, Unset):
            connection = self.connection

        if_modified_since = self.if_modified_since

        content_type: dict[str, Any] | Unset = UNSET
        if not isinstance(self.content_type, Unset):
            content_type = self.content_type.to_dict()

        origin = self.origin

        range_: list[Any] | Unset = UNSET
        if not isinstance(self.range_, Unset):
            range_ = self.range_

        bearer_auth = self.bearer_auth

        cache_control = self.cache_control

        expires = self.expires

        allow: list[Any] | Unset = UNSET
        if not isinstance(self.allow, Unset):
            allow = self.allow

        accept_language: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.accept_language, Unset):
            accept_language = []
            for accept_language_item_data in self.accept_language:
                accept_language_item = accept_language_item_data.to_dict()
                accept_language.append(accept_language_item)

        basic_auth = self.basic_auth

        accept: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.accept, Unset):
            accept = []
            for accept_item_data in self.accept:
                accept_item = accept_item_data.to_dict()
                accept.append(accept_item)

        accept_language_as_locales: list[str] | Unset = UNSET
        if not isinstance(self.accept_language_as_locales, Unset):
            accept_language_as_locales = self.accept_language_as_locales

        accept_patch: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.accept_patch, Unset):
            accept_patch = []
            for accept_patch_item_data in self.accept_patch:
                accept_patch_item = accept_patch_item_data.to_dict()
                accept_patch.append(accept_patch_item)

        access_control_allow_credentials = self.access_control_allow_credentials

        access_control_allow_headers: list[str] | Unset = UNSET
        if not isinstance(self.access_control_allow_headers, Unset):
            access_control_allow_headers = self.access_control_allow_headers

        access_control_allow_methods: list[Any] | Unset = UNSET
        if not isinstance(self.access_control_allow_methods, Unset):
            access_control_allow_methods = self.access_control_allow_methods

        access_control_allow_origin = self.access_control_allow_origin

        access_control_expose_headers: list[str] | Unset = UNSET
        if not isinstance(self.access_control_expose_headers, Unset):
            access_control_expose_headers = self.access_control_expose_headers

        access_control_max_age = self.access_control_max_age

        access_control_request_headers: list[str] | Unset = UNSET
        if not isinstance(self.access_control_request_headers, Unset):
            access_control_request_headers = self.access_control_request_headers

        access_control_request_method = self.access_control_request_method

        etag = self.etag

        if_match: list[str] | Unset = UNSET
        if not isinstance(self.if_match, Unset):
            if_match = self.if_match

        if_none_match: list[str] | Unset = UNSET
        if not isinstance(self.if_none_match, Unset):
            if_none_match = self.if_none_match

        if_unmodified_since = self.if_unmodified_since

        pragma = self.pragma

        upgrade = self.upgrade

        vary: list[str] | Unset = UNSET
        if not isinstance(self.vary, Unset):
            vary = self.vary

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if empty is not UNSET:
            field_dict["empty"] = empty
        if location is not UNSET:
            field_dict["location"] = location
        if host is not UNSET:
            field_dict["host"] = host
        if all_ is not UNSET:
            field_dict["all"] = all_
        if last_modified is not UNSET:
            field_dict["lastModified"] = last_modified
        if date is not UNSET:
            field_dict["date"] = date
        if content_length is not UNSET:
            field_dict["contentLength"] = content_length
        if content_disposition is not UNSET:
            field_dict["contentDisposition"] = content_disposition
        if accept_charset is not UNSET:
            field_dict["acceptCharset"] = accept_charset
        if content_language is not UNSET:
            field_dict["contentLanguage"] = content_language
        if connection is not UNSET:
            field_dict["connection"] = connection
        if if_modified_since is not UNSET:
            field_dict["ifModifiedSince"] = if_modified_since
        if content_type is not UNSET:
            field_dict["contentType"] = content_type
        if origin is not UNSET:
            field_dict["origin"] = origin
        if range_ is not UNSET:
            field_dict["range"] = range_
        if bearer_auth is not UNSET:
            field_dict["bearerAuth"] = bearer_auth
        if cache_control is not UNSET:
            field_dict["cacheControl"] = cache_control
        if expires is not UNSET:
            field_dict["expires"] = expires
        if allow is not UNSET:
            field_dict["allow"] = allow
        if accept_language is not UNSET:
            field_dict["acceptLanguage"] = accept_language
        if basic_auth is not UNSET:
            field_dict["basicAuth"] = basic_auth
        if accept is not UNSET:
            field_dict["accept"] = accept
        if accept_language_as_locales is not UNSET:
            field_dict["acceptLanguageAsLocales"] = accept_language_as_locales
        if accept_patch is not UNSET:
            field_dict["acceptPatch"] = accept_patch
        if access_control_allow_credentials is not UNSET:
            field_dict["accessControlAllowCredentials"] = access_control_allow_credentials
        if access_control_allow_headers is not UNSET:
            field_dict["accessControlAllowHeaders"] = access_control_allow_headers
        if access_control_allow_methods is not UNSET:
            field_dict["accessControlAllowMethods"] = access_control_allow_methods
        if access_control_allow_origin is not UNSET:
            field_dict["accessControlAllowOrigin"] = access_control_allow_origin
        if access_control_expose_headers is not UNSET:
            field_dict["accessControlExposeHeaders"] = access_control_expose_headers
        if access_control_max_age is not UNSET:
            field_dict["accessControlMaxAge"] = access_control_max_age
        if access_control_request_headers is not UNSET:
            field_dict["accessControlRequestHeaders"] = access_control_request_headers
        if access_control_request_method is not UNSET:
            field_dict["accessControlRequestMethod"] = access_control_request_method
        if etag is not UNSET:
            field_dict["etag"] = etag
        if if_match is not UNSET:
            field_dict["ifMatch"] = if_match
        if if_none_match is not UNSET:
            field_dict["ifNoneMatch"] = if_none_match
        if if_unmodified_since is not UNSET:
            field_dict["ifUnmodifiedSince"] = if_unmodified_since
        if pragma is not UNSET:
            field_dict["pragma"] = pragma
        if upgrade is not UNSET:
            field_dict["upgrade"] = upgrade
        if vary is not UNSET:
            field_dict["vary"] = vary

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.content_disposition import ContentDisposition
        from ..models.http_headers_accept_language_item import HttpHeadersAcceptLanguageItem
        from ..models.http_headers_all import HttpHeadersAll
        from ..models.http_headers_host import HttpHeadersHost
        from ..models.media_type import MediaType

        d = dict(src_dict)
        empty = d.pop("empty", UNSET)

        location = d.pop("location", UNSET)

        _host = d.pop("host", UNSET)
        host: HttpHeadersHost | Unset
        if isinstance(_host, Unset):
            host = UNSET
        else:
            host = HttpHeadersHost.from_dict(_host)

        _all_ = d.pop("all", UNSET)
        all_: HttpHeadersAll | Unset
        if isinstance(_all_, Unset):
            all_ = UNSET
        else:
            all_ = HttpHeadersAll.from_dict(_all_)

        last_modified = d.pop("lastModified", UNSET)

        date = d.pop("date", UNSET)

        content_length = d.pop("contentLength", UNSET)

        _content_disposition = d.pop("contentDisposition", UNSET)
        content_disposition: ContentDisposition | Unset
        if isinstance(_content_disposition, Unset):
            content_disposition = UNSET
        else:
            content_disposition = ContentDisposition.from_dict(_content_disposition)

        accept_charset = cast(list[str], d.pop("acceptCharset", UNSET))

        content_language = d.pop("contentLanguage", UNSET)

        connection = cast(list[str], d.pop("connection", UNSET))

        if_modified_since = d.pop("ifModifiedSince", UNSET)

        _content_type = d.pop("contentType", UNSET)
        content_type: MediaType | Unset
        if isinstance(_content_type, Unset):
            content_type = UNSET
        else:
            content_type = MediaType.from_dict(_content_type)

        origin = d.pop("origin", UNSET)

        range_ = cast(list[Any], d.pop("range", UNSET))

        bearer_auth = d.pop("bearerAuth", UNSET)

        cache_control = d.pop("cacheControl", UNSET)

        expires = d.pop("expires", UNSET)

        allow = cast(list[Any], d.pop("allow", UNSET))

        _accept_language = d.pop("acceptLanguage", UNSET)
        accept_language: list[HttpHeadersAcceptLanguageItem] | Unset = UNSET
        if _accept_language is not UNSET:
            accept_language = []
            for accept_language_item_data in _accept_language:
                accept_language_item = HttpHeadersAcceptLanguageItem.from_dict(accept_language_item_data)

                accept_language.append(accept_language_item)

        basic_auth = d.pop("basicAuth", UNSET)

        _accept = d.pop("accept", UNSET)
        accept: list[MediaType] | Unset = UNSET
        if _accept is not UNSET:
            accept = []
            for accept_item_data in _accept:
                accept_item = MediaType.from_dict(accept_item_data)

                accept.append(accept_item)

        accept_language_as_locales = cast(list[str], d.pop("acceptLanguageAsLocales", UNSET))

        _accept_patch = d.pop("acceptPatch", UNSET)
        accept_patch: list[MediaType] | Unset = UNSET
        if _accept_patch is not UNSET:
            accept_patch = []
            for accept_patch_item_data in _accept_patch:
                accept_patch_item = MediaType.from_dict(accept_patch_item_data)

                accept_patch.append(accept_patch_item)

        access_control_allow_credentials = d.pop("accessControlAllowCredentials", UNSET)

        access_control_allow_headers = cast(list[str], d.pop("accessControlAllowHeaders", UNSET))

        access_control_allow_methods = cast(list[Any], d.pop("accessControlAllowMethods", UNSET))

        access_control_allow_origin = d.pop("accessControlAllowOrigin", UNSET)

        access_control_expose_headers = cast(list[str], d.pop("accessControlExposeHeaders", UNSET))

        access_control_max_age = d.pop("accessControlMaxAge", UNSET)

        access_control_request_headers = cast(list[str], d.pop("accessControlRequestHeaders", UNSET))

        access_control_request_method = d.pop("accessControlRequestMethod", UNSET)

        etag = d.pop("etag", UNSET)

        if_match = cast(list[str], d.pop("ifMatch", UNSET))

        if_none_match = cast(list[str], d.pop("ifNoneMatch", UNSET))

        if_unmodified_since = d.pop("ifUnmodifiedSince", UNSET)

        pragma = d.pop("pragma", UNSET)

        upgrade = d.pop("upgrade", UNSET)

        vary = cast(list[str], d.pop("vary", UNSET))

        http_headers = cls(
            empty=empty,
            location=location,
            host=host,
            all_=all_,
            last_modified=last_modified,
            date=date,
            content_length=content_length,
            content_disposition=content_disposition,
            accept_charset=accept_charset,
            content_language=content_language,
            connection=connection,
            if_modified_since=if_modified_since,
            content_type=content_type,
            origin=origin,
            range_=range_,
            bearer_auth=bearer_auth,
            cache_control=cache_control,
            expires=expires,
            allow=allow,
            accept_language=accept_language,
            basic_auth=basic_auth,
            accept=accept,
            accept_language_as_locales=accept_language_as_locales,
            accept_patch=accept_patch,
            access_control_allow_credentials=access_control_allow_credentials,
            access_control_allow_headers=access_control_allow_headers,
            access_control_allow_methods=access_control_allow_methods,
            access_control_allow_origin=access_control_allow_origin,
            access_control_expose_headers=access_control_expose_headers,
            access_control_max_age=access_control_max_age,
            access_control_request_headers=access_control_request_headers,
            access_control_request_method=access_control_request_method,
            etag=etag,
            if_match=if_match,
            if_none_match=if_none_match,
            if_unmodified_since=if_unmodified_since,
            pragma=pragma,
            upgrade=upgrade,
            vary=vary,
        )

        http_headers.additional_properties = d
        return http_headers

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
