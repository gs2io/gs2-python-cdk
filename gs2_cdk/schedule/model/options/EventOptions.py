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
from ..enum.EventScheduleType import EventScheduleType
from ..enum.EventRepeatType import EventRepeatType
from ..enum.EventRepeatBeginDayOfWeek import EventRepeatBeginDayOfWeek
from ..enum.EventRepeatEndDayOfWeek import EventRepeatEndDayOfWeek


class EventOptions:
    metadata: Optional[str]
    absolute_begin: Optional[int]
    absolute_end: Optional[int]
    repeat_begin_day_of_month: Optional[int]
    repeat_end_day_of_month: Optional[int]
    repeat_begin_day_of_week: Optional[EventRepeatBeginDayOfWeek]
    repeat_end_day_of_week: Optional[EventRepeatEndDayOfWeek]
    repeat_begin_hour: Optional[int]
    repeat_end_hour: Optional[int]
    relative_trigger_name: Optional[str]
    
    def __init__(
        self,
        metadata: Optional[str] = None,
        absolute_begin: Optional[int] = None,
        absolute_end: Optional[int] = None,
        repeat_begin_day_of_month: Optional[int] = None,
        repeat_end_day_of_month: Optional[int] = None,
        repeat_begin_day_of_week: Optional[EventRepeatBeginDayOfWeek] = None,
        repeat_end_day_of_week: Optional[EventRepeatEndDayOfWeek] = None,
        repeat_begin_hour: Optional[int] = None,
        repeat_end_hour: Optional[int] = None,
        relative_trigger_name: Optional[str] = None,
    ):
        self.metadata = metadata
        self.absolute_begin = absolute_begin
        self.absolute_end = absolute_end
        self.repeat_begin_day_of_month = repeat_begin_day_of_month
        self.repeat_end_day_of_month = repeat_end_day_of_month
        self.repeat_begin_day_of_week = repeat_begin_day_of_week
        self.repeat_end_day_of_week = repeat_end_day_of_week
        self.repeat_begin_hour = repeat_begin_hour
        self.repeat_end_hour = repeat_end_hour
        self.relative_trigger_name = relative_trigger_name

