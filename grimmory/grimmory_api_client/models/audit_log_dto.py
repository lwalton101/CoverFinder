from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.audit_log_dto_action import AuditLogDtoAction
from ..types import UNSET, Unset

T = TypeVar("T", bound="AuditLogDto")


@_attrs_define
class AuditLogDto:
    """
    Attributes:
        id (int | Unset):
        user_id (int | Unset):
        username (str | Unset):
        action (AuditLogDtoAction | Unset):
        entity_type (str | Unset):
        entity_id (int | Unset):
        description (str | Unset):
        ip_address (str | Unset):
        country_code (str | Unset):
        created_at (datetime.datetime | Unset):
    """

    id: int | Unset = UNSET
    user_id: int | Unset = UNSET
    username: str | Unset = UNSET
    action: AuditLogDtoAction | Unset = UNSET
    entity_type: str | Unset = UNSET
    entity_id: int | Unset = UNSET
    description: str | Unset = UNSET
    ip_address: str | Unset = UNSET
    country_code: str | Unset = UNSET
    created_at: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        user_id = self.user_id

        username = self.username

        action: str | Unset = UNSET
        if not isinstance(self.action, Unset):
            action = self.action.value

        entity_type = self.entity_type

        entity_id = self.entity_id

        description = self.description

        ip_address = self.ip_address

        country_code = self.country_code

        created_at: str | Unset = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if user_id is not UNSET:
            field_dict["userId"] = user_id
        if username is not UNSET:
            field_dict["username"] = username
        if action is not UNSET:
            field_dict["action"] = action
        if entity_type is not UNSET:
            field_dict["entityType"] = entity_type
        if entity_id is not UNSET:
            field_dict["entityId"] = entity_id
        if description is not UNSET:
            field_dict["description"] = description
        if ip_address is not UNSET:
            field_dict["ipAddress"] = ip_address
        if country_code is not UNSET:
            field_dict["countryCode"] = country_code
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        user_id = d.pop("userId", UNSET)

        username = d.pop("username", UNSET)

        _action = d.pop("action", UNSET)
        action: AuditLogDtoAction | Unset
        if isinstance(_action, Unset):
            action = UNSET
        else:
            action = AuditLogDtoAction(_action)

        entity_type = d.pop("entityType", UNSET)

        entity_id = d.pop("entityId", UNSET)

        description = d.pop("description", UNSET)

        ip_address = d.pop("ipAddress", UNSET)

        country_code = d.pop("countryCode", UNSET)

        _created_at = d.pop("createdAt", UNSET)
        created_at: datetime.datetime | Unset
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = datetime.datetime.fromisoformat(_created_at)

        audit_log_dto = cls(
            id=id,
            user_id=user_id,
            username=username,
            action=action,
            entity_type=entity_type,
            entity_id=entity_id,
            description=description,
            ip_address=ip_address,
            country_code=country_code,
            created_at=created_at,
        )

        audit_log_dto.additional_properties = d
        return audit_log_dto

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
