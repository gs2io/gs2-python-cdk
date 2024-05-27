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
from ..FixedTiming import FixedTiming
from ..Scope import Scope


class GlobalRankingSettingOptions:
    calculate_fixed_timing: Optional[FixedTiming]
    additional_scopes: Optional[List[Scope]]
    ignore_user_ids: Optional[List[str]]
    generation: Optional[str]
    
    def __init__(
        self,
        calculate_fixed_timing: Optional[FixedTiming] = None,
        additional_scopes: Optional[List[Scope]] = None,
        ignore_user_ids: Optional[List[str]] = None,
        generation: Optional[str] = None,
    ):
        self.calculate_fixed_timing = calculate_fixed_timing
        self.additional_scopes = additional_scopes
        self.ignore_user_ids = ignore_user_ids
        self.generation = generation

