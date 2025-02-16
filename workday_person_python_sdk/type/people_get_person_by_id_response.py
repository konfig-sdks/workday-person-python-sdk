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

from workday_person_python_sdk.type.person_representation_e451ce2c8b48100007c312f3f72700b3 import PersonRepresentationE451ce2c8b48100007c312f3f72700b3

class RequiredPeopleGetPersonByIdResponse(TypedDict):
    pass

class OptionalPeopleGetPersonByIdResponse(TypedDict, total=False):
    data: typing.List[PersonRepresentationE451ce2c8b48100007c312f3f72700b3]

    total: int

class PeopleGetPersonByIdResponse(RequiredPeopleGetPersonByIdResponse, OptionalPeopleGetPersonByIdResponse):
    pass
