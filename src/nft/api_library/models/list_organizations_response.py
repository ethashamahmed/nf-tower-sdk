from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.organization_db_dto import OrganizationDbDto


T = TypeVar("T", bound="ListOrganizationsResponse")


@attr.s(auto_attribs=True)
class ListOrganizationsResponse:
    """
    Attributes:
        organizations (List['OrganizationDbDto']):
        total_size (Union[Unset, int]):
    """

    organizations: List["OrganizationDbDto"]
    total_size: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        organizations = []
        for organizations_item_data in self.organizations:
            organizations_item = organizations_item_data.to_dict()

            organizations.append(organizations_item)

        total_size = self.total_size

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "organizations": organizations,
            }
        )
        if total_size is not UNSET:
            field_dict["totalSize"] = total_size

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.organization_db_dto import OrganizationDbDto

        d = src_dict.copy()
        organizations = []
        _organizations = d.pop("organizations")
        for organizations_item_data in _organizations:
            organizations_item = OrganizationDbDto.from_dict(organizations_item_data)

            organizations.append(organizations_item)

        total_size = d.pop("totalSize", UNSET)

        list_organizations_response = cls(
            organizations=organizations,
            total_size=total_size,
        )

        list_organizations_response.additional_properties = d
        return list_organizations_response

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
