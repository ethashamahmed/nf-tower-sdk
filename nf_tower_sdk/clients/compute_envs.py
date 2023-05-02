"""Client for compute envs endpoints in Tower."""

from typing import Union

from nf_tower_sdk.clients.client import AuthenticatedTowerClient
from nf_tower_sdk.exceptions import NextflowTowerClientError
from nf_tower_sdk.interfaces import ComputeEnvsClientInterface
from nf_tower_sdk.nft.api_library.api.default import list_compute_envs
from nf_tower_sdk.nft.api_library.models import ListComputeEnvsResponse


# pylint: disable=too-few-public-methods
class ComputeEnvs(ComputeEnvsClientInterface, AuthenticatedTowerClient):
    """Client for interacting with compute envs related endpoints in Nextflow Tower API."""

    def get_compute_env_id(
        self, workspace_id: int, compute_env_name: str
    ) -> Union[str, NextflowTowerClientError]:
        compute_envs = list_compute_envs.sync(
            client=self._client,
            workspace_id=workspace_id,
            status="AVAILABLE",
        )
        if isinstance(compute_envs, ListComputeEnvsResponse):
            for compute_env in compute_envs.compute_envs:
                if compute_env.name.lower() == compute_env_name.lower():
                    return str(compute_env.id)

        raise NextflowTowerClientError(
            f"Failed to find compute env: {compute_env_name}. Response from tower: {compute_envs}"
        )
