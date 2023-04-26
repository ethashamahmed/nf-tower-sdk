from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.label_db_dto import LabelDbDto
    from ..models.progress_data import ProgressData
    from ..models.workflow_db_dto import WorkflowDbDto


T = TypeVar("T", bound="ListWorkflowsResponseListWorkflowsElement")


@attr.s(auto_attribs=True)
class ListWorkflowsResponseListWorkflowsElement:
    """
    Attributes:
        labels (Union[Unset, List['LabelDbDto']]):
        progress (Union[Unset, ProgressData]):
        starred (Union[Unset, bool]):
        optimized (Union[Unset, bool]):
        workflow (Union[Unset, WorkflowDbDto]):
    """

    labels: Union[Unset, List["LabelDbDto"]] = UNSET
    progress: Union[Unset, "ProgressData"] = UNSET
    starred: Union[Unset, bool] = UNSET
    optimized: Union[Unset, bool] = UNSET
    workflow: Union[Unset, "WorkflowDbDto"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        labels: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.labels, Unset):
            labels = []
            for labels_item_data in self.labels:
                labels_item = labels_item_data.to_dict()

                labels.append(labels_item)

        progress: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.progress, Unset):
            progress = self.progress.to_dict()

        starred = self.starred
        optimized = self.optimized
        workflow: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.workflow, Unset):
            workflow = self.workflow.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if labels is not UNSET:
            field_dict["labels"] = labels
        if progress is not UNSET:
            field_dict["progress"] = progress
        if starred is not UNSET:
            field_dict["starred"] = starred
        if optimized is not UNSET:
            field_dict["optimized"] = optimized
        if workflow is not UNSET:
            field_dict["workflow"] = workflow

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.label_db_dto import LabelDbDto
        from ..models.progress_data import ProgressData
        from ..models.workflow_db_dto import WorkflowDbDto

        d = src_dict.copy()
        labels = []
        _labels = d.pop("labels", UNSET)
        for labels_item_data in _labels or []:
            labels_item = LabelDbDto.from_dict(labels_item_data)

            labels.append(labels_item)

        _progress = d.pop("progress", UNSET)
        progress: Union[Unset, ProgressData]
        if isinstance(_progress, Unset):
            progress = UNSET
        else:
            progress = ProgressData.from_dict(_progress)

        starred = d.pop("starred", UNSET)

        optimized = d.pop("optimized", UNSET)

        _workflow = d.pop("workflow", UNSET)
        workflow: Union[Unset, WorkflowDbDto]
        if isinstance(_workflow, Unset):
            workflow = UNSET
        else:
            workflow = WorkflowDbDto.from_dict(_workflow)

        list_workflows_response_list_workflows_element = cls(
            labels=labels,
            progress=progress,
            starred=starred,
            optimized=optimized,
            workflow=workflow,
        )

        list_workflows_response_list_workflows_element.additional_properties = d
        return list_workflows_response_list_workflows_element

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
