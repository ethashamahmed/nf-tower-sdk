"""Unit tests for ComputeEnvs."""

from typing import List

import pytest

from nf_tower_sdk.clients import ComputeEnvs
from nf_tower_sdk.exceptions import NextflowTowerClientError
from nf_tower_sdk.nft.api_library.models import (
    ComputeEnvResponseDto,
    CreateComputeEnvRequest,
)


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
    compute_envs = compute_env_client.get_compute_envs(
        test_workspace["id"]
    )
    assert isinstance(compute_envs, List)


def test_get_compute_envs_raises_error_for_bad_request(
    compute_env_client: ComputeEnvs,
    test_workspace: dict,
):
    """
    Tests if client raises error when get_compute_envs fails.
    """
    with pytest.raises(NextflowTowerClientError):
        compute_env_client.get_compute_envs(
            test_workspace["id"], status="Created"
        )


def test_client_can_get_compute_env_details(
    compute_env_client: ComputeEnvs,
    test_compute_env: dict,
    test_workspace: dict,
):
    """
    Tests if client can get details of compute env from Tower.
    """
    details = compute_env_client.get_compute_env_details(
        test_workspace["id"], test_compute_env["id"]
    )
    assert isinstance(details, ComputeEnvResponseDto)


def test_get_compute_env_details_raises_error_for_bad_request(
    compute_env_client: ComputeEnvs,
    test_workspace: dict,
):
    """
    Tests if client can get details of compute env from Tower.
    """
    with pytest.raises(NextflowTowerClientError):
        compute_env_client.get_compute_env_details(
            test_workspace["id"], 1
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


def test_get_compute_env_id_raises_error_for_bad_request(
    compute_env_client: ComputeEnvs,
    test_workspace: dict,
):
    """
    Tests if client raises error when get_compute_env_id fails.
    """
    with pytest.raises(NextflowTowerClientError):
        compute_env_client.get_compute_env_id(
            test_workspace["id"], "non-existant-compute"
        )


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
