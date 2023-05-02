"""Client for workflows endpoints in Tower."""

from typing import Union

from httpx._exceptions import ReadTimeout

from nf_tower_sdk.clients.client import AuthenticatedTowerClient
from nf_tower_sdk.exceptions import NextflowTowerClientError
from nf_tower_sdk.interfaces import WorkflowsClientInterface
from nf_tower_sdk.nft.api_library.api.default import (
    create_workflow_launch,
    describe_workflow_launch,
)
from nf_tower_sdk.nft.api_library.models import (
    ErrorResponse,
    Launch,
    SubmitWorkflowLaunchRequest,
    WorkflowLaunchResponse,
)


# pylint: disable=too-few-public-methods
class Workflows(WorkflowsClientInterface, AuthenticatedTowerClient):
    """Client for interacting with workflows related endpoints in Nextflow Tower API."""

    def get_workflow_launch(
        self, workspace_id: int, workflow_id: str
    ) -> Union[WorkflowLaunchResponse, NextflowTowerClientError]:
        workflow = describe_workflow_launch.sync(
            client=self._client,
            workspace_id=workspace_id,
            workflow_id=workflow_id,
        )
        if isinstance(workflow, (ErrorResponse, type(None))):
            raise NextflowTowerClientError(
                f"Failed to find a workflow launch in Tower for workflow_id: {workflow_id}. "
                f"Response from tower: {workflow}"
            )
        return workflow.launch

    def launch_workflow(
        self, workspace_id: int, request: Launch
    ) -> Union[str, NextflowTowerClientError]:
        try:
            submit_workflow_response = create_workflow_launch.sync(
                client=self._client,
                workspace_id=workspace_id,
                json_body=SubmitWorkflowLaunchRequest(launch=request),
            )
        except ReadTimeout as err:
            raise NextflowTowerClientError(
                f"Tower API call timeout when launching pipeline: {request.pipeline}. "
                f"NOTE: Workflow might have launched before read timeout."
            ) from err

        if isinstance(submit_workflow_response, ErrorResponse):
            raise NextflowTowerClientError(
                f"Failed to launch pipeline: {request.pipeline}, "
                f"error: {submit_workflow_response}"
            )
        return submit_workflow_response.workflow_id
