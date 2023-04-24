from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.multi_request_file_schema import MultiRequestFileSchema
from ...models.upload_dataset_version_response import UploadDatasetVersionResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    workspace_id: int,
    dataset_id: str,
    *,
    client: AuthenticatedClient,
    multipart_data: MultiRequestFileSchema,
    header: Union[Unset, None, bool] = UNSET,
) -> Dict[str, Any]:
    url = "{}/workspaces/{workspaceId}/datasets/{datasetId}/upload".format(
        client.base_url, workspaceId=workspace_id, datasetId=dataset_id
    )

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["header"] = header

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    multipart_multipart_data = multipart_data.to_multipart()

    return {
        "method": "post",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "follow_redirects": client.follow_redirects,
        "files": multipart_multipart_data,
        "params": params,
    }


def _parse_response(
    *, client: Client, response: httpx.Response
) -> Optional[Union[Any, ErrorResponse, UploadDatasetVersionResponse]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = UploadDatasetVersionResponse.from_dict(response.json())

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
) -> Response[Union[Any, ErrorResponse, UploadDatasetVersionResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    workspace_id: int,
    dataset_id: str,
    *,
    client: AuthenticatedClient,
    multipart_data: MultiRequestFileSchema,
    header: Union[Unset, None, bool] = UNSET,
) -> Response[Union[Any, ErrorResponse, UploadDatasetVersionResponse]]:
    """Upload the content of a new dataset version

    Args:
        workspace_id (int):
        dataset_id (str):
        header (Union[Unset, None, bool]):
        multipart_data (MultiRequestFileSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ErrorResponse, UploadDatasetVersionResponse]]
    """

    kwargs = _get_kwargs(
        workspace_id=workspace_id,
        dataset_id=dataset_id,
        client=client,
        multipart_data=multipart_data,
        header=header,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    workspace_id: int,
    dataset_id: str,
    *,
    client: AuthenticatedClient,
    multipart_data: MultiRequestFileSchema,
    header: Union[Unset, None, bool] = UNSET,
) -> Optional[Union[Any, ErrorResponse, UploadDatasetVersionResponse]]:
    """Upload the content of a new dataset version

    Args:
        workspace_id (int):
        dataset_id (str):
        header (Union[Unset, None, bool]):
        multipart_data (MultiRequestFileSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ErrorResponse, UploadDatasetVersionResponse]
    """

    return sync_detailed(
        workspace_id=workspace_id,
        dataset_id=dataset_id,
        client=client,
        multipart_data=multipart_data,
        header=header,
    ).parsed


async def asyncio_detailed(
    workspace_id: int,
    dataset_id: str,
    *,
    client: AuthenticatedClient,
    multipart_data: MultiRequestFileSchema,
    header: Union[Unset, None, bool] = UNSET,
) -> Response[Union[Any, ErrorResponse, UploadDatasetVersionResponse]]:
    """Upload the content of a new dataset version

    Args:
        workspace_id (int):
        dataset_id (str):
        header (Union[Unset, None, bool]):
        multipart_data (MultiRequestFileSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ErrorResponse, UploadDatasetVersionResponse]]
    """

    kwargs = _get_kwargs(
        workspace_id=workspace_id,
        dataset_id=dataset_id,
        client=client,
        multipart_data=multipart_data,
        header=header,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    workspace_id: int,
    dataset_id: str,
    *,
    client: AuthenticatedClient,
    multipart_data: MultiRequestFileSchema,
    header: Union[Unset, None, bool] = UNSET,
) -> Optional[Union[Any, ErrorResponse, UploadDatasetVersionResponse]]:
    """Upload the content of a new dataset version

    Args:
        workspace_id (int):
        dataset_id (str):
        header (Union[Unset, None, bool]):
        multipart_data (MultiRequestFileSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ErrorResponse, UploadDatasetVersionResponse]
    """

    return (
        await asyncio_detailed(
            workspace_id=workspace_id,
            dataset_id=dataset_id,
            client=client,
            multipart_data=multipart_data,
            header=header,
        )
    ).parsed
