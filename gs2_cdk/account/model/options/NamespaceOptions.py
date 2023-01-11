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
    create_account_script: Optional[ScriptSetting]
    authentication_script: Optional[ScriptSetting]
    create_take_over_script: Optional[ScriptSetting]
    do_take_over_script: Optional[ScriptSetting]
    log_setting: Optional[LogSetting]
    
    def __init__(
        self,
        description: Optional[str] = None,
        create_account_script: Optional[ScriptSetting] = None,
        authentication_script: Optional[ScriptSetting] = None,
        create_take_over_script: Optional[ScriptSetting] = None,
        do_take_over_script: Optional[ScriptSetting] = None,
        log_setting: Optional[LogSetting] = None,
    ):
        self.description = description
        self.create_account_script = create_account_script
        self.authentication_script = authentication_script
        self.create_take_over_script = create_take_over_script
        self.do_take_over_script = do_take_over_script
        self.log_setting = log_setting

