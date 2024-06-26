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

from ....core.model import CdkResource, Stack
from ....core.func import GetAttr
from ....core.model import ScriptSetting
from ....core.model import NotificationSetting
from ....core.model import LogSetting


class NamespaceOptions:
    description: Optional[str]
    enable_rating: Optional[bool]
    enable_disconnect_detection: Optional[NamespaceEnableDisconnectDetection]
    disconnect_detection_timeout_seconds: Optional[int]
    create_gathering_trigger_realtime_namespace_id: Optional[str]
    create_gathering_trigger_script_id: Optional[str]
    complete_matchmaking_trigger_realtime_namespace_id: Optional[str]
    complete_matchmaking_trigger_script_id: Optional[str]
    enable_collaborate_season_rating: Optional[NamespaceEnableCollaborateSeasonRating]
    collaborate_season_rating_namespace_id: Optional[str]
    collaborate_season_rating_ttl: Optional[int]
    change_rating_script: Optional[ScriptSetting]
    join_notification: Optional[NotificationSetting]
    leave_notification: Optional[NotificationSetting]
    complete_notification: Optional[NotificationSetting]
    change_rating_notification: Optional[NotificationSetting]
    log_setting: Optional[LogSetting]
    
    def __init__(
        self,
        description: Optional[str] = None,
        enable_rating: Optional[bool] = None,
        enable_disconnect_detection: Optional[NamespaceEnableDisconnectDetection] = None,
        disconnect_detection_timeout_seconds: Optional[int] = None,
        create_gathering_trigger_realtime_namespace_id: Optional[str] = None,
        create_gathering_trigger_script_id: Optional[str] = None,
        complete_matchmaking_trigger_realtime_namespace_id: Optional[str] = None,
        complete_matchmaking_trigger_script_id: Optional[str] = None,
        enable_collaborate_season_rating: Optional[NamespaceEnableCollaborateSeasonRating] = None,
        collaborate_season_rating_namespace_id: Optional[str] = None,
        collaborate_season_rating_ttl: Optional[int] = None,
        change_rating_script: Optional[ScriptSetting] = None,
        join_notification: Optional[NotificationSetting] = None,
        leave_notification: Optional[NotificationSetting] = None,
        complete_notification: Optional[NotificationSetting] = None,
        change_rating_notification: Optional[NotificationSetting] = None,
        log_setting: Optional[LogSetting] = None,
    ):
        self.description = description
        self.enable_rating = enable_rating
        self.enable_disconnect_detection = enable_disconnect_detection
        self.disconnect_detection_timeout_seconds = disconnect_detection_timeout_seconds
        self.create_gathering_trigger_realtime_namespace_id = create_gathering_trigger_realtime_namespace_id
        self.create_gathering_trigger_script_id = create_gathering_trigger_script_id
        self.complete_matchmaking_trigger_realtime_namespace_id = complete_matchmaking_trigger_realtime_namespace_id
        self.complete_matchmaking_trigger_script_id = complete_matchmaking_trigger_script_id
        self.enable_collaborate_season_rating = enable_collaborate_season_rating
        self.collaborate_season_rating_namespace_id = collaborate_season_rating_namespace_id
        self.collaborate_season_rating_ttl = collaborate_season_rating_ttl
        self.change_rating_script = change_rating_script
        self.join_notification = join_notification
        self.leave_notification = leave_notification
        self.complete_notification = complete_notification
        self.change_rating_notification = change_rating_notification
        self.log_setting = log_setting

