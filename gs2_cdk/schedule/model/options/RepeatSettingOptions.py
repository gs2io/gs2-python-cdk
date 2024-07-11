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
from ..enum.RepeatSettingRepeatType import RepeatSettingRepeatType
from ..enum.RepeatSettingBeginDayOfWeek import RepeatSettingBeginDayOfWeek
from ..enum.RepeatSettingEndDayOfWeek import RepeatSettingEndDayOfWeek


class RepeatSettingOptions:
    begin_day_of_month: Optional[int]
    end_day_of_month: Optional[int]
    begin_day_of_week: Optional[RepeatSettingBeginDayOfWeek]
    end_day_of_week: Optional[RepeatSettingEndDayOfWeek]
    begin_hour: Optional[int]
    end_hour: Optional[int]
    anchor_timestamp: Optional[int]
    active_days: Optional[int]
    inactive_days: Optional[int]
    
    def __init__(
        self,
        begin_day_of_month: Optional[int] = None,
        end_day_of_month: Optional[int] = None,
        begin_day_of_week: Optional[RepeatSettingBeginDayOfWeek] = None,
        end_day_of_week: Optional[RepeatSettingEndDayOfWeek] = None,
        begin_hour: Optional[int] = None,
        end_hour: Optional[int] = None,
        anchor_timestamp: Optional[int] = None,
        active_days: Optional[int] = None,
        inactive_days: Optional[int] = None,
    ):
        self.begin_day_of_month = begin_day_of_month
        self.end_day_of_month = end_day_of_month
        self.begin_day_of_week = begin_day_of_week
        self.end_day_of_week = end_day_of_week
        self.begin_hour = begin_hour
        self.end_hour = end_hour
        self.anchor_timestamp = anchor_timestamp
        self.active_days = active_days
        self.inactive_days = inactive_days

