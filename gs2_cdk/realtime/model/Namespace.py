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
from ...core.model import LogSetting

from ..ref.NamespaceRef import NamespaceRef
from .enums.NamespaceServerType import NamespaceServerType
from .enums.NamespaceServerSpec import NamespaceServerSpec

from .options.NamespaceOptions import NamespaceOptions


class Namespace(CdkResource):
    stack: Stack
    name: str
    server_type: NamespaceServerType
    server_spec: NamespaceServerSpec
    description: Optional[str] = None
    create_notification: Optional[NotificationSetting] = None
    log_setting: Optional[LogSetting] = None

    def __init__(
        self,
        stack: Stack,
        name: str,
        server_type: NamespaceServerType,
        server_spec: NamespaceServerSpec,
        options: Optional[NamespaceOptions] = NamespaceOptions(),
    ):
        super().__init__(
            "Realtime_Namespace_" + name
        )

        self.stack = stack
        self.name = name
        self.server_type = server_type
        self.server_spec = server_spec
        self.description = options.description if options.description else None
        self.create_notification = options.create_notification if options.create_notification else None
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
        return "GS2::Realtime::Namespace"

    def properties(
        self,
    ) -> Dict[str, Any]:
        properties: Dict[str, Any] = {}

        if self.name is not None:
            properties["Name"] = self.name
        if self.description is not None:
            properties["Description"] = self.description
        if self.server_type is not None:
            properties["ServerType"] = self.server_type
        if self.server_spec is not None:
            properties["ServerSpec"] = self.server_spec
        if self.create_notification is not None:
            properties["CreateNotification"] = self.create_notification.properties(
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
