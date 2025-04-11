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
from ....core.model import AcquireAction
from ..AcquireActionList import AcquireActionList
from ..enums.CategoryModelRewardResetMode import CategoryModelRewardResetMode


class CategoryModelOptions:
    metadata: Optional[str]
    idle_period_schedule_id: Optional[str]
    receive_period_schedule_id: Optional[str]
    
    def __init__(
        self,
        metadata: Optional[str] = None,
        idle_period_schedule_id: Optional[str] = None,
        receive_period_schedule_id: Optional[str] = None,
    ):
        self.metadata = metadata
        self.idle_period_schedule_id = idle_period_schedule_id
        self.receive_period_schedule_id = receive_period_schedule_id

