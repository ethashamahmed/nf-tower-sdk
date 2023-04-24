from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.analytics import Analytics
    from ..models.navbar_config import NavbarConfig


T = TypeVar("T", bound="ServiceInfo")


@attr.s(auto_attribs=True)
class ServiceInfo:
    """
    Attributes:
        version (Union[Unset, str]):
        api_version (Union[Unset, str]):
        commit_id (Union[Unset, str]):
        auth_types (Union[Unset, List[str]]):
        login_path (Union[Unset, str]):
        navbar (Union[Unset, NavbarConfig]):
        heartbeat_interval (Union[Unset, int]):
        user_workspace_enabled (Union[Unset, bool]):
        allow_instance_credentials (Union[Unset, bool]):
        landing_url (Union[Unset, str]):
        terms_of_use_url (Union[Unset, str]):
        content_url (Union[Unset, str]):
        analytics (Union[Unset, Analytics]):
        allow_local_repos (Union[Unset, bool]):
        content_max_file_size (Union[Unset, int]):
    """

    version: Union[Unset, str] = UNSET
    api_version: Union[Unset, str] = UNSET
    commit_id: Union[Unset, str] = UNSET
    auth_types: Union[Unset, List[str]] = UNSET
    login_path: Union[Unset, str] = UNSET
    navbar: Union[Unset, "NavbarConfig"] = UNSET
    heartbeat_interval: Union[Unset, int] = UNSET
    user_workspace_enabled: Union[Unset, bool] = UNSET
    allow_instance_credentials: Union[Unset, bool] = UNSET
    landing_url: Union[Unset, str] = UNSET
    terms_of_use_url: Union[Unset, str] = UNSET
    content_url: Union[Unset, str] = UNSET
    analytics: Union[Unset, "Analytics"] = UNSET
    allow_local_repos: Union[Unset, bool] = UNSET
    content_max_file_size: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        version = self.version
        api_version = self.api_version
        commit_id = self.commit_id
        auth_types: Union[Unset, List[str]] = UNSET
        if not isinstance(self.auth_types, Unset):
            auth_types = self.auth_types

        login_path = self.login_path
        navbar: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.navbar, Unset):
            navbar = self.navbar.to_dict()

        heartbeat_interval = self.heartbeat_interval
        user_workspace_enabled = self.user_workspace_enabled
        allow_instance_credentials = self.allow_instance_credentials
        landing_url = self.landing_url
        terms_of_use_url = self.terms_of_use_url
        content_url = self.content_url
        analytics: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.analytics, Unset):
            analytics = self.analytics.to_dict()

        allow_local_repos = self.allow_local_repos
        content_max_file_size = self.content_max_file_size

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if version is not UNSET:
            field_dict["version"] = version
        if api_version is not UNSET:
            field_dict["apiVersion"] = api_version
        if commit_id is not UNSET:
            field_dict["commitId"] = commit_id
        if auth_types is not UNSET:
            field_dict["authTypes"] = auth_types
        if login_path is not UNSET:
            field_dict["loginPath"] = login_path
        if navbar is not UNSET:
            field_dict["navbar"] = navbar
        if heartbeat_interval is not UNSET:
            field_dict["heartbeatInterval"] = heartbeat_interval
        if user_workspace_enabled is not UNSET:
            field_dict["userWorkspaceEnabled"] = user_workspace_enabled
        if allow_instance_credentials is not UNSET:
            field_dict["allowInstanceCredentials"] = allow_instance_credentials
        if landing_url is not UNSET:
            field_dict["landingUrl"] = landing_url
        if terms_of_use_url is not UNSET:
            field_dict["termsOfUseUrl"] = terms_of_use_url
        if content_url is not UNSET:
            field_dict["contentUrl"] = content_url
        if analytics is not UNSET:
            field_dict["analytics"] = analytics
        if allow_local_repos is not UNSET:
            field_dict["allowLocalRepos"] = allow_local_repos
        if content_max_file_size is not UNSET:
            field_dict["contentMaxFileSize"] = content_max_file_size

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.analytics import Analytics
        from ..models.navbar_config import NavbarConfig

        d = src_dict.copy()
        version = d.pop("version", UNSET)

        api_version = d.pop("apiVersion", UNSET)

        commit_id = d.pop("commitId", UNSET)

        auth_types = cast(List[str], d.pop("authTypes", UNSET))

        login_path = d.pop("loginPath", UNSET)

        _navbar = d.pop("navbar", UNSET)
        navbar: Union[Unset, NavbarConfig]
        if isinstance(_navbar, Unset):
            navbar = UNSET
        else:
            navbar = NavbarConfig.from_dict(_navbar)

        heartbeat_interval = d.pop("heartbeatInterval", UNSET)

        user_workspace_enabled = d.pop("userWorkspaceEnabled", UNSET)

        allow_instance_credentials = d.pop("allowInstanceCredentials", UNSET)

        landing_url = d.pop("landingUrl", UNSET)

        terms_of_use_url = d.pop("termsOfUseUrl", UNSET)

        content_url = d.pop("contentUrl", UNSET)

        _analytics = d.pop("analytics", UNSET)
        analytics: Union[Unset, Analytics]
        if isinstance(_analytics, Unset):
            analytics = UNSET
        else:
            analytics = Analytics.from_dict(_analytics)

        allow_local_repos = d.pop("allowLocalRepos", UNSET)

        content_max_file_size = d.pop("contentMaxFileSize", UNSET)

        service_info = cls(
            version=version,
            api_version=api_version,
            commit_id=commit_id,
            auth_types=auth_types,
            login_path=login_path,
            navbar=navbar,
            heartbeat_interval=heartbeat_interval,
            user_workspace_enabled=user_workspace_enabled,
            allow_instance_credentials=allow_instance_credentials,
            landing_url=landing_url,
            terms_of_use_url=terms_of_use_url,
            content_url=content_url,
            analytics=analytics,
            allow_local_repos=allow_local_repos,
            content_max_file_size=content_max_file_size,
        )

        service_info.additional_properties = d
        return service_info

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
