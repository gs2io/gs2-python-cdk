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
from .options.UnleashQuantityMaterialSettingOptions import UnleashQuantityMaterialSettingOptions
from .options.UnleashQuantityMaterialSettingMatchTypeIsSameGroupOptions import UnleashQuantityMaterialSettingMatchTypeIsSameGroupOptions
from .options.UnleashQuantityMaterialSettingMatchTypeIsSpecifiedOptions import UnleashQuantityMaterialSettingMatchTypeIsSpecifiedOptions
from .enums.UnleashQuantityMaterialSettingMatchType import UnleashQuantityMaterialSettingMatchType


class UnleashQuantityMaterialSetting:
    match_type: UnleashQuantityMaterialSettingMatchType
    count: int
    material_inventory_model_id: Optional[str] = None
    item_model_id: Optional[str] = None

    def __init__(
        self,
        match_type: UnleashQuantityMaterialSettingMatchType,
        count: int,
        options: Optional[UnleashQuantityMaterialSettingOptions] = UnleashQuantityMaterialSettingOptions(),
    ):
        self.match_type = match_type
        self.count = count
        self.material_inventory_model_id = options.material_inventory_model_id if options.material_inventory_model_id else None
        self.item_model_id = options.item_model_id if options.item_model_id else None

    @staticmethod
    def match_type_is_same_group(
        count: int,
        material_inventory_model_id: str,
        options: Optional[UnleashQuantityMaterialSettingMatchTypeIsSameGroupOptions] = UnleashQuantityMaterialSettingMatchTypeIsSameGroupOptions(),
    ) -> UnleashQuantityMaterialSetting:
        return UnleashQuantityMaterialSetting(
            UnleashQuantityMaterialSettingMatchType.SAME_GROUP,
            count,
            UnleashQuantityMaterialSettingOptions(
                material_inventory_model_id,
            ),
        )

    @staticmethod
    def match_type_is_specified(
        count: int,
        item_model_id: str,
        options: Optional[UnleashQuantityMaterialSettingMatchTypeIsSpecifiedOptions] = UnleashQuantityMaterialSettingMatchTypeIsSpecifiedOptions(),
    ) -> UnleashQuantityMaterialSetting:
        return UnleashQuantityMaterialSetting(
            UnleashQuantityMaterialSettingMatchType.SPECIFIED,
            count,
            UnleashQuantityMaterialSettingOptions(
                item_model_id,
            ),
        )

    def properties(
        self,
    ) -> Dict[str, Any]:
        properties: Dict[str, Any] = {}

        if self.match_type is not None:
            properties["matchType"] = self.match_type.value
        if self.material_inventory_model_id is not None:
            properties["materialInventoryModelId"] = self.material_inventory_model_id
        if self.item_model_id is not None:
            properties["itemModelId"] = self.item_model_id
        if self.count is not None:
            properties["count"] = self.count

        return properties
