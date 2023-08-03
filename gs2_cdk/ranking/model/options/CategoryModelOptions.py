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
from ..Scope import Scope
from ..enum.CategoryModelOrderDirection import CategoryModelOrderDirection
from ..enum.CategoryModelScope import CategoryModelScope


class CategoryModelOptions:
    metadata: Optional[str]
    minimum_value: Optional[int]
    maximum_value: Optional[int]
    sum: Optional[bool]
    calculate_fixed_timing_hour: Optional[int]
    calculate_fixed_timing_minute: Optional[int]
    calculate_interval_minutes: Optional[int]
    additional_scopes: Optional[List[Scope]]
    entry_period_event_id: Optional[str]
    access_period_event_id: Optional[str]
    ignore_user_ids: Optional[List[str]]
    generation: Optional[str]
    
    def __init__(
        self,
        metadata: Optional[str] = None,
        minimum_value: Optional[int] = None,
        maximum_value: Optional[int] = None,
        sum: Optional[bool] = None,
        calculate_fixed_timing_hour: Optional[int] = None,
        calculate_fixed_timing_minute: Optional[int] = None,
        calculate_interval_minutes: Optional[int] = None,
        additional_scopes: Optional[List[Scope]] = None,
        entry_period_event_id: Optional[str] = None,
        access_period_event_id: Optional[str] = None,
        ignore_user_ids: Optional[List[str]] = None,
        generation: Optional[str] = None,
    ):
        self.metadata = metadata
        self.minimum_value = minimum_value
        self.maximum_value = maximum_value
        self.sum = sum
        self.calculate_fixed_timing_hour = calculate_fixed_timing_hour
        self.calculate_fixed_timing_minute = calculate_fixed_timing_minute
        self.calculate_interval_minutes = calculate_interval_minutes
        self.additional_scopes = additional_scopes
        self.entry_period_event_id = entry_period_event_id
        self.access_period_event_id = access_period_event_id
        self.ignore_user_ids = ignore_user_ids
        self.generation = generation

