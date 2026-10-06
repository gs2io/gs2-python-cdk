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
from .UnleashIndividualMaterialSetting import UnleashIndividualMaterialSetting
from .UnleashQuantityMaterialSetting import UnleashQuantityMaterialSetting
from .UnleashMaterial import UnleashMaterial
from .options.UnleashRecipeOptions import UnleashRecipeOptions


class UnleashRecipe:
    name: str
    materials: List[UnleashMaterial]
    metadata: Optional[str] = None
    target_group_keys: Optional[List[str]] = None

    def __init__(
        self,
        name: str,
        materials: List[UnleashMaterial],
        options: Optional[UnleashRecipeOptions] = UnleashRecipeOptions(),
    ):
        self.name = name
        self.materials = materials
        self.metadata = options.metadata if options.metadata else None
        self.target_group_keys = options.target_group_keys if options.target_group_keys else None

    def properties(
        self,
    ) -> Dict[str, Any]:
        properties: Dict[str, Any] = {}

        if self.name is not None:
            properties["name"] = self.name
        if self.metadata is not None:
            properties["metadata"] = self.metadata
        if self.target_group_keys is not None:
            properties["targetGroupKeys"] = self.target_group_keys
        if self.materials is not None:
            properties["materials"] = [
                v.properties(
                )
                for v in self.materials
            ]

        return properties
