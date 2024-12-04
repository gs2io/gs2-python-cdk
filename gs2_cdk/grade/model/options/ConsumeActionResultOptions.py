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


class ConsumeActionResultOptions:
    status_code: Optional[int]
    consume_result: Optional[str]
    
    def __init__(
        self,
        status_code: Optional[int] = None,
        consume_result: Optional[str] = None,
    ):
        self.status_code = status_code
        self.consume_result = consume_result

