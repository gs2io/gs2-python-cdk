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
from ..Version import Version
from ..enum.VersionModelScope import VersionModelScope


class VersionModelOptions:
    metadata: Optional[str]
    current_version: Optional[Version]
    need_signature: Optional[bool]
    signature_key_id: Optional[str]
    
    def __init__(
        self,
        metadata: Optional[str] = None,
        current_version: Optional[Version] = None,
        need_signature: Optional[bool] = None,
        signature_key_id: Optional[str] = None,
    ):
        self.metadata = metadata
        self.current_version = current_version
        self.need_signature = need_signature
        self.signature_key_id = signature_key_id

