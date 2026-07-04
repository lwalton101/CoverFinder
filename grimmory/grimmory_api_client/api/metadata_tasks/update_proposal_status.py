from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import UNSET, Response


def _get_kwargs(
    task_id: str,
    proposal_id: int,
    *,
    status: str,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["status"] = status

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/metadata/tasks/{task_id}/proposals/{proposal_id}/status".format(
            task_id=quote(str(task_id), safe=""),
            proposal_id=quote(str(proposal_id), safe=""),
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
    task_id: str,
    proposal_id: int,
    *,
    client: AuthenticatedClient | Client,
    status: str,
) -> Response[Any]:
    """Update proposal status

     Update the status of a proposal for a metadata task. Requires metadata edit permission or admin.

    Args:
        task_id (str):
        proposal_id (int):
        status (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        task_id=task_id,
        proposal_id=proposal_id,
        status=status,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    task_id: str,
    proposal_id: int,
    *,
    client: AuthenticatedClient | Client,
    status: str,
) -> Response[Any]:
    """Update proposal status

     Update the status of a proposal for a metadata task. Requires metadata edit permission or admin.

    Args:
        task_id (str):
        proposal_id (int):
        status (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        task_id=task_id,
        proposal_id=proposal_id,
        status=status,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
