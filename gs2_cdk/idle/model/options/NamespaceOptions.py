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
from ....core.model import TransactionSetting
from ....core.model import ScriptSetting
from ....core.model import LogSetting


class NamespaceOptions:
    description: Optional[str]
    transaction_setting: Optional[TransactionSetting]
    receive_script: Optional[ScriptSetting]
    override_acquire_actions_script_id: Optional[str]
    log_setting: Optional[LogSetting]
    
    def __init__(
        self,
        description: Optional[str] = None,
        transaction_setting: Optional[TransactionSetting] = None,
        receive_script: Optional[ScriptSetting] = None,
        override_acquire_actions_script_id: Optional[str] = None,
        log_setting: Optional[LogSetting] = None,
    ):
        self.description = description
        self.transaction_setting = transaction_setting
        self.receive_script = receive_script
        self.override_acquire_actions_script_id = override_acquire_actions_script_id
        self.log_setting = log_setting

