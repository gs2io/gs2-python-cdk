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
from ..MaxStaminaTable import MaxStaminaTable
from ..RecoverIntervalTable import RecoverIntervalTable
from ..RecoverValueTable import RecoverValueTable


class StaminaModelOptions:
    metadata: Optional[str]
    max_capacity: Optional[int]
    max_stamina_table: Optional[MaxStaminaTable]
    recover_interval_table: Optional[RecoverIntervalTable]
    recover_value_table: Optional[RecoverValueTable]
    
    def __init__(
        self,
        metadata: Optional[str] = None,
        max_capacity: Optional[int] = None,
        max_stamina_table: Optional[MaxStaminaTable] = None,
        recover_interval_table: Optional[RecoverIntervalTable] = None,
        recover_value_table: Optional[RecoverValueTable] = None,
    ):
        self.metadata = metadata
        self.max_capacity = max_capacity
        self.max_stamina_table = max_stamina_table
        self.recover_interval_table = recover_interval_table
        self.recover_value_table = recover_value_table

