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
from .options.UserDataEntryOptions import UserDataEntryOptions


class UserDataEntry:
    service: str
    namespace_name: str
    kind: str
    payload: str

    def __init__(
        self,
        service: str,
        namespace_name: str,
        kind: str,
        payload: str,
        options: Optional[UserDataEntryOptions] = UserDataEntryOptions(),
    ):
        self.service = service
        self.namespace_name = namespace_name
        self.kind = kind
        self.payload = payload

    def properties(
        self,
    ) -> Dict[str, Any]:
        properties: Dict[str, Any] = {}

        if self.service is not None:
            properties["service"] = self.service
        if self.namespace_name is not None:
            properties["namespaceName"] = self.namespace_name
        if self.kind is not None:
            properties["kind"] = self.kind
        if self.payload is not None:
            properties["payload"] = self.payload

        return properties
