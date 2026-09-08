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
from .options.TransactionSettingV2Options import TransactionSettingV2Options


class TransactionSettingV2:
    distributor_namespace_id: str
    enable_parallel_execution: bool

    def __init__(
        self,
        distributor_namespace_id: str,
        enable_parallel_execution: bool,
        options: Optional[TransactionSettingV2Options] = TransactionSettingV2Options(),
    ):
        self.distributor_namespace_id = distributor_namespace_id
        self.enable_parallel_execution = enable_parallel_execution

    def properties(
        self,
    ) -> Dict[str, Any]:
        properties: Dict[str, Any] = {}

        if self.distributor_namespace_id is not None:
            properties["distributorNamespaceId"] = self.distributor_namespace_id
        if self.enable_parallel_execution is not None:
            properties["enableParallelExecution"] = self.enable_parallel_execution

        return properties
