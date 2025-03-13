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


class AppleAppStoreSettingOptions:
    bundle_id: Optional[str]
    shared_secret_key: Optional[str]
    issuer_id: Optional[str]
    key_id: Optional[str]
    private_key_pem: Optional[str]
    
    def __init__(
        self,
        bundle_id: Optional[str] = None,
        shared_secret_key: Optional[str] = None,
        issuer_id: Optional[str] = None,
        key_id: Optional[str] = None,
        private_key_pem: Optional[str] = None,
    ):
        self.bundle_id = bundle_id
        self.shared_secret_key = shared_secret_key
        self.issuer_id = issuer_id
        self.key_id = key_id
        self.private_key_pem = private_key_pem

