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
from ..RepeatSetting import RepeatSetting
from ..enum.EventScheduleType import EventScheduleType
from ..enum.EventRepeatType import EventRepeatType
from ..enum.EventRepeatBeginDayOfWeek import EventRepeatBeginDayOfWeek
from ..enum.EventRepeatEndDayOfWeek import EventRepeatEndDayOfWeek


class EventScheduleTypeIsRelativeOptions:
    metadata: Optional[str]
    absolute_begin: Optional[int]
    absolute_end: Optional[int]
    
    def __init__(
        self,
        metadata: Optional[str] = None,
        absolute_begin: Optional[int] = None,
        absolute_end: Optional[int] = None,
    ):
        self.metadata = metadata
        self.absolute_begin = absolute_begin
        self.absolute_end = absolute_end
