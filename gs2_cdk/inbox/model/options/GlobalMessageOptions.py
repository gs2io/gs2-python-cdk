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
from ..TimeSpan import TimeSpan


class GlobalMessageOptions:
    read_acquire_actions: Optional[List[AcquireAction]]
    expires_time_span: Optional[TimeSpan]
    expires_at: Optional[int]
    message_reception_period_event_id: Optional[str]
    
    def __init__(
        self,
        read_acquire_actions: Optional[List[AcquireAction]] = None,
        expires_time_span: Optional[TimeSpan] = None,
        expires_at: Optional[int] = None,
        message_reception_period_event_id: Optional[str] = None,
    ):
        self.read_acquire_actions = read_acquire_actions
        self.expires_time_span = expires_time_span
        self.expires_at = expires_at
        self.message_reception_period_event_id = message_reception_period_event_id

