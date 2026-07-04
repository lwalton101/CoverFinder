from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.metadata_update_wrapper import MetadataUpdateWrapper
from ...models.update_metadata_replace_mode import UpdateMetadataReplaceMode
from ...types import UNSET, Response, Unset


def _get_kwargs(
    book_id: int,
    *,
    body: MetadataUpdateWrapper,
    merge_categories: bool | Unset = False,
    replace_mode: UpdateMetadataReplaceMode | Unset = UpdateMetadataReplaceMode.REPLACE_ALL,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["mergeCategories"] = merge_categories

    json_replace_mode: str | Unset = UNSET
    if not isinstance(replace_mode, Unset):
        json_replace_mode = replace_mode.value

    params["replaceMode"] = json_replace_mode

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/api/v1/books/{book_id}/metadata".format(
            book_id=quote(str(book_id), safe=""),
        ),
        "params": params,
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
    book_id: int,
    *,
    client: AuthenticatedClient | Client,
    body: MetadataUpdateWrapper,
    merge_categories: bool | Unset = False,
    replace_mode: UpdateMetadataReplaceMode | Unset = UpdateMetadataReplaceMode.REPLACE_ALL,
) -> Response[Any]:
    """Update book metadata

     Update metadata for a book. Requires metadata edit permission or admin.

    Args:
        book_id (int):
        merge_categories (bool | Unset):  Default: False.
        replace_mode (UpdateMetadataReplaceMode | Unset):  Default:
            UpdateMetadataReplaceMode.REPLACE_ALL.
        body (MetadataUpdateWrapper): Metadata update wrapper

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        book_id=book_id,
        body=body,
        merge_categories=merge_categories,
        replace_mode=replace_mode,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    book_id: int,
    *,
    client: AuthenticatedClient | Client,
    body: MetadataUpdateWrapper,
    merge_categories: bool | Unset = False,
    replace_mode: UpdateMetadataReplaceMode | Unset = UpdateMetadataReplaceMode.REPLACE_ALL,
) -> Response[Any]:
    """Update book metadata

     Update metadata for a book. Requires metadata edit permission or admin.

    Args:
        book_id (int):
        merge_categories (bool | Unset):  Default: False.
        replace_mode (UpdateMetadataReplaceMode | Unset):  Default:
            UpdateMetadataReplaceMode.REPLACE_ALL.
        body (MetadataUpdateWrapper): Metadata update wrapper

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        book_id=book_id,
        body=body,
        merge_categories=merge_categories,
        replace_mode=replace_mode,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
