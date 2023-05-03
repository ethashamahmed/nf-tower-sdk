"""Client for performing operations on Nextflow Tower API endpoints."""

from http import HTTPStatus
from typing import Union

from nf_tower_sdk.exceptions import NextflowTowerClientError
from nf_tower_sdk.interfaces import AuthenticatedTowerClientInterface
from nf_tower_sdk.nft.api_library import AuthenticatedClient
from nf_tower_sdk.nft.api_library.models import ErrorResponse
from nf_tower_sdk.nft.api_library.types import Response


# pylint: disable=too-few-public-methods
class AuthenticatedTowerClient(AuthenticatedTowerClientInterface):
    """Authenticated client for Nextflow Tower API."""

    def __init__(self, client: AuthenticatedClient):
        """
        Tower client with an `AuthenticatedClient` for making API calls.

        :param client: `AuthenticatedClient` object for Tower API.
        """
        self._client = client

    def _handle_api_response(
        self, response: Response
    ) -> Union[Response, NextflowTowerClientError]:
        """
        Checks if API returned error response.

        :param response: `Response` object from Tower API.
        """
        if isinstance(response, Response):
            if response.status_code in [
                HTTPStatus.BAD_REQUEST,
                HTTPStatus.CONFLICT,
            ]:
                raise NextflowTowerClientError(
                    response.content,
                )
            if response.status_code is HTTPStatus.FORBIDDEN:
                raise NextflowTowerClientError("Operation not allowed.")
        if isinstance(response, ErrorResponse):
            raise NextflowTowerClientError(
                response.content,
            )

        return response
