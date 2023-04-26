from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.google_life_sciences_platform_metainfo_bucket import GoogleLifeSciencesPlatformMetainfoBucket
    from ..models.google_life_sciences_platform_metainfo_filestore import GoogleLifeSciencesPlatformMetainfoFilestore


T = TypeVar("T", bound="GoogleLifeSciencesPlatformMetainfo")


@attr.s(auto_attribs=True)
class GoogleLifeSciencesPlatformMetainfo:
    """
    Attributes:
        warnings (Union[Unset, List[str]]):
        zones (Union[Unset, List[str]]):
        locations (Union[Unset, List[str]]):
        buckets (Union[Unset, List['GoogleLifeSciencesPlatformMetainfoBucket']]):
        filestores (Union[Unset, List['GoogleLifeSciencesPlatformMetainfoFilestore']]):
    """

    warnings: Union[Unset, List[str]] = UNSET
    zones: Union[Unset, List[str]] = UNSET
    locations: Union[Unset, List[str]] = UNSET
    buckets: Union[Unset, List["GoogleLifeSciencesPlatformMetainfoBucket"]] = UNSET
    filestores: Union[Unset, List["GoogleLifeSciencesPlatformMetainfoFilestore"]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        warnings: Union[Unset, List[str]] = UNSET
        if not isinstance(self.warnings, Unset):
            warnings = self.warnings

        zones: Union[Unset, List[str]] = UNSET
        if not isinstance(self.zones, Unset):
            zones = self.zones

        locations: Union[Unset, List[str]] = UNSET
        if not isinstance(self.locations, Unset):
            locations = self.locations

        buckets: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.buckets, Unset):
            buckets = []
            for buckets_item_data in self.buckets:
                buckets_item = buckets_item_data.to_dict()

                buckets.append(buckets_item)

        filestores: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.filestores, Unset):
            filestores = []
            for filestores_item_data in self.filestores:
                filestores_item = filestores_item_data.to_dict()

                filestores.append(filestores_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if warnings is not UNSET:
            field_dict["warnings"] = warnings
        if zones is not UNSET:
            field_dict["zones"] = zones
        if locations is not UNSET:
            field_dict["locations"] = locations
        if buckets is not UNSET:
            field_dict["buckets"] = buckets
        if filestores is not UNSET:
            field_dict["filestores"] = filestores

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.google_life_sciences_platform_metainfo_bucket import GoogleLifeSciencesPlatformMetainfoBucket
        from ..models.google_life_sciences_platform_metainfo_filestore import (
            GoogleLifeSciencesPlatformMetainfoFilestore,
        )

        d = src_dict.copy()
        warnings = cast(List[str], d.pop("warnings", UNSET))

        zones = cast(List[str], d.pop("zones", UNSET))

        locations = cast(List[str], d.pop("locations", UNSET))

        buckets = []
        _buckets = d.pop("buckets", UNSET)
        for buckets_item_data in _buckets or []:
            buckets_item = GoogleLifeSciencesPlatformMetainfoBucket.from_dict(buckets_item_data)

            buckets.append(buckets_item)

        filestores = []
        _filestores = d.pop("filestores", UNSET)
        for filestores_item_data in _filestores or []:
            filestores_item = GoogleLifeSciencesPlatformMetainfoFilestore.from_dict(filestores_item_data)

            filestores.append(filestores_item)

        google_life_sciences_platform_metainfo = cls(
            warnings=warnings,
            zones=zones,
            locations=locations,
            buckets=buckets,
            filestores=filestores,
        )

        google_life_sciences_platform_metainfo.additional_properties = d
        return google_life_sciences_platform_metainfo

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
