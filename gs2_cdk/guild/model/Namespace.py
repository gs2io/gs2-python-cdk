# Copyright 2016- Game Server Services, Inc. or its affiliates. All Rights
# Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License").
# You may not use this file except in compliance with the License.
# A copy of the License is located at
#
#  http://www.apache.org/licenses/LICENSE-2.0
#
# or in the "license" file accompanying this file. This file is distributed
# on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either
# express or implied. See the License for the specific language governing
# permissions and limitations under the License.
from __future__ import annotations
from typing import *

from ...core.model import CdkResource, Stack
from ...core.func import GetAttr
from ...core.model import NotificationSetting
from ...core.model import ScriptSetting
from ...core.model import LogSetting

from ..ref.NamespaceRef import NamespaceRef
from .CurrentMasterData import CurrentMasterData
from .GuildModel import GuildModel

from .options.NamespaceOptions import NamespaceOptions


class Namespace(CdkResource):
    stack: Stack
    name: str
    description: Optional[str] = None
    change_notification: Optional[NotificationSetting] = None
    join_notification: Optional[NotificationSetting] = None
    leave_notification: Optional[NotificationSetting] = None
    change_member_notification: Optional[NotificationSetting] = None
    receive_request_notification: Optional[NotificationSetting] = None
    remove_request_notification: Optional[NotificationSetting] = None
    create_guild_script: Optional[ScriptSetting] = None
    update_guild_script: Optional[ScriptSetting] = None
    join_guild_script: Optional[ScriptSetting] = None
    leave_guild_script: Optional[ScriptSetting] = None
    change_role_script: Optional[ScriptSetting] = None
    delete_guild_script: Optional[ScriptSetting] = None
    log_setting: Optional[LogSetting] = None

    def __init__(
        self,
        stack: Stack,
        name: str,
        options: Optional[NamespaceOptions] = NamespaceOptions(),
    ):
        super().__init__(
            "Guild_Namespace_" + name
        )

        self.stack = stack
        self.name = name
        self.description = options.description if options.description else None
        self.change_notification = options.change_notification if options.change_notification else None
        self.join_notification = options.join_notification if options.join_notification else None
        self.leave_notification = options.leave_notification if options.leave_notification else None
        self.change_member_notification = options.change_member_notification if options.change_member_notification else None
        self.receive_request_notification = options.receive_request_notification if options.receive_request_notification else None
        self.remove_request_notification = options.remove_request_notification if options.remove_request_notification else None
        self.create_guild_script = options.create_guild_script if options.create_guild_script else None
        self.update_guild_script = options.update_guild_script if options.update_guild_script else None
        self.join_guild_script = options.join_guild_script if options.join_guild_script else None
        self.leave_guild_script = options.leave_guild_script if options.leave_guild_script else None
        self.change_role_script = options.change_role_script if options.change_role_script else None
        self.delete_guild_script = options.delete_guild_script if options.delete_guild_script else None
        self.log_setting = options.log_setting if options.log_setting else None
        stack.add_resource(
            self,
        )


    def alternate_keys(
        self,
    ):
        return "name"

    def resource_type(
        self,
    ) -> str:
        return "GS2::Guild::Namespace"

    def properties(
        self,
    ) -> Dict[str, Any]:
        properties: Dict[str, Any] = {}

        if self.name is not None:
            properties["Name"] = self.name
        if self.description is not None:
            properties["Description"] = self.description
        if self.change_notification is not None:
            properties["ChangeNotification"] = self.change_notification.properties(
            )
        if self.join_notification is not None:
            properties["JoinNotification"] = self.join_notification.properties(
            )
        if self.leave_notification is not None:
            properties["LeaveNotification"] = self.leave_notification.properties(
            )
        if self.change_member_notification is not None:
            properties["ChangeMemberNotification"] = self.change_member_notification.properties(
            )
        if self.receive_request_notification is not None:
            properties["ReceiveRequestNotification"] = self.receive_request_notification.properties(
            )
        if self.remove_request_notification is not None:
            properties["RemoveRequestNotification"] = self.remove_request_notification.properties(
            )
        if self.create_guild_script is not None:
            properties["CreateGuildScript"] = self.create_guild_script.properties(
            )
        if self.update_guild_script is not None:
            properties["UpdateGuildScript"] = self.update_guild_script.properties(
            )
        if self.join_guild_script is not None:
            properties["JoinGuildScript"] = self.join_guild_script.properties(
            )
        if self.leave_guild_script is not None:
            properties["LeaveGuildScript"] = self.leave_guild_script.properties(
            )
        if self.change_role_script is not None:
            properties["ChangeRoleScript"] = self.change_role_script.properties(
            )
        if self.delete_guild_script is not None:
            properties["DeleteGuildScript"] = self.delete_guild_script.properties(
            )
        if self.log_setting is not None:
            properties["LogSetting"] = self.log_setting.properties(
            )

        return properties

    def ref(
        self,
    ) -> NamespaceRef:
        return NamespaceRef(
            self.name,
        )

    def get_attr_namespace_id(
        self,
    ) -> GetAttr:
        return GetAttr(
            self,
            "Item.NamespaceId",
            None,
        )

    def master_data(
        self,
        guild_models: List[GuildModel],
    ) -> Namespace:
        CurrentMasterData(
            self.stack,
            self.name,
            guild_models,
        ).add_depends_on(
            self,
        )
        return self
