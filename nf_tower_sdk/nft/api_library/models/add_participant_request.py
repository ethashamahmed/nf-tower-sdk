from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="AddParticipantRequest")


@attr.s(auto_attribs=True)
class AddParticipantRequest:
    """
    Attributes:
        member_id (Union[Unset, int]):
        team_id (Union[Unset, int]):
        user_name_or_email (Union[Unset, str]):
    """

    member_id: Union[Unset, int] = UNSET
    team_id: Union[Unset, int] = UNSET
    user_name_or_email: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        member_id = self.member_id
        team_id = self.team_id
        user_name_or_email = self.user_name_or_email

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if member_id is not UNSET:
            field_dict["memberId"] = member_id
        if team_id is not UNSET:
            field_dict["teamId"] = team_id
        if user_name_or_email is not UNSET:
            field_dict["userNameOrEmail"] = user_name_or_email

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        member_id = d.pop("memberId", UNSET)

        team_id = d.pop("teamId", UNSET)

        user_name_or_email = d.pop("userNameOrEmail", UNSET)

        add_participant_request = cls(
            member_id=member_id,
            team_id=team_id,
            user_name_or_email=user_name_or_email,
        )

        add_participant_request.additional_properties = d
        return add_participant_request

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
