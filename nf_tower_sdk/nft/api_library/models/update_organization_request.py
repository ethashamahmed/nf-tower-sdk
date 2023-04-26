from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateOrganizationRequest")


@attr.s(auto_attribs=True)
class UpdateOrganizationRequest:
    """
    Attributes:
        full_name (Union[Unset, str]):
        description (Union[Unset, str]):
        logo_id (Union[Unset, str]):
        website (Union[Unset, str]):
        location (Union[Unset, str]):
    """

    full_name: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    logo_id: Union[Unset, str] = UNSET
    website: Union[Unset, str] = UNSET
    location: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        full_name = self.full_name
        description = self.description
        logo_id = self.logo_id
        website = self.website
        location = self.location

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if full_name is not UNSET:
            field_dict["fullName"] = full_name
        if description is not UNSET:
            field_dict["description"] = description
        if logo_id is not UNSET:
            field_dict["logoId"] = logo_id
        if website is not UNSET:
            field_dict["website"] = website
        if location is not UNSET:
            field_dict["location"] = location

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        full_name = d.pop("fullName", UNSET)

        description = d.pop("description", UNSET)

        logo_id = d.pop("logoId", UNSET)

        website = d.pop("website", UNSET)

        location = d.pop("location", UNSET)

        update_organization_request = cls(
            full_name=full_name,
            description=description,
            logo_id=logo_id,
            website=website,
            location=location,
        )

        update_organization_request.additional_properties = d
        return update_organization_request

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
