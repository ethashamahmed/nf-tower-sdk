"""Client for performing operations on Nextflow Tower API endpoints."""

from nf_tower_sdk.interfaces import AuthenticatedTowerClientInterface
from nf_tower_sdk.nft.api_library import AuthenticatedClient


# pylint: disable=too-few-public-methods
class AuthenticatedTowerClient(AuthenticatedTowerClientInterface):
    """Authenticated client for Nextflow Tower API."""

    def __init__(self, client: AuthenticatedClient):
        """
        Tower client with an `AuthenticatedClient` for making API calls.

        :param client: `AuthenticatedClient` object for Tower API.
        """
        self._client = client
