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
from ..AppleAppStoreVerifyReceiptEvent import AppleAppStoreVerifyReceiptEvent
from ..GooglePlayVerifyReceiptEvent import GooglePlayVerifyReceiptEvent
from ..enums.RefundEventPlatform import RefundEventPlatform


class RefundEventOptions:
    apple_app_store_refund_event: Optional[AppleAppStoreVerifyReceiptEvent]
    google_play_refund_event: Optional[GooglePlayVerifyReceiptEvent]
    
    def __init__(
        self,
        apple_app_store_refund_event: Optional[AppleAppStoreVerifyReceiptEvent] = None,
        google_play_refund_event: Optional[GooglePlayVerifyReceiptEvent] = None,
    ):
        self.apple_app_store_refund_event = apple_app_store_refund_event
        self.google_play_refund_event = google_play_refund_event

