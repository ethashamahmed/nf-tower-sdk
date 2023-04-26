from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.action_response_dto import ActionResponseDto


T = TypeVar("T", bound="DescribeActionResponse")


@attr.s(auto_attribs=True)
class DescribeActionResponse:
    """
    Attributes:
        action (Union[Unset, ActionResponseDto]):
    """

    action: Union[Unset, "ActionResponseDto"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        action: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.action, Unset):
            action = self.action.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if action is not UNSET:
            field_dict["action"] = action

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.action_response_dto import ActionResponseDto

        d = src_dict.copy()
        _action = d.pop("action", UNSET)
        action: Union[Unset, ActionResponseDto]
        if isinstance(_action, Unset):
            action = UNSET
        else:
            action = ActionResponseDto.from_dict(_action)

        describe_action_response = cls(
            action=action,
        )

        describe_action_response.additional_properties = d
        return describe_action_response

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
