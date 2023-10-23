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
    rank_cap_script_id: Optional[str]
    change_experience_script: Optional[ScriptSetting]
    change_rank_script: Optional[ScriptSetting]
    change_rank_cap_script: Optional[ScriptSetting]
    overflow_experience_script: Optional[str]
    log_setting: Optional[LogSetting]
    
    def __init__(
        self,
        description: Optional[str] = None,
        transaction_setting: Optional[TransactionSetting] = None,
        rank_cap_script_id: Optional[str] = None,
        change_experience_script: Optional[ScriptSetting] = None,
        change_rank_script: Optional[ScriptSetting] = None,
        change_rank_cap_script: Optional[ScriptSetting] = None,
        overflow_experience_script: Optional[str] = None,
        log_setting: Optional[LogSetting] = None,
    ):
        self.description = description
        self.transaction_setting = transaction_setting
        self.rank_cap_script_id = rank_cap_script_id
        self.change_experience_script = change_experience_script
        self.change_rank_script = change_rank_script
        self.change_rank_cap_script = change_rank_cap_script
        self.overflow_experience_script = overflow_experience_script
        self.log_setting = log_setting

