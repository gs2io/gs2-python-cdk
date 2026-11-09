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
from ...core.model import AcquireAction
from .options.BonusOptions import BonusOptions


class Bonus:
    route_key: str
    acquire_actions: List[AcquireAction]

    def __init__(
        self,
        route_key: str,
        acquire_actions: List[AcquireAction],
        options: Optional[BonusOptions] = BonusOptions(),
    ):
        self.route_key = route_key
        self.acquire_actions = acquire_actions

    def properties(
        self,
    ) -> Dict[str, Any]:
        properties: Dict[str, Any] = {}

        if self.route_key is not None:
            properties["routeKey"] = self.route_key
        if self.acquire_actions is not None:
            properties["acquireActions"] = [
                v.properties(
                )
                for v in self.acquire_actions
            ]

        return properties
