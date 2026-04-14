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
from .Label import Label
from .LogEntry import LogEntry
from .options.TraceOptions import TraceOptions


class Trace:
    truncated: bool
    spans: Optional[List[LogEntry]] = None

    def __init__(
        self,
        truncated: bool,
        options: Optional[TraceOptions] = TraceOptions(),
    ):
        self.truncated = truncated
        self.spans = options.spans if options.spans else None

    def properties(
        self,
    ) -> Dict[str, Any]:
        properties: Dict[str, Any] = {}

        if self.spans is not None:
            properties["spans"] = [
                v.properties(
                )
                for v in self.spans
            ]
        if self.truncated is not None:
            properties["truncated"] = self.truncated

        return properties
