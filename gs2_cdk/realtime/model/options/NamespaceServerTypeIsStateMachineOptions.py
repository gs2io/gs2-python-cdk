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
from ..TransactionSettingV2 import TransactionSettingV2
from ..SyncSetting import SyncSetting
from ..StateMachineSetting import StateMachineSetting
from ..ParticipantSetting import ParticipantSetting
from ..MobileNotificationMessage import MobileNotificationMessage
from ....core.model import NotificationSetting
from ....core.model import LogSetting
from ..enums.NamespaceServerType import NamespaceServerType
from ..enums.NamespaceServerSpec import NamespaceServerSpec


class NamespaceServerTypeIsStateMachineOptions:
    description: Optional[str]
    transaction_setting: Optional[TransactionSetting]
    transaction_setting_v2: Optional[TransactionSettingV2]
    sync_setting: Optional[SyncSetting]
    participant_setting: Optional[ParticipantSetting]
    create_notification: Optional[NotificationSetting]
    log_setting: Optional[LogSetting]
    revision: Optional[int]
    
    def __init__(
        self,
        description: Optional[str] = None,
        transaction_setting: Optional[TransactionSetting] = None,
        transaction_setting_v2: Optional[TransactionSettingV2] = None,
        sync_setting: Optional[SyncSetting] = None,
        participant_setting: Optional[ParticipantSetting] = None,
        create_notification: Optional[NotificationSetting] = None,
        log_setting: Optional[LogSetting] = None,
        revision: Optional[int] = None,
    ):
        self.description = description
        self.transaction_setting = transaction_setting
        self.transaction_setting_v2 = transaction_setting_v2
        self.sync_setting = sync_setting
        self.participant_setting = participant_setting
        self.create_notification = create_notification
        self.log_setting = log_setting
        self.revision = revision
