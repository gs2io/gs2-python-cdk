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
from .options.UnleashMaterialSelectionOptions import UnleashMaterialSelectionOptions


class UnleashMaterialSelection:
    name: str
    item_set_ids: List[str]

    def __init__(
        self,
        name: str,
        item_set_ids: List[str],
        options: Optional[UnleashMaterialSelectionOptions] = UnleashMaterialSelectionOptions(),
    ):
        self.name = name
        self.item_set_ids = item_set_ids

    def properties(
        self,
    ) -> Dict[str, Any]:
        properties: Dict[str, Any] = {}

        if self.name is not None:
            properties["name"] = self.name
        if self.item_set_ids is not None:
            properties["itemSetIds"] = self.item_set_ids

        return properties
