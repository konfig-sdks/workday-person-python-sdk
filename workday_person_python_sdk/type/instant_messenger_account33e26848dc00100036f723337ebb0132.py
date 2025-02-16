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

from workday_person_python_sdk.type.type33e26848dc00100037bb584480fe014a import Type33e26848dc00100037bb584480fe014a
from workday_person_python_sdk.type.usage_ab827579ee1710002266db48222201a4 import UsageAb827579ee1710002266db48222201a4

InstantMessengerAccount33e26848dc00100036f723337ebb0132 = typing.Union[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]]
