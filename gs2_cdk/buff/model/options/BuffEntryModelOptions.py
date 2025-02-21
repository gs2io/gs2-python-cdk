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
from ..BuffTargetGrn import BuffTargetGrn
from ..BuffTargetModel import BuffTargetModel
from ..BuffTargetAction import BuffTargetAction
from ..enums.BuffEntryModelExpression import BuffEntryModelExpression
from ..enums.BuffEntryModelTargetType import BuffEntryModelTargetType


class BuffEntryModelOptions:
    metadata: Optional[str]
    target_model: Optional[BuffTargetModel]
    target_action: Optional[BuffTargetAction]
    apply_period_schedule_event_id: Optional[str]
    
    def __init__(
        self,
        metadata: Optional[str] = None,
        target_model: Optional[BuffTargetModel] = None,
        target_action: Optional[BuffTargetAction] = None,
        apply_period_schedule_event_id: Optional[str] = None,
    ):
        self.metadata = metadata
        self.target_model = target_model
        self.target_action = target_action
        self.apply_period_schedule_event_id = apply_period_schedule_event_id

