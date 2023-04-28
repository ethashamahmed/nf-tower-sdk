"""Client for performing operations on Nextflow Tower API endpoints."""

from nf_tower_sdk.interfaces import AuthenticatedTowerClientInterface


# pylint: disable=too-few-public-methods
class AuthenticatedTowerClient(AuthenticatedTowerClientInterface):
    """Authenticated client for Nextflow Tower API."""
