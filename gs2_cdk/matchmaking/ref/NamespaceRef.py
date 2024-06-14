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
from .RatingModelRef import RatingModelRef
from .SeasonModelRef import SeasonModelRef
from ..stamp_sheet.VerifyIncludeParticipantByUserId import VerifyIncludeParticipantByUserId


class NamespaceRef:
    namespace_name: str

    def __init__(
        self,
        namespace_name: str,
    ):
        self.namespace_name = namespace_name

    def rating_model(
        self,
        rating_name: str,
    ) -> RatingModelRef:
        return RatingModelRef(
            self.namespace_name,
            rating_name,
        )

    def season_model(
        self,
        season_name: str,
    ) -> SeasonModelRef:
        return SeasonModelRef(
            self.namespace_name,
            season_name,
        )

    def verify_include_participant(
        self,
        season_name: str,
        season: int,
        tier: int,
        verify_type: str,
        season_gathering_name: Optional[str] = None,
        user_id: Optional[str] = "#{userId}",
    ) -> VerifyIncludeParticipantByUserId:
        return VerifyIncludeParticipantByUserId(
            self.namespace_name,
            season_name,
            season,
            tier,
            verify_type,
            season_gathering_name,
            user_id,
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
                "matchmaking",
                self.namespace_name,
            ],
        ).str(
        )
