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
from .options.AccountDeletionSettingOptions import AccountDeletionSettingOptions
from .enums.AccountDeletionSettingLoginDuringGracePeriod import AccountDeletionSettingLoginDuringGracePeriod
from .enums.AccountDeletionSettingCleanUserDataScope import AccountDeletionSettingCleanUserDataScope


class AccountDeletionSetting:
    grace_period_minutes: int
    login_during_grace_period: AccountDeletionSettingLoginDuringGracePeriod
    clean_user_data_scope: AccountDeletionSettingCleanUserDataScope

    def __init__(
        self,
        grace_period_minutes: int,
        login_during_grace_period: AccountDeletionSettingLoginDuringGracePeriod,
        clean_user_data_scope: AccountDeletionSettingCleanUserDataScope,
        options: Optional[AccountDeletionSettingOptions] = AccountDeletionSettingOptions(),
    ):
        self.grace_period_minutes = grace_period_minutes
        self.login_during_grace_period = login_during_grace_period
        self.clean_user_data_scope = clean_user_data_scope

    def properties(
        self,
    ) -> Dict[str, Any]:
        properties: Dict[str, Any] = {}

        if self.grace_period_minutes is not None:
            properties["gracePeriodMinutes"] = self.grace_period_minutes
        if self.login_during_grace_period is not None:
            properties["loginDuringGracePeriod"] = self.login_during_grace_period.value
        if self.clean_user_data_scope is not None:
            properties["cleanUserDataScope"] = self.clean_user_data_scope.value

        return properties
