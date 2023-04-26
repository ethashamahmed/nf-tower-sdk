from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.visibility import Visibility

T = TypeVar("T", bound="UpdateWorkspaceRequest")


@attr.s(auto_attribs=True)
class UpdateWorkspaceRequest:
    """
    Attributes:
        full_name (str):
        visibility (Visibility):
        description (str):
    """

    full_name: str
    visibility: Visibility
    description: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        full_name = self.full_name
        visibility = self.visibility.value

        description = self.description

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "fullName": full_name,
                "visibility": visibility,
                "description": description,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        full_name = d.pop("fullName")

        visibility = Visibility(d.pop("visibility"))

        description = d.pop("description")

        update_workspace_request = cls(
            full_name=full_name,
            visibility=visibility,
            description=description,
        )

        update_workspace_request.additional_properties = d
        return update_workspace_request

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
