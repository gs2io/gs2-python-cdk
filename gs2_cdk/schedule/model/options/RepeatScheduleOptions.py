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


class RepeatScheduleOptions:
    current_repeat_start_at: Optional[int]
    current_repeat_end_at: Optional[int]
    last_repeat_end_at: Optional[int]
    next_repeat_start_at: Optional[int]
    
    def __init__(
        self,
        current_repeat_start_at: Optional[int] = None,
        current_repeat_end_at: Optional[int] = None,
        last_repeat_end_at: Optional[int] = None,
        next_repeat_start_at: Optional[int] = None,
    ):
        self.current_repeat_start_at = current_repeat_start_at
        self.current_repeat_end_at = current_repeat_end_at
        self.last_repeat_end_at = last_repeat_end_at
        self.next_repeat_start_at = next_repeat_start_at

