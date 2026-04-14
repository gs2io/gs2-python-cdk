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

from ...core.model import CdkResource, Stack
from ...core.func import GetAttr

from ..ref.FacetModelRef import FacetModelRef
from .enums.FacetModelType import FacetModelType

from .options.FacetModelOptions import FacetModelOptions


class FacetModel(CdkResource):
    stack: Stack
    namespace_name: str
    field: str
    type: FacetModelType
    display_name: str
    order: Optional[int] = None

    def __init__(
        self,
        stack: Stack,
        namespace_name: str,
        field: str,
        type: FacetModelType,
        display_name: str,
        options: Optional[FacetModelOptions] = FacetModelOptions(),
    ):
        super().__init__(
            "Log_FacetModel_" + field
        )

        self.stack = stack
        self.namespace_name = namespace_name
        self.field = field
        self.type = type
        self.display_name = display_name
        self.order = options.order if options.order else None
        stack.add_resource(
            self,
        )


    def alternate_keys(
        self,
    ):
        return "field"

    def resource_type(
        self,
    ) -> str:
        return "GS2::Log::FacetModel"

    def properties(
        self,
    ) -> Dict[str, Any]:
        properties: Dict[str, Any] = {}

        if self.namespace_name is not None:
            properties["NamespaceName"] = self.namespace_name
        if self.field is not None:
            properties["Field"] = self.field
        if self.type is not None:
            properties["Type"] = self.type
        if self.display_name is not None:
            properties["DisplayName"] = self.display_name
        if self.order is not None:
            properties["Order"] = self.order

        return properties

    def ref(
        self,
    ) -> FacetModelRef:
        return FacetModelRef(
            self.namespace_name,
            self.field,
        )

    def get_attr_facet_model_id(
        self,
    ) -> GetAttr:
        return GetAttr(
            self,
            "Item.FacetModelId",
            None,
        )
