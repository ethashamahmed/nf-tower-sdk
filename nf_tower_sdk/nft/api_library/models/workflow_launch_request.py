import datetime
from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="WorkflowLaunchRequest")


@attr.s(auto_attribs=True)
class WorkflowLaunchRequest:
    """
    Attributes:
        id (Union[Unset, str]):
        compute_env_id (Union[Unset, str]):
        run_name (Union[Unset, str]):
        pipeline (Union[Unset, str]):
        work_dir (Union[Unset, str]):
        revision (Union[Unset, str]):
        session_id (Union[Unset, str]):
        config_profiles (Union[Unset, List[str]]):
        user_secrets (Union[Unset, List[str]]):
        workspace_secrets (Union[Unset, List[str]]):
        config_text (Union[Unset, str]):
        tower_config (Union[Unset, str]):
        params_text (Union[Unset, str]):
        pre_run_script (Union[Unset, str]):
        post_run_script (Union[Unset, str]):
        main_script (Union[Unset, str]):
        entry_name (Union[Unset, str]):
        schema_name (Union[Unset, str]):
        resume (Union[Unset, bool]):
        pull_latest (Union[Unset, bool]):
        stub_run (Union[Unset, bool]):
        optimization_id (Union[Unset, str]):
        labels_ids (Union[Unset, List[int]]):
        date_created (Union[Unset, datetime.datetime]):
    """

    id: Union[Unset, str] = UNSET
    compute_env_id: Union[Unset, str] = UNSET
    run_name: Union[Unset, str] = UNSET
    pipeline: Union[Unset, str] = UNSET
    work_dir: Union[Unset, str] = UNSET
    revision: Union[Unset, str] = UNSET
    session_id: Union[Unset, str] = UNSET
    config_profiles: Union[Unset, List[str]] = UNSET
    user_secrets: Union[Unset, List[str]] = UNSET
    workspace_secrets: Union[Unset, List[str]] = UNSET
    config_text: Union[Unset, str] = UNSET
    tower_config: Union[Unset, str] = UNSET
    params_text: Union[Unset, str] = UNSET
    pre_run_script: Union[Unset, str] = UNSET
    post_run_script: Union[Unset, str] = UNSET
    main_script: Union[Unset, str] = UNSET
    entry_name: Union[Unset, str] = UNSET
    schema_name: Union[Unset, str] = UNSET
    resume: Union[Unset, bool] = UNSET
    pull_latest: Union[Unset, bool] = UNSET
    stub_run: Union[Unset, bool] = UNSET
    optimization_id: Union[Unset, str] = UNSET
    labels_ids: Union[Unset, List[int]] = UNSET
    date_created: Union[Unset, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        compute_env_id = self.compute_env_id
        run_name = self.run_name
        pipeline = self.pipeline
        work_dir = self.work_dir
        revision = self.revision
        session_id = self.session_id
        config_profiles: Union[Unset, List[str]] = UNSET
        if not isinstance(self.config_profiles, Unset):
            config_profiles = self.config_profiles

        user_secrets: Union[Unset, List[str]] = UNSET
        if not isinstance(self.user_secrets, Unset):
            user_secrets = self.user_secrets

        workspace_secrets: Union[Unset, List[str]] = UNSET
        if not isinstance(self.workspace_secrets, Unset):
            workspace_secrets = self.workspace_secrets

        config_text = self.config_text
        tower_config = self.tower_config
        params_text = self.params_text
        pre_run_script = self.pre_run_script
        post_run_script = self.post_run_script
        main_script = self.main_script
        entry_name = self.entry_name
        schema_name = self.schema_name
        resume = self.resume
        pull_latest = self.pull_latest
        stub_run = self.stub_run
        optimization_id = self.optimization_id
        labels_ids: Union[Unset, List[int]] = UNSET
        if not isinstance(self.labels_ids, Unset):
            labels_ids = self.labels_ids

        date_created: Union[Unset, str] = UNSET
        if not isinstance(self.date_created, Unset):
            date_created = self.date_created.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if compute_env_id is not UNSET:
            field_dict["computeEnvId"] = compute_env_id
        if run_name is not UNSET:
            field_dict["runName"] = run_name
        if pipeline is not UNSET:
            field_dict["pipeline"] = pipeline
        if work_dir is not UNSET:
            field_dict["workDir"] = work_dir
        if revision is not UNSET:
            field_dict["revision"] = revision
        if session_id is not UNSET:
            field_dict["sessionId"] = session_id
        if config_profiles is not UNSET:
            field_dict["configProfiles"] = config_profiles
        if user_secrets is not UNSET:
            field_dict["userSecrets"] = user_secrets
        if workspace_secrets is not UNSET:
            field_dict["workspaceSecrets"] = workspace_secrets
        if config_text is not UNSET:
            field_dict["configText"] = config_text
        if tower_config is not UNSET:
            field_dict["towerConfig"] = tower_config
        if params_text is not UNSET:
            field_dict["paramsText"] = params_text
        if pre_run_script is not UNSET:
            field_dict["preRunScript"] = pre_run_script
        if post_run_script is not UNSET:
            field_dict["postRunScript"] = post_run_script
        if main_script is not UNSET:
            field_dict["mainScript"] = main_script
        if entry_name is not UNSET:
            field_dict["entryName"] = entry_name
        if schema_name is not UNSET:
            field_dict["schemaName"] = schema_name
        if resume is not UNSET:
            field_dict["resume"] = resume
        if pull_latest is not UNSET:
            field_dict["pullLatest"] = pull_latest
        if stub_run is not UNSET:
            field_dict["stubRun"] = stub_run
        if optimization_id is not UNSET:
            field_dict["optimizationId"] = optimization_id
        if labels_ids is not UNSET:
            field_dict["labelsIds"] = labels_ids
        if date_created is not UNSET:
            field_dict["dateCreated"] = date_created

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        compute_env_id = d.pop("computeEnvId", UNSET)

        run_name = d.pop("runName", UNSET)

        pipeline = d.pop("pipeline", UNSET)

        work_dir = d.pop("workDir", UNSET)

        revision = d.pop("revision", UNSET)

        session_id = d.pop("sessionId", UNSET)

        config_profiles = cast(List[str], d.pop("configProfiles", UNSET))

        user_secrets = cast(List[str], d.pop("userSecrets", UNSET))

        workspace_secrets = cast(List[str], d.pop("workspaceSecrets", UNSET))

        config_text = d.pop("configText", UNSET)

        tower_config = d.pop("towerConfig", UNSET)

        params_text = d.pop("paramsText", UNSET)

        pre_run_script = d.pop("preRunScript", UNSET)

        post_run_script = d.pop("postRunScript", UNSET)

        main_script = d.pop("mainScript", UNSET)

        entry_name = d.pop("entryName", UNSET)

        schema_name = d.pop("schemaName", UNSET)

        resume = d.pop("resume", UNSET)

        pull_latest = d.pop("pullLatest", UNSET)

        stub_run = d.pop("stubRun", UNSET)

        optimization_id = d.pop("optimizationId", UNSET)

        labels_ids = cast(List[int], d.pop("labelsIds", UNSET))

        _date_created = d.pop("dateCreated", UNSET)
        date_created: Union[Unset, datetime.datetime]
        if isinstance(_date_created, Unset):
            date_created = UNSET
        else:
            date_created = isoparse(_date_created)

        workflow_launch_request = cls(
            id=id,
            compute_env_id=compute_env_id,
            run_name=run_name,
            pipeline=pipeline,
            work_dir=work_dir,
            revision=revision,
            session_id=session_id,
            config_profiles=config_profiles,
            user_secrets=user_secrets,
            workspace_secrets=workspace_secrets,
            config_text=config_text,
            tower_config=tower_config,
            params_text=params_text,
            pre_run_script=pre_run_script,
            post_run_script=post_run_script,
            main_script=main_script,
            entry_name=entry_name,
            schema_name=schema_name,
            resume=resume,
            pull_latest=pull_latest,
            stub_run=stub_run,
            optimization_id=optimization_id,
            labels_ids=labels_ids,
            date_created=date_created,
        )

        workflow_launch_request.additional_properties = d
        return workflow_launch_request

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
