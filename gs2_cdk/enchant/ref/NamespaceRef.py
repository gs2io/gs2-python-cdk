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
from .BalanceParameterModelRef import BalanceParameterModelRef
from .RarityParameterModelRef import RarityParameterModelRef
from ..stamp_sheet.ReDrawBalanceParameterStatusByUserId import ReDrawBalanceParameterStatusByUserId
from ..stamp_sheet.ReDrawRarityParameterStatusByUserId import ReDrawRarityParameterStatusByUserId
from ..stamp_sheet.AddRarityParameterStatusByUserId import AddRarityParameterStatusByUserId
from ..stamp_sheet.VerifyRarityParameterStatusByUserId import VerifyRarityParameterStatusByUserId


class NamespaceRef:
    namespace_name: str

    def __init__(
        self,
        namespace_name: str,
    ):
        self.namespace_name = namespace_name

    def balance_parameter_model(
        self,
        parameter_name: str,
    ) -> BalanceParameterModelRef:
        return BalanceParameterModelRef(
            self.namespace_name,
            parameter_name,
        )

    def rarity_parameter_model(
        self,
        parameter_name: str,
    ) -> RarityParameterModelRef:
        return RarityParameterModelRef(
            self.namespace_name,
            parameter_name,
        )

    def re_draw_balance_parameter_status(
        self,
        parameter_name: str,
        property_id: str,
        fixed_parameter_names: Optional[List[str]] = None,
        user_id: Optional[str] = "#{userId}",
    ) -> ReDrawBalanceParameterStatusByUserId:
        return ReDrawBalanceParameterStatusByUserId(
            self.namespace_name,
            parameter_name,
            property_id,
            fixed_parameter_names,
            user_id,
        )

    def re_draw_rarity_parameter_status(
        self,
        parameter_name: str,
        property_id: str,
        fixed_parameter_names: Optional[List[str]] = None,
        user_id: Optional[str] = "#{userId}",
    ) -> ReDrawRarityParameterStatusByUserId:
        return ReDrawRarityParameterStatusByUserId(
            self.namespace_name,
            parameter_name,
            property_id,
            fixed_parameter_names,
            user_id,
        )

    def add_rarity_parameter_status(
        self,
        parameter_name: str,
        property_id: str,
        count: int,
        user_id: Optional[str] = "#{userId}",
    ) -> AddRarityParameterStatusByUserId:
        return AddRarityParameterStatusByUserId(
            self.namespace_name,
            parameter_name,
            property_id,
            count,
            user_id,
        )

    def verify_rarity_parameter_status(
        self,
        parameter_name: str,
        property_id: str,
        verify_type: str,
        parameter_value_name: str,
        parameter_count: int,
        user_id: Optional[str] = "#{userId}",
    ) -> VerifyRarityParameterStatusByUserId:
        return VerifyRarityParameterStatusByUserId(
            self.namespace_name,
            parameter_name,
            property_id,
            verify_type,
            parameter_value_name,
            parameter_count,
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
                "enchant",
                self.namespace_name,
            ],
        ).str(
        )