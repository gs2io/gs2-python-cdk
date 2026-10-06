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
from .UnleashRecipe import UnleashRecipe
from .options.UnleashRateEntryModelOptions import UnleashRateEntryModelOptions
from .options.UnleashRateEntryModelTypeIsSimpleOptions import UnleashRateEntryModelTypeIsSimpleOptions
from .options.UnleashRateEntryModelTypeIsRecipeOptions import UnleashRateEntryModelTypeIsRecipeOptions
from .enums.UnleashRateEntryModelType import UnleashRateEntryModelType


class UnleashRateEntryModel:
    grade_value: int
    type: UnleashRateEntryModelType
    need_count: Optional[int] = None
    recipes: Optional[List[UnleashRecipe]] = None

    def __init__(
        self,
        grade_value: int,
        type: UnleashRateEntryModelType,
        options: Optional[UnleashRateEntryModelOptions] = UnleashRateEntryModelOptions(),
    ):
        self.grade_value = grade_value
        self.type = type
        self.need_count = options.need_count if options.need_count else None
        self.recipes = options.recipes if options.recipes else None

    @staticmethod
    def type_is_simple(
        grade_value: int,
        need_count: int,
        options: Optional[UnleashRateEntryModelTypeIsSimpleOptions] = UnleashRateEntryModelTypeIsSimpleOptions(),
    ) -> UnleashRateEntryModel:
        return UnleashRateEntryModel(
            grade_value,
            UnleashRateEntryModelType.SIMPLE,
            UnleashRateEntryModelOptions(
                need_count,
            ),
        )

    @staticmethod
    def type_is_recipe(
        grade_value: int,
        recipes: List[UnleashRecipe],
        options: Optional[UnleashRateEntryModelTypeIsRecipeOptions] = UnleashRateEntryModelTypeIsRecipeOptions(),
    ) -> UnleashRateEntryModel:
        return UnleashRateEntryModel(
            grade_value,
            UnleashRateEntryModelType.RECIPE,
            UnleashRateEntryModelOptions(
                recipes,
            ),
        )

    def properties(
        self,
    ) -> Dict[str, Any]:
        properties: Dict[str, Any] = {}

        if self.grade_value is not None:
            properties["gradeValue"] = self.grade_value
        if self.type is not None:
            properties["type"] = self.type.value
        if self.need_count is not None:
            properties["needCount"] = self.need_count
        if self.recipes is not None:
            properties["recipes"] = [
                v.properties(
                )
                for v in self.recipes
            ]

        return properties
