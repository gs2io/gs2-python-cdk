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
from .options.LogEntryOptions import LogEntryOptions
from .enums.LogEntryStatus import LogEntryStatus


class LogEntry:
    timestamp: int
    status: LogEntryStatus
    duration: int
    line: str
    labels: Optional[List[Label]] = None

    def __init__(
        self,
        timestamp: int,
        status: LogEntryStatus,
        duration: int,
        line: str,
        options: Optional[LogEntryOptions] = LogEntryOptions(),
    ):
        self.timestamp = timestamp
        self.status = status
        self.duration = duration
        self.line = line
        self.labels = options.labels if options.labels else None

    def properties(
        self,
    ) -> Dict[str, Any]:
        properties: Dict[str, Any] = {}

        if self.timestamp is not None:
            properties["timestamp"] = self.timestamp
        if self.status is not None:
            properties["status"] = self.status.value
        if self.duration is not None:
            properties["duration"] = self.duration
        if self.line is not None:
            properties["line"] = self.line
        if self.labels is not None:
            properties["labels"] = [
                v.properties(
                )
                for v in self.labels
            ]

        return properties
