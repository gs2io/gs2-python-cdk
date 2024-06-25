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


class GooglePlaySettingOptions:
    package_name: Optional[str]
    public_key: Optional[str]
    
    def __init__(
        self,
        package_name: Optional[str] = None,
        public_key: Optional[str] = None,
    ):
        self.package_name = package_name
        self.public_key = public_key

