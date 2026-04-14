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




class AggregationConfigType:
    value: str
    COUNT: 'AggregationConfigType'
    UNIQUE: 'AggregationConfigType'
    SUM: 'AggregationConfigType'
    AVG: 'AggregationConfigType'
    MAX: 'AggregationConfigType'
    MIN: 'AggregationConfigType'
    P90: 'AggregationConfigType'
    P95: 'AggregationConfigType'
    P99: 'AggregationConfigType'

    def __init__(
        self,
        value: str,
    ):
        self.value = value


AggregationConfigType.COUNT = AggregationConfigType("count")
AggregationConfigType.UNIQUE = AggregationConfigType("unique")
AggregationConfigType.SUM = AggregationConfigType("sum")
AggregationConfigType.AVG = AggregationConfigType("avg")
AggregationConfigType.MAX = AggregationConfigType("max")
AggregationConfigType.MIN = AggregationConfigType("min")
AggregationConfigType.P90 = AggregationConfigType("p90")
AggregationConfigType.P95 = AggregationConfigType("p95")
AggregationConfigType.P99 = AggregationConfigType("p99")
