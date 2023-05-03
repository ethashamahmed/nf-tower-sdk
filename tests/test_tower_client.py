"""Unit tests for NextflowTowerClient."""

from unittest import mock

from nf_tower_sdk.nft.api_library.api.default import (
    create_workflow_launch,
)
from nf_tower_sdk.nft.api_library.models import (
    Launch,
    SubmitWorkflowLaunchResponse,
    WorkflowLaunchResponse,
)
from nf_tower_sdk.tower import NextflowTowerClient


def test_client_can_validate_pipeline_params(
    tower_client: NextflowTowerClient,
    test_workflow: dict,
    test_workspace: dict,
):
    """
    Tests if client can validate input params for a pipeline
    based on the schema defined for it in Tower.
    """
    assert (
        tower_client.pipelines.is_valid_pipeline_params(
            test_workspace["id"],
            test_workflow["pipeline_id"],
            test_workflow["params"],
        )
        is True
    )


def test_client_can_get_compute_env_id(
    tower_client: NextflowTowerClient,
    test_compute_env: dict,
    test_workspace: dict,
):
    """
    Tests if client can get Tower ID for compute environment
    based on name.
    """
    compute_env_id = tower_client.compute_envs.get_compute_env_id(
        workspace_id=test_workspace["id"],
        compute_env_name=test_compute_env["name"],
    )
    assert isinstance(compute_env_id, str) is True


def test_client_can_get_org_id(
    tower_client: NextflowTowerClient, test_org: dict
):
    """
    Tests if client can get Tower ID for organisation based on name.
    """
    org_id = tower_client.orgs.get_org_id(test_org["name"])
    assert isinstance(org_id, int) is True


def test_client_can_get_pipeline_id(
    tower_client: NextflowTowerClient,
    test_workspace: dict,
    test_workflow: dict,
):
    """
    Tests if client can get Tower ID for pipeline based on name.
    """
    pipeline_id = tower_client.pipelines.get_pipeline_id(
        test_workspace["id"], test_workflow["name"]
    )
    assert isinstance(pipeline_id, int) is True


def test_client_can_get_pipeline_launch(
    tower_client: NextflowTowerClient,
    test_workspace: dict,
    test_workflow: dict,
):
    """
    Tests if client can get launch configuration for pipelines.
    """
    launch = tower_client.pipelines.get_pipeline_launch(
        test_workspace["id"], test_workflow["pipeline_id"]
    )
    assert isinstance(launch, Launch) is True


def test_client_can_get_pipeline_params_schema(
    tower_client: NextflowTowerClient,
    test_workspace: dict,
    test_workflow: dict,
):
    """
    Tests if client can get the schema of params for pipelines.
    """
    schema = tower_client.pipelines.get_pipeline_params_schema(
        test_workspace["id"], test_workflow["pipeline_id"]
    )
    assert isinstance(schema, str) is True


def test_client_can_get_workspace_id(
    tower_client: NextflowTowerClient,
    test_org: dict,
    test_workspace: dict,
):
    """
    Tests if client can get Tower ID for pipeline based on name.
    """
    workspace_id = tower_client.workspaces.get_workspace_id(
        test_org["id"], test_workspace["name"]
    )
    assert isinstance(workspace_id, int) is True


def test_client_can_get_workflow_launch(
    tower_client: NextflowTowerClient,
    test_workflow: dict,
    test_workspace: dict,
):
    """
    Tests if client can get launch configuration for workflows.
    """
    launch = tower_client.workflows.get_workflow_launch(
        test_workspace["id"], test_workflow["workflow_id"]
    )
    assert isinstance(launch, WorkflowLaunchResponse) is True


# pylint: disable=unused-argument
@mock.patch.object(
    create_workflow_launch,
    "sync",
    return_value=SubmitWorkflowLaunchResponse(workflow_id="test1"),
)
def test_client_can_launch_workflows(
    mocked_create,
    tower_client: NextflowTowerClient,
    test_workspace: dict,
    test_workflow: dict,
):
    """
    Tests if client can launch workflows in Nextflow Tower.
    """
    launch = tower_client.pipelines.get_pipeline_launch(
        test_workspace["id"], test_workflow["pipeline_id"]
    )
    workflow_id = tower_client.workflows.launch_workflow(
        test_workspace["id"], launch
    )
    assert isinstance(workflow_id, str) is True
