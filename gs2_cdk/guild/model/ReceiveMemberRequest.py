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
from .options.ReceiveMemberRequestOptions import ReceiveMemberRequestOptions


class ReceiveMemberRequest:
    user_id: str
    target_guild_name: str
    metadata: Optional[str] = None

    def __init__(
        self,
        user_id: str,
        target_guild_name: str,
        options: Optional[ReceiveMemberRequestOptions] = ReceiveMemberRequestOptions(),
    ):
        self.user_id = user_id
        self.target_guild_name = target_guild_name
        self.metadata = options.metadata if options.metadata else None

    def properties(
        self,
    ) -> Dict[str, Any]:
        properties: Dict[str, Any] = {}

        if self.user_id is not None:
            properties["userId"] = self.user_id
        if self.target_guild_name is not None:
            properties["targetGuildName"] = self.target_guild_name
        if self.metadata is not None:
            properties["metadata"] = self.metadata

        return properties
