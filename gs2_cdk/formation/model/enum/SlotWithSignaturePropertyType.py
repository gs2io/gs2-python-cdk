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




class SlotWithSignaturePropertyType:
    value: str
    GS2_INVENTORY: 'SlotWithSignaturePropertyType'
    GS2_DICTIONARY: 'SlotWithSignaturePropertyType'

    def __init__(
        self,
        value: str,
    ):
        self.value = value


SlotWithSignaturePropertyType.GS2_INVENTORY = SlotWithSignaturePropertyType("gs2_inventory")
SlotWithSignaturePropertyType.GS2_DICTIONARY = SlotWithSignaturePropertyType("gs2_dictionary")
