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
from ..stamp_sheet.AddMoldCapacityByUserId import AddMoldCapacityByUserId
from ..stamp_sheet.SetMoldCapacityByUserId import SetMoldCapacityByUserId
from ..stamp_sheet.AcquireActionsToFormProperties import AcquireActionsToFormProperties
from ...core.model import AcquireAction
from ..model.AcquireActionConfig import AcquireActionConfig


class MoldModelRef:
    namespace_name: str
    mold_name: str

    def __init__(
        self,
        namespace_name: str,
        mold_name: str,
    ):
        self.namespace_name = namespace_name
        self.mold_name = mold_name

    def add_mold_capacity(
        self,
        capacity: int,
        user_id: Optional[str] = "#{userId}",
    ) -> AddMoldCapacityByUserId:
        return AddMoldCapacityByUserId(
            self.namespace_name,
            self.mold_name,
            capacity,
            user_id,
        )

    def set_mold_capacity(
        self,
        capacity: int,
        user_id: Optional[str] = "#{userId}",
    ) -> SetMoldCapacityByUserId:
        return SetMoldCapacityByUserId(
            self.namespace_name,
            self.mold_name,
            capacity,
            user_id,
        )

    def acquire_actions_to_form_properties(
        self,
        index: int,
        acquire_action: AcquireAction,
        config: Optional[List[AcquireActionConfig]] = None,
        user_id: Optional[str] = "#{userId}",
    ) -> AcquireActionsToFormProperties:
        return AcquireActionsToFormProperties(
            self.namespace_name,
            self.mold_name,
            index,
            acquire_action,
            config,
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
                "formation",
                self.namespace_name,
                "model",
                "mold",
                self.mold_name,
            ],
        ).str(
        )
