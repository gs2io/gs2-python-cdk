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
from ..UnleashIndividualMaterialSetting import UnleashIndividualMaterialSetting
from ..UnleashQuantityMaterialSetting import UnleashQuantityMaterialSetting
from ..enums.UnleashMaterialMaterialType import UnleashMaterialMaterialType


class UnleashMaterialOptions:
    individual_setting: Optional[UnleashIndividualMaterialSetting]
    quantity_setting: Optional[UnleashQuantityMaterialSetting]
    
    def __init__(
        self,
        individual_setting: Optional[UnleashIndividualMaterialSetting] = None,
        quantity_setting: Optional[UnleashQuantityMaterialSetting] = None,
    ):
        self.individual_setting = individual_setting
        self.quantity_setting = quantity_setting

