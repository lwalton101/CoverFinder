from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import UNSET, Response, Unset


def _get_kwargs(
    series_name: str,
    *,
    page: int | Unset = 0,
    size: int | Unset = 20,
    sort: str | Unset = "seriesNumber",
    dir_: str | Unset = "asc",
    library_id: int | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["page"] = page

    params["size"] = size

    params["sort"] = sort

    params["dir"] = dir_

    params["libraryId"] = library_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/app/series/{series_name}/books".format(
            series_name=quote(str(series_name), safe=""),
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
    series_name: str,
    *,
    client: AuthenticatedClient | Client,
    page: int | Unset = 0,
    size: int | Unset = 20,
    sort: str | Unset = "seriesNumber",
    dir_: str | Unset = "asc",
    library_id: int | Unset = UNSET,
) -> Response[Any]:
    """List books in app series

     Retrieve paginated books belonging to a specific series for the app.

    Args:
        series_name (str):
        page (int | Unset):  Default: 0.
        size (int | Unset):  Default: 20.
        sort (str | Unset):  Default: 'seriesNumber'.
        dir_ (str | Unset):  Default: 'asc'.
        library_id (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        series_name=series_name,
        page=page,
        size=size,
        sort=sort,
        dir_=dir_,
        library_id=library_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    series_name: str,
    *,
    client: AuthenticatedClient | Client,
    page: int | Unset = 0,
    size: int | Unset = 20,
    sort: str | Unset = "seriesNumber",
    dir_: str | Unset = "asc",
    library_id: int | Unset = UNSET,
) -> Response[Any]:
    """List books in app series

     Retrieve paginated books belonging to a specific series for the app.

    Args:
        series_name (str):
        page (int | Unset):  Default: 0.
        size (int | Unset):  Default: 20.
        sort (str | Unset):  Default: 'seriesNumber'.
        dir_ (str | Unset):  Default: 'asc'.
        library_id (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        series_name=series_name,
        page=page,
        size=size,
        sort=sort,
        dir_=dir_,
        library_id=library_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
