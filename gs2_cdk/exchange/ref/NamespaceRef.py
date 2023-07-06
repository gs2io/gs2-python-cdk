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
from .RateModelRef import RateModelRef
from ..stamp_sheet.ExchangeByUserId import ExchangeByUserId
from ...core.model import Config
from ..stamp_sheet.CreateAwaitByUserId import CreateAwaitByUserId
from ..stamp_sheet.DeleteAwaitByUserId import DeleteAwaitByUserId


class NamespaceRef:
    namespace_name: str

    def __init__(
        self,
        namespace_name: str,
    ):
        self.namespace_name = namespace_name

    def rate_model(
        self,
        rate_name: str,
    ) -> RateModelRef:
        return RateModelRef(
            self.namespace_name,
            rate_name,
        )

    def exchange(
        self,
        rate_name: str,
        count: int,
        config: Optional[List[Config]] = None,
        user_id: Optional[str] = "#{userId}",
    ) -> ExchangeByUserId:
        return ExchangeByUserId(
            self.namespace_name,
            rate_name,
            count,
            config,
            user_id,
        )

    def create_await(
        self,
        rate_name: str,
        count: int,
        user_id: Optional[str] = "#{userId}",
    ) -> CreateAwaitByUserId:
        return CreateAwaitByUserId(
            self.namespace_name,
            rate_name,
            count,
            user_id,
        )

    def delete_await(
        self,
        await_name: str,
        user_id: Optional[str] = "#{userId}",
    ) -> DeleteAwaitByUserId:
        return DeleteAwaitByUserId(
            self.namespace_name,
            await_name,
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
                "exchange",
                self.namespace_name,
            ],
        ).str(
        )
