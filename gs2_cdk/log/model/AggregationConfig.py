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
from .options.AggregationConfigOptions import AggregationConfigOptions
from .enums.AggregationConfigType import AggregationConfigType


class AggregationConfig:
    type: Optional[AggregationConfigType] = None
    field: Optional[str] = None

    def __init__(
        self,
        options: Optional[AggregationConfigOptions] = AggregationConfigOptions(),
    ):
        self.type = options.type if options.type else None
        self.field = options.field if options.field else None

    def properties(
        self,
    ) -> Dict[str, Any]:
        properties: Dict[str, Any] = {}

        if self.type is not None:
            properties["type"] = self.type.value
        if self.field is not None:
            properties["field"] = self.field

        return properties
