from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="GoogleLifeSciencesPlatformMetainfoFilestore")


@attr.s(auto_attribs=True)
class GoogleLifeSciencesPlatformMetainfoFilestore:
    """
    Attributes:
        name (Union[Unset, str]):
        location (Union[Unset, str]):
        target (Union[Unset, str]):
    """

    name: Union[Unset, str] = UNSET
    location: Union[Unset, str] = UNSET
    target: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        location = self.location
        target = self.target

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if location is not UNSET:
            field_dict["location"] = location
        if target is not UNSET:
            field_dict["target"] = target

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name", UNSET)

        location = d.pop("location", UNSET)

        target = d.pop("target", UNSET)

        google_life_sciences_platform_metainfo_filestore = cls(
            name=name,
            location=location,
            target=target,
        )

        google_life_sciences_platform_metainfo_filestore.additional_properties = d
        return google_life_sciences_platform_metainfo_filestore

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
