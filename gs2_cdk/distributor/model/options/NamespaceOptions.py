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
from ....core.model import NotificationSetting
from ....core.model import LogSetting


class NamespaceOptions:
    description: Optional[str]
    assume_user_id: Optional[str]
    auto_run_stamp_sheet_notification: Optional[NotificationSetting]
    auto_run_transaction_notification: Optional[NotificationSetting]
    log_setting: Optional[LogSetting]
    
    def __init__(
        self,
        description: Optional[str] = None,
        assume_user_id: Optional[str] = None,
        auto_run_stamp_sheet_notification: Optional[NotificationSetting] = None,
        auto_run_transaction_notification: Optional[NotificationSetting] = None,
        log_setting: Optional[LogSetting] = None,
    ):
        self.description = description
        self.assume_user_id = assume_user_id
        self.auto_run_stamp_sheet_notification = auto_run_stamp_sheet_notification
        self.auto_run_transaction_notification = auto_run_transaction_notification
        self.log_setting = log_setting

