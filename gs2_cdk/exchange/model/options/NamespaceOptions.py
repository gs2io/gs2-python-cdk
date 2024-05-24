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
from ....core.model import TransactionSetting
from ....core.model import ScriptSetting
from ....core.model import LogSetting


class NamespaceOptions:
    description: Optional[str]
    enable_await_exchange: Optional[bool]
    enable_direct_exchange: Optional[bool]
    transaction_setting: Optional[TransactionSetting]
    exchange_script: Optional[ScriptSetting]
    incremental_exchange_script: Optional[ScriptSetting]
    log_setting: Optional[LogSetting]
    queue_namespace_id: Optional[str]
    key_id: Optional[str]
    
    def __init__(
        self,
        description: Optional[str] = None,
        enable_await_exchange: Optional[bool] = None,
        enable_direct_exchange: Optional[bool] = None,
        transaction_setting: Optional[TransactionSetting] = None,
        exchange_script: Optional[ScriptSetting] = None,
        incremental_exchange_script: Optional[ScriptSetting] = None,
        log_setting: Optional[LogSetting] = None,
        queue_namespace_id: Optional[str] = None,
        key_id: Optional[str] = None,
    ):
        self.description = description
        self.enable_await_exchange = enable_await_exchange
        self.enable_direct_exchange = enable_direct_exchange
        self.transaction_setting = transaction_setting
        self.exchange_script = exchange_script
        self.incremental_exchange_script = incremental_exchange_script
        self.log_setting = log_setting
        self.queue_namespace_id = queue_namespace_id
        self.key_id = key_id

