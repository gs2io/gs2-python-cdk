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
from .options.MobileNotificationMessageOptions import MobileNotificationMessageOptions


class MobileNotificationMessage:
    locale: Optional[str] = None
    title: Optional[str] = None
    message: Optional[str] = None

    def __init__(
        self,
        options: Optional[MobileNotificationMessageOptions] = MobileNotificationMessageOptions(),
    ):
        self.locale = options.locale if options.locale else None
        self.title = options.title if options.title else None
        self.message = options.message if options.message else None

    def properties(
        self,
    ) -> Dict[str, Any]:
        properties: Dict[str, Any] = {}

        if self.locale is not None:
            properties["locale"] = self.locale
        if self.title is not None:
            properties["title"] = self.title
        if self.message is not None:
            properties["message"] = self.message

        return properties
