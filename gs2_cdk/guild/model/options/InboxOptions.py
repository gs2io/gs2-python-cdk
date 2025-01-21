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
from ..ReceiveMemberRequest import ReceiveMemberRequest


class InboxOptions:
    from_user_ids: Optional[List[str]]
    receive_member_requests: Optional[List[ReceiveMemberRequest]]
    revision: Optional[int]
    
    def __init__(
        self,
        from_user_ids: Optional[List[str]] = None,
        receive_member_requests: Optional[List[ReceiveMemberRequest]] = None,
        revision: Optional[int] = None,
    ):
        self.from_user_ids = from_user_ids
        self.receive_member_requests = receive_member_requests
        self.revision = revision

