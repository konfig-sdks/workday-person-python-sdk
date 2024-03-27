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

from workday_person_python_sdk.pydantic.web_address33e26848dc0010003893a0202ced0165 import WebAddress33e26848dc0010003893a0202ced0165

class PeopleGetWorkWebAddressesResponse(BaseModel):
    data: typing.Optional[typing.List[WebAddress33e26848dc0010003893a0202ced0165]] = Field(None, alias='data')

    total: typing.Optional[int] = Field(None, alias='total')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
