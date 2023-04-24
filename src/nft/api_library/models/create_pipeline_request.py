from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.workflow_launch_request import WorkflowLaunchRequest


T = TypeVar("T", bound="CreatePipelineRequest")


@attr.s(auto_attribs=True)
class CreatePipelineRequest:
    """
    Attributes:
        name (Union[Unset, str]):
        description (Union[Unset, str]):
        icon (Union[Unset, str]):
        launch (Union[Unset, WorkflowLaunchRequest]):
        labels_ids (Union[Unset, List[int]]):
    """

    name: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    icon: Union[Unset, str] = UNSET
    launch: Union[Unset, "WorkflowLaunchRequest"] = UNSET
    labels_ids: Union[Unset, List[int]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        description = self.description
        icon = self.icon
        launch: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.launch, Unset):
            launch = self.launch.to_dict()

        labels_ids: Union[Unset, List[int]] = UNSET
        if not isinstance(self.labels_ids, Unset):
            labels_ids = self.labels_ids

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if icon is not UNSET:
            field_dict["icon"] = icon
        if launch is not UNSET:
            field_dict["launch"] = launch
        if labels_ids is not UNSET:
            field_dict["labelsIds"] = labels_ids

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.workflow_launch_request import WorkflowLaunchRequest

        d = src_dict.copy()
        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        icon = d.pop("icon", UNSET)

        _launch = d.pop("launch", UNSET)
        launch: Union[Unset, WorkflowLaunchRequest]
        if isinstance(_launch, Unset):
            launch = UNSET
        else:
            launch = WorkflowLaunchRequest.from_dict(_launch)

        labels_ids = cast(List[int], d.pop("labelsIds", UNSET))

        create_pipeline_request = cls(
            name=name,
            description=description,
            icon=icon,
            launch=launch,
            labels_ids=labels_ids,
        )

        create_pipeline_request.additional_properties = d
        return create_pipeline_request

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
