from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.book_metadata import BookMetadata
from ...models.fetch_metadata_request import FetchMetadataRequest
from ...types import UNSET, Response, Unset


def _get_kwargs(
    book_id: int,
    *,
    body: FetchMetadataRequest | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/books/{book_id}/metadata/prospective".format(
            book_id=quote(str(book_id), safe=""),
        ),
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> list[BookMetadata] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.text
        for response_200_item_data in _response_200:
            response_200_item = BookMetadata.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[list[BookMetadata]]:
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
    body: FetchMetadataRequest | Unset = UNSET,
) -> Response[list[BookMetadata]]:
    """Get prospective metadata for a book

     Fetch prospective metadata for a book by its ID. Requires metadata edit permission or admin.

    Args:
        book_id (int):
        body (FetchMetadataRequest | Unset): Fetch metadata request

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[BookMetadata]]
    """

    kwargs = _get_kwargs(
        book_id=book_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    book_id: int,
    *,
    client: AuthenticatedClient | Client,
    body: FetchMetadataRequest | Unset = UNSET,
) -> list[BookMetadata] | None:
    """Get prospective metadata for a book

     Fetch prospective metadata for a book by its ID. Requires metadata edit permission or admin.

    Args:
        book_id (int):
        body (FetchMetadataRequest | Unset): Fetch metadata request

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[BookMetadata]
    """

    return sync_detailed(
        book_id=book_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    book_id: int,
    *,
    client: AuthenticatedClient | Client,
    body: FetchMetadataRequest | Unset = UNSET,
) -> Response[list[BookMetadata]]:
    """Get prospective metadata for a book

     Fetch prospective metadata for a book by its ID. Requires metadata edit permission or admin.

    Args:
        book_id (int):
        body (FetchMetadataRequest | Unset): Fetch metadata request

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[BookMetadata]]
    """

    kwargs = _get_kwargs(
        book_id=book_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    book_id: int,
    *,
    client: AuthenticatedClient | Client,
    body: FetchMetadataRequest | Unset = UNSET,
) -> list[BookMetadata] | None:
    """Get prospective metadata for a book

     Fetch prospective metadata for a book by its ID. Requires metadata edit permission or admin.

    Args:
        book_id (int):
        body (FetchMetadataRequest | Unset): Fetch metadata request

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[BookMetadata]
    """

    return (
        await asyncio_detailed(
            book_id=book_id,
            client=client,
            body=body,
        )
    ).parsed
