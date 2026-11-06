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
from .options.StateMachineSettingOptions import StateMachineSettingOptions


class StateMachineSetting:
    namespace_id: str
    version: Optional[int] = None

    def __init__(
        self,
        namespace_id: str,
        options: Optional[StateMachineSettingOptions] = StateMachineSettingOptions(),
    ):
        self.namespace_id = namespace_id
        self.version = options.version if options.version else None

    def properties(
        self,
    ) -> Dict[str, Any]:
        properties: Dict[str, Any] = {}

        if self.namespace_id is not None:
            properties["namespaceId"] = self.namespace_id
        if self.version is not None:
            properties["version"] = self.version

        return properties
