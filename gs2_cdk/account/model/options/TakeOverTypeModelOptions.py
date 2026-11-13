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
from ..ScopeValue import ScopeValue
from ..OpenIdConnectSetting import OpenIdConnectSetting
from ..IssuedCodeSetting import IssuedCodeSetting
from ..enums.TakeOverTypeModelTakeOverMethod import TakeOverTypeModelTakeOverMethod


class TakeOverTypeModelOptions:
    metadata: Optional[str]
    open_id_connect_setting: Optional[OpenIdConnectSetting]
    issued_code_setting: Optional[IssuedCodeSetting]
    
    def __init__(
        self,
        metadata: Optional[str] = None,
        open_id_connect_setting: Optional[OpenIdConnectSetting] = None,
        issued_code_setting: Optional[IssuedCodeSetting] = None,
    ):
        self.metadata = metadata
        self.open_id_connect_setting = open_id_connect_setting
        self.issued_code_setting = issued_code_setting

