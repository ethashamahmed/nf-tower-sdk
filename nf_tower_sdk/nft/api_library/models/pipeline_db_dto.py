from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.label_db_dto import LabelDbDto


T = TypeVar("T", bound="PipelineDbDto")


@attr.s(auto_attribs=True)
class PipelineDbDto:
    """
    Attributes:
        pipeline_id (Union[Unset, int]):
        name (Union[Unset, str]):
        description (Union[Unset, str]):
        icon (Union[Unset, str]):
        repository (Union[Unset, str]):
        user_id (Union[Unset, int]):
        user_name (Union[Unset, str]):
        user_first_name (Union[Unset, str]):
        user_last_name (Union[Unset, str]):
        org_id (Union[Unset, int]):
        org_name (Union[Unset, str]):
        workspace_id (Union[Unset, int]):
        workspace_name (Union[Unset, str]):
        visibility (Union[Unset, str]):
        optimized (Union[Unset, bool]):
        labels (Union[Unset, List['LabelDbDto']]):
    """

    pipeline_id: Union[Unset, int] = UNSET
    name: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    icon: Union[Unset, str] = UNSET
    repository: Union[Unset, str] = UNSET
    user_id: Union[Unset, int] = UNSET
    user_name: Union[Unset, str] = UNSET
    user_first_name: Union[Unset, str] = UNSET
    user_last_name: Union[Unset, str] = UNSET
    org_id: Union[Unset, int] = UNSET
    org_name: Union[Unset, str] = UNSET
    workspace_id: Union[Unset, int] = UNSET
    workspace_name: Union[Unset, str] = UNSET
    visibility: Union[Unset, str] = UNSET
    optimized: Union[Unset, bool] = UNSET
    labels: Union[Unset, List["LabelDbDto"]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        pipeline_id = self.pipeline_id
        name = self.name
        description = self.description
        icon = self.icon
        repository = self.repository
        user_id = self.user_id
        user_name = self.user_name
        user_first_name = self.user_first_name
        user_last_name = self.user_last_name
        org_id = self.org_id
        org_name = self.org_name
        workspace_id = self.workspace_id
        workspace_name = self.workspace_name
        visibility = self.visibility
        optimized = self.optimized
        labels: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.labels, Unset):
            labels = []
            for labels_item_data in self.labels:
                labels_item = labels_item_data.to_dict()

                labels.append(labels_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if pipeline_id is not UNSET:
            field_dict["pipelineId"] = pipeline_id
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if icon is not UNSET:
            field_dict["icon"] = icon
        if repository is not UNSET:
            field_dict["repository"] = repository
        if user_id is not UNSET:
            field_dict["userId"] = user_id
        if user_name is not UNSET:
            field_dict["userName"] = user_name
        if user_first_name is not UNSET:
            field_dict["userFirstName"] = user_first_name
        if user_last_name is not UNSET:
            field_dict["userLastName"] = user_last_name
        if org_id is not UNSET:
            field_dict["orgId"] = org_id
        if org_name is not UNSET:
            field_dict["orgName"] = org_name
        if workspace_id is not UNSET:
            field_dict["workspaceId"] = workspace_id
        if workspace_name is not UNSET:
            field_dict["workspaceName"] = workspace_name
        if visibility is not UNSET:
            field_dict["visibility"] = visibility
        if optimized is not UNSET:
            field_dict["optimized"] = optimized
        if labels is not UNSET:
            field_dict["labels"] = labels

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.label_db_dto import LabelDbDto

        d = src_dict.copy()
        pipeline_id = d.pop("pipelineId", UNSET)

        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        icon = d.pop("icon", UNSET)

        repository = d.pop("repository", UNSET)

        user_id = d.pop("userId", UNSET)

        user_name = d.pop("userName", UNSET)

        user_first_name = d.pop("userFirstName", UNSET)

        user_last_name = d.pop("userLastName", UNSET)

        org_id = d.pop("orgId", UNSET)

        org_name = d.pop("orgName", UNSET)

        workspace_id = d.pop("workspaceId", UNSET)

        workspace_name = d.pop("workspaceName", UNSET)

        visibility = d.pop("visibility", UNSET)

        optimized = d.pop("optimized", UNSET)

        labels = []
        _labels = d.pop("labels", UNSET)
        for labels_item_data in _labels or []:
            labels_item = LabelDbDto.from_dict(labels_item_data)

            labels.append(labels_item)

        pipeline_db_dto = cls(
            pipeline_id=pipeline_id,
            name=name,
            description=description,
            icon=icon,
            repository=repository,
            user_id=user_id,
            user_name=user_name,
            user_first_name=user_first_name,
            user_last_name=user_last_name,
            org_id=org_id,
            org_name=org_name,
            workspace_id=workspace_id,
            workspace_name=workspace_name,
            visibility=visibility,
            optimized=optimized,
            labels=labels,
        )

        pipeline_db_dto.additional_properties = d
        return pipeline_db_dto

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
