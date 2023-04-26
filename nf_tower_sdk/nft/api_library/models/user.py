import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="User")


@attr.s(auto_attribs=True)
class User:
    """
    Attributes:
        user_name (str):
        id (Union[Unset, None, int]):
        email (Union[Unset, str]):
        first_name (Union[Unset, str]):
        last_name (Union[Unset, str]):
        organization (Union[Unset, str]):
        description (Union[Unset, str]):
        avatar (Union[Unset, str]):
        notification (Union[Unset, bool]):
        terms_of_use_consent (Union[Unset, bool]):
        marketing_consent (Union[Unset, bool]):
        last_access (Union[Unset, datetime.datetime]):
        date_created (Union[Unset, datetime.datetime]):
        last_updated (Union[Unset, datetime.datetime]):
        deleted (Union[Unset, bool]):
    """

    user_name: str
    id: Union[Unset, None, int] = UNSET
    email: Union[Unset, str] = UNSET
    first_name: Union[Unset, str] = UNSET
    last_name: Union[Unset, str] = UNSET
    organization: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    avatar: Union[Unset, str] = UNSET
    notification: Union[Unset, bool] = UNSET
    terms_of_use_consent: Union[Unset, bool] = UNSET
    marketing_consent: Union[Unset, bool] = UNSET
    last_access: Union[Unset, datetime.datetime] = UNSET
    date_created: Union[Unset, datetime.datetime] = UNSET
    last_updated: Union[Unset, datetime.datetime] = UNSET
    deleted: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        user_name = self.user_name
        id = self.id
        email = self.email
        first_name = self.first_name
        last_name = self.last_name
        organization = self.organization
        description = self.description
        avatar = self.avatar
        notification = self.notification
        terms_of_use_consent = self.terms_of_use_consent
        marketing_consent = self.marketing_consent
        last_access: Union[Unset, str] = UNSET
        if not isinstance(self.last_access, Unset):
            last_access = self.last_access.isoformat()

        date_created: Union[Unset, str] = UNSET
        if not isinstance(self.date_created, Unset):
            date_created = self.date_created.isoformat()

        last_updated: Union[Unset, str] = UNSET
        if not isinstance(self.last_updated, Unset):
            last_updated = self.last_updated.isoformat()

        deleted = self.deleted

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "userName": user_name,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if email is not UNSET:
            field_dict["email"] = email
        if first_name is not UNSET:
            field_dict["firstName"] = first_name
        if last_name is not UNSET:
            field_dict["lastName"] = last_name
        if organization is not UNSET:
            field_dict["organization"] = organization
        if description is not UNSET:
            field_dict["description"] = description
        if avatar is not UNSET:
            field_dict["avatar"] = avatar
        if notification is not UNSET:
            field_dict["notification"] = notification
        if terms_of_use_consent is not UNSET:
            field_dict["termsOfUseConsent"] = terms_of_use_consent
        if marketing_consent is not UNSET:
            field_dict["marketingConsent"] = marketing_consent
        if last_access is not UNSET:
            field_dict["lastAccess"] = last_access
        if date_created is not UNSET:
            field_dict["dateCreated"] = date_created
        if last_updated is not UNSET:
            field_dict["lastUpdated"] = last_updated
        if deleted is not UNSET:
            field_dict["deleted"] = deleted

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        user_name = d.pop("userName")

        id = d.pop("id", UNSET)

        email = d.pop("email", UNSET)

        first_name = d.pop("firstName", UNSET)

        last_name = d.pop("lastName", UNSET)

        organization = d.pop("organization", UNSET)

        description = d.pop("description", UNSET)

        avatar = d.pop("avatar", UNSET)

        notification = d.pop("notification", UNSET)

        terms_of_use_consent = d.pop("termsOfUseConsent", UNSET)

        marketing_consent = d.pop("marketingConsent", UNSET)

        _last_access = d.pop("lastAccess", UNSET)
        last_access: Union[Unset, datetime.datetime]
        if isinstance(_last_access, Unset):
            last_access = UNSET
        else:
            last_access = isoparse(_last_access)

        _date_created = d.pop("dateCreated", UNSET)
        date_created: Union[Unset, datetime.datetime]
        if isinstance(_date_created, Unset):
            date_created = UNSET
        else:
            date_created = isoparse(_date_created)

        _last_updated = d.pop("lastUpdated", UNSET)
        last_updated: Union[Unset, datetime.datetime]
        if isinstance(_last_updated, Unset):
            last_updated = UNSET
        else:
            last_updated = isoparse(_last_updated)

        deleted = d.pop("deleted", UNSET)

        user = cls(
            user_name=user_name,
            id=id,
            email=email,
            first_name=first_name,
            last_name=last_name,
            organization=organization,
            description=description,
            avatar=avatar,
            notification=notification,
            terms_of_use_consent=terms_of_use_consent,
            marketing_consent=marketing_consent,
            last_access=last_access,
            date_created=date_created,
            last_updated=last_updated,
            deleted=deleted,
        )

        user.additional_properties = d
        return user

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
