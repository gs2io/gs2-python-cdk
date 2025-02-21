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
from ..enums.SubscribeRankingModelOrderDirection import SubscribeRankingModelOrderDirection


class SubscribeRankingModelOptions:
    metadata: Optional[str]
    minimum_value: Optional[int]
    maximum_value: Optional[int]
    entry_period_event_id: Optional[str]
    access_period_event_id: Optional[str]
    
    def __init__(
        self,
        metadata: Optional[str] = None,
        minimum_value: Optional[int] = None,
        maximum_value: Optional[int] = None,
        entry_period_event_id: Optional[str] = None,
        access_period_event_id: Optional[str] = None,
    ):
        self.metadata = metadata
        self.minimum_value = minimum_value
        self.maximum_value = maximum_value
        self.entry_period_event_id = entry_period_event_id
        self.access_period_event_id = access_period_event_id

