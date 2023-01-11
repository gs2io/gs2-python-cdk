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




class MissionGroupModelResetDayOfWeek:
    value: str
    SUNDAY: 'MissionGroupModelResetDayOfWeek'
    MONDAY: 'MissionGroupModelResetDayOfWeek'
    TUESDAY: 'MissionGroupModelResetDayOfWeek'
    WEDNESDAY: 'MissionGroupModelResetDayOfWeek'
    THURSDAY: 'MissionGroupModelResetDayOfWeek'
    FRIDAY: 'MissionGroupModelResetDayOfWeek'
    SATURDAY: 'MissionGroupModelResetDayOfWeek'

    def __init__(
        self,
        value: str,
    ):
        self.value = value


MissionGroupModelResetDayOfWeek.SUNDAY = MissionGroupModelResetDayOfWeek("sunday")
MissionGroupModelResetDayOfWeek.MONDAY = MissionGroupModelResetDayOfWeek("monday")
MissionGroupModelResetDayOfWeek.TUESDAY = MissionGroupModelResetDayOfWeek("tuesday")
MissionGroupModelResetDayOfWeek.WEDNESDAY = MissionGroupModelResetDayOfWeek("wednesday")
MissionGroupModelResetDayOfWeek.THURSDAY = MissionGroupModelResetDayOfWeek("thursday")
MissionGroupModelResetDayOfWeek.FRIDAY = MissionGroupModelResetDayOfWeek("friday")
MissionGroupModelResetDayOfWeek.SATURDAY = MissionGroupModelResetDayOfWeek("saturday")
