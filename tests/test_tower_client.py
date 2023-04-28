"""Unit tests for NextflowTowerClient."""

from nf_tower_sdk.tower import (
    Launch,
    NextflowTowerClient,
    WorkflowLaunchResponse,
)


def test_client_has_workflow_run_base_url(
    test_client: NextflowTowerClient,
):
    """
    Tests if client has property containing base url
    for workflow runs in Tower.
    """
    assert (
        test_client.tower_workflow_run_base_url
        == "https://tower.nf/orgs/community/workspaces/showcase/watch"
    )


def test_client_can_validate_pipeline_params(
    test_client: NextflowTowerClient, test_workflow: dict
):
    """
    Tests if client can validate input params for a pipeline
    based on the schema defined for it in Tower.
    """
    assert (
        test_client.pipelines.is_valid_pipeline_params(
            test_workflow["workspace_id"],
            test_workflow["id"],
            test_workflow["params"],
        )
        is True
    )


def test_client_can_get_compute_env_id(
    test_client: NextflowTowerClient,
):
    """
    Tests if client can get Tower ID for compute environment
    based on name.
    """
    compute_env_id = test_client.get_compute_env_id("AWS_Batch_Ireland")
    assert isinstance(compute_env_id, str) is True


def test_client_can_get_org_id(test_client: NextflowTowerClient):
    """
    Tests if client can get Tower ID for organisation based on name.
    """
    org_id = test_client.get_org_id("community")
    assert isinstance(org_id, int) is True


def test_client_can_get_pipeline_id(
    test_client: NextflowTowerClient, test_workflow: dict
):
    """
    Tests if client can get Tower ID for pipeline based on name.
    """
    pipeline_id = test_client.pipelines.get_pipeline_id(
        test_workflow["workspace_id"], test_workflow["name"]
    )
    assert isinstance(pipeline_id, int) is True


def test_client_can_get_pipeline_launch(
    test_client: NextflowTowerClient, test_workflow: dict
):
    """
    Tests if client can get launch configuration for pipelines.
    """
    launch = test_client.pipelines.get_pipeline_launch(
        test_workflow["workspace_id"], test_workflow["id"]
    )
    assert isinstance(launch, Launch) is True


def test_client_can_get_pipeline_params_schema(
    test_client: NextflowTowerClient, test_workflow: dict
):
    """
    Tests if client can get the schema of params for pipelines.
    """
    schema = test_client.pipelines.get_pipeline_params_schema(
        test_workflow["workspace_id"], test_workflow["id"]
    )
    assert isinstance(schema, str) is True


def test_client_can_get_workspace_id(test_client: NextflowTowerClient):
    """
    Tests if client can get Tower ID for pipeline based on name.
    """
    workspace_id = test_client.get_workspace_id(
        187965850823746, "showcase"
    )
    assert isinstance(workspace_id, int) is True


def test_client_can_get_workflow_launch(
    test_client: NextflowTowerClient,
):
    """
    Tests if client can get launch configuration for workflows.
    """
    launch = test_client.get_workflow_launch("2ZTGegpXyjPF3U")
    assert isinstance(launch, WorkflowLaunchResponse) is True


def test_client_can_launch_workflows(
    test_client: NextflowTowerClient, test_workflow: dict
):
    """
    Tests if client can launch workflows in Nextflow Tower.
    """
    launch = test_client.get_pipeline_launch(
        test_workflow["workspace_id"], test_workflow["id"]
    )
    workflow_id = test_client.launch_workflow(launch)
    assert isinstance(workflow_id, str) is True
