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
from ..enums.BlockingPolicyModelDefaultRestriction import BlockingPolicyModelDefaultRestriction
from ..enums.BlockingPolicyModelLocationDetection import BlockingPolicyModelLocationDetection
from ..enums.BlockingPolicyModelLocationRestriction import BlockingPolicyModelLocationRestriction
from ..enums.BlockingPolicyModelAnonymousIpDetection import BlockingPolicyModelAnonymousIpDetection
from ..enums.BlockingPolicyModelAnonymousIpRestriction import BlockingPolicyModelAnonymousIpRestriction
from ..enums.BlockingPolicyModelHostingProviderIpDetection import BlockingPolicyModelHostingProviderIpDetection
from ..enums.BlockingPolicyModelHostingProviderIpRestriction import BlockingPolicyModelHostingProviderIpRestriction
from ..enums.BlockingPolicyModelReputationIpDetection import BlockingPolicyModelReputationIpDetection
from ..enums.BlockingPolicyModelReputationIpRestriction import BlockingPolicyModelReputationIpRestriction
from ..enums.BlockingPolicyModelIpAddressesDetection import BlockingPolicyModelIpAddressesDetection
from ..enums.BlockingPolicyModelIpAddressRestriction import BlockingPolicyModelIpAddressRestriction


class BlockingPolicyModelOptions:
    locations: Optional[List[str]]
    location_restriction: Optional[BlockingPolicyModelLocationRestriction]
    anonymous_ip_restriction: Optional[BlockingPolicyModelAnonymousIpRestriction]
    hosting_provider_ip_restriction: Optional[BlockingPolicyModelHostingProviderIpRestriction]
    reputation_ip_restriction: Optional[BlockingPolicyModelReputationIpRestriction]
    ip_addresses: Optional[List[str]]
    ip_address_restriction: Optional[BlockingPolicyModelIpAddressRestriction]
    
    def __init__(
        self,
        locations: Optional[List[str]] = None,
        location_restriction: Optional[BlockingPolicyModelLocationRestriction] = None,
        anonymous_ip_restriction: Optional[BlockingPolicyModelAnonymousIpRestriction] = None,
        hosting_provider_ip_restriction: Optional[BlockingPolicyModelHostingProviderIpRestriction] = None,
        reputation_ip_restriction: Optional[BlockingPolicyModelReputationIpRestriction] = None,
        ip_addresses: Optional[List[str]] = None,
        ip_address_restriction: Optional[BlockingPolicyModelIpAddressRestriction] = None,
    ):
        self.locations = locations
        self.location_restriction = location_restriction
        self.anonymous_ip_restriction = anonymous_ip_restriction
        self.hosting_provider_ip_restriction = hosting_provider_ip_restriction
        self.reputation_ip_restriction = reputation_ip_restriction
        self.ip_addresses = ip_addresses
        self.ip_address_restriction = ip_address_restriction

