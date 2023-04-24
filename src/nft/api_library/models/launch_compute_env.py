import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.compute_env_platform import ComputeEnvPlatform
from ..models.compute_env_status import ComputeEnvStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.altair_pbs_configuration import AltairPBSConfiguration
    from ..models.amazon_eks_cluster_configuration import AmazonEKSClusterConfiguration
    from ..models.aws_batch_configuration import AWSBatchConfiguration
    from ..models.azure_batch_configuration import AzureBatchConfiguration
    from ..models.google_gke_cluster_configuration import GoogleGKEClusterConfiguration
    from ..models.google_life_sciences_configuration import GoogleLifeSciencesConfiguration
    from ..models.ibmlsf_configuration import IBMLSFConfiguration
    from ..models.kubernetes_compute_configuration import KubernetesComputeConfiguration
    from ..models.slurm_configuration import SlurmConfiguration
    from ..models.univa_grid_engine_configuration import UnivaGridEngineConfiguration


T = TypeVar("T", bound="LaunchComputeEnv")


@attr.s(auto_attribs=True)
class LaunchComputeEnv:
    """
    Attributes:
        name (str):
        config (Union['AWSBatchConfiguration', 'AltairPBSConfiguration', 'AmazonEKSClusterConfiguration',
            'AzureBatchConfiguration', 'GoogleGKEClusterConfiguration', 'GoogleLifeSciencesConfiguration',
            'IBMLSFConfiguration', 'KubernetesComputeConfiguration', 'SlurmConfiguration', 'UnivaGridEngineConfiguration']):
        id (Union[Unset, str]):
        description (Union[Unset, str]):
        platform (Union[Unset, ComputeEnvPlatform]):
        date_created (Union[Unset, datetime.datetime]):
        last_updated (Union[Unset, datetime.datetime]):
        last_used (Union[Unset, datetime.datetime]):
        deleted (Union[Unset, bool]):
        status (Union[Unset, ComputeEnvStatus]):
        message (Union[Unset, str]):
        primary (Union[Unset, bool]):
        credentials_id (Union[Unset, str]):
        org_id (Union[Unset, int]):
        workspace_id (Union[Unset, int]):
    """

    name: str
    config: Union[
        "AWSBatchConfiguration",
        "AltairPBSConfiguration",
        "AmazonEKSClusterConfiguration",
        "AzureBatchConfiguration",
        "GoogleGKEClusterConfiguration",
        "GoogleLifeSciencesConfiguration",
        "IBMLSFConfiguration",
        "KubernetesComputeConfiguration",
        "SlurmConfiguration",
        "UnivaGridEngineConfiguration",
    ]
    id: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    platform: Union[Unset, ComputeEnvPlatform] = UNSET
    date_created: Union[Unset, datetime.datetime] = UNSET
    last_updated: Union[Unset, datetime.datetime] = UNSET
    last_used: Union[Unset, datetime.datetime] = UNSET
    deleted: Union[Unset, bool] = UNSET
    status: Union[Unset, ComputeEnvStatus] = UNSET
    message: Union[Unset, str] = UNSET
    primary: Union[Unset, bool] = UNSET
    credentials_id: Union[Unset, str] = UNSET
    org_id: Union[Unset, int] = UNSET
    workspace_id: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.amazon_eks_cluster_configuration import AmazonEKSClusterConfiguration
        from ..models.aws_batch_configuration import AWSBatchConfiguration
        from ..models.azure_batch_configuration import AzureBatchConfiguration
        from ..models.google_gke_cluster_configuration import GoogleGKEClusterConfiguration
        from ..models.google_life_sciences_configuration import GoogleLifeSciencesConfiguration
        from ..models.ibmlsf_configuration import IBMLSFConfiguration
        from ..models.kubernetes_compute_configuration import KubernetesComputeConfiguration
        from ..models.slurm_configuration import SlurmConfiguration
        from ..models.univa_grid_engine_configuration import UnivaGridEngineConfiguration

        name = self.name
        config: Dict[str, Any]

        if isinstance(self.config, AWSBatchConfiguration):
            config = self.config.to_dict()

        elif isinstance(self.config, GoogleLifeSciencesConfiguration):
            config = self.config.to_dict()

        elif isinstance(self.config, AzureBatchConfiguration):
            config = self.config.to_dict()

        elif isinstance(self.config, IBMLSFConfiguration):
            config = self.config.to_dict()

        elif isinstance(self.config, SlurmConfiguration):
            config = self.config.to_dict()

        elif isinstance(self.config, KubernetesComputeConfiguration):
            config = self.config.to_dict()

        elif isinstance(self.config, AmazonEKSClusterConfiguration):
            config = self.config.to_dict()

        elif isinstance(self.config, GoogleGKEClusterConfiguration):
            config = self.config.to_dict()

        elif isinstance(self.config, UnivaGridEngineConfiguration):
            config = self.config.to_dict()

        else:
            config = self.config.to_dict()

        id = self.id
        description = self.description
        platform: Union[Unset, str] = UNSET
        if not isinstance(self.platform, Unset):
            platform = self.platform.value

        date_created: Union[Unset, str] = UNSET
        if not isinstance(self.date_created, Unset):
            date_created = self.date_created.isoformat()

        last_updated: Union[Unset, str] = UNSET
        if not isinstance(self.last_updated, Unset):
            last_updated = self.last_updated.isoformat()

        last_used: Union[Unset, str] = UNSET
        if not isinstance(self.last_used, Unset):
            last_used = self.last_used.isoformat()

        deleted = self.deleted
        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        message = self.message
        primary = self.primary
        credentials_id = self.credentials_id
        org_id = self.org_id
        workspace_id = self.workspace_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "config": config,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if description is not UNSET:
            field_dict["description"] = description
        if platform is not UNSET:
            field_dict["platform"] = platform
        if date_created is not UNSET:
            field_dict["dateCreated"] = date_created
        if last_updated is not UNSET:
            field_dict["lastUpdated"] = last_updated
        if last_used is not UNSET:
            field_dict["lastUsed"] = last_used
        if deleted is not UNSET:
            field_dict["deleted"] = deleted
        if status is not UNSET:
            field_dict["status"] = status
        if message is not UNSET:
            field_dict["message"] = message
        if primary is not UNSET:
            field_dict["primary"] = primary
        if credentials_id is not UNSET:
            field_dict["credentialsId"] = credentials_id
        if org_id is not UNSET:
            field_dict["orgId"] = org_id
        if workspace_id is not UNSET:
            field_dict["workspaceId"] = workspace_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.altair_pbs_configuration import AltairPBSConfiguration
        from ..models.amazon_eks_cluster_configuration import AmazonEKSClusterConfiguration
        from ..models.aws_batch_configuration import AWSBatchConfiguration
        from ..models.azure_batch_configuration import AzureBatchConfiguration
        from ..models.google_gke_cluster_configuration import GoogleGKEClusterConfiguration
        from ..models.google_life_sciences_configuration import GoogleLifeSciencesConfiguration
        from ..models.ibmlsf_configuration import IBMLSFConfiguration
        from ..models.kubernetes_compute_configuration import KubernetesComputeConfiguration
        from ..models.slurm_configuration import SlurmConfiguration
        from ..models.univa_grid_engine_configuration import UnivaGridEngineConfiguration

        d = src_dict.copy()
        name = d.pop("name")

        def _parse_config(
            data: object,
        ) -> Union[
            "AWSBatchConfiguration",
            "AltairPBSConfiguration",
            "AmazonEKSClusterConfiguration",
            "AzureBatchConfiguration",
            "GoogleGKEClusterConfiguration",
            "GoogleLifeSciencesConfiguration",
            "IBMLSFConfiguration",
            "KubernetesComputeConfiguration",
            "SlurmConfiguration",
            "UnivaGridEngineConfiguration",
        ]:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_compute_config_type_0 = AWSBatchConfiguration.from_dict(data)

                return componentsschemas_compute_config_type_0
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_compute_config_type_1 = GoogleLifeSciencesConfiguration.from_dict(data)

                return componentsschemas_compute_config_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_compute_config_type_2 = AzureBatchConfiguration.from_dict(data)

                return componentsschemas_compute_config_type_2
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_compute_config_type_3 = IBMLSFConfiguration.from_dict(data)

                return componentsschemas_compute_config_type_3
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_compute_config_type_4 = SlurmConfiguration.from_dict(data)

                return componentsschemas_compute_config_type_4
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_compute_config_type_5 = KubernetesComputeConfiguration.from_dict(data)

                return componentsschemas_compute_config_type_5
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_compute_config_type_6 = AmazonEKSClusterConfiguration.from_dict(data)

                return componentsschemas_compute_config_type_6
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_compute_config_type_7 = GoogleGKEClusterConfiguration.from_dict(data)

                return componentsschemas_compute_config_type_7
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_compute_config_type_8 = UnivaGridEngineConfiguration.from_dict(data)

                return componentsschemas_compute_config_type_8
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_compute_config_type_9 = AltairPBSConfiguration.from_dict(data)

            return componentsschemas_compute_config_type_9

        config = _parse_config(d.pop("config"))

        id = d.pop("id", UNSET)

        description = d.pop("description", UNSET)

        _platform = d.pop("platform", UNSET)
        platform: Union[Unset, ComputeEnvPlatform]
        if isinstance(_platform, Unset):
            platform = UNSET
        else:
            platform = ComputeEnvPlatform(_platform)

        _date_created = d.pop("dateCreated", UNSET)
        date_created: Union[Unset, datetime.datetime]
        if isinstance(_date_created, Unset):
            date_created = UNSET
        else:
            date_created = isoparse(_date_created)

        _last_updated = d.pop("lastUpdated", UNSET)
        last_updated: Union[Unset, datetime.datetime]
        if isinstance(_last_updated, Unset):
            last_updated = UNSET
        else:
            last_updated = isoparse(_last_updated)

        _last_used = d.pop("lastUsed", UNSET)
        last_used: Union[Unset, datetime.datetime]
        if isinstance(_last_used, Unset):
            last_used = UNSET
        else:
            last_used = isoparse(_last_used)

        deleted = d.pop("deleted", UNSET)

        _status = d.pop("status", UNSET)
        status: Union[Unset, ComputeEnvStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = ComputeEnvStatus(_status)

        message = d.pop("message", UNSET)

        primary = d.pop("primary", UNSET)

        credentials_id = d.pop("credentialsId", UNSET)

        org_id = d.pop("orgId", UNSET)

        workspace_id = d.pop("workspaceId", UNSET)

        launch_compute_env = cls(
            name=name,
            config=config,
            id=id,
            description=description,
            platform=platform,
            date_created=date_created,
            last_updated=last_updated,
            last_used=last_used,
            deleted=deleted,
            status=status,
            message=message,
            primary=primary,
            credentials_id=credentials_id,
            org_id=org_id,
            workspace_id=workspace_id,
        )

        launch_compute_env.additional_properties = d
        return launch_compute_env

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
