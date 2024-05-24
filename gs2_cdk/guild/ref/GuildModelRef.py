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

from ...core.func import GetAttr, Join
from .RoleModelRef import RoleModelRef
from ..stamp_sheet.IncreaseMaximumCurrentMaximumMemberCountByGuildName import IncreaseMaximumCurrentMaximumMemberCountByGuildName
from ..stamp_sheet.SetMaximumCurrentMaximumMemberCountByGuildName import SetMaximumCurrentMaximumMemberCountByGuildName
from ..stamp_sheet.DecreaseMaximumCurrentMaximumMemberCountByGuildName import DecreaseMaximumCurrentMaximumMemberCountByGuildName


class GuildModelRef:
    namespace_name: str
    guild_model_name: str

    def __init__(
        self,
        namespace_name: str,
        guild_model_name: str,
    ):
        self.namespace_name = namespace_name
        self.guild_model_name = guild_model_name

    def role_model(
        self,
    ) -> RoleModelRef:
        return RoleModelRef(
            self.namespace_name,
            self.guild_model_name,
        )

    def increase_maximum_current_maximum_member_count_by_guild_name(
        self,
        guild_name: str,
        value: Optional[int] = None,
    ) -> IncreaseMaximumCurrentMaximumMemberCountByGuildName:
        return IncreaseMaximumCurrentMaximumMemberCountByGuildName(
            self.namespace_name,
            self.guild_model_name,
            guild_name,
            value,
        )

    def set_maximum_current_maximum_member_count_by_guild_name(
        self,
        guild_name: str,
        value: Optional[int] = None,
    ) -> SetMaximumCurrentMaximumMemberCountByGuildName:
        return SetMaximumCurrentMaximumMemberCountByGuildName(
            self.namespace_name,
            guild_name,
            self.guild_model_name,
            value,
        )

    def decrease_maximum_current_maximum_member_count_by_guild_name(
        self,
        guild_name: str,
        value: Optional[int] = None,
    ) -> DecreaseMaximumCurrentMaximumMemberCountByGuildName:
        return DecreaseMaximumCurrentMaximumMemberCountByGuildName(
            self.namespace_name,
            self.guild_model_name,
            guild_name,
            value,
        )

    def grn(
        self,
    ) -> str:
        return Join(
            ":",
            [
                "grn",
                "gs2",
                GetAttr.region(
                ).str(
                ),
                GetAttr.owner_id(
                ).str(
                ),
                "guild",
                self.namespace_name,
                "model",
                self.guild_model_name,
            ],
        ).str(
        )
