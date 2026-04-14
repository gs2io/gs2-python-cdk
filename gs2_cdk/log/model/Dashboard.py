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
#
# deny overwrite
from __future__ import annotations
from typing import *

from ...core.model import CdkResource, Stack
from ...core.func import GetAttr

from ..ref.DashboardRef import DashboardRef

from .options.DashboardOptions import DashboardOptions


class Dashboard(CdkResource):
    stack: Stack
    namespace_name: str
    display_name: str
    description: Optional[str] = None

    def __init__(
        self,
        stack: Stack,
        namespace_name: str,
        display_name: str,
        options: Optional[DashboardOptions] = DashboardOptions(),
    ):
        super().__init__(
            "Log_Dashboard_" + display_name
        )

        self.stack = stack
        self.namespace_name = namespace_name
        self.display_name = display_name
        self.description = options.description if options.description else None
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
        return "GS2::Log::Dashboard"

    def properties(
        self,
    ) -> Dict[str, Any]:
        properties: Dict[str, Any] = {}

        if self.namespace_name is not None:
            properties["NamespaceName"] = self.namespace_name
        if self.display_name is not None:
            properties["DisplayName"] = self.display_name
        if self.description is not None:
            properties["Description"] = self.description

        return properties

    def ref(
        self,
        name: str,
    ) -> DashboardRef:
        return DashboardRef(
            self.namespace_name,
            name,
        )

    def get_attr_dashboard_id(
        self,
    ) -> GetAttr:
        return GetAttr(
            self,
            "Item.DashboardId",
            None,
        )
