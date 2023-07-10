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
#
# deny overwrite
from __future__ import annotations
from typing import *
from ..enum.LotteryModelMode import LotteryModelMode
from ..enum.LotteryModelMethod import LotteryModelMethod


class LotteryModelOptions:
    metadata: Optional[str]
    prize_table_name: Optional[str]
    choice_prize_table_script_id: Optional[str]
    
    def __init__(
        self,
        metadata: Optional[str] = None,
        prize_table_name: Optional[str] = None,
        choice_prize_table_script_id: Optional[str] = None,
    ):
        self.metadata = metadata
        self.prize_table_name = prize_table_name
        self.choice_prize_table_script_id = choice_prize_table_script_id

