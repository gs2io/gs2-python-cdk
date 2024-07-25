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
from ..TargetCounterModel import TargetCounterModel
from ....core.model import VerifyAction
from ....core.model import AcquireAction
from ..MissionTaskModel import MissionTaskModel
from ..enum.MissionGroupModelResetType import MissionGroupModelResetType
from ..enum.MissionGroupModelResetDayOfWeek import MissionGroupModelResetDayOfWeek


class MissionGroupModelResetTypeIsDailyOptions:
    metadata: Optional[str]
    tasks: Optional[List[MissionTaskModel]]
    complete_notification_namespace_id: Optional[str]
    
    def __init__(
        self,
        metadata: Optional[str] = None,
        tasks: Optional[List[MissionTaskModel]] = None,
        complete_notification_namespace_id: Optional[str] = None,
    ):
        self.metadata = metadata
        self.tasks = tasks
        self.complete_notification_namespace_id = complete_notification_namespace_id
