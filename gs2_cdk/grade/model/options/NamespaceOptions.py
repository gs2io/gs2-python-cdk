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
from ..TransactionSettingV2 import TransactionSettingV2
from ....core.model import ScriptSetting
from ....core.model import LogSetting


class NamespaceOptions:
    description: Optional[str]
    # @deprecated
    transaction_setting: Optional[TransactionSetting]
    transaction_setting_v2: Optional[TransactionSettingV2]
    change_grade_script: Optional[ScriptSetting]
    log_setting: Optional[LogSetting]
    
    def __init__(
        self,
        description: Optional[str] = None,
        transaction_setting: Optional[TransactionSetting] = None,
        transaction_setting_v2: Optional[TransactionSettingV2] = None,
        change_grade_script: Optional[ScriptSetting] = None,
        log_setting: Optional[LogSetting] = None,
    ):
        self.description = description
        self.transaction_setting = transaction_setting
        self.transaction_setting_v2 = transaction_setting_v2
        self.change_grade_script = change_grade_script
        self.log_setting = log_setting

