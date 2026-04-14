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
from .options.TimeseriesMetadataOptions import TimeseriesMetadataOptions


class TimeseriesMetadata:
    keys: Optional[List[str]] = None
    group_by: Optional[List[str]] = None

    def __init__(
        self,
        options: Optional[TimeseriesMetadataOptions] = TimeseriesMetadataOptions(),
    ):
        self.keys = options.keys if options.keys else None
        self.group_by = options.group_by if options.group_by else None

    def properties(
        self,
    ) -> Dict[str, Any]:
        properties: Dict[str, Any] = {}

        if self.keys is not None:
            properties["keys"] = self.keys
        if self.group_by is not None:
            properties["groupBy"] = self.group_by

        return properties
