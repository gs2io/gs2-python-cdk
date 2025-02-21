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
from ..TwoFactorAuthenticationSetting import TwoFactorAuthenticationSetting
from ..enums.PasswordEnableTwoFactorAuthentication import PasswordEnableTwoFactorAuthentication


class PasswordEnableTwoFactorAuthenticationIsDisableOptions:
    two_factor_authentication_setting: Optional[TwoFactorAuthenticationSetting]
    revision: Optional[int]
    
    def __init__(
        self,
        two_factor_authentication_setting: Optional[TwoFactorAuthenticationSetting] = None,
        revision: Optional[int] = None,
    ):
        self.two_factor_authentication_setting = two_factor_authentication_setting
        self.revision = revision
