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

from workday_person_python_sdk.type.name33e26848dc0010002f1ae76d63ec0061 import Name33e26848dc0010002f1ae76d63ec0061

class RequiredPeopleGetPreferredNameResponse(TypedDict):
    pass

class OptionalPeopleGetPreferredNameResponse(TypedDict, total=False):
    data: typing.List[Name33e26848dc0010002f1ae76d63ec0061]

    total: int

class PeopleGetPreferredNameResponse(RequiredPeopleGetPreferredNameResponse, OptionalPeopleGetPreferredNameResponse):
    pass
