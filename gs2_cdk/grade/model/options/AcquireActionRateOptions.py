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
from ..enum.AcquireActionRateMode import AcquireActionRateMode


class AcquireActionRateOptions:
    rates: Optional[List[float]]
    big_rates: Optional[List[str]]
    
    def __init__(
        self,
        rates: Optional[List[float]] = None,
        big_rates: Optional[List[str]] = None,
    ):
        self.rates = rates
        self.big_rates = big_rates

