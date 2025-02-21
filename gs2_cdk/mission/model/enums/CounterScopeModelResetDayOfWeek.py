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




class CounterScopeModelResetDayOfWeek:
    value: str
    SUNDAY: 'CounterScopeModelResetDayOfWeek'
    MONDAY: 'CounterScopeModelResetDayOfWeek'
    TUESDAY: 'CounterScopeModelResetDayOfWeek'
    WEDNESDAY: 'CounterScopeModelResetDayOfWeek'
    THURSDAY: 'CounterScopeModelResetDayOfWeek'
    FRIDAY: 'CounterScopeModelResetDayOfWeek'
    SATURDAY: 'CounterScopeModelResetDayOfWeek'

    def __init__(
        self,
        value: str,
    ):
        self.value = value


CounterScopeModelResetDayOfWeek.SUNDAY = CounterScopeModelResetDayOfWeek("sunday")
CounterScopeModelResetDayOfWeek.MONDAY = CounterScopeModelResetDayOfWeek("monday")
CounterScopeModelResetDayOfWeek.TUESDAY = CounterScopeModelResetDayOfWeek("tuesday")
CounterScopeModelResetDayOfWeek.WEDNESDAY = CounterScopeModelResetDayOfWeek("wednesday")
CounterScopeModelResetDayOfWeek.THURSDAY = CounterScopeModelResetDayOfWeek("thursday")
CounterScopeModelResetDayOfWeek.FRIDAY = CounterScopeModelResetDayOfWeek("friday")
CounterScopeModelResetDayOfWeek.SATURDAY = CounterScopeModelResetDayOfWeek("saturday")
