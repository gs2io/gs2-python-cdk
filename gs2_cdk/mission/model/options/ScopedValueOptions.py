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
from ..enums.ScopedValueScopeType import ScopedValueScopeType
from ..enums.ScopedValueResetType import ScopedValueResetType


class ScopedValueOptions:
    reset_type: Optional[ScopedValueResetType]
    condition_name: Optional[str]
    next_reset_at: Optional[int]
    
    def __init__(
        self,
        reset_type: Optional[ScopedValueResetType] = None,
        condition_name: Optional[str] = None,
        next_reset_at: Optional[int] = None,
    ):
        self.reset_type = reset_type
        self.condition_name = condition_name
        self.next_reset_at = next_reset_at

