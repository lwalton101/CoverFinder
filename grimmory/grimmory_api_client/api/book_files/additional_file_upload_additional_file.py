from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.additional_file_upload_additional_file_body import AdditionalFileUploadAdditionalFileBody
from ...models.additional_file_upload_additional_file_book_type import AdditionalFileUploadAdditionalFileBookType
from ...types import UNSET, Response, Unset


def _get_kwargs(
    book_id: int,
    *,
    body: AdditionalFileUploadAdditionalFileBody | Unset = UNSET,
    is_book: bool,
    book_type: AdditionalFileUploadAdditionalFileBookType | Unset = UNSET,
    description: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["isBook"] = is_book

    json_book_type: str | Unset = UNSET
    if not isinstance(book_type, Unset):
        json_book_type = book_type.value

    params["bookType"] = json_book_type

    params["description"] = description

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/books/{book_id}/files".format(
            book_id=quote(str(book_id), safe=""),
        ),
        "params": params,
    }

    if not isinstance(body, Unset):
        _kwargs["files"] = body.to_multipart()

    headers["Content-Type"] = "multipart/form-data; boundary=+++"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | None:
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    book_id: int,
    *,
    client: AuthenticatedClient | Client,
    body: AdditionalFileUploadAdditionalFileBody | Unset = UNSET,
    is_book: bool,
    book_type: AdditionalFileUploadAdditionalFileBookType | Unset = UNSET,
    description: str | Unset = UNSET,
) -> Response[Any]:
    """Upload additional book file

     Upload and attach a new additional file to a specific book.

    Args:
        book_id (int):
        is_book (bool):
        book_type (AdditionalFileUploadAdditionalFileBookType | Unset):
        description (str | Unset):
        body (AdditionalFileUploadAdditionalFileBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        book_id=book_id,
        body=body,
        is_book=is_book,
        book_type=book_type,
        description=description,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    book_id: int,
    *,
    client: AuthenticatedClient | Client,
    body: AdditionalFileUploadAdditionalFileBody | Unset = UNSET,
    is_book: bool,
    book_type: AdditionalFileUploadAdditionalFileBookType | Unset = UNSET,
    description: str | Unset = UNSET,
) -> Response[Any]:
    """Upload additional book file

     Upload and attach a new additional file to a specific book.

    Args:
        book_id (int):
        is_book (bool):
        book_type (AdditionalFileUploadAdditionalFileBookType | Unset):
        description (str | Unset):
        body (AdditionalFileUploadAdditionalFileBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        book_id=book_id,
        body=body,
        is_book=is_book,
        book_type=book_type,
        description=description,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
