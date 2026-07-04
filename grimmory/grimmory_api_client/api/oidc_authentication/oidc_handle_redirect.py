from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import UNSET, Response


def _get_kwargs(
    *,
    code: str,
    code_verifier: str,
    redirect_uri: str,
    nonce: str,
    state: str,
    app_redirect_uri: str,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["code"] = code

    params["code_verifier"] = code_verifier

    params["redirect_uri"] = redirect_uri

    params["nonce"] = nonce

    params["state"] = state

    params["app_redirect_uri"] = app_redirect_uri

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/auth/oidc/redirect",
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
    *,
    client: AuthenticatedClient | Client,
    code: str,
    code_verifier: str,
    redirect_uri: str,
    nonce: str,
    state: str,
    app_redirect_uri: str,
) -> Response[Any]:
    """Handle OIDC redirect callback

     Handle redirect-based OIDC callback and redirect back to the app with token information.

    Args:
        code (str):
        code_verifier (str):
        redirect_uri (str):
        nonce (str):
        state (str):
        app_redirect_uri (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        code=code,
        code_verifier=code_verifier,
        redirect_uri=redirect_uri,
        nonce=nonce,
        state=state,
        app_redirect_uri=app_redirect_uri,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    code: str,
    code_verifier: str,
    redirect_uri: str,
    nonce: str,
    state: str,
    app_redirect_uri: str,
) -> Response[Any]:
    """Handle OIDC redirect callback

     Handle redirect-based OIDC callback and redirect back to the app with token information.

    Args:
        code (str):
        code_verifier (str):
        redirect_uri (str):
        nonce (str):
        state (str):
        app_redirect_uri (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        code=code,
        code_verifier=code_verifier,
        redirect_uri=redirect_uri,
        nonce=nonce,
        state=state,
        app_redirect_uri=app_redirect_uri,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
