import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.action_source import ActionSource
from ..models.action_status import ActionStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.action_tower_action_config import ActionTowerActionConfig
    from ..models.action_tower_action_event import ActionTowerActionEvent
    from ..models.github_action_config import GithubActionConfig
    from ..models.github_action_event import GithubActionEvent
    from ..models.label_db_dto import LabelDbDto
    from ..models.launch import Launch


T = TypeVar("T", bound="ActionResponseDto")


@attr.s(auto_attribs=True)
class ActionResponseDto:
    """
    Attributes:
        id (Union[Unset, str]):
        launch (Union[Unset, Launch]):
        name (Union[Unset, str]):
        hook_id (Union[Unset, str]):
        hook_url (Union[Unset, str]):
        message (Union[Unset, str]):
        source (Union[Unset, ActionSource]):
        status (Union[Unset, ActionStatus]):
        config (Union['ActionTowerActionConfig', 'GithubActionConfig', Unset]):
        event (Union['ActionTowerActionEvent', 'GithubActionEvent', Unset]):
        last_seen (Union[Unset, datetime.datetime]):
        date_created (Union[Unset, datetime.datetime]):
        last_updated (Union[Unset, datetime.datetime]):
        labels (Union[Unset, List['LabelDbDto']]):
    """

    id: Union[Unset, str] = UNSET
    launch: Union[Unset, "Launch"] = UNSET
    name: Union[Unset, str] = UNSET
    hook_id: Union[Unset, str] = UNSET
    hook_url: Union[Unset, str] = UNSET
    message: Union[Unset, str] = UNSET
    source: Union[Unset, ActionSource] = UNSET
    status: Union[Unset, ActionStatus] = UNSET
    config: Union["ActionTowerActionConfig", "GithubActionConfig", Unset] = UNSET
    event: Union["ActionTowerActionEvent", "GithubActionEvent", Unset] = UNSET
    last_seen: Union[Unset, datetime.datetime] = UNSET
    date_created: Union[Unset, datetime.datetime] = UNSET
    last_updated: Union[Unset, datetime.datetime] = UNSET
    labels: Union[Unset, List["LabelDbDto"]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.action_tower_action_config import ActionTowerActionConfig
        from ..models.github_action_event import GithubActionEvent

        id = self.id
        launch: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.launch, Unset):
            launch = self.launch.to_dict()

        name = self.name
        hook_id = self.hook_id
        hook_url = self.hook_url
        message = self.message
        source: Union[Unset, str] = UNSET
        if not isinstance(self.source, Unset):
            source = self.source.value

        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        config: Union[Dict[str, Any], Unset]
        if isinstance(self.config, Unset):
            config = UNSET

        elif isinstance(self.config, ActionTowerActionConfig):
            config = self.config.to_dict()

        else:
            config = self.config.to_dict()

        event: Union[Dict[str, Any], Unset]
        if isinstance(self.event, Unset):
            event = UNSET

        elif isinstance(self.event, GithubActionEvent):
            event = self.event.to_dict()

        else:
            event = self.event.to_dict()

        last_seen: Union[Unset, str] = UNSET
        if not isinstance(self.last_seen, Unset):
            last_seen = self.last_seen.isoformat()

        date_created: Union[Unset, str] = UNSET
        if not isinstance(self.date_created, Unset):
            date_created = self.date_created.isoformat()

        last_updated: Union[Unset, str] = UNSET
        if not isinstance(self.last_updated, Unset):
            last_updated = self.last_updated.isoformat()

        labels: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.labels, Unset):
            labels = []
            for labels_item_data in self.labels:
                labels_item = labels_item_data.to_dict()

                labels.append(labels_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if launch is not UNSET:
            field_dict["launch"] = launch
        if name is not UNSET:
            field_dict["name"] = name
        if hook_id is not UNSET:
            field_dict["hookId"] = hook_id
        if hook_url is not UNSET:
            field_dict["hookUrl"] = hook_url
        if message is not UNSET:
            field_dict["message"] = message
        if source is not UNSET:
            field_dict["source"] = source
        if status is not UNSET:
            field_dict["status"] = status
        if config is not UNSET:
            field_dict["config"] = config
        if event is not UNSET:
            field_dict["event"] = event
        if last_seen is not UNSET:
            field_dict["lastSeen"] = last_seen
        if date_created is not UNSET:
            field_dict["dateCreated"] = date_created
        if last_updated is not UNSET:
            field_dict["lastUpdated"] = last_updated
        if labels is not UNSET:
            field_dict["labels"] = labels

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.action_tower_action_config import ActionTowerActionConfig
        from ..models.action_tower_action_event import ActionTowerActionEvent
        from ..models.github_action_config import GithubActionConfig
        from ..models.github_action_event import GithubActionEvent
        from ..models.label_db_dto import LabelDbDto
        from ..models.launch import Launch

        d = src_dict.copy()
        id = d.pop("id", UNSET)

        _launch = d.pop("launch", UNSET)
        launch: Union[Unset, Launch]
        if isinstance(_launch, Unset):
            launch = UNSET
        else:
            launch = Launch.from_dict(_launch)

        name = d.pop("name", UNSET)

        hook_id = d.pop("hookId", UNSET)

        hook_url = d.pop("hookUrl", UNSET)

        message = d.pop("message", UNSET)

        _source = d.pop("source", UNSET)
        source: Union[Unset, ActionSource]
        if isinstance(_source, Unset):
            source = UNSET
        else:
            source = ActionSource(_source)

        _status = d.pop("status", UNSET)
        status: Union[Unset, ActionStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = ActionStatus(_status)

        def _parse_config(data: object) -> Union["ActionTowerActionConfig", "GithubActionConfig", Unset]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_action_config_type_type_0 = ActionTowerActionConfig.from_dict(data)

                return componentsschemas_action_config_type_type_0
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_action_config_type_type_1 = GithubActionConfig.from_dict(data)

            return componentsschemas_action_config_type_type_1

        config = _parse_config(d.pop("config", UNSET))

        def _parse_event(data: object) -> Union["ActionTowerActionEvent", "GithubActionEvent", Unset]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_action_event_type_type_0 = GithubActionEvent.from_dict(data)

                return componentsschemas_action_event_type_type_0
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_action_event_type_type_1 = ActionTowerActionEvent.from_dict(data)

            return componentsschemas_action_event_type_type_1

        event = _parse_event(d.pop("event", UNSET))

        _last_seen = d.pop("lastSeen", UNSET)
        last_seen: Union[Unset, datetime.datetime]
        if isinstance(_last_seen, Unset):
            last_seen = UNSET
        else:
            last_seen = isoparse(_last_seen)

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

        labels = []
        _labels = d.pop("labels", UNSET)
        for labels_item_data in _labels or []:
            labels_item = LabelDbDto.from_dict(labels_item_data)

            labels.append(labels_item)

        action_response_dto = cls(
            id=id,
            launch=launch,
            name=name,
            hook_id=hook_id,
            hook_url=hook_url,
            message=message,
            source=source,
            status=status,
            config=config,
            event=event,
            last_seen=last_seen,
            date_created=date_created,
            last_updated=last_updated,
            labels=labels,
        )

        action_response_dto.additional_properties = d
        return action_response_dto

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
