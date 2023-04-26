from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.submit_workflow_launch_request import SubmitWorkflowLaunchRequest
from ...models.submit_workflow_launch_response import SubmitWorkflowLaunchResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    json_body: SubmitWorkflowLaunchRequest,
    workspace_id: Union[Unset, None, int] = UNSET,
    optimized: Union[Unset, None, bool] = UNSET,
    source_workspace_id: Union[Unset, None, int] = UNSET,
) -> Dict[str, Any]:
    url = "{}/workflow/launch".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["workspaceId"] = workspace_id

    params["optimized"] = optimized

    params["sourceWorkspaceId"] = source_workspace_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    json_json_body = json_body.to_dict()

    return {
        "method": "post",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "follow_redirects": client.follow_redirects,
        "json": json_json_body,
        "params": params,
    }


def _parse_response(
    *, client: Client, response: httpx.Response
) -> Optional[Union[Any, ErrorResponse, SubmitWorkflowLaunchResponse]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = SubmitWorkflowLaunchResponse.from_dict(response.json())

        return response_200
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


def _build_response(
    *, client: Client, response: httpx.Response
) -> Response[Union[Any, ErrorResponse, SubmitWorkflowLaunchResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    json_body: SubmitWorkflowLaunchRequest,
    workspace_id: Union[Unset, None, int] = UNSET,
    optimized: Union[Unset, None, bool] = UNSET,
    source_workspace_id: Union[Unset, None, int] = UNSET,
) -> Response[Union[Any, ErrorResponse, SubmitWorkflowLaunchResponse]]:
    """Submit a Workflow execution

    Args:
        workspace_id (Union[Unset, None, int]):
        optimized (Union[Unset, None, bool]):
        source_workspace_id (Union[Unset, None, int]):
        json_body (SubmitWorkflowLaunchRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ErrorResponse, SubmitWorkflowLaunchResponse]]
    """

    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
        workspace_id=workspace_id,
        optimized=optimized,
        source_workspace_id=source_workspace_id,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    json_body: SubmitWorkflowLaunchRequest,
    workspace_id: Union[Unset, None, int] = UNSET,
    optimized: Union[Unset, None, bool] = UNSET,
    source_workspace_id: Union[Unset, None, int] = UNSET,
) -> Optional[Union[Any, ErrorResponse, SubmitWorkflowLaunchResponse]]:
    """Submit a Workflow execution

    Args:
        workspace_id (Union[Unset, None, int]):
        optimized (Union[Unset, None, bool]):
        source_workspace_id (Union[Unset, None, int]):
        json_body (SubmitWorkflowLaunchRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ErrorResponse, SubmitWorkflowLaunchResponse]
    """

    return sync_detailed(
        client=client,
        json_body=json_body,
        workspace_id=workspace_id,
        optimized=optimized,
        source_workspace_id=source_workspace_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    json_body: SubmitWorkflowLaunchRequest,
    workspace_id: Union[Unset, None, int] = UNSET,
    optimized: Union[Unset, None, bool] = UNSET,
    source_workspace_id: Union[Unset, None, int] = UNSET,
) -> Response[Union[Any, ErrorResponse, SubmitWorkflowLaunchResponse]]:
    """Submit a Workflow execution

    Args:
        workspace_id (Union[Unset, None, int]):
        optimized (Union[Unset, None, bool]):
        source_workspace_id (Union[Unset, None, int]):
        json_body (SubmitWorkflowLaunchRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ErrorResponse, SubmitWorkflowLaunchResponse]]
    """

    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
        workspace_id=workspace_id,
        optimized=optimized,
        source_workspace_id=source_workspace_id,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    json_body: SubmitWorkflowLaunchRequest,
    workspace_id: Union[Unset, None, int] = UNSET,
    optimized: Union[Unset, None, bool] = UNSET,
    source_workspace_id: Union[Unset, None, int] = UNSET,
) -> Optional[Union[Any, ErrorResponse, SubmitWorkflowLaunchResponse]]:
    """Submit a Workflow execution

    Args:
        workspace_id (Union[Unset, None, int]):
        optimized (Union[Unset, None, bool]):
        source_workspace_id (Union[Unset, None, int]):
        json_body (SubmitWorkflowLaunchRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ErrorResponse, SubmitWorkflowLaunchResponse]
    """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
            workspace_id=workspace_id,
            optimized=optimized,
            source_workspace_id=source_workspace_id,
        )
    ).parsed
