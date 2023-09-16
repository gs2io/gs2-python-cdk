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
from ..AdMob import AdMob
from ..UnityAd import UnityAd
from ....core.model import NotificationSetting
from ....core.model import LogSetting


class NamespaceOptions:
    admob: Optional[AdMob]
    unity_ad: Optional[UnityAd]
    description: Optional[str]
    log_setting: Optional[LogSetting]
    
    def __init__(
        self,
        admob: Optional[AdMob] = None,
        unity_ad: Optional[UnityAd] = None,
        description: Optional[str] = None,
        log_setting: Optional[LogSetting] = None,
    ):
        self.admob = admob
        self.unity_ad = unity_ad
        self.description = description
        self.log_setting = log_setting

