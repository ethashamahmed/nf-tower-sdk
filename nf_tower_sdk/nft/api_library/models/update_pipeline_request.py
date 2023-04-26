from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.workflow_launch_request import WorkflowLaunchRequest


T = TypeVar("T", bound="UpdatePipelineRequest")


@attr.s(auto_attribs=True)
class UpdatePipelineRequest:
    """
    Attributes:
        description (Union[Unset, str]):
        icon (Union[Unset, str]):
        launch (Union[Unset, WorkflowLaunchRequest]):
        labels_ids (Union[Unset, List[int]]):
    """

    description: Union[Unset, str] = UNSET
    icon: Union[Unset, str] = UNSET
    launch: Union[Unset, "WorkflowLaunchRequest"] = UNSET
    labels_ids: Union[Unset, List[int]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
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
        description = d.pop("description", UNSET)

        icon = d.pop("icon", UNSET)

        _launch = d.pop("launch", UNSET)
        launch: Union[Unset, WorkflowLaunchRequest]
        if isinstance(_launch, Unset):
            launch = UNSET
        else:
            launch = WorkflowLaunchRequest.from_dict(_launch)

        labels_ids = cast(List[int], d.pop("labelsIds", UNSET))

        update_pipeline_request = cls(
            description=description,
            icon=icon,
            launch=launch,
            labels_ids=labels_ids,
        )

        update_pipeline_request.additional_properties = d
        return update_pipeline_request

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
