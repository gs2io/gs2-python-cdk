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
from ..RankingReward import RankingReward
from ..enums.GlobalRankingModelOrderDirection import GlobalRankingModelOrderDirection
from ..enums.GlobalRankingModelRewardCalculationIndex import GlobalRankingModelRewardCalculationIndex


class GlobalRankingModelOptions:
    metadata: Optional[str]
    minimum_value: Optional[int]
    maximum_value: Optional[int]
    entry_period_event_id: Optional[str]
    ranking_rewards: Optional[List[RankingReward]]
    access_period_event_id: Optional[str]
    
    def __init__(
        self,
        metadata: Optional[str] = None,
        minimum_value: Optional[int] = None,
        maximum_value: Optional[int] = None,
        entry_period_event_id: Optional[str] = None,
        ranking_rewards: Optional[List[RankingReward]] = None,
        access_period_event_id: Optional[str] = None,
    ):
        self.metadata = metadata
        self.minimum_value = minimum_value
        self.maximum_value = maximum_value
        self.entry_period_event_id = entry_period_event_id
        self.ranking_rewards = ranking_rewards
        self.access_period_event_id = access_period_event_id

