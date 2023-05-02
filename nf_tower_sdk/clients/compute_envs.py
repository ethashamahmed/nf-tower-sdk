"""Client for compute envs endpoints in Tower."""

from typing import List, Union

from nf_tower_sdk.clients.client import AuthenticatedTowerClient
from nf_tower_sdk.exceptions import NextflowTowerClientError
from nf_tower_sdk.interfaces import ComputeEnvsClientInterface
from nf_tower_sdk.nft.api_library.api.default import list_compute_envs
from nf_tower_sdk.nft.api_library.models import (
    CreateComputeEnvRequest,
    DescribeComputeEnvResponse,
    ListComputeEnvsResponse,
)


class ComputeEnvs(ComputeEnvsClientInterface, AuthenticatedTowerClient):
    """Client for interacting with compute envs related endpoints in Nextflow Tower API."""

    def create_compute_env(
        self, workspace_id: int, compute_env: CreateComputeEnvRequest
    ) -> Union[str, NextflowTowerClientError]:
        raise NotImplementedError()

    def delete_compute_env(
        self, workspace_id: int, compute_env_id: str
    ) -> Union[bool, NextflowTowerClientError]:
        raise NotImplementedError()

    def get_compute_envs(
        self, workspace_id: int, status: str = None
    ) -> Union[List, NextflowTowerClientError]:
        raise NotImplementedError()

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

    def get_compute_env_details(
        self, workspace_id: int, compute_env_id: str
    ) -> Union[DescribeComputeEnvResponse, NextflowTowerClientError]:
        raise NotImplementedError()

    def set_primary_compute_env(
        self, workspace_id: int, compute_env_id: str
    ) -> Union[bool, NextflowTowerClientError]:
        raise NotImplementedError()

    def validate_compute_env_name(
        self, workspace_id: int, name: str
    ) -> Union[bool, NextflowTowerClientError]:
        raise NotImplementedError()
