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
from .FacetValueCount import FacetValueCount
from .NumericRange import NumericRange
from .options.FacetOptions import FacetOptions


class Facet:
    field: str
    values: Optional[List[FacetValueCount]] = None
    range: Optional[NumericRange] = None
    global_range: Optional[NumericRange] = None

    def __init__(
        self,
        field: str,
        options: Optional[FacetOptions] = FacetOptions(),
    ):
        self.field = field
        self.values = options.values if options.values else None
        self.range = options.range if options.range else None
        self.global_range = options.global_range if options.global_range else None

    def properties(
        self,
    ) -> Dict[str, Any]:
        properties: Dict[str, Any] = {}

        if self.field is not None:
            properties["field"] = self.field
        if self.values is not None:
            properties["values"] = [
                v.properties(
                )
                for v in self.values
            ]
        if self.range is not None:
            properties["range"] = self.range.properties(
            )
        if self.global_range is not None:
            properties["globalRange"] = self.global_range.properties(
            )

        return properties
