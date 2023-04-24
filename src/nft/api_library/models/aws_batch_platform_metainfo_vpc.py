from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="AwsBatchPlatformMetainfoVpc")


@attr.s(auto_attribs=True)
class AwsBatchPlatformMetainfoVpc:
    """
    Attributes:
        id (Union[Unset, str]):
        is_default (Union[Unset, bool]):
    """

    id: Union[Unset, str] = UNSET
    is_default: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        is_default = self.is_default

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if is_default is not UNSET:
            field_dict["isDefault"] = is_default

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        is_default = d.pop("isDefault", UNSET)

        aws_batch_platform_metainfo_vpc = cls(
            id=id,
            is_default=is_default,
        )

        aws_batch_platform_metainfo_vpc.additional_properties = d
        return aws_batch_platform_metainfo_vpc

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
