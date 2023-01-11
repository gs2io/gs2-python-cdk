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
from ....core.model import NotificationSetting
from ....core.model import LogSetting


class NamespaceOptions:
    description: Optional[str]
    is_automatic_deleting_enabled: Optional[bool]
    transaction_setting: Optional[TransactionSetting]
    receive_message_script: Optional[ScriptSetting]
    read_message_script: Optional[ScriptSetting]
    delete_message_script: Optional[ScriptSetting]
    receive_notification: Optional[NotificationSetting]
    log_setting: Optional[LogSetting]
    queue_namespace_id: Optional[str]
    key_id: Optional[str]
    
    def __init__(
        self,
        description: Optional[str] = None,
        is_automatic_deleting_enabled: Optional[bool] = None,
        transaction_setting: Optional[TransactionSetting] = None,
        receive_message_script: Optional[ScriptSetting] = None,
        read_message_script: Optional[ScriptSetting] = None,
        delete_message_script: Optional[ScriptSetting] = None,
        receive_notification: Optional[NotificationSetting] = None,
        log_setting: Optional[LogSetting] = None,
        queue_namespace_id: Optional[str] = None,
        key_id: Optional[str] = None,
    ):
        self.description = description
        self.is_automatic_deleting_enabled = is_automatic_deleting_enabled
        self.transaction_setting = transaction_setting
        self.receive_message_script = receive_message_script
        self.read_message_script = read_message_script
        self.delete_message_script = delete_message_script
        self.receive_notification = receive_notification
        self.log_setting = log_setting
        self.queue_namespace_id = queue_namespace_id
        self.key_id = key_id

