"""Client for performing operations on Nextflow Tower API endpoints."""

from nf_tower_sdk.interfaces import AuthenticatedTowerClientInterface
from nf_tower_sdk.nft.api_library import AuthenticatedClient


# pylint: disable=too-few-public-methods
class AuthenticatedTowerClient(AuthenticatedTowerClientInterface):
    """Authenticated client for Nextflow Tower API."""

    def __init__(self, client: AuthenticatedClient):
        """
        Client which has been authenticated for Nextflow Tower API.

        :param url: URL for Nextflow tower. Example "https://tower.nf".
        :param api_token: Tower API authentication token.
        :param timeout: The maximum amount of a time in seconds a request can take.
             API functions will raise httpx.TimeoutException if this is exceeded.
        """
        self._client = client
