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


class MissionTaskModelOptions:
    metadata: Optional[str]
    complete_acquire_actions: Optional[List[AcquireAction]]
    challenge_period_event_id: Optional[str]
    premise_mission_task_name: Optional[str]
    
    def __init__(
        self,
        metadata: Optional[str] = None,
        complete_acquire_actions: Optional[List[AcquireAction]] = None,
        challenge_period_event_id: Optional[str] = None,
        premise_mission_task_name: Optional[str] = None,
    ):
        self.metadata = metadata
        self.complete_acquire_actions = complete_acquire_actions
        self.challenge_period_event_id = challenge_period_event_id
        self.premise_mission_task_name = premise_mission_task_name

