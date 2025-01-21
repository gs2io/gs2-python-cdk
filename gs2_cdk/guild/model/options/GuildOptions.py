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

from ....core.model import CdkResource, Stack
from ....core.func import GetAttr
from ..RoleModel import RoleModel


class GuildOptions:
    attribute1: Optional[int]
    attribute2: Optional[int]
    attribute3: Optional[int]
    attribute4: Optional[int]
    attribute5: Optional[int]
    metadata: Optional[str]
    member_metadata: Optional[str]
    custom_roles: Optional[List[RoleModel]]
    guild_member_default_role: Optional[str]
    time_offset_token: Optional[str]
    
    def __init__(
        self,
        attribute1: Optional[int] = None,
        attribute2: Optional[int] = None,
        attribute3: Optional[int] = None,
        attribute4: Optional[int] = None,
        attribute5: Optional[int] = None,
        metadata: Optional[str] = None,
        member_metadata: Optional[str] = None,
        custom_roles: Optional[List[RoleModel]] = None,
        guild_member_default_role: Optional[str] = None,
        time_offset_token: Optional[str] = None,
    ):
        self.attribute1 = attribute1
        self.attribute2 = attribute2
        self.attribute3 = attribute3
        self.attribute4 = attribute4
        self.attribute5 = attribute5
        self.metadata = metadata
        self.member_metadata = member_metadata
        self.custom_roles = custom_roles
        self.guild_member_default_role = guild_member_default_role
        self.time_offset_token = time_offset_token

