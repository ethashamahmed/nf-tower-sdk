"""Unit tests for ComputeEnvs."""

import pytest

from nf_tower_sdk.clients import ComputeEnvs
from nf_tower_sdk.nft.api_library.models import CreateComputeEnvRequest


def test_client_can_create_compute_env(
    compute_env_client: ComputeEnvs, test_workspace: dict
):
    """
    Tests if client can create compute env in Tower.
    """
    with pytest.raises(NotImplementedError):
        compute_env_client.create_compute_env(
            test_workspace["id"], CreateComputeEnvRequest()
        )


def test_client_can_delete_compute_env(
    compute_env_client: ComputeEnvs,
    test_compute_env: dict,
    test_workspace: dict,
):
    """
    Tests if client can create compute env in Tower.
    """
    with pytest.raises(NotImplementedError):
        compute_env_client.delete_compute_env(
            test_workspace["id"], test_compute_env["id"]
        )


def test_client_can_get_compute_envs(
    compute_env_client: ComputeEnvs,
    test_workspace: dict,
):
    """
    Tests if client can get compute envs from Tower.
    """
    with pytest.raises(NotImplementedError):
        compute_env_client.get_compute_envs(test_workspace["id"])


def test_client_can_get_compute_env_details(
    compute_env_client: ComputeEnvs,
    test_compute_env: dict,
    test_workspace: dict,
):
    """
    Tests if client can get details of compute env from Tower.
    """
    with pytest.raises(NotImplementedError):
        compute_env_client.get_compute_env_details(
            test_workspace["id"], test_compute_env["id"]
        )


def test_client_can_get_compute_env_id(
    compute_env_client: ComputeEnvs,
    test_compute_env: dict,
    test_workspace: dict,
):
    """
    Tests if client can get Tower ID for compute environment
    based on name.
    """
    compute_env_id = compute_env_client.get_compute_env_id(
        test_workspace["id"], test_compute_env["name"]
    )
    assert isinstance(compute_env_id, str) is True


def test_client_can_set_compute_env(
    compute_env_client: ComputeEnvs,
    test_compute_env: dict,
    test_workspace: dict,
):
    """
    Tests if client can set the primary compute env in Tower.
    """
    with pytest.raises(NotImplementedError):
        compute_env_client.set_primary_compute_env(
            test_workspace["id"], test_compute_env["id"]
        )


def test_client_can_validate_compute_env_name(
    compute_env_client: ComputeEnvs,
    test_compute_env: dict,
    test_workspace: dict,
):
    """
    Tests if client can validate the compute env name.
    """
    with pytest.raises(NotImplementedError):
        compute_env_client.validate_compute_env_name(
            test_workspace["id"], test_compute_env["name"]
        )
