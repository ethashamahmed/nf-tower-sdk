"""Interfaces for Nextflow Tower clients."""

from abc import ABC, abstractmethod
from typing import List, Union

from nf_tower_sdk.exceptions import NextflowTowerClientError
from nf_tower_sdk.nft.api_library import AuthenticatedClient
from nf_tower_sdk.nft.api_library.models import (
    ComputeEnvResponseDto,
    CreateComputeEnvRequest,
    Launch,
    WorkflowLaunchResponse,
)


# pylint: disable=too-few-public-methods
class AuthenticatedTowerClientInterface(ABC):
    """Interface for Nextflow Tower client authenticated with API token."""

    _client: AuthenticatedClient


class ComputeEnvsClientInterface(ABC):
    """Interface for compute environments client."""

    @abstractmethod
    def create_compute_env(
        self,
        compute_env: CreateComputeEnvRequest,
        workspace_id: int = None,
    ) -> Union[str, NextflowTowerClientError]:
        """
        Create a new Tower compute environment.

        :param workspace_id: ID of Workspace containing the compute env.
        :param compute_env: Configuration for compute env to create.

        :return: Compute environment ID.
        """

    @abstractmethod
    def delete_compute_env(
        self,
        compute_env_id: str,
        workspace_id: int = None,
    ) -> Union[bool, NextflowTowerClientError]:
        """
        Delete an existing Tower compute environment.

        :param workspace_id: ID of Workspace containing the compute env.
        :param compute_env_id: ID of compute environment in Tower.

        :return: True if compute env is successfully deleted.
        """

    @abstractmethod
    def get_compute_envs(
        self, workspace_id: int = None, status: str = None
    ) -> Union[List, NextflowTowerClientError]:
        """
        List all Tower compute environments for the authenticated user or given workspace.

        :param workspace_id: ID of Workspace containing the compute env.
        :param status: Compute env status. Allowed: `CREATING┃AVAILABLE┃ERRORED┃INVALID`.

        :return: List of compute environments.
        """

    @abstractmethod
    def get_compute_env_id(
        self, compute_env_name: str, workspace_id: int = None
    ) -> Union[str, NextflowTowerClientError]:
        """
        Return compute env ID using compute env name. Exact name must be given.

        :param workspace_id: ID of Workspace containing the compute env.
        :param compute_env_name: Exact name of compute environment in Tower.

        :return: Compute environment ID.
        """

    @abstractmethod
    def get_compute_env_details(
        self, compute_env_id: str, workspace_id: int = None
    ) -> Union[ComputeEnvResponseDto, NextflowTowerClientError]:
        """
        Describe a Tower compute environment.

        :param workspace_id: ID of Workspace containing the compute env.
        :param compute_env_id: ID of compute environment in Tower.

        :return: Details of the compute environment in Tower.
        """

    @abstractmethod
    def set_primary_compute_env(
        self, compute_env_id: str, workspace_id: int = None
    ) -> Union[bool, NextflowTowerClientError]:
        """
        Defines the primary Tower compute environment.

        :param workspace_id: ID of Workspace containing the compute env.
        :param compute_env_id: ID of compute environment in Tower.

        :return: True if compute env is successfully set.
        """

    @abstractmethod
    def validate_compute_env_name(
        self, name: str, workspace_id: int = None
    ) -> Union[bool, NextflowTowerClientError]:
        """
        Check that is a valid compute env name.

        :param workspace_id: ID of Workspace containing the compute env.
        :param name: Name to validate.

        :return: True if name is valid.
        """


class OrgsClientInterface(ABC):
    """Interface for organisation client."""

    @abstractmethod
    def get_org_id(
        self, org_name: str
    ) -> Union[int, NextflowTowerClientError]:
        """
        Return organisation ID based on name.

        :param org_name: Name of organisation
        """


class PipelinesClientInterface(ABC):
    """Interface for Pipelines client."""

    @abstractmethod
    def is_valid_pipeline_params(
        self, workspace_id: int, pipeline_id: int, params: dict
    ) -> Union[bool, NextflowTowerClientError]:
        """
        Validate pipeline params using schema.

        Schema is retrieved from the pipeline defined in Tower.

        :param workspace_id: ID of Workspace containing the pipeline.
        :param pipeline_id: Pipeline numeric identifier
        :param params: Dictionary containing pipeline parameters

        :return: True if parameters are valid.
        """

    @abstractmethod
    def get_pipeline_id(
        self, workspace_id: int, pipeline_name: str
    ) -> Union[int, NextflowTowerClientError]:
        """
        Return pipeline id using pipeline_name.

        Every pipeline has a distinct name so searching using the
        exact name should only return one pipeline. If it fails
        to find the pipeline or gets error response from Tower
        a NextflowTowerClientError is raised

        :param workspace_id: ID of Workspace containing the pipeline.
        :param pipeline_name: Exact name of the pipeline

        :return: Pipeline ID
        """

    @abstractmethod
    def get_pipeline_launch(
        self, workspace_id: int, pipeline_id: int
    ) -> Union[Launch, NextflowTowerClientError]:
        """
        Return a pipeline launch for the given pipeline ID.

        Raise NextflowTowerClientError if no matching pipeline launch
        is found in Tower

        :param workspace_id: ID of Workspace containing the pipeline.
        :param pipeline_id: Pipeline numeric identifier

        :return: a Pipeline Launch object
        """

    @abstractmethod
    def get_pipeline_params_schema(
        self, workspace_id: int, pipeline_id: int
    ) -> Union[str, NextflowTowerClientError]:
        """
        Return the schema defined for the pipelines input parameters.

        :param workspace_id: ID of Workspace containing the pipeline.
        :param pipeline_id: Pipeline numeric identifier
        """


class WorkflowsClientInterface(ABC):
    """Interface for workflows client."""

    @abstractmethod
    def get_workflow_launch(
        self, workspace_id: int, workflow_id: str
    ) -> Union[WorkflowLaunchResponse, NextflowTowerClientError]:
        """
        Describe a workflow launch for the given ID.

        :param workspace_id: ID of Workspace containing the workflow.
        :param workflow_id: Workflow string identifier
        :return: Workflow description
        """

    @abstractmethod
    def launch_workflow(
        self, workspace_id: int, request: Launch
    ) -> Union[str, NextflowTowerClientError]:
        """
        Launch a new workflow and returns the workflow ID.

        Raise NextflowTowerClientError if Tower returns error
        when launching workflow.

        :param workspace_id: ID of Workspace containing the workflow.
        :param launch_request: a WorkflowLaunchRequest object

        :return: new workflow run ID
        """


class WorkspacesClientInterface(ABC):
    """Interface for workflows client."""

    @abstractmethod
    def get_workspace_id(
        self, org_id: int, workspace_name: str
    ) -> Union[int, NextflowTowerClientError]:
        """
        Return the ID in Nextflow Tower for a given workspace name.

        Raise NextflowTowerClientError if no matching workspace found in Tower.

        :param org_id: Organisation ID the workspace belongs to.
        :workspace_name: Name of the workspace.

        :return: Workspace ID
        """


class NextflowTowerClientInterface(ABC):
    """Interface for Nextflow Tower Client."""

    compute_envs: ComputeEnvsClientInterface
    orgs: OrgsClientInterface
    pipelines: PipelinesClientInterface
    workflows: WorkflowsClientInterface
    workspaces: WorkspacesClientInterface
