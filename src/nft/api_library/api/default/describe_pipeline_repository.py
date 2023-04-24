from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.describe_pipeline_info_response import DescribePipelineInfoResponse
from ...models.error_response import ErrorResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    name: Union[Unset, None, str] = UNSET,
    revision: Union[Unset, None, str] = UNSET,
    workspace_id: Union[Unset, None, int] = UNSET,
) -> Dict[str, Any]:
    url = "{}/pipelines/info".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["name"] = name

    params["revision"] = revision

    params["workspaceId"] = workspace_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "follow_redirects": client.follow_redirects,
        "params": params,
    }


def _parse_response(
    *, client: Client, response: httpx.Response
) -> Optional[Union[Any, DescribePipelineInfoResponse, ErrorResponse]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = DescribePipelineInfoResponse.from_dict(response.json())

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
) -> Response[Union[Any, DescribePipelineInfoResponse, ErrorResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    name: Union[Unset, None, str] = UNSET,
    revision: Union[Unset, None, str] = UNSET,
    workspace_id: Union[Unset, None, int] = UNSET,
) -> Response[Union[Any, DescribePipelineInfoResponse, ErrorResponse]]:
    """Describe the Pipeline entity for the given id

    Args:
        name (Union[Unset, None, str]):
        revision (Union[Unset, None, str]):
        workspace_id (Union[Unset, None, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, DescribePipelineInfoResponse, ErrorResponse]]
    """

    kwargs = _get_kwargs(
        client=client,
        name=name,
        revision=revision,
        workspace_id=workspace_id,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    name: Union[Unset, None, str] = UNSET,
    revision: Union[Unset, None, str] = UNSET,
    workspace_id: Union[Unset, None, int] = UNSET,
) -> Optional[Union[Any, DescribePipelineInfoResponse, ErrorResponse]]:
    """Describe the Pipeline entity for the given id

    Args:
        name (Union[Unset, None, str]):
        revision (Union[Unset, None, str]):
        workspace_id (Union[Unset, None, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, DescribePipelineInfoResponse, ErrorResponse]
    """

    return sync_detailed(
        client=client,
        name=name,
        revision=revision,
        workspace_id=workspace_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    name: Union[Unset, None, str] = UNSET,
    revision: Union[Unset, None, str] = UNSET,
    workspace_id: Union[Unset, None, int] = UNSET,
) -> Response[Union[Any, DescribePipelineInfoResponse, ErrorResponse]]:
    """Describe the Pipeline entity for the given id

    Args:
        name (Union[Unset, None, str]):
        revision (Union[Unset, None, str]):
        workspace_id (Union[Unset, None, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, DescribePipelineInfoResponse, ErrorResponse]]
    """

    kwargs = _get_kwargs(
        client=client,
        name=name,
        revision=revision,
        workspace_id=workspace_id,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    name: Union[Unset, None, str] = UNSET,
    revision: Union[Unset, None, str] = UNSET,
    workspace_id: Union[Unset, None, int] = UNSET,
) -> Optional[Union[Any, DescribePipelineInfoResponse, ErrorResponse]]:
    """Describe the Pipeline entity for the given id

    Args:
        name (Union[Unset, None, str]):
        revision (Union[Unset, None, str]):
        workspace_id (Union[Unset, None, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, DescribePipelineInfoResponse, ErrorResponse]
    """

    return (
        await asyncio_detailed(
            client=client,
            name=name,
            revision=revision,
            workspace_id=workspace_id,
        )
    ).parsed
