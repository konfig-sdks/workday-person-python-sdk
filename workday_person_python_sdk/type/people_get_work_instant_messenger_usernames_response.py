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

from workday_person_python_sdk.type.instant_messenger_account33e26848dc00100036f723337ebb0132 import InstantMessengerAccount33e26848dc00100036f723337ebb0132

class RequiredPeopleGetWorkInstantMessengerUsernamesResponse(TypedDict):
    pass

class OptionalPeopleGetWorkInstantMessengerUsernamesResponse(TypedDict, total=False):
    data: typing.List[InstantMessengerAccount33e26848dc00100036f723337ebb0132]

    total: int

class PeopleGetWorkInstantMessengerUsernamesResponse(RequiredPeopleGetWorkInstantMessengerUsernamesResponse, OptionalPeopleGetWorkInstantMessengerUsernamesResponse):
    pass
