from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.credentials_spec import CredentialsSpec


T = TypeVar("T", bound="CreateCredentialsRequest")


@attr.s(auto_attribs=True)
class CreateCredentialsRequest:
    """
    Attributes:
        credentials (Union[Unset, CredentialsSpec]):
    """

    credentials: Union[Unset, "CredentialsSpec"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        credentials: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.credentials, Unset):
            credentials = self.credentials.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if credentials is not UNSET:
            field_dict["credentials"] = credentials

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.credentials_spec import CredentialsSpec

        d = src_dict.copy()
        _credentials = d.pop("credentials", UNSET)
        credentials: Union[Unset, CredentialsSpec]
        if isinstance(_credentials, Unset):
            credentials = UNSET
        else:
            credentials = CredentialsSpec.from_dict(_credentials)

        create_credentials_request = cls(
            credentials=credentials,
        )

        create_credentials_request.additional_properties = d
        return create_credentials_request

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
