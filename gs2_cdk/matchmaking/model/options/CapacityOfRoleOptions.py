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
from ..Attribute import Attribute
from ..Player import Player


class CapacityOfRoleOptions:
    role_aliases: Optional[List[str]]
    participants: Optional[List[Player]]
    
    def __init__(
        self,
        role_aliases: Optional[List[str]] = None,
        participants: Optional[List[Player]] = None,
    ):
        self.role_aliases = role_aliases
        self.participants = participants

