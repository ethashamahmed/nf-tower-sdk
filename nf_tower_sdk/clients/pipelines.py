"""Client for pipelines endpoints in Tower."""

import json
from typing import Union

from jsonschema import ValidationError, validate

from nf_tower_sdk.clients.client import AuthenticatedTowerClient
from nf_tower_sdk.exceptions import NextflowTowerClientError
from nf_tower_sdk.interfaces import PipelinesClientInterface
from nf_tower_sdk.nft.api_library.api.default import (
    describe_pipeline_launch,
    describe_pipeline_schema,
    list_pipelines,
)
from nf_tower_sdk.nft.api_library.models import (
    ErrorResponse,
    Launch,
    ListPipelinesResponse,
)


class Pipelines(PipelinesClientInterface, AuthenticatedTowerClient):
    """Client for interacting with pipelines related endpoints in Nextflow Tower API."""

    def is_valid_pipeline_params(
        self, workspace_id: int, pipeline_id: int, params: dict
    ) -> Union[bool, NextflowTowerClientError]:
        params_schema = self.get_pipeline_params_schema(
            workspace_id, pipeline_id
        )
        try:
            validate(instance=params, schema=json.loads(params_schema))
        except ValidationError as err:
            raise NextflowTowerClientError from err
        return True

    def get_pipeline_id(
        self, workspace_id: int, pipeline_name: str
    ) -> Union[int, NextflowTowerClientError]:
        pipeline_list_response = list_pipelines.sync(
            client=self._client,
            workspace_id=workspace_id,
            search=pipeline_name,
        )
        if isinstance(pipeline_list_response, ListPipelinesResponse):
            for pipeline in pipeline_list_response.pipelines:
                if pipeline.name.lower() == pipeline_name.lower():
                    return pipeline.pipeline_id
        raise NextflowTowerClientError(
            f"Failed to find pipeline: {pipeline_name}, "
            f"Response from Tower: {pipeline_list_response}"
        )

    def get_pipeline_launch(
        self, workspace_id: int, pipeline_id: int
    ) -> Union[Launch, NextflowTowerClientError]:
        pipeline = describe_pipeline_launch.sync(
            client=self._client,
            workspace_id=workspace_id,
            pipeline_id=pipeline_id,
        )
        if isinstance(pipeline, (ErrorResponse, type(None))):
            raise NextflowTowerClientError(
                f"Failed to find a pipeline launch in Tower for pipeline_id: {pipeline_id}. "
                f"Response from tower: {pipeline}"
            )
        return pipeline.launch

    def get_pipeline_params_schema(
        self, workspace_id: int, pipeline_id: int
    ) -> Union[str, NextflowTowerClientError]:
        get_schema_response = describe_pipeline_schema.sync(
            client=self._client,
            workspace_id=workspace_id,
            pipeline_id=pipeline_id,
        )
        if isinstance(get_schema_response, (ErrorResponse, type(None))):
            raise NextflowTowerClientError(
                f"Failed to get pipeline parameters schema. Error: {get_schema_response}"
            )
        return get_schema_response.schema
