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
from ..PlatformSetting import PlatformSetting
from ....core.model import ScriptSetting
from ....core.model import NotificationSetting
from ....core.model import LogSetting


class NamespaceOptions:
    description: Optional[str]
    deposit_balance_script: Optional[ScriptSetting]
    withdraw_balance_script: Optional[ScriptSetting]
    subscribe_script: Optional[str]
    renew_script: Optional[str]
    unsubscribe_script: Optional[str]
    take_over_script: Optional[ScriptSetting]
    change_subscription_status_notification: Optional[NotificationSetting]
    log_setting: Optional[LogSetting]
    
    def __init__(
        self,
        description: Optional[str] = None,
        deposit_balance_script: Optional[ScriptSetting] = None,
        withdraw_balance_script: Optional[ScriptSetting] = None,
        subscribe_script: Optional[str] = None,
        renew_script: Optional[str] = None,
        unsubscribe_script: Optional[str] = None,
        take_over_script: Optional[ScriptSetting] = None,
        change_subscription_status_notification: Optional[NotificationSetting] = None,
        log_setting: Optional[LogSetting] = None,
    ):
        self.description = description
        self.deposit_balance_script = deposit_balance_script
        self.withdraw_balance_script = withdraw_balance_script
        self.subscribe_script = subscribe_script
        self.renew_script = renew_script
        self.unsubscribe_script = unsubscribe_script
        self.take_over_script = take_over_script
        self.change_subscription_status_notification = change_subscription_status_notification
        self.log_setting = log_setting

