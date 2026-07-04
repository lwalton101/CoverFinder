from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import UNSET, Response, Unset


def _get_kwargs(
    book_id: int,
    page_number: int,
    *,
    book_type: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["bookType"] = book_type

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/media/book/{book_id}/cbx/pages/{page_number}".format(
            book_id=quote(str(book_id), safe=""),
            page_number=quote(str(page_number), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | None:
    if response.status_code == 200:
        return None

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
    page_number: int,
    *,
    client: AuthenticatedClient | Client,
    book_type: str | Unset = UNSET,
) -> Response[Any]:
    """Get CBX page as image

     Retrieve a specific page from a CBX book as an image.

    Args:
        book_id (int):
        page_number (int):
        book_type (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        book_id=book_id,
        page_number=page_number,
        book_type=book_type,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    book_id: int,
    page_number: int,
    *,
    client: AuthenticatedClient | Client,
    book_type: str | Unset = UNSET,
) -> Response[Any]:
    """Get CBX page as image

     Retrieve a specific page from a CBX book as an image.

    Args:
        book_id (int):
        page_number (int):
        book_type (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        book_id=book_id,
        page_number=page_number,
        book_type=book_type,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
