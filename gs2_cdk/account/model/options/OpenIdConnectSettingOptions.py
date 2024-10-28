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


class OpenIdConnectSettingOptions:
    client_secret: Optional[str]
    apple_team_id: Optional[str]
    apple_key_id: Optional[str]
    apple_private_key_pem: Optional[str]
    done_endpoint_url: Optional[str]
    
    def __init__(
        self,
        client_secret: Optional[str] = None,
        apple_team_id: Optional[str] = None,
        apple_key_id: Optional[str] = None,
        apple_private_key_pem: Optional[str] = None,
        done_endpoint_url: Optional[str] = None,
    ):
        self.client_secret = client_secret
        self.apple_team_id = apple_team_id
        self.apple_key_id = apple_key_id
        self.apple_private_key_pem = apple_private_key_pem
        self.done_endpoint_url = done_endpoint_url

