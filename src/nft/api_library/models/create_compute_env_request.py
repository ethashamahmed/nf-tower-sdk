from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.compute_env import ComputeEnv


T = TypeVar("T", bound="CreateComputeEnvRequest")


@attr.s(auto_attribs=True)
class CreateComputeEnvRequest:
    """
    Attributes:
        compute_env (Union[Unset, ComputeEnv]):
        labels_ids (Union[Unset, List[int]]):
    """

    compute_env: Union[Unset, "ComputeEnv"] = UNSET
    labels_ids: Union[Unset, List[int]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        compute_env: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.compute_env, Unset):
            compute_env = self.compute_env.to_dict()

        labels_ids: Union[Unset, List[int]] = UNSET
        if not isinstance(self.labels_ids, Unset):
            labels_ids = self.labels_ids

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if compute_env is not UNSET:
            field_dict["computeEnv"] = compute_env
        if labels_ids is not UNSET:
            field_dict["labelsIds"] = labels_ids

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.compute_env import ComputeEnv

        d = src_dict.copy()
        _compute_env = d.pop("computeEnv", UNSET)
        compute_env: Union[Unset, ComputeEnv]
        if isinstance(_compute_env, Unset):
            compute_env = UNSET
        else:
            compute_env = ComputeEnv.from_dict(_compute_env)

        labels_ids = cast(List[int], d.pop("labelsIds", UNSET))

        create_compute_env_request = cls(
            compute_env=compute_env,
            labels_ids=labels_ids,
        )

        create_compute_env_request.additional_properties = d
        return create_compute_env_request

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
