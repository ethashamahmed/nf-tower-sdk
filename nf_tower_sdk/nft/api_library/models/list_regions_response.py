from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.compute_region import ComputeRegion


T = TypeVar("T", bound="ListRegionsResponse")


@attr.s(auto_attribs=True)
class ListRegionsResponse:
    """
    Attributes:
        regions (Union[Unset, List['ComputeRegion']]):
    """

    regions: Union[Unset, List["ComputeRegion"]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        regions: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.regions, Unset):
            regions = []
            for regions_item_data in self.regions:
                regions_item = regions_item_data.to_dict()

                regions.append(regions_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if regions is not UNSET:
            field_dict["regions"] = regions

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.compute_region import ComputeRegion

        d = src_dict.copy()
        regions = []
        _regions = d.pop("regions", UNSET)
        for regions_item_data in _regions or []:
            regions_item = ComputeRegion.from_dict(regions_item_data)

            regions.append(regions_item)

        list_regions_response = cls(
            regions=regions,
        )

        list_regions_response.additional_properties = d
        return list_regions_response

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
