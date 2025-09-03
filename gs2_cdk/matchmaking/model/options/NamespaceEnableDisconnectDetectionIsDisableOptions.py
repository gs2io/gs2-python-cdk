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
from ....core.model import TransactionSetting
from ....core.model import ScriptSetting
from ....core.model import NotificationSetting
from ....core.model import LogSetting
from ..enums.NamespaceEnableDisconnectDetection import NamespaceEnableDisconnectDetection
from ..enums.NamespaceCreateGatheringTriggerType import NamespaceCreateGatheringTriggerType
from ..enums.NamespaceCompleteMatchmakingTriggerType import NamespaceCompleteMatchmakingTriggerType
from ..enums.NamespaceEnableCollaborateSeasonRating import NamespaceEnableCollaborateSeasonRating


class NamespaceEnableDisconnectDetectionIsDisableOptions:
    description: Optional[str]
    transaction_setting: Optional[TransactionSetting]
    change_rating_script: Optional[ScriptSetting]
    join_notification: Optional[NotificationSetting]
    leave_notification: Optional[NotificationSetting]
    complete_notification: Optional[NotificationSetting]
    change_rating_notification: Optional[NotificationSetting]
    log_setting: Optional[LogSetting]
    revision: Optional[int]
    
    def __init__(
        self,
        description: Optional[str] = None,
        transaction_setting: Optional[TransactionSetting] = None,
        change_rating_script: Optional[ScriptSetting] = None,
        join_notification: Optional[NotificationSetting] = None,
        leave_notification: Optional[NotificationSetting] = None,
        complete_notification: Optional[NotificationSetting] = None,
        change_rating_notification: Optional[NotificationSetting] = None,
        log_setting: Optional[LogSetting] = None,
        revision: Optional[int] = None,
    ):
        self.description = description
        self.transaction_setting = transaction_setting
        self.change_rating_script = change_rating_script
        self.join_notification = join_notification
        self.leave_notification = leave_notification
        self.complete_notification = complete_notification
        self.change_rating_notification = change_rating_notification
        self.log_setting = log_setting
        self.revision = revision
