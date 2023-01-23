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
from ....core.model import NotificationSetting
from ....core.model import LogSetting


class NamespaceOptions:
    description: Optional[str]
    allow_create_room: Optional[bool]
    post_message_script: Optional[ScriptSetting]
    create_room_script: Optional[ScriptSetting]
    delete_room_script: Optional[ScriptSetting]
    subscribe_room_script: Optional[ScriptSetting]
    unsubscribe_room_script: Optional[ScriptSetting]
    post_notification: Optional[NotificationSetting]
    log_setting: Optional[LogSetting]
    
    def __init__(
        self,
        description: Optional[str] = None,
        allow_create_room: Optional[bool] = None,
        post_message_script: Optional[ScriptSetting] = None,
        create_room_script: Optional[ScriptSetting] = None,
        delete_room_script: Optional[ScriptSetting] = None,
        subscribe_room_script: Optional[ScriptSetting] = None,
        unsubscribe_room_script: Optional[ScriptSetting] = None,
        post_notification: Optional[NotificationSetting] = None,
        log_setting: Optional[LogSetting] = None,
    ):
        self.description = description
        self.allow_create_room = allow_create_room
        self.post_message_script = post_message_script
        self.create_room_script = create_room_script
        self.delete_room_script = delete_room_script
        self.subscribe_room_script = subscribe_room_script
        self.unsubscribe_room_script = unsubscribe_room_script
        self.post_notification = post_notification
        self.log_setting = log_setting

