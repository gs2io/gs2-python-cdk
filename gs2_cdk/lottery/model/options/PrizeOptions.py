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
from ..enums.PrizeType import PrizeType


class PrizeOptions:
    acquire_actions: Optional[List[AcquireAction]]
    drawn_limit: Optional[int]
    limit_fail_over_prize_id: Optional[str]
    prize_table_name: Optional[str]
    
    def __init__(
        self,
        acquire_actions: Optional[List[AcquireAction]] = None,
        drawn_limit: Optional[int] = None,
        limit_fail_over_prize_id: Optional[str] = None,
        prize_table_name: Optional[str] = None,
    ):
        self.acquire_actions = acquire_actions
        self.drawn_limit = drawn_limit
        self.limit_fail_over_prize_id = limit_fail_over_prize_id
        self.prize_table_name = prize_table_name

