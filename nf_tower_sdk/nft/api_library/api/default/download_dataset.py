from http import HTTPStatus
from io import BytesIO
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...types import File, Response


def _get_kwargs(
    workspace_id: int,
    dataset_id: str,
    version: str,
    file_name: str,
    *,
    client: AuthenticatedClient,
) -> Dict[str, Any]:
    url = "{}/workspaces/{workspaceId}/datasets/{datasetId}/v/{version}/n/{fileName}".format(
        client.base_url, workspaceId=workspace_id, datasetId=dataset_id, version=version, fileName=file_name
    )

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "follow_redirects": client.follow_redirects,
    }


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[Union[Any, ErrorResponse, File]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = File(payload=BytesIO(response.json()))

        return response_200
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = ErrorResponse.from_dict(response.json())

        return response_400
    if response.status_code == HTTPStatus.FORBIDDEN:
        response_403 = cast(Any, None)
        return response_403
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = ErrorResponse.from_dict(response.json())

        return response_404
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[Union[Any, ErrorResponse, File]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    workspace_id: int,
    dataset_id: str,
    version: str,
    file_name: str,
    *,
    client: AuthenticatedClient,
) -> Response[Union[Any, ErrorResponse, File]]:
    """Download the content of a dataset version

    Args:
        workspace_id (int):
        dataset_id (str):
        version (str):
        file_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ErrorResponse, File]]
    """

    kwargs = _get_kwargs(
        workspace_id=workspace_id,
        dataset_id=dataset_id,
        version=version,
        file_name=file_name,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    workspace_id: int,
    dataset_id: str,
    version: str,
    file_name: str,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[Any, ErrorResponse, File]]:
    """Download the content of a dataset version

    Args:
        workspace_id (int):
        dataset_id (str):
        version (str):
        file_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ErrorResponse, File]
    """

    return sync_detailed(
        workspace_id=workspace_id,
        dataset_id=dataset_id,
        version=version,
        file_name=file_name,
        client=client,
    ).parsed


async def asyncio_detailed(
    workspace_id: int,
    dataset_id: str,
    version: str,
    file_name: str,
    *,
    client: AuthenticatedClient,
) -> Response[Union[Any, ErrorResponse, File]]:
    """Download the content of a dataset version

    Args:
        workspace_id (int):
        dataset_id (str):
        version (str):
        file_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ErrorResponse, File]]
    """

    kwargs = _get_kwargs(
        workspace_id=workspace_id,
        dataset_id=dataset_id,
        version=version,
        file_name=file_name,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    workspace_id: int,
    dataset_id: str,
    version: str,
    file_name: str,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[Any, ErrorResponse, File]]:
    """Download the content of a dataset version

    Args:
        workspace_id (int):
        dataset_id (str):
        version (str):
        file_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ErrorResponse, File]
    """

    return (
        await asyncio_detailed(
            workspace_id=workspace_id,
            dataset_id=dataset_id,
            version=version,
            file_name=file_name,
            client=client,
        )
    ).parsed
