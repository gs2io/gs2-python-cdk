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


class AccessTokenOptions:
    federation_from_user_id: Optional[str]
    federation_policy_document: Optional[str]
    
    def __init__(
        self,
        federation_from_user_id: Optional[str] = None,
        federation_policy_document: Optional[str] = None,
    ):
        self.federation_from_user_id = federation_from_user_id
        self.federation_policy_document = federation_policy_document

