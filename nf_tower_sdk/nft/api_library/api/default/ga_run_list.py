from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import Client
from ...models.error_response import ErrorResponse
from ...models.run_list_response import RunListResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    page_size: Union[Unset, None, int] = UNSET,
    page_token: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/ga4gh/wes/v1/runs".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["page_size"] = page_size

    params["page_token"] = page_token

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
) -> Optional[Union[Any, ErrorResponse, RunListResponse]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = RunListResponse.from_dict(response.json())

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
) -> Response[Union[Any, ErrorResponse, RunListResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Client,
    page_size: Union[Unset, None, int] = UNSET,
    page_token: Union[Unset, None, str] = UNSET,
) -> Response[Union[Any, ErrorResponse, RunListResponse]]:
    """GA4GH list runs

    Args:
        page_size (Union[Unset, None, int]):
        page_token (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ErrorResponse, RunListResponse]]
    """

    kwargs = _get_kwargs(
        client=client,
        page_size=page_size,
        page_token=page_token,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Client,
    page_size: Union[Unset, None, int] = UNSET,
    page_token: Union[Unset, None, str] = UNSET,
) -> Optional[Union[Any, ErrorResponse, RunListResponse]]:
    """GA4GH list runs

    Args:
        page_size (Union[Unset, None, int]):
        page_token (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ErrorResponse, RunListResponse]
    """

    return sync_detailed(
        client=client,
        page_size=page_size,
        page_token=page_token,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    page_size: Union[Unset, None, int] = UNSET,
    page_token: Union[Unset, None, str] = UNSET,
) -> Response[Union[Any, ErrorResponse, RunListResponse]]:
    """GA4GH list runs

    Args:
        page_size (Union[Unset, None, int]):
        page_token (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ErrorResponse, RunListResponse]]
    """

    kwargs = _get_kwargs(
        client=client,
        page_size=page_size,
        page_token=page_token,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Client,
    page_size: Union[Unset, None, int] = UNSET,
    page_token: Union[Unset, None, str] = UNSET,
) -> Optional[Union[Any, ErrorResponse, RunListResponse]]:
    """GA4GH list runs

    Args:
        page_size (Union[Unset, None, int]):
        page_token (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ErrorResponse, RunListResponse]
    """

    return (
        await asyncio_detailed(
            client=client,
            page_size=page_size,
            page_token=page_token,
        )
    ).parsed
