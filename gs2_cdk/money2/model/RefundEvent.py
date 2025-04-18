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
from .AppleAppStoreVerifyReceiptEvent import AppleAppStoreVerifyReceiptEvent
from .GooglePlayVerifyReceiptEvent import GooglePlayVerifyReceiptEvent
from .options.RefundEventOptions import RefundEventOptions
from .enums.RefundEventPlatform import RefundEventPlatform


class RefundEvent:
    content_name: str
    platform: RefundEventPlatform
    apple_app_store_refund_event: Optional[AppleAppStoreVerifyReceiptEvent] = None
    google_play_refund_event: Optional[GooglePlayVerifyReceiptEvent] = None

    def __init__(
        self,
        content_name: str,
        platform: RefundEventPlatform,
        options: Optional[RefundEventOptions] = RefundEventOptions(),
    ):
        self.content_name = content_name
        self.platform = platform
        self.apple_app_store_refund_event = options.apple_app_store_refund_event if options.apple_app_store_refund_event else None
        self.google_play_refund_event = options.google_play_refund_event if options.google_play_refund_event else None

    def properties(
        self,
    ) -> Dict[str, Any]:
        properties: Dict[str, Any] = {}

        if self.content_name is not None:
            properties["contentName"] = self.content_name
        if self.platform is not None:
            properties["platform"] = self.platform.value
        if self.apple_app_store_refund_event is not None:
            properties["appleAppStoreRefundEvent"] = self.apple_app_store_refund_event.properties(
            )
        if self.google_play_refund_event is not None:
            properties["googlePlayRefundEvent"] = self.google_play_refund_event.properties(
            )

        return properties
