"""Client for organisations endpoints in Tower."""

from typing import Union

from nf_tower_sdk.clients.client import AuthenticatedTowerClient
from nf_tower_sdk.exceptions import NextflowTowerClientError
from nf_tower_sdk.interfaces import OrgsClientInterface
from nf_tower_sdk.nft.api_library.api.default import list_organizations
from nf_tower_sdk.nft.api_library.models import (
    ListOrganizationsResponse,
)


# pylint: disable=too-few-public-methods
class Orgs(OrgsClientInterface, AuthenticatedTowerClient):
    """Client for interacting with organisations related endpoints in Nextflow Tower API."""

    def get_org_id(
        self, org_name: str
    ) -> Union[int, NextflowTowerClientError]:
        list_org_response = list_organizations.sync(client=self._client)
        if isinstance(list_org_response, ListOrganizationsResponse):
            for org in list_org_response.organizations:
                if org.name.lower() == org_name.lower():
                    return org.org_id
        raise NextflowTowerClientError(
            f"Tower organisation {org_name} doesn't exist."
        )
