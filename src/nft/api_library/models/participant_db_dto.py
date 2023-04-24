from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.org_role import OrgRole
from ..models.participant_type import ParticipantType
from ..models.wsp_role import WspRole
from ..types import UNSET, Unset

T = TypeVar("T", bound="ParticipantDbDto")


@attr.s(auto_attribs=True)
class ParticipantDbDto:
    """
    Attributes:
        user_name (str):
        member_id (int):
        email (str):
        last_name (str):
        first_name (str):
        participant_id (int):
        org_role (OrgRole):
        team_id (int):
        team_name (str):
        wsp_role (WspRole):
        user_avatar_url (str):
        type (Union[Unset, ParticipantType]):
        team_avatar_url (Union[Unset, str]):
    """

    user_name: str
    member_id: int
    email: str
    last_name: str
    first_name: str
    participant_id: int
    org_role: OrgRole
    team_id: int
    team_name: str
    wsp_role: WspRole
    user_avatar_url: str
    type: Union[Unset, ParticipantType] = UNSET
    team_avatar_url: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        user_name = self.user_name
        member_id = self.member_id
        email = self.email
        last_name = self.last_name
        first_name = self.first_name
        participant_id = self.participant_id
        org_role = self.org_role.value

        team_id = self.team_id
        team_name = self.team_name
        wsp_role = self.wsp_role.value

        user_avatar_url = self.user_avatar_url
        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        team_avatar_url = self.team_avatar_url

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "userName": user_name,
                "memberId": member_id,
                "email": email,
                "lastName": last_name,
                "firstName": first_name,
                "participantId": participant_id,
                "orgRole": org_role,
                "teamId": team_id,
                "teamName": team_name,
                "wspRole": wsp_role,
                "userAvatarUrl": user_avatar_url,
            }
        )
        if type is not UNSET:
            field_dict["type"] = type
        if team_avatar_url is not UNSET:
            field_dict["teamAvatarUrl"] = team_avatar_url

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        user_name = d.pop("userName")

        member_id = d.pop("memberId")

        email = d.pop("email")

        last_name = d.pop("lastName")

        first_name = d.pop("firstName")

        participant_id = d.pop("participantId")

        org_role = OrgRole(d.pop("orgRole"))

        team_id = d.pop("teamId")

        team_name = d.pop("teamName")

        wsp_role = WspRole(d.pop("wspRole"))

        user_avatar_url = d.pop("userAvatarUrl")

        _type = d.pop("type", UNSET)
        type: Union[Unset, ParticipantType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = ParticipantType(_type)

        team_avatar_url = d.pop("teamAvatarUrl", UNSET)

        participant_db_dto = cls(
            user_name=user_name,
            member_id=member_id,
            email=email,
            last_name=last_name,
            first_name=first_name,
            participant_id=participant_id,
            org_role=org_role,
            team_id=team_id,
            team_name=team_name,
            wsp_role=wsp_role,
            user_avatar_url=user_avatar_url,
            type=type,
            team_avatar_url=team_avatar_url,
        )

        participant_db_dto.additional_properties = d
        return participant_db_dto

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
