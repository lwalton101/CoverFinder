from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    page: int | Unset = 0,
    size: int | Unset = 30,
    sort: str | Unset = "name",
    dir_: str | Unset = "asc",
    library_id: int | Unset = UNSET,
    search: str | Unset = UNSET,
    has_photo: bool | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["page"] = page

    params["size"] = size

    params["sort"] = sort

    params["dir"] = dir_

    params["libraryId"] = library_id

    params["search"] = search

    params["hasPhoto"] = has_photo

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/app/authors",
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
    *,
    client: AuthenticatedClient | Client,
    page: int | Unset = 0,
    size: int | Unset = 30,
    sort: str | Unset = "name",
    dir_: str | Unset = "asc",
    library_id: int | Unset = UNSET,
    search: str | Unset = UNSET,
    has_photo: bool | Unset = UNSET,
) -> Response[Any]:
    """List app authors

     Retrieve paginated authors for the app with optional filtering and sorting.

    Args:
        page (int | Unset):  Default: 0.
        size (int | Unset):  Default: 30.
        sort (str | Unset):  Default: 'name'.
        dir_ (str | Unset):  Default: 'asc'.
        library_id (int | Unset):
        search (str | Unset):
        has_photo (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        page=page,
        size=size,
        sort=sort,
        dir_=dir_,
        library_id=library_id,
        search=search,
        has_photo=has_photo,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    page: int | Unset = 0,
    size: int | Unset = 30,
    sort: str | Unset = "name",
    dir_: str | Unset = "asc",
    library_id: int | Unset = UNSET,
    search: str | Unset = UNSET,
    has_photo: bool | Unset = UNSET,
) -> Response[Any]:
    """List app authors

     Retrieve paginated authors for the app with optional filtering and sorting.

    Args:
        page (int | Unset):  Default: 0.
        size (int | Unset):  Default: 30.
        sort (str | Unset):  Default: 'name'.
        dir_ (str | Unset):  Default: 'asc'.
        library_id (int | Unset):
        search (str | Unset):
        has_photo (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        page=page,
        size=size,
        sort=sort,
        dir_=dir_,
        library_id=library_id,
        search=search,
        has_photo=has_photo,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
