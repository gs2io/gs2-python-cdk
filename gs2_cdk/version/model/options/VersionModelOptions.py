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
from ..enum.VersionModelScope import VersionModelScope
from ..enum.VersionModelType import VersionModelType
from ..enum.VersionModelApproveRequirement import VersionModelApproveRequirement


class VersionModelOptions:
    metadata: Optional[str]
    current_version: Optional[Version]
    warning_version: Optional[Version]
    error_version: Optional[Version]
    schedule_versions: Optional[List[ScheduleVersion]]
    need_signature: Optional[bool]
    signature_key_id: Optional[str]
    approve_requirement: Optional[VersionModelApproveRequirement]
    
    def __init__(
        self,
        metadata: Optional[str] = None,
        current_version: Optional[Version] = None,
        warning_version: Optional[Version] = None,
        error_version: Optional[Version] = None,
        schedule_versions: Optional[List[ScheduleVersion]] = None,
        need_signature: Optional[bool] = None,
        signature_key_id: Optional[str] = None,
        approve_requirement: Optional[VersionModelApproveRequirement] = None,
    ):
        self.metadata = metadata
        self.current_version = current_version
        self.warning_version = warning_version
        self.error_version = error_version
        self.schedule_versions = schedule_versions
        self.need_signature = need_signature
        self.signature_key_id = signature_key_id
        self.approve_requirement = approve_requirement

