"""Client for workspaces endpoints in Tower."""

from typing import Union

from nf_tower_sdk.clients.client import AuthenticatedTowerClient
from nf_tower_sdk.exceptions import NextflowTowerClientError
from nf_tower_sdk.interfaces import WorkspacesClientInterface
from nf_tower_sdk.nft.api_library.api.default import list_workspaces
from nf_tower_sdk.nft.api_library.models import ListWorkspacesResponse


# pylint: disable=too-few-public-methods
class Workspaces(WorkspacesClientInterface, AuthenticatedTowerClient):
    """Client for interacting with workspaces related endpoints in Nextflow Tower API."""

    def get_workspace_id(
        self, org_id: int, workspace_name: str
    ) -> Union[int, NextflowTowerClientError]:
        workspaces_response = list_workspaces.sync(
            client=self._client, org_id=org_id
        )
        if isinstance(workspaces_response, ListWorkspacesResponse):
            for workspace in workspaces_response.workspaces:
                if workspace.name == workspace_name:
                    return workspace.id
        raise NextflowTowerClientError(
            f"Tower Workspace {workspace_name} doesn't exist."
        )
