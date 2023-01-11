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


class DistributorModelOptions:
    metadata: Optional[str]
    inbox_namespace_id: Optional[str]
    white_list_target_ids: Optional[List[str]]
    
    def __init__(
        self,
        metadata: Optional[str] = None,
        inbox_namespace_id: Optional[str] = None,
        white_list_target_ids: Optional[List[str]] = None,
    ):
        self.metadata = metadata
        self.inbox_namespace_id = inbox_namespace_id
        self.white_list_target_ids = white_list_target_ids

