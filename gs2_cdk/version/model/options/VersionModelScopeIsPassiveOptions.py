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
from ..Version import Version
from ..ScheduleVersion import ScheduleVersion
from ..enums.VersionModelScope import VersionModelScope
from ..enums.VersionModelType import VersionModelType
from ..enums.VersionModelApproveRequirement import VersionModelApproveRequirement


class VersionModelScopeIsPassiveOptions:
    metadata: Optional[str]
    schedule_versions: Optional[List[ScheduleVersion]]
    
    def __init__(
        self,
        metadata: Optional[str] = None,
        schedule_versions: Optional[List[ScheduleVersion]] = None,
    ):
        self.metadata = metadata
        self.schedule_versions = schedule_versions
