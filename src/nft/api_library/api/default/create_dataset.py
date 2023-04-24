from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_dataset_request import CreateDatasetRequest
from ...models.create_dataset_response import CreateDatasetResponse
from ...models.error_response import ErrorResponse
from ...types import Response


def _get_kwargs(
    workspace_id: int,
    *,
    client: AuthenticatedClient,
    json_body: CreateDatasetRequest,
) -> Dict[str, Any]:
    url = "{}/workspaces/{workspaceId}/datasets".format(client.base_url, workspaceId=workspace_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_json_body = json_body.to_dict()

    return {
        "method": "post",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "follow_redirects": client.follow_redirects,
        "json": json_json_body,
    }


def _parse_response(
    *, client: Client, response: httpx.Response
) -> Optional[Union[Any, CreateDatasetResponse, ErrorResponse]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = CreateDatasetResponse.from_dict(response.json())

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
) -> Response[Union[Any, CreateDatasetResponse, ErrorResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    workspace_id: int,
    *,
    client: AuthenticatedClient,
    json_body: CreateDatasetRequest,
) -> Response[Union[Any, CreateDatasetResponse, ErrorResponse]]:
    """Create a dataset

    Args:
        workspace_id (int):
        json_body (CreateDatasetRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, CreateDatasetResponse, ErrorResponse]]
    """

    kwargs = _get_kwargs(
        workspace_id=workspace_id,
        client=client,
        json_body=json_body,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    workspace_id: int,
    *,
    client: AuthenticatedClient,
    json_body: CreateDatasetRequest,
) -> Optional[Union[Any, CreateDatasetResponse, ErrorResponse]]:
    """Create a dataset

    Args:
        workspace_id (int):
        json_body (CreateDatasetRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, CreateDatasetResponse, ErrorResponse]
    """

    return sync_detailed(
        workspace_id=workspace_id,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    workspace_id: int,
    *,
    client: AuthenticatedClient,
    json_body: CreateDatasetRequest,
) -> Response[Union[Any, CreateDatasetResponse, ErrorResponse]]:
    """Create a dataset

    Args:
        workspace_id (int):
        json_body (CreateDatasetRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, CreateDatasetResponse, ErrorResponse]]
    """

    kwargs = _get_kwargs(
        workspace_id=workspace_id,
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    workspace_id: int,
    *,
    client: AuthenticatedClient,
    json_body: CreateDatasetRequest,
) -> Optional[Union[Any, CreateDatasetResponse, ErrorResponse]]:
    """Create a dataset

    Args:
        workspace_id (int):
        json_body (CreateDatasetRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, CreateDatasetResponse, ErrorResponse]
    """

    return (
        await asyncio_detailed(
            workspace_id=workspace_id,
            client=client,
            json_body=json_body,
        )
    ).parsed
