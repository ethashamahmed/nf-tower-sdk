from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="TeamDbDto")


@attr.s(auto_attribs=True)
class TeamDbDto:
    """
    Attributes:
        team_id (Union[Unset, int]):
        name (Union[Unset, str]):
        description (Union[Unset, str]):
        avatar_url (Union[Unset, str]):
        members_count (Union[Unset, int]):
    """

    team_id: Union[Unset, int] = UNSET
    name: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    avatar_url: Union[Unset, str] = UNSET
    members_count: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        team_id = self.team_id
        name = self.name
        description = self.description
        avatar_url = self.avatar_url
        members_count = self.members_count

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if team_id is not UNSET:
            field_dict["teamId"] = team_id
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if avatar_url is not UNSET:
            field_dict["avatarUrl"] = avatar_url
        if members_count is not UNSET:
            field_dict["membersCount"] = members_count

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        team_id = d.pop("teamId", UNSET)

        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        avatar_url = d.pop("avatarUrl", UNSET)

        members_count = d.pop("membersCount", UNSET)

        team_db_dto = cls(
            team_id=team_id,
            name=name,
            description=description,
            avatar_url=avatar_url,
            members_count=members_count,
        )

        team_db_dto.additional_properties = d
        return team_db_dto

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
