# coding: utf-8

"""
    person

    The Person REST APIs enable you to access information about the worker person, including country-specific configuration information about name components.

    The version of the OpenAPI document: v4
    Generated by: https://konfigthis.com
"""

from datetime import datetime, date
import typing
from enum import Enum
from typing_extensions import TypedDict, Literal, TYPE_CHECKING
from pydantic import BaseModel, Field, RootModel, ConfigDict

from workday_person_python_sdk.pydantic.work_address_reference_c1bb9f46f65210002d2fa259a1c10095 import WorkAddressReferenceC1bb9f46f65210002d2fa259a1c10095

class WorkContactInformationChangesGetAddressesStagedResponse(BaseModel):
    data: typing.Optional[typing.List[WorkAddressReferenceC1bb9f46f65210002d2fa259a1c10095]] = Field(None, alias='data')

    total: typing.Optional[int] = Field(None, alias='total')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
