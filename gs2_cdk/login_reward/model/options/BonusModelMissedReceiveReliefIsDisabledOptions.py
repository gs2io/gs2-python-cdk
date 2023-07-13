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
from ..Reward import Reward
from ....core.model import ConsumeAction
from ..enum.BonusModelMode import BonusModelMode
from ..enum.BonusModelRepeat import BonusModelRepeat
from ..enum.BonusModelMissedReceiveRelief import BonusModelMissedReceiveRelief


class BonusModelMissedReceiveReliefIsDisabledOptions:
    metadata: Optional[str]
    period_event_id: Optional[str]
    rewards: Optional[List[Reward]]
    missed_receive_relief_consume_actions: Optional[List[ConsumeAction]]
    
    def __init__(
        self,
        metadata: Optional[str] = None,
        period_event_id: Optional[str] = None,
        rewards: Optional[List[Reward]] = None,
        missed_receive_relief_consume_actions: Optional[List[ConsumeAction]] = None,
    ):
        self.metadata = metadata
        self.period_event_id = period_event_id
        self.rewards = rewards
        self.missed_receive_relief_consume_actions = missed_receive_relief_consume_actions
