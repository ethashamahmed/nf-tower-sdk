"""Unit tests for ComputeEnvs."""

from typing import List
from unittest import mock

import pytest

from nf_tower_sdk.clients import ComputeEnvs
from nf_tower_sdk.exceptions import NextflowTowerClientError
from nf_tower_sdk.nft.api_library.api.default import (
    create_compute_env,
    delete_compute_env,
    update_compute_env_primary,
)
from nf_tower_sdk.nft.api_library.models import (
    ComputeEnvResponseDto,
    CreateComputeEnvRequest,
    CreateComputeEnvResponse,
)
from nf_tower_sdk.nft.api_library.types import Response


# pylint: disable=unused-argument
@mock.patch.object(
    create_compute_env,
    "sync_detailed",
    return_value=Response(
        status_code=204,
        parsed=CreateComputeEnvResponse("Test1"),
        headers="",
        content="",
    ),
)
def test_client_can_create_compute_env(
    mocked_create_compute,
    compute_env_client: ComputeEnvs,
    compute_env_request: CreateComputeEnvRequest,
):
    """
    Tests if client can create compute env in Tower.
    """
    compute_env_id = compute_env_client.create_compute_env(
        compute_env_request
    )
    assert isinstance(compute_env_id, str)


def test_create_compute_env_raises_error_for_bad_request(
    compute_env_client: ComputeEnvs,
):
    """
    Tests if create_compute_env raises error if request is missing required params.
    """
    with pytest.raises(NextflowTowerClientError):
        compute_env_client.create_compute_env(CreateComputeEnvRequest())


# pylint: disable=unused-argument
@mock.patch.object(
    delete_compute_env,
    "sync_detailed",
    return_value=Response(
        status_code=204,
        parsed=None,
        headers="",
        content="",
    ),
)
def test_client_can_delete_compute_env(
    mocked_delete_compute,
    compute_env_client: ComputeEnvs,
    test_compute_env: dict,
):
    """
    Tests if client can delete compute env in Tower.
    """
    is_deleted = compute_env_client.delete_compute_env(
        test_compute_env["id"]
    )
    assert is_deleted is True


def test_delete_compute_env_raises_error_for_bad_request(
    compute_env_client: ComputeEnvs,
):
    """
    Tests if delete_compute_env raises error for bad request.
    """
    with pytest.raises(NextflowTowerClientError):
        compute_env_client.delete_compute_env("test3534wtgd")


def test_client_can_get_compute_envs(
    compute_env_client: ComputeEnvs,
    test_workspace: dict,
):
    """
    Tests if client can get compute envs from Tower.
    """
    compute_envs = compute_env_client.get_compute_envs(
        workspace_id=test_workspace["id"]
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
            workspace_id=test_workspace["id"], status="Created"
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
        workspace_id=test_workspace["id"],
        compute_env_id=test_compute_env["id"],
    )
    assert isinstance(details, ComputeEnvResponseDto)


def test_get_compute_env_details_raises_error_for_bad_request(
    compute_env_client: ComputeEnvs,
    test_workspace: dict,
):
    """
    Tests if client raises error when get_compute_env_details fails.
    """
    with pytest.raises(NextflowTowerClientError):
        compute_env_client.get_compute_env_details(
            workspace_id=test_workspace["id"], compute_env_id=1
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
        workspace_id=test_workspace["id"],
        compute_env_name=test_compute_env["name"],
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
            workspace_id=test_workspace["id"],
            compute_env_name="non-existant-compute",
        )


# pylint: disable=unused-argument
@mock.patch.object(
    update_compute_env_primary,
    "sync_detailed",
    return_value=Response(
        status_code=204,
        parsed=None,
        headers="",
        content="",
    ),
)
def test_client_can_set_compute_env(
    mocked_compute_update_primary,
    compute_env_client: ComputeEnvs,
    test_compute_env: dict,
):
    """
    Tests if client can set the primary compute env in Tower.
    """
    is_updated = compute_env_client.set_primary_compute_env(
        test_compute_env["id"]
    )
    assert is_updated is True


def test_set_primary_compute_env_raises_error_for_bad_request(
    compute_env_client: ComputeEnvs,
):
    """
    Tests if client raises error when set_primary_compute_env fails.
    """
    with pytest.raises(NextflowTowerClientError):
        compute_env_client.set_primary_compute_env("difghdrfoihg")


def test_client_can_validate_compute_env_name(
    compute_env_client: ComputeEnvs,
):
    """
    Tests if client can validate the compute env name.
    """
    is_valid_name = compute_env_client.validate_compute_env_name(
        "hello-world"
    )
    assert is_valid_name is True


def test_validate_compute_env_name_raises_error_for_bad_name(
    compute_env_client: ComputeEnvs,
):
    """
    Tests validate_compute_env_name raises error if name doesn't meet requirements.
    """
    with pytest.raises(NextflowTowerClientError):
        compute_env_client.validate_compute_env_name("a")
