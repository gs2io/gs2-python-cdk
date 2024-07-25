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
    follow_script: Optional[ScriptSetting]
    unfollow_script: Optional[ScriptSetting]
    send_request_script: Optional[ScriptSetting]
    cancel_request_script: Optional[ScriptSetting]
    accept_request_script: Optional[ScriptSetting]
    reject_request_script: Optional[ScriptSetting]
    delete_friend_script: Optional[ScriptSetting]
    update_profile_script: Optional[ScriptSetting]
    follow_notification: Optional[NotificationSetting]
    receive_request_notification: Optional[NotificationSetting]
    cancel_request_notification: Optional[NotificationSetting]
    accept_request_notification: Optional[NotificationSetting]
    reject_request_notification: Optional[NotificationSetting]
    delete_friend_notification: Optional[NotificationSetting]
    log_setting: Optional[LogSetting]
    
    def __init__(
        self,
        description: Optional[str] = None,
        follow_script: Optional[ScriptSetting] = None,
        unfollow_script: Optional[ScriptSetting] = None,
        send_request_script: Optional[ScriptSetting] = None,
        cancel_request_script: Optional[ScriptSetting] = None,
        accept_request_script: Optional[ScriptSetting] = None,
        reject_request_script: Optional[ScriptSetting] = None,
        delete_friend_script: Optional[ScriptSetting] = None,
        update_profile_script: Optional[ScriptSetting] = None,
        follow_notification: Optional[NotificationSetting] = None,
        receive_request_notification: Optional[NotificationSetting] = None,
        cancel_request_notification: Optional[NotificationSetting] = None,
        accept_request_notification: Optional[NotificationSetting] = None,
        reject_request_notification: Optional[NotificationSetting] = None,
        delete_friend_notification: Optional[NotificationSetting] = None,
        log_setting: Optional[LogSetting] = None,
    ):
        self.description = description
        self.follow_script = follow_script
        self.unfollow_script = unfollow_script
        self.send_request_script = send_request_script
        self.cancel_request_script = cancel_request_script
        self.accept_request_script = accept_request_script
        self.reject_request_script = reject_request_script
        self.delete_friend_script = delete_friend_script
        self.update_profile_script = update_profile_script
        self.follow_notification = follow_notification
        self.receive_request_notification = receive_request_notification
        self.cancel_request_notification = cancel_request_notification
        self.accept_request_notification = accept_request_notification
        self.reject_request_notification = reject_request_notification
        self.delete_friend_notification = delete_friend_notification
        self.log_setting = log_setting

