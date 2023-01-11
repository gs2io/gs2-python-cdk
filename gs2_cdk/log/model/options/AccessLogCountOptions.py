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


class AccessLogCountOptions:
    service: Optional[str]
    method: Optional[str]
    user_id: Optional[str]
    
    def __init__(
        self,
        service: Optional[str] = None,
        method: Optional[str] = None,
        user_id: Optional[str] = None,
    ):
        self.service = service
        self.method = method
        self.user_id = user_id

