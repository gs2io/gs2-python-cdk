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
from ....core.model import VerifyAction
from ....core.model import ConsumeAction
from ....core.model import AcquireAction


class NodeModelOptions:
    metadata: Optional[str]
    release_verify_actions: Optional[List[VerifyAction]]
    return_acquire_actions: Optional[List[AcquireAction]]
    premise_node_names: Optional[List[str]]
    
    def __init__(
        self,
        metadata: Optional[str] = None,
        release_verify_actions: Optional[List[VerifyAction]] = None,
        return_acquire_actions: Optional[List[AcquireAction]] = None,
        premise_node_names: Optional[List[str]] = None,
    ):
        self.metadata = metadata
        self.release_verify_actions = release_verify_actions
        self.return_acquire_actions = return_acquire_actions
        self.premise_node_names = premise_node_names

