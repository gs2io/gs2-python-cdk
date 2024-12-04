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
from ..VerifyActionResult import VerifyActionResult
from ..ConsumeActionResult import ConsumeActionResult
from ..AcquireActionResult import AcquireActionResult


class TransactionResultOptions:
    verify_results: Optional[List[VerifyActionResult]]
    consume_results: Optional[List[ConsumeActionResult]]
    acquire_results: Optional[List[AcquireActionResult]]
    
    def __init__(
        self,
        verify_results: Optional[List[VerifyActionResult]] = None,
        consume_results: Optional[List[ConsumeActionResult]] = None,
        acquire_results: Optional[List[AcquireActionResult]] = None,
    ):
        self.verify_results = verify_results
        self.consume_results = consume_results
        self.acquire_results = acquire_results

