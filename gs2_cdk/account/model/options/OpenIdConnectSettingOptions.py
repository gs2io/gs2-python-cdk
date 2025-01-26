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
from ..ScopeValue import ScopeValue


class OpenIdConnectSettingOptions:
    client_secret: Optional[str]
    apple_team_id: Optional[str]
    apple_key_id: Optional[str]
    apple_private_key_pem: Optional[str]
    done_endpoint_url: Optional[str]
    additional_scope_values: Optional[List[ScopeValue]]
    additional_return_values: Optional[List[str]]
    
    def __init__(
        self,
        client_secret: Optional[str] = None,
        apple_team_id: Optional[str] = None,
        apple_key_id: Optional[str] = None,
        apple_private_key_pem: Optional[str] = None,
        done_endpoint_url: Optional[str] = None,
        additional_scope_values: Optional[List[ScopeValue]] = None,
        additional_return_values: Optional[List[str]] = None,
    ):
        self.client_secret = client_secret
        self.apple_team_id = apple_team_id
        self.apple_key_id = apple_key_id
        self.apple_private_key_pem = apple_private_key_pem
        self.done_endpoint_url = done_endpoint_url
        self.additional_scope_values = additional_scope_values
        self.additional_return_values = additional_return_values

