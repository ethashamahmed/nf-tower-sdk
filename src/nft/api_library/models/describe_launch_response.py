from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.launch import Launch


T = TypeVar("T", bound="DescribeLaunchResponse")


@attr.s(auto_attribs=True)
class DescribeLaunchResponse:
    """
    Attributes:
        launch (Union[Unset, Launch]):
    """

    launch: Union[Unset, "Launch"] = UNSET
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
        from ..models.launch import Launch

        d = src_dict.copy()
        _launch = d.pop("launch", UNSET)
        launch: Union[Unset, Launch]
        if isinstance(_launch, Unset):
            launch = UNSET
        else:
            launch = Launch.from_dict(_launch)

        describe_launch_response = cls(
            launch=launch,
        )

        describe_launch_response.additional_properties = d
        return describe_launch_response

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
