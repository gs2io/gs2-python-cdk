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
from ..AdMob import AdMob
from ..UnityAd import UnityAd
from ..AppLovinMax import AppLovinMax
from ....core.model import ScriptSetting
from ....core.model import NotificationSetting
from ....core.model import LogSetting


class NamespaceOptions:
    description: Optional[str]
    transaction_setting: Optional[TransactionSetting]
    admob: Optional[AdMob]
    unity_ad: Optional[UnityAd]
    app_lovin_maxes: Optional[List[AppLovinMax]]
    acquire_point_script: Optional[ScriptSetting]
    consume_point_script: Optional[ScriptSetting]
    change_point_notification: Optional[NotificationSetting]
    log_setting: Optional[LogSetting]
    
    def __init__(
        self,
        description: Optional[str] = None,
        transaction_setting: Optional[TransactionSetting] = None,
        admob: Optional[AdMob] = None,
        unity_ad: Optional[UnityAd] = None,
        app_lovin_maxes: Optional[List[AppLovinMax]] = None,
        acquire_point_script: Optional[ScriptSetting] = None,
        consume_point_script: Optional[ScriptSetting] = None,
        change_point_notification: Optional[NotificationSetting] = None,
        log_setting: Optional[LogSetting] = None,
    ):
        self.description = description
        self.transaction_setting = transaction_setting
        self.admob = admob
        self.unity_ad = unity_ad
        self.app_lovin_maxes = app_lovin_maxes
        self.acquire_point_script = acquire_point_script
        self.consume_point_script = consume_point_script
        self.change_point_notification = change_point_notification
        self.log_setting = log_setting

