from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="AgentSecurityKeys")


@attr.s(auto_attribs=True)
class AgentSecurityKeys:
    """
    Attributes:
        connection_id (Union[Unset, str]):
        work_dir (Union[Unset, str]):
        discriminator (Union[Unset, str]):
    """

    connection_id: Union[Unset, str] = UNSET
    work_dir: Union[Unset, str] = UNSET
    discriminator: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        connection_id = self.connection_id
        work_dir = self.work_dir
        discriminator = self.discriminator

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if connection_id is not UNSET:
            field_dict["connectionId"] = connection_id
        if work_dir is not UNSET:
            field_dict["workDir"] = work_dir
        if discriminator is not UNSET:
            field_dict["discriminator"] = discriminator

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        connection_id = d.pop("connectionId", UNSET)

        work_dir = d.pop("workDir", UNSET)

        discriminator = d.pop("discriminator", UNSET)

        agent_security_keys = cls(
            connection_id=connection_id,
            work_dir=work_dir,
            discriminator=discriminator,
        )

        agent_security_keys.additional_properties = d
        return agent_security_keys

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
