from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import UNSET, Response, Unset


def _get_kwargs(
    author_id: int,
    *,
    q: str | Unset = UNSET,
    asin: str | Unset = UNSET,
    region: str | Unset = "us",
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["q"] = q

    params["asin"] = asin

    params["region"] = region

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/authors/{author_id}/search-metadata".format(
            author_id=quote(str(author_id), safe=""),
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
    author_id: int,
    *,
    client: AuthenticatedClient | Client,
    q: str | Unset = UNSET,
    asin: str | Unset = UNSET,
    region: str | Unset = "us",
) -> Response[Any]:
    """Search author metadata

     Search external providers for author metadata candidates.

    Args:
        author_id (int):
        q (str | Unset):
        asin (str | Unset):
        region (str | Unset):  Default: 'us'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        author_id=author_id,
        q=q,
        asin=asin,
        region=region,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    author_id: int,
    *,
    client: AuthenticatedClient | Client,
    q: str | Unset = UNSET,
    asin: str | Unset = UNSET,
    region: str | Unset = "us",
) -> Response[Any]:
    """Search author metadata

     Search external providers for author metadata candidates.

    Args:
        author_id (int):
        q (str | Unset):
        asin (str | Unset):
        region (str | Unset):  Default: 'us'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        author_id=author_id,
        q=q,
        asin=asin,
        region=region,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
