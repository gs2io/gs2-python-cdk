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
from ....core.model import ConsumeAction
from ....core.model import AcquireAction


class StampSheetResultOptions:
    task_requests: Optional[List[ConsumeAction]]
    task_result_codes: Optional[List[int]]
    task_results: Optional[List[str]]
    sheet_result_code: Optional[int]
    sheet_result: Optional[str]
    next_transaction_id: Optional[str]
    revision: Optional[int]
    
    def __init__(
        self,
        task_requests: Optional[List[ConsumeAction]] = None,
        task_result_codes: Optional[List[int]] = None,
        task_results: Optional[List[str]] = None,
        sheet_result_code: Optional[int] = None,
        sheet_result: Optional[str] = None,
        next_transaction_id: Optional[str] = None,
        revision: Optional[int] = None,
    ):
        self.task_requests = task_requests
        self.task_result_codes = task_result_codes
        self.task_results = task_results
        self.sheet_result_code = sheet_result_code
        self.sheet_result = sheet_result
        self.next_transaction_id = next_transaction_id
        self.revision = revision

