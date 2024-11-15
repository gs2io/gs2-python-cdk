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
from ..RoleModel import RoleModel


class GuildModelOptions:
    metadata: Optional[str]
    max_concurrent_join_guilds: Optional[int]
    max_concurrent_guild_master_count: Optional[int]
    
    def __init__(
        self,
        metadata: Optional[str] = None,
        max_concurrent_join_guilds: Optional[int] = None,
        max_concurrent_guild_master_count: Optional[int] = None,
    ):
        self.metadata = metadata
        self.max_concurrent_join_guilds = max_concurrent_join_guilds
        self.max_concurrent_guild_master_count = max_concurrent_guild_master_count

