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

from ....core.model import CdkResource, Stack
from ....core.func import GetAttr
from ....core.model import ScriptSetting
from ....core.model import LogSetting


class NamespaceOptions:
    description: Optional[str]
    apple_key: Optional[str]
    google_key: Optional[str]
    enable_fake_receipt: Optional[bool]
    create_wallet_script: Optional[ScriptSetting]
    deposit_script: Optional[ScriptSetting]
    withdraw_script: Optional[ScriptSetting]
    log_setting: Optional[LogSetting]
    
    def __init__(
        self,
        description: Optional[str] = None,
        apple_key: Optional[str] = None,
        google_key: Optional[str] = None,
        enable_fake_receipt: Optional[bool] = None,
        create_wallet_script: Optional[ScriptSetting] = None,
        deposit_script: Optional[ScriptSetting] = None,
        withdraw_script: Optional[ScriptSetting] = None,
        log_setting: Optional[LogSetting] = None,
    ):
        self.description = description
        self.apple_key = apple_key
        self.google_key = google_key
        self.enable_fake_receipt = enable_fake_receipt
        self.create_wallet_script = create_wallet_script
        self.deposit_script = deposit_script
        self.withdraw_script = withdraw_script
        self.log_setting = log_setting

