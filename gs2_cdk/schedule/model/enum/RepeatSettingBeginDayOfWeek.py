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




class RepeatSettingBeginDayOfWeek:
    value: str
    SUNDAY: 'RepeatSettingBeginDayOfWeek'
    MONDAY: 'RepeatSettingBeginDayOfWeek'
    TUESDAY: 'RepeatSettingBeginDayOfWeek'
    WEDNESDAY: 'RepeatSettingBeginDayOfWeek'
    THURSDAY: 'RepeatSettingBeginDayOfWeek'
    FRIDAY: 'RepeatSettingBeginDayOfWeek'
    SATURDAY: 'RepeatSettingBeginDayOfWeek'

    def __init__(
        self,
        value: str,
    ):
        self.value = value


RepeatSettingBeginDayOfWeek.SUNDAY = RepeatSettingBeginDayOfWeek("sunday")
RepeatSettingBeginDayOfWeek.MONDAY = RepeatSettingBeginDayOfWeek("monday")
RepeatSettingBeginDayOfWeek.TUESDAY = RepeatSettingBeginDayOfWeek("tuesday")
RepeatSettingBeginDayOfWeek.WEDNESDAY = RepeatSettingBeginDayOfWeek("wednesday")
RepeatSettingBeginDayOfWeek.THURSDAY = RepeatSettingBeginDayOfWeek("thursday")
RepeatSettingBeginDayOfWeek.FRIDAY = RepeatSettingBeginDayOfWeek("friday")
RepeatSettingBeginDayOfWeek.SATURDAY = RepeatSettingBeginDayOfWeek("saturday")
