from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.org_role import OrgRole
from ..types import UNSET, Unset

T = TypeVar("T", bound="MemberDbDto")


@attr.s(auto_attribs=True)
class MemberDbDto:
    """
    Attributes:
        user_name (Union[Unset, str]):
        member_id (Union[Unset, int]):
        email (Union[Unset, str]):
        last_name (Union[Unset, str]):
        role (Union[Unset, OrgRole]):
        first_name (Union[Unset, str]):
        avatar (Union[Unset, str]):
    """

    user_name: Union[Unset, str] = UNSET
    member_id: Union[Unset, int] = UNSET
    email: Union[Unset, str] = UNSET
    last_name: Union[Unset, str] = UNSET
    role: Union[Unset, OrgRole] = UNSET
    first_name: Union[Unset, str] = UNSET
    avatar: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        user_name = self.user_name
        member_id = self.member_id
        email = self.email
        last_name = self.last_name
        role: Union[Unset, str] = UNSET
        if not isinstance(self.role, Unset):
            role = self.role.value

        first_name = self.first_name
        avatar = self.avatar

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if user_name is not UNSET:
            field_dict["userName"] = user_name
        if member_id is not UNSET:
            field_dict["memberId"] = member_id
        if email is not UNSET:
            field_dict["email"] = email
        if last_name is not UNSET:
            field_dict["lastName"] = last_name
        if role is not UNSET:
            field_dict["role"] = role
        if first_name is not UNSET:
            field_dict["firstName"] = first_name
        if avatar is not UNSET:
            field_dict["avatar"] = avatar

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        user_name = d.pop("userName", UNSET)

        member_id = d.pop("memberId", UNSET)

        email = d.pop("email", UNSET)

        last_name = d.pop("lastName", UNSET)

        _role = d.pop("role", UNSET)
        role: Union[Unset, OrgRole]
        if isinstance(_role, Unset):
            role = UNSET
        else:
            role = OrgRole(_role)

        first_name = d.pop("firstName", UNSET)

        avatar = d.pop("avatar", UNSET)

        member_db_dto = cls(
            user_name=user_name,
            member_id=member_id,
            email=email,
            last_name=last_name,
            role=role,
            first_name=first_name,
            avatar=avatar,
        )

        member_db_dto.additional_properties = d
        return member_db_dto

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
