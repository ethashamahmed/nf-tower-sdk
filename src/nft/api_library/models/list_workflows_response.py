from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.list_workflows_response_list_workflows_element import ListWorkflowsResponseListWorkflowsElement


T = TypeVar("T", bound="ListWorkflowsResponse")


@attr.s(auto_attribs=True)
class ListWorkflowsResponse:
    """
    Attributes:
        workflows (Union[Unset, List['ListWorkflowsResponseListWorkflowsElement']]):
    """

    workflows: Union[Unset, List["ListWorkflowsResponseListWorkflowsElement"]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        workflows: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.workflows, Unset):
            workflows = []
            for workflows_item_data in self.workflows:
                workflows_item = workflows_item_data.to_dict()

                workflows.append(workflows_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if workflows is not UNSET:
            field_dict["workflows"] = workflows

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.list_workflows_response_list_workflows_element import ListWorkflowsResponseListWorkflowsElement

        d = src_dict.copy()
        workflows = []
        _workflows = d.pop("workflows", UNSET)
        for workflows_item_data in _workflows or []:
            workflows_item = ListWorkflowsResponseListWorkflowsElement.from_dict(workflows_item_data)

            workflows.append(workflows_item)

        list_workflows_response = cls(
            workflows=workflows,
        )

        list_workflows_response.additional_properties = d
        return list_workflows_response

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
