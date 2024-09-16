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
from ....core.model import VerifyAction
from ..enum.CounterScopeModelScopeType import CounterScopeModelScopeType
from ..enum.CounterScopeModelResetType import CounterScopeModelResetType
from ..enum.CounterScopeModelResetDayOfWeek import CounterScopeModelResetDayOfWeek


class CounterScopeModelOptions:
    reset_type: Optional[CounterScopeModelResetType]
    reset_day_of_month: Optional[int]
    reset_day_of_week: Optional[CounterScopeModelResetDayOfWeek]
    reset_hour: Optional[int]
    condition_name: Optional[str]
    condition: Optional[VerifyAction]
    
    def __init__(
        self,
        reset_type: Optional[CounterScopeModelResetType] = None,
        reset_day_of_month: Optional[int] = None,
        reset_day_of_week: Optional[CounterScopeModelResetDayOfWeek] = None,
        reset_hour: Optional[int] = None,
        condition_name: Optional[str] = None,
        condition: Optional[VerifyAction] = None,
    ):
        self.reset_type = reset_type
        self.reset_day_of_month = reset_day_of_month
        self.reset_day_of_week = reset_day_of_week
        self.reset_hour = reset_hour
        self.condition_name = condition_name
        self.condition = condition

