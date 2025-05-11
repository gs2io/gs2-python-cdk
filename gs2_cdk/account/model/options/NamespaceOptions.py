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
    change_password_if_take_over: Optional[bool]
    different_user_id_for_login_and_data_retention: Optional[bool]
    create_account_script: Optional[ScriptSetting]
    authentication_script: Optional[ScriptSetting]
    create_take_over_script: Optional[ScriptSetting]
    do_take_over_script: Optional[ScriptSetting]
    ban_script: Optional[ScriptSetting]
    un_ban_script: Optional[ScriptSetting]
    log_setting: Optional[LogSetting]
    
    def __init__(
        self,
        description: Optional[str] = None,
        change_password_if_take_over: Optional[bool] = None,
        different_user_id_for_login_and_data_retention: Optional[bool] = None,
        create_account_script: Optional[ScriptSetting] = None,
        authentication_script: Optional[ScriptSetting] = None,
        create_take_over_script: Optional[ScriptSetting] = None,
        do_take_over_script: Optional[ScriptSetting] = None,
        ban_script: Optional[ScriptSetting] = None,
        un_ban_script: Optional[ScriptSetting] = None,
        log_setting: Optional[LogSetting] = None,
    ):
        self.description = description
        self.change_password_if_take_over = change_password_if_take_over
        self.different_user_id_for_login_and_data_retention = different_user_id_for_login_and_data_retention
        self.create_account_script = create_account_script
        self.authentication_script = authentication_script
        self.create_take_over_script = create_take_over_script
        self.do_take_over_script = do_take_over_script
        self.ban_script = ban_script
        self.un_ban_script = un_ban_script
        self.log_setting = log_setting

