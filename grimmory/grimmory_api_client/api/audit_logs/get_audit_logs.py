import datetime
from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_audit_logs_action import GetAuditLogsAction
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    page: int | Unset = 0,
    size: int | Unset = 25,
    action: GetAuditLogsAction | Unset = UNSET,
    user_id: int | Unset = UNSET,
    username: str | Unset = UNSET,
    from_: datetime.datetime | Unset = UNSET,
    to: datetime.datetime | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["page"] = page

    params["size"] = size

    json_action: str | Unset = UNSET
    if not isinstance(action, Unset):
        json_action = action.value

    params["action"] = json_action

    params["userId"] = user_id

    params["username"] = username

    json_from_: str | Unset = UNSET
    if not isinstance(from_, Unset):
        json_from_ = from_.isoformat()
    params["from"] = json_from_

    json_to: str | Unset = UNSET
    if not isinstance(to, Unset):
        json_to = to.isoformat()
    params["to"] = json_to

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/audit-logs",
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
    size: int | Unset = 25,
    action: GetAuditLogsAction | Unset = UNSET,
    user_id: int | Unset = UNSET,
    username: str | Unset = UNSET,
    from_: datetime.datetime | Unset = UNSET,
    to: datetime.datetime | Unset = UNSET,
) -> Response[Any]:
    """Get audit logs

     Retrieve paginated audit logs with optional filters. Requires admin.

    Args:
        page (int | Unset):  Default: 0.
        size (int | Unset):  Default: 25.
        action (GetAuditLogsAction | Unset):
        user_id (int | Unset):
        username (str | Unset):
        from_ (datetime.datetime | Unset):
        to (datetime.datetime | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        page=page,
        size=size,
        action=action,
        user_id=user_id,
        username=username,
        from_=from_,
        to=to,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    page: int | Unset = 0,
    size: int | Unset = 25,
    action: GetAuditLogsAction | Unset = UNSET,
    user_id: int | Unset = UNSET,
    username: str | Unset = UNSET,
    from_: datetime.datetime | Unset = UNSET,
    to: datetime.datetime | Unset = UNSET,
) -> Response[Any]:
    """Get audit logs

     Retrieve paginated audit logs with optional filters. Requires admin.

    Args:
        page (int | Unset):  Default: 0.
        size (int | Unset):  Default: 25.
        action (GetAuditLogsAction | Unset):
        user_id (int | Unset):
        username (str | Unset):
        from_ (datetime.datetime | Unset):
        to (datetime.datetime | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        page=page,
        size=size,
        action=action,
        user_id=user_id,
        username=username,
        from_=from_,
        to=to,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
