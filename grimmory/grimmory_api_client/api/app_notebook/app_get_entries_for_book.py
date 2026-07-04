from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import UNSET, Response, Unset


def _get_kwargs(
    book_id: int,
    *,
    page: int | Unset = 0,
    size: int | Unset = 20,
    types: list[str] | Unset = UNSET,
    search: str | Unset = UNSET,
    sort: str | Unset = "date_desc",
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["page"] = page

    params["size"] = size

    json_types: list[str] | Unset = UNSET
    if not isinstance(types, Unset):
        json_types = types

    params["types"] = json_types

    params["search"] = search

    params["sort"] = sort

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/app/notebook/books/{book_id}/entries".format(
            book_id=quote(str(book_id), safe=""),
        ),
        "params": params,
    }

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
    page: int | Unset = 0,
    size: int | Unset = 20,
    types: list[str] | Unset = UNSET,
    search: str | Unset = UNSET,
    sort: str | Unset = "date_desc",
) -> Response[Any]:
    """List notebook entries for book

     Retrieve paginated notebook entries for a specific book in the app.

    Args:
        book_id (int):
        page (int | Unset):  Default: 0.
        size (int | Unset):  Default: 20.
        types (list[str] | Unset):
        search (str | Unset):
        sort (str | Unset):  Default: 'date_desc'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        book_id=book_id,
        page=page,
        size=size,
        types=types,
        search=search,
        sort=sort,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    book_id: int,
    *,
    client: AuthenticatedClient | Client,
    page: int | Unset = 0,
    size: int | Unset = 20,
    types: list[str] | Unset = UNSET,
    search: str | Unset = UNSET,
    sort: str | Unset = "date_desc",
) -> Response[Any]:
    """List notebook entries for book

     Retrieve paginated notebook entries for a specific book in the app.

    Args:
        book_id (int):
        page (int | Unset):  Default: 0.
        size (int | Unset):  Default: 20.
        types (list[str] | Unset):
        search (str | Unset):
        sort (str | Unset):  Default: 'date_desc'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        book_id=book_id,
        page=page,
        size=size,
        types=types,
        search=search,
        sort=sort,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
