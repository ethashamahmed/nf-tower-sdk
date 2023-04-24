from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.update_action_request import UpdateActionRequest
from ...types import UNSET, Response, Unset


def _get_kwargs(
    action_id: str,
    *,
    client: AuthenticatedClient,
    json_body: UpdateActionRequest,
    workspace_id: Union[Unset, None, int] = UNSET,
) -> Dict[str, Any]:
    url = "{}/actions/{actionId}".format(client.base_url, actionId=action_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["workspaceId"] = workspace_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    json_json_body = json_body.to_dict()

    return {
        "method": "put",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "follow_redirects": client.follow_redirects,
        "json": json_json_body,
        "params": params,
    }


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[Union[Any, ErrorResponse]]:
    if response.status_code == HTTPStatus.NO_CONTENT:
        response_204 = cast(Any, None)
        return response_204
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = ErrorResponse.from_dict(response.json())

        return response_400
    if response.status_code == HTTPStatus.FORBIDDEN:
        response_403 = cast(Any, None)
        return response_403
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[Union[Any, ErrorResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    action_id: str,
    *,
    client: AuthenticatedClient,
    json_body: UpdateActionRequest,
    workspace_id: Union[Unset, None, int] = UNSET,
) -> Response[Union[Any, ErrorResponse]]:
    """Update a Pipeline Action

    Args:
        action_id (str):
        workspace_id (Union[Unset, None, int]):
        json_body (UpdateActionRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ErrorResponse]]
    """

    kwargs = _get_kwargs(
        action_id=action_id,
        client=client,
        json_body=json_body,
        workspace_id=workspace_id,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    action_id: str,
    *,
    client: AuthenticatedClient,
    json_body: UpdateActionRequest,
    workspace_id: Union[Unset, None, int] = UNSET,
) -> Optional[Union[Any, ErrorResponse]]:
    """Update a Pipeline Action

    Args:
        action_id (str):
        workspace_id (Union[Unset, None, int]):
        json_body (UpdateActionRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ErrorResponse]
    """

    return sync_detailed(
        action_id=action_id,
        client=client,
        json_body=json_body,
        workspace_id=workspace_id,
    ).parsed


async def asyncio_detailed(
    action_id: str,
    *,
    client: AuthenticatedClient,
    json_body: UpdateActionRequest,
    workspace_id: Union[Unset, None, int] = UNSET,
) -> Response[Union[Any, ErrorResponse]]:
    """Update a Pipeline Action

    Args:
        action_id (str):
        workspace_id (Union[Unset, None, int]):
        json_body (UpdateActionRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ErrorResponse]]
    """

    kwargs = _get_kwargs(
        action_id=action_id,
        client=client,
        json_body=json_body,
        workspace_id=workspace_id,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    action_id: str,
    *,
    client: AuthenticatedClient,
    json_body: UpdateActionRequest,
    workspace_id: Union[Unset, None, int] = UNSET,
) -> Optional[Union[Any, ErrorResponse]]:
    """Update a Pipeline Action

    Args:
        action_id (str):
        workspace_id (Union[Unset, None, int]):
        json_body (UpdateActionRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ErrorResponse]
    """

    return (
        await asyncio_detailed(
            action_id=action_id,
            client=client,
            json_body=json_body,
            workspace_id=workspace_id,
        )
    ).parsed
