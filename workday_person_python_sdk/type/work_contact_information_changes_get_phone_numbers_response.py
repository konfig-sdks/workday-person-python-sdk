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

from workday_person_python_sdk.type.phone_reference1089da0ab90910000f70891a998b0887 import PhoneReference1089da0ab90910000f70891a998b0887

class RequiredWorkContactInformationChangesGetPhoneNumbersResponse(TypedDict):
    pass

class OptionalWorkContactInformationChangesGetPhoneNumbersResponse(TypedDict, total=False):
    data: typing.List[PhoneReference1089da0ab90910000f70891a998b0887]

    total: int

class WorkContactInformationChangesGetPhoneNumbersResponse(RequiredWorkContactInformationChangesGetPhoneNumbersResponse, OptionalWorkContactInformationChangesGetPhoneNumbersResponse):
    pass
