"""Client for compute envs endpoints in Tower."""

from typing import List, Union

from nf_tower_sdk.clients.client import AuthenticatedTowerClient
from nf_tower_sdk.exceptions import NextflowTowerClientError
from nf_tower_sdk.interfaces import ComputeEnvsClientInterface
from nf_tower_sdk.nft.api_library.api.default import (
    create_compute_env,
    delete_compute_env,
    describe_compute_env,
    list_compute_envs,
    update_compute_env_primary,
    validate_compute_env_name,
)
from nf_tower_sdk.nft.api_library.models import (
    ComputeEnvResponseDto,
    CreateComputeEnvRequest,
    CreateComputeEnvResponse,
    EmptyBodyRequest,
    ListComputeEnvsResponse,
)
from nf_tower_sdk.nft.api_library.types import Response


class ComputeEnvs(ComputeEnvsClientInterface, AuthenticatedTowerClient):
    """Client for interacting with compute envs related endpoints in Nextflow Tower API."""

    def create_compute_env(
        self,
        compute_env: CreateComputeEnvRequest,
        workspace_id: int = None,
    ) -> Union[str, NextflowTowerClientError]:
        response: Response[
            CreateComputeEnvResponse
        ] = self._handle_api_response(
            create_compute_env.sync_detailed(
                client=self._client,
                workspace_id=workspace_id,
                json_body=compute_env,
            )
        )
        return response.parsed.compute_env_id

    def delete_compute_env(
        self,
        compute_env_id: str,
        workspace_id: int = None,
    ) -> Union[bool, NextflowTowerClientError]:
        self._handle_api_response(
            delete_compute_env.sync_detailed(
                client=self._client,
                workspace_id=workspace_id,
                compute_env_id=compute_env_id,
            )
        )
        return True

    def get_compute_envs(
        self, workspace_id: int = None, status: str = None
    ) -> Union[List, NextflowTowerClientError]:
        response: Response[
            ListComputeEnvsResponse
        ] = self._handle_api_response(
            list_compute_envs.sync_detailed(
                client=self._client,
                workspace_id=workspace_id,
                status=status,
            )
        )
        return response.parsed.compute_envs

    def get_compute_env_id(
        self, compute_env_name: str, workspace_id: int = None
    ) -> Union[str, NextflowTowerClientError]:
        response: Response[
            ListComputeEnvsResponse
        ] = self._handle_api_response(
            list_compute_envs.sync_detailed(
                client=self._client,
                workspace_id=workspace_id,
                status="AVAILABLE",
            )
        )
        for compute_env in response.parsed.compute_envs:
            if compute_env.name.lower() == compute_env_name.lower():
                return str(compute_env.id)
        raise NextflowTowerClientError(
            f"Failed to find compute env with name {compute_env_name}."
        )

    def get_compute_env_details(
        self, compute_env_id: str, workspace_id: int = None
    ) -> Union[ComputeEnvResponseDto, NextflowTowerClientError]:
        response: Response[
            ComputeEnvResponseDto
        ] = self._handle_api_response(
            describe_compute_env.sync_detailed(
                client=self._client,
                workspace_id=workspace_id,
                compute_env_id=compute_env_id,
            )
        )
        return response.parsed.compute_env

    def set_primary_compute_env(
        self, compute_env_id: str, workspace_id: int = None
    ) -> Union[bool, NextflowTowerClientError]:
        self._handle_api_response(
            update_compute_env_primary.sync_detailed(
                client=self._client,
                workspace_id=workspace_id,
                compute_env_id=compute_env_id,
                json_body=EmptyBodyRequest(),
            )
        )
        return True

    def validate_compute_env_name(
        self, name: str, workspace_id: int = None
    ) -> Union[bool, NextflowTowerClientError]:
        self._handle_api_response(
            validate_compute_env_name.sync_detailed(
                client=self._client,
                workspace_id=workspace_id,
                name=name,
            )
        )
        return True
