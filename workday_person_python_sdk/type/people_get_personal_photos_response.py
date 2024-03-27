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

from workday_person_python_sdk.type.person_photo6b9baf67ce60100007d43c79e7a30011 import PersonPhoto6b9baf67ce60100007d43c79e7a30011

class RequiredPeopleGetPersonalPhotosResponse(TypedDict):
    pass

class OptionalPeopleGetPersonalPhotosResponse(TypedDict, total=False):
    data: typing.List[PersonPhoto6b9baf67ce60100007d43c79e7a30011]

    total: int

class PeopleGetPersonalPhotosResponse(RequiredPeopleGetPersonalPhotosResponse, OptionalPeopleGetPersonalPhotosResponse):
    pass
