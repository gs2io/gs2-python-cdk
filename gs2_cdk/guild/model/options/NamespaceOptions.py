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
from ....core.model import NotificationSetting
from ....core.model import ScriptSetting
from ....core.model import LogSetting


class NamespaceOptions:
    description: Optional[str]
    change_notification: Optional[NotificationSetting]
    join_notification: Optional[NotificationSetting]
    leave_notification: Optional[NotificationSetting]
    change_member_notification: Optional[NotificationSetting]
    receive_request_notification: Optional[NotificationSetting]
    remove_request_notification: Optional[NotificationSetting]
    create_guild_script: Optional[ScriptSetting]
    update_guild_script: Optional[ScriptSetting]
    join_guild_script: Optional[ScriptSetting]
    leave_guild_script: Optional[ScriptSetting]
    change_role_script: Optional[ScriptSetting]
    delete_guild_script: Optional[ScriptSetting]
    log_setting: Optional[LogSetting]
    
    def __init__(
        self,
        description: Optional[str] = None,
        change_notification: Optional[NotificationSetting] = None,
        join_notification: Optional[NotificationSetting] = None,
        leave_notification: Optional[NotificationSetting] = None,
        change_member_notification: Optional[NotificationSetting] = None,
        receive_request_notification: Optional[NotificationSetting] = None,
        remove_request_notification: Optional[NotificationSetting] = None,
        create_guild_script: Optional[ScriptSetting] = None,
        update_guild_script: Optional[ScriptSetting] = None,
        join_guild_script: Optional[ScriptSetting] = None,
        leave_guild_script: Optional[ScriptSetting] = None,
        change_role_script: Optional[ScriptSetting] = None,
        delete_guild_script: Optional[ScriptSetting] = None,
        log_setting: Optional[LogSetting] = None,
    ):
        self.description = description
        self.change_notification = change_notification
        self.join_notification = join_notification
        self.leave_notification = leave_notification
        self.change_member_notification = change_member_notification
        self.receive_request_notification = receive_request_notification
        self.remove_request_notification = remove_request_notification
        self.create_guild_script = create_guild_script
        self.update_guild_script = update_guild_script
        self.join_guild_script = join_guild_script
        self.leave_guild_script = leave_guild_script
        self.change_role_script = change_role_script
        self.delete_guild_script = delete_guild_script
        self.log_setting = log_setting

