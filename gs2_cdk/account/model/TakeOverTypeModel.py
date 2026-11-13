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
from .ScopeValue import ScopeValue
from .OpenIdConnectSetting import OpenIdConnectSetting
from .IssuedCodeSetting import IssuedCodeSetting
from .options.TakeOverTypeModelOptions import TakeOverTypeModelOptions
from .options.TakeOverTypeModelTakeOverMethodIsOpenIdConnectOptions import TakeOverTypeModelTakeOverMethodIsOpenIdConnectOptions
from .options.TakeOverTypeModelTakeOverMethodIsIssuedCodeOptions import TakeOverTypeModelTakeOverMethodIsIssuedCodeOptions
from .enums.TakeOverTypeModelTakeOverMethod import TakeOverTypeModelTakeOverMethod


class TakeOverTypeModel:
    type: int
    take_over_method: TakeOverTypeModelTakeOverMethod
    metadata: Optional[str] = None
    open_id_connect_setting: Optional[OpenIdConnectSetting] = None
    issued_code_setting: Optional[IssuedCodeSetting] = None

    def __init__(
        self,
        type: int,
        take_over_method: TakeOverTypeModelTakeOverMethod,
        options: Optional[TakeOverTypeModelOptions] = TakeOverTypeModelOptions(),
    ):
        self.type = type
        self.take_over_method = take_over_method
        self.metadata = options.metadata if options.metadata else None
        self.open_id_connect_setting = options.open_id_connect_setting if options.open_id_connect_setting else None
        self.issued_code_setting = options.issued_code_setting if options.issued_code_setting else None

    @staticmethod
    def take_over_method_is_open_id_connect(
        type: int,
        open_id_connect_setting: OpenIdConnectSetting,
        options: Optional[TakeOverTypeModelTakeOverMethodIsOpenIdConnectOptions] = TakeOverTypeModelTakeOverMethodIsOpenIdConnectOptions(),
    ) -> TakeOverTypeModel:
        return TakeOverTypeModel(
            type,
            TakeOverTypeModelTakeOverMethod.OPEN_ID_CONNECT,
            TakeOverTypeModelOptions(
                open_id_connect_setting,
                options.metadata,
            ),
        )

    @staticmethod
    def take_over_method_is_issued_code(
        type: int,
        issued_code_setting: IssuedCodeSetting,
        options: Optional[TakeOverTypeModelTakeOverMethodIsIssuedCodeOptions] = TakeOverTypeModelTakeOverMethodIsIssuedCodeOptions(),
    ) -> TakeOverTypeModel:
        return TakeOverTypeModel(
            type,
            TakeOverTypeModelTakeOverMethod.ISSUED_CODE,
            TakeOverTypeModelOptions(
                issued_code_setting,
                options.metadata,
            ),
        )

    def properties(
        self,
    ) -> Dict[str, Any]:
        properties: Dict[str, Any] = {}

        if self.type is not None:
            properties["type"] = self.type
        if self.metadata is not None:
            properties["metadata"] = self.metadata
        if self.take_over_method is not None:
            properties["takeOverMethod"] = self.take_over_method.value
        if self.open_id_connect_setting is not None:
            properties["openIdConnectSetting"] = self.open_id_connect_setting.properties(
            )
        if self.issued_code_setting is not None:
            properties["issuedCodeSetting"] = self.issued_code_setting.properties(
            )

        return properties
