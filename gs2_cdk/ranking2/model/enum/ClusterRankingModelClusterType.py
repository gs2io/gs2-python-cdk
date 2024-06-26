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




class ClusterRankingModelClusterType:
    value: str
    RAW: 'ClusterRankingModelClusterType'
    GS2_GUILD__GUILD: 'ClusterRankingModelClusterType'
    GS2_MATCHMAKING__SEASON_GATHERING: 'ClusterRankingModelClusterType'

    def __init__(
        self,
        value: str,
    ):
        self.value = value


ClusterRankingModelClusterType.RAW = ClusterRankingModelClusterType("Raw")
ClusterRankingModelClusterType.GS2_GUILD__GUILD = ClusterRankingModelClusterType("Gs2Guild::Guild")
ClusterRankingModelClusterType.GS2_MATCHMAKING__SEASON_GATHERING = ClusterRankingModelClusterType("Gs2Matchmaking::SeasonGathering")
