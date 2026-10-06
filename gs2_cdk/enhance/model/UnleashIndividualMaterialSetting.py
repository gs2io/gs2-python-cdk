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
from .options.UnleashIndividualMaterialSettingOptions import UnleashIndividualMaterialSettingOptions
from .options.UnleashIndividualMaterialSettingGradeConditionIsAnyOptions import UnleashIndividualMaterialSettingGradeConditionIsAnyOptions
from .options.UnleashIndividualMaterialSettingGradeConditionIsSameAsTargetOptions import UnleashIndividualMaterialSettingGradeConditionIsSameAsTargetOptions
from .options.UnleashIndividualMaterialSettingGradeConditionIsEqualOptions import UnleashIndividualMaterialSettingGradeConditionIsEqualOptions
from .enums.UnleashIndividualMaterialSettingMatchType import UnleashIndividualMaterialSettingMatchType
from .enums.UnleashIndividualMaterialSettingGradeCondition import UnleashIndividualMaterialSettingGradeCondition


class UnleashIndividualMaterialSetting:
    match_type: UnleashIndividualMaterialSettingMatchType
    grade_condition: UnleashIndividualMaterialSettingGradeCondition
    count: int
    grade_value: Optional[int] = None

    def __init__(
        self,
        match_type: UnleashIndividualMaterialSettingMatchType,
        grade_condition: UnleashIndividualMaterialSettingGradeCondition,
        count: int,
        options: Optional[UnleashIndividualMaterialSettingOptions] = UnleashIndividualMaterialSettingOptions(),
    ):
        self.match_type = match_type
        self.grade_condition = grade_condition
        self.count = count
        self.grade_value = options.grade_value if options.grade_value else None

    @staticmethod
    def grade_condition_is_any(
        match_type: UnleashIndividualMaterialSettingMatchType,
        count: int,
        options: Optional[UnleashIndividualMaterialSettingGradeConditionIsAnyOptions] = UnleashIndividualMaterialSettingGradeConditionIsAnyOptions(),
    ) -> UnleashIndividualMaterialSetting:
        return UnleashIndividualMaterialSetting(
            match_type,
            UnleashIndividualMaterialSettingGradeCondition.ANY,
            count,
            UnleashIndividualMaterialSettingOptions(
            ),
        )

    @staticmethod
    def grade_condition_is_same_as_target(
        match_type: UnleashIndividualMaterialSettingMatchType,
        count: int,
        options: Optional[UnleashIndividualMaterialSettingGradeConditionIsSameAsTargetOptions] = UnleashIndividualMaterialSettingGradeConditionIsSameAsTargetOptions(),
    ) -> UnleashIndividualMaterialSetting:
        return UnleashIndividualMaterialSetting(
            match_type,
            UnleashIndividualMaterialSettingGradeCondition.SAME_AS_TARGET,
            count,
            UnleashIndividualMaterialSettingOptions(
            ),
        )

    @staticmethod
    def grade_condition_is_equal(
        match_type: UnleashIndividualMaterialSettingMatchType,
        count: int,
        grade_value: int,
        options: Optional[UnleashIndividualMaterialSettingGradeConditionIsEqualOptions] = UnleashIndividualMaterialSettingGradeConditionIsEqualOptions(),
    ) -> UnleashIndividualMaterialSetting:
        return UnleashIndividualMaterialSetting(
            match_type,
            UnleashIndividualMaterialSettingGradeCondition.EQUAL,
            count,
            UnleashIndividualMaterialSettingOptions(
                grade_value,
            ),
        )

    def properties(
        self,
    ) -> Dict[str, Any]:
        properties: Dict[str, Any] = {}

        if self.match_type is not None:
            properties["matchType"] = self.match_type.value
        if self.grade_condition is not None:
            properties["gradeCondition"] = self.grade_condition.value
        if self.grade_value is not None:
            properties["gradeValue"] = self.grade_value
        if self.count is not None:
            properties["count"] = self.count

        return properties
