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

from workday_person_python_sdk.type.status6de928ab1284100059f5dc66f77e01f6 import Status6de928ab1284100059f5dc66f77e01f6

MaritalStatusInformation6de928ab1284100059f5dc52629b01f4 = typing.Union[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]]
