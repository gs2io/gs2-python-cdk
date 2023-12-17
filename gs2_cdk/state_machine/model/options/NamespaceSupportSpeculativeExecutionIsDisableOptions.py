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
from ....core.model import TransactionSetting
from ....core.model import ScriptSetting
from ....core.model import LogSetting
from ..enum.NamespaceSupportSpeculativeExecution import NamespaceSupportSpeculativeExecution


class NamespaceSupportSpeculativeExecutionIsDisableOptions:
    description: Optional[str]
    transaction_setting: Optional[TransactionSetting]
    start_script: Optional[ScriptSetting]
    pass_script: Optional[ScriptSetting]
    error_script: Optional[ScriptSetting]
    lowest_state_machine_version: Optional[int]
    log_setting: Optional[LogSetting]
    revision: Optional[int]
    
    def __init__(
        self,
        description: Optional[str] = None,
        transaction_setting: Optional[TransactionSetting] = None,
        start_script: Optional[ScriptSetting] = None,
        pass_script: Optional[ScriptSetting] = None,
        error_script: Optional[ScriptSetting] = None,
        lowest_state_machine_version: Optional[int] = None,
        log_setting: Optional[LogSetting] = None,
        revision: Optional[int] = None,
    ):
        self.description = description
        self.transaction_setting = transaction_setting
        self.start_script = start_script
        self.pass_script = pass_script
        self.error_script = error_script
        self.lowest_state_machine_version = lowest_state_machine_version
        self.log_setting = log_setting
        self.revision = revision
