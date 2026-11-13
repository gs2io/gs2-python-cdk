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
from .options.IssuedCodeSettingOptions import IssuedCodeSettingOptions


class IssuedCodeSetting:
    expires_days: int
    delete_on_use: bool
    max_failed_attempts: Optional[int] = None

    def __init__(
        self,
        expires_days: int,
        delete_on_use: bool,
        options: Optional[IssuedCodeSettingOptions] = IssuedCodeSettingOptions(),
    ):
        self.expires_days = expires_days
        self.delete_on_use = delete_on_use
        self.max_failed_attempts = options.max_failed_attempts if options.max_failed_attempts else None

    def properties(
        self,
    ) -> Dict[str, Any]:
        properties: Dict[str, Any] = {}

        if self.expires_days is not None:
            properties["expiresDays"] = self.expires_days
        if self.max_failed_attempts is not None:
            properties["maxFailedAttempts"] = self.max_failed_attempts
        if self.delete_on_use is not None:
            properties["deleteOnUse"] = self.delete_on_use

        return properties
