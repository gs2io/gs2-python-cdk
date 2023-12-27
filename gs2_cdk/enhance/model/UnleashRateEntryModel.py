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
from .options.UnleashRateEntryModelOptions import UnleashRateEntryModelOptions


class UnleashRateEntryModel:
    grade_value: int
    need_count: int

    def __init__(
        self,
        grade_value: int,
        need_count: int,
        options: Optional[UnleashRateEntryModelOptions] = UnleashRateEntryModelOptions(),
    ):
        self.grade_value = grade_value
        self.need_count = need_count

    def properties(
        self,
    ) -> Dict[str, Any]:
        properties: Dict[str, Any] = {}

        if self.grade_value is not None:
            properties["gradeValue"] = self.grade_value
        if self.need_count is not None:
            properties["needCount"] = self.need_count

        return properties
