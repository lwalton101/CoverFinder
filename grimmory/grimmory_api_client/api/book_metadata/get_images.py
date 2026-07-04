from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.cover_fetch_request import CoverFetchRequest
from ...types import Response


def _get_kwargs(
    book_id: int,
    *,
    body: CoverFetchRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/books/{book_id}/metadata/covers".format(
            book_id=quote(str(book_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> list[Any] | None:
    if response.status_code == 200:
        response_200 = cast(list[Any], response.text)

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[list[Any]]:
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
    body: CoverFetchRequest,
) -> Response[list[Any]]:
    """Get cover images for a book

     Fetch cover images for a book.

    Args:
        book_id (int):
        body (CoverFetchRequest): Cover fetch request

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[Any]]
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
    body: CoverFetchRequest,
) -> list[Any] | None:
    """Get cover images for a book

     Fetch cover images for a book.

    Args:
        book_id (int):
        body (CoverFetchRequest): Cover fetch request

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[Any]
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
    body: CoverFetchRequest,
) -> Response[list[Any]]:
    """Get cover images for a book

     Fetch cover images for a book.

    Args:
        book_id (int):
        body (CoverFetchRequest): Cover fetch request

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[Any]]
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
    body: CoverFetchRequest,
) -> list[Any] | None:
    """Get cover images for a book

     Fetch cover images for a book.

    Args:
        book_id (int):
        body (CoverFetchRequest): Cover fetch request

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[Any]
    """

    return (
        await asyncio_detailed(
            book_id=book_id,
            client=client,
            body=body,
        )
    ).parsed
