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




class SubscribeTransactionStatusDetail:
    value: str
    ACTIVE_ACTIVE: 'SubscribeTransactionStatusDetail'
    ACTIVE_CONVERTED_FROM_TRIAL: 'SubscribeTransactionStatusDetail'
    ACTIVE_IN_TRIAL: 'SubscribeTransactionStatusDetail'
    ACTIVE_IN_INTRO_OFFER: 'SubscribeTransactionStatusDetail'
    GRACE_CANCELED: 'SubscribeTransactionStatusDetail'
    GRACE_GRACE_PERIOD: 'SubscribeTransactionStatusDetail'
    GRACE_ON_HOLD: 'SubscribeTransactionStatusDetail'
    INACTIVE_EXPIRED: 'SubscribeTransactionStatusDetail'
    INACTIVE_REVOKED: 'SubscribeTransactionStatusDetail'

    def __init__(
        self,
        value: str,
    ):
        self.value = value


SubscribeTransactionStatusDetail.ACTIVE_ACTIVE = SubscribeTransactionStatusDetail("active@active")
SubscribeTransactionStatusDetail.ACTIVE_CONVERTED_FROM_TRIAL = SubscribeTransactionStatusDetail("active@converted_from_trial")
SubscribeTransactionStatusDetail.ACTIVE_IN_TRIAL = SubscribeTransactionStatusDetail("active@in_trial")
SubscribeTransactionStatusDetail.ACTIVE_IN_INTRO_OFFER = SubscribeTransactionStatusDetail("active@in_intro_offer")
SubscribeTransactionStatusDetail.GRACE_CANCELED = SubscribeTransactionStatusDetail("grace@canceled")
SubscribeTransactionStatusDetail.GRACE_GRACE_PERIOD = SubscribeTransactionStatusDetail("grace@grace_period")
SubscribeTransactionStatusDetail.GRACE_ON_HOLD = SubscribeTransactionStatusDetail("grace@on_hold")
SubscribeTransactionStatusDetail.INACTIVE_EXPIRED = SubscribeTransactionStatusDetail("inactive@expired")
SubscribeTransactionStatusDetail.INACTIVE_REVOKED = SubscribeTransactionStatusDetail("inactive@revoked")
