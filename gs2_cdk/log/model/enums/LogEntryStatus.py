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




class LogEntryStatus:
    value: str
    OK: 'LogEntryStatus'
    INFO: 'LogEntryStatus'
    NOTICE: 'LogEntryStatus'
    ERROR: 'LogEntryStatus'
    WARN: 'LogEntryStatus'
    EMAG: 'LogEntryStatus'

    def __init__(
        self,
        value: str,
    ):
        self.value = value


LogEntryStatus.OK = LogEntryStatus("ok")
LogEntryStatus.INFO = LogEntryStatus("info")
LogEntryStatus.NOTICE = LogEntryStatus("notice")
LogEntryStatus.ERROR = LogEntryStatus("error")
LogEntryStatus.WARN = LogEntryStatus("warn")
LogEntryStatus.EMAG = LogEntryStatus("emag")
