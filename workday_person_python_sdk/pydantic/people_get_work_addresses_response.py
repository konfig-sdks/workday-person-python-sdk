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

from workday_person_python_sdk.pydantic.address_reference9c3ab7b846e4100009e5ec55fa530024 import AddressReference9c3ab7b846e4100009e5ec55fa530024

class PeopleGetWorkAddressesResponse(BaseModel):
    data: typing.Optional[typing.List[AddressReference9c3ab7b846e4100009e5ec55fa530024]] = Field(None, alias='data')

    total: typing.Optional[int] = Field(None, alias='total')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
