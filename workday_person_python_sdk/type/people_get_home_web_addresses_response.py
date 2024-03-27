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

from workday_person_python_sdk.type.web_address33e26848dc0010003893a0202ced0165 import WebAddress33e26848dc0010003893a0202ced0165

class RequiredPeopleGetHomeWebAddressesResponse(TypedDict):
    pass

class OptionalPeopleGetHomeWebAddressesResponse(TypedDict, total=False):
    data: typing.List[WebAddress33e26848dc0010003893a0202ced0165]

    total: int

class PeopleGetHomeWebAddressesResponse(RequiredPeopleGetHomeWebAddressesResponse, OptionalPeopleGetHomeWebAddressesResponse):
    pass