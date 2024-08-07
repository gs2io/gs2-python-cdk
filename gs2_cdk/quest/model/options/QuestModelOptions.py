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
from ..Contents import Contents
from ....core.model import VerifyAction
from ....core.model import ConsumeAction


class QuestModelOptions:
    metadata: Optional[str]
    challenge_period_event_id: Optional[str]
    first_complete_acquire_actions: Optional[List[AcquireAction]]
    verify_actions: Optional[List[VerifyAction]]
    consume_actions: Optional[List[ConsumeAction]]
    failed_acquire_actions: Optional[List[AcquireAction]]
    premise_quest_names: Optional[List[str]]
    
    def __init__(
        self,
        metadata: Optional[str] = None,
        challenge_period_event_id: Optional[str] = None,
        first_complete_acquire_actions: Optional[List[AcquireAction]] = None,
        verify_actions: Optional[List[VerifyAction]] = None,
        consume_actions: Optional[List[ConsumeAction]] = None,
        failed_acquire_actions: Optional[List[AcquireAction]] = None,
        premise_quest_names: Optional[List[str]] = None,
    ):
        self.metadata = metadata
        self.challenge_period_event_id = challenge_period_event_id
        self.first_complete_acquire_actions = first_complete_acquire_actions
        self.verify_actions = verify_actions
        self.consume_actions = consume_actions
        self.failed_acquire_actions = failed_acquire_actions
        self.premise_quest_names = premise_quest_names

