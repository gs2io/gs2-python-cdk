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


class NamespaceOptions:
    description: Optional[str]
    gcp_credential_json: Optional[str]
    big_query_dataset_name: Optional[str]
    log_expire_days: Optional[int]
    aws_region: Optional[str]
    aws_access_key_id: Optional[str]
    aws_secret_access_key: Optional[str]
    firehose_stream_name: Optional[str]
    
    def __init__(
        self,
        description: Optional[str] = None,
        gcp_credential_json: Optional[str] = None,
        big_query_dataset_name: Optional[str] = None,
        log_expire_days: Optional[int] = None,
        aws_region: Optional[str] = None,
        aws_access_key_id: Optional[str] = None,
        aws_secret_access_key: Optional[str] = None,
        firehose_stream_name: Optional[str] = None,
    ):
        self.description = description
        self.gcp_credential_json = gcp_credential_json
        self.big_query_dataset_name = big_query_dataset_name
        self.log_expire_days = log_expire_days
        self.aws_region = aws_region
        self.aws_access_key_id = aws_access_key_id
        self.aws_secret_access_key = aws_secret_access_key
        self.firehose_stream_name = firehose_stream_name

