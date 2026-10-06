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
from ..enums.UnleashQuantityMaterialSettingMatchType import UnleashQuantityMaterialSettingMatchType


class UnleashQuantityMaterialSettingOptions:
    material_inventory_model_id: Optional[str]
    item_model_id: Optional[str]
    
    def __init__(
        self,
        material_inventory_model_id: Optional[str] = None,
        item_model_id: Optional[str] = None,
    ):
        self.material_inventory_model_id = material_inventory_model_id
        self.item_model_id = item_model_id

