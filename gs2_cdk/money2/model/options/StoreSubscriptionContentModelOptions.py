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
from ..AppleAppStoreSubscriptionContent import AppleAppStoreSubscriptionContent
from ..GooglePlaySubscriptionContent import GooglePlaySubscriptionContent
from ..enums.StoreSubscriptionContentModelTriggerExtendMode import StoreSubscriptionContentModelTriggerExtendMode


class StoreSubscriptionContentModelOptions:
    metadata: Optional[str]
    rollup_hour: Optional[int]
    apple_app_store: Optional[AppleAppStoreSubscriptionContent]
    google_play: Optional[GooglePlaySubscriptionContent]
    
    def __init__(
        self,
        metadata: Optional[str] = None,
        rollup_hour: Optional[int] = None,
        apple_app_store: Optional[AppleAppStoreSubscriptionContent] = None,
        google_play: Optional[GooglePlaySubscriptionContent] = None,
    ):
        self.metadata = metadata
        self.rollup_hour = rollup_hour
        self.apple_app_store = apple_app_store
        self.google_play = google_play

