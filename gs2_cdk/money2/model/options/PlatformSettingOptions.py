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
from ..AppleAppStoreSetting import AppleAppStoreSetting
from ..GooglePlaySetting import GooglePlaySetting
from ..FakeSetting import FakeSetting


class PlatformSettingOptions:
    apple_app_store: Optional[AppleAppStoreSetting]
    google_play: Optional[GooglePlaySetting]
    fake: Optional[FakeSetting]
    
    def __init__(
        self,
        apple_app_store: Optional[AppleAppStoreSetting] = None,
        google_play: Optional[GooglePlaySetting] = None,
        fake: Optional[FakeSetting] = None,
    ):
        self.apple_app_store = apple_app_store
        self.google_play = google_play
        self.fake = fake

