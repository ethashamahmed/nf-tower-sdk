from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.workflow_launch_response import WorkflowLaunchResponse


T = TypeVar("T", bound="DescribeWorkflowLaunchResponse")


@attr.s(auto_attribs=True)
class DescribeWorkflowLaunchResponse:
    """
    Attributes:
        launch (Union[Unset, WorkflowLaunchResponse]):
    """

    launch: Union[Unset, "WorkflowLaunchResponse"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        launch: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.launch, Unset):
            launch = self.launch.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if launch is not UNSET:
            field_dict["launch"] = launch

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.workflow_launch_response import WorkflowLaunchResponse

        d = src_dict.copy()
        _launch = d.pop("launch", UNSET)
        launch: Union[Unset, WorkflowLaunchResponse]
        if isinstance(_launch, Unset):
            launch = UNSET
        else:
            launch = WorkflowLaunchResponse.from_dict(_launch)

        describe_workflow_launch_response = cls(
            launch=launch,
        )

        describe_workflow_launch_response.additional_properties = d
        return describe_workflow_launch_response

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
