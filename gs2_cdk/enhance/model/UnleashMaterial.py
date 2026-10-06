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
from .options.UnleashMaterialOptions import UnleashMaterialOptions
from .options.UnleashMaterialMaterialTypeIsIndividualOptions import UnleashMaterialMaterialTypeIsIndividualOptions
from .options.UnleashMaterialMaterialTypeIsQuantityOptions import UnleashMaterialMaterialTypeIsQuantityOptions
from .enums.UnleashMaterialMaterialType import UnleashMaterialMaterialType


class UnleashMaterial:
    name: str
    material_type: UnleashMaterialMaterialType
    individual_setting: Optional[UnleashIndividualMaterialSetting] = None
    quantity_setting: Optional[UnleashQuantityMaterialSetting] = None

    def __init__(
        self,
        name: str,
        material_type: UnleashMaterialMaterialType,
        options: Optional[UnleashMaterialOptions] = UnleashMaterialOptions(),
    ):
        self.name = name
        self.material_type = material_type
        self.individual_setting = options.individual_setting if options.individual_setting else None
        self.quantity_setting = options.quantity_setting if options.quantity_setting else None

    @staticmethod
    def material_type_is_individual(
        name: str,
        individual_setting: UnleashIndividualMaterialSetting,
        options: Optional[UnleashMaterialMaterialTypeIsIndividualOptions] = UnleashMaterialMaterialTypeIsIndividualOptions(),
    ) -> UnleashMaterial:
        return UnleashMaterial(
            name,
            UnleashMaterialMaterialType.INDIVIDUAL,
            UnleashMaterialOptions(
                individual_setting,
            ),
        )

    @staticmethod
    def material_type_is_quantity(
        name: str,
        quantity_setting: UnleashQuantityMaterialSetting,
        options: Optional[UnleashMaterialMaterialTypeIsQuantityOptions] = UnleashMaterialMaterialTypeIsQuantityOptions(),
    ) -> UnleashMaterial:
        return UnleashMaterial(
            name,
            UnleashMaterialMaterialType.QUANTITY,
            UnleashMaterialOptions(
                quantity_setting,
            ),
        )

    def properties(
        self,
    ) -> Dict[str, Any]:
        properties: Dict[str, Any] = {}

        if self.name is not None:
            properties["name"] = self.name
        if self.material_type is not None:
            properties["materialType"] = self.material_type.value
        if self.individual_setting is not None:
            properties["individualSetting"] = self.individual_setting.properties(
            )
        if self.quantity_setting is not None:
            properties["quantitySetting"] = self.quantity_setting.properties(
            )

        return properties
