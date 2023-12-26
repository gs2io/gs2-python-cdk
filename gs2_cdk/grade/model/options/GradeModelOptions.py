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
from ..DefaultGradeModel import DefaultGradeModel
from ..GradeEntryModel import GradeEntryModel
from ..AcquireActionRate import AcquireActionRate


class GradeModelOptions:
    metadata: Optional[str]
    default_grades: Optional[List[DefaultGradeModel]]
    acquire_action_rates: Optional[List[AcquireActionRate]]
    
    def __init__(
        self,
        metadata: Optional[str] = None,
        default_grades: Optional[List[DefaultGradeModel]] = None,
        acquire_action_rates: Optional[List[AcquireActionRate]] = None,
    ):
        self.metadata = metadata
        self.default_grades = default_grades
        self.acquire_action_rates = acquire_action_rates

