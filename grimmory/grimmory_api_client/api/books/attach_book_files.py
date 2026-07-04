from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.attach_book_file_request import AttachBookFileRequest
from ...types import Response


def _get_kwargs(
    target_book_id: int,
    *,
    body: AttachBookFileRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/books/{target_book_id}/attach-file".format(
            target_book_id=quote(str(target_book_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

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
    target_book_id: int,
    *,
    client: AuthenticatedClient | Client,
    body: AttachBookFileRequest,
) -> Response[Any]:
    """Attach book files

     Attach book files from single-file source books to a target book as alternative formats.

    Args:
        target_book_id (int):
        body (AttachBookFileRequest): Request containing source book IDs and delete option

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        target_book_id=target_book_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    target_book_id: int,
    *,
    client: AuthenticatedClient | Client,
    body: AttachBookFileRequest,
) -> Response[Any]:
    """Attach book files

     Attach book files from single-file source books to a target book as alternative formats.

    Args:
        target_book_id (int):
        body (AttachBookFileRequest): Request containing source book IDs and delete option

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        target_book_id=target_book_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
