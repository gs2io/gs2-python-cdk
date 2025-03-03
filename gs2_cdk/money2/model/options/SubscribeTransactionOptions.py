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
from ..enums.SubscribeTransactionStore import SubscribeTransactionStore
from ..enums.SubscribeTransactionStatusDetail import SubscribeTransactionStatusDetail


class SubscribeTransactionOptions:
    user_id: Optional[str]
    last_allocated_at: Optional[int]
    last_take_over_at: Optional[int]
    revision: Optional[int]
    
    def __init__(
        self,
        user_id: Optional[str] = None,
        last_allocated_at: Optional[int] = None,
        last_take_over_at: Optional[int] = None,
        revision: Optional[int] = None,
    ):
        self.user_id = user_id
        self.last_allocated_at = last_allocated_at
        self.last_take_over_at = last_take_over_at
        self.revision = revision

