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

from workday_person_python_sdk.type.instancemodelreference import INSTANCEMODELREFERENCE

ContentType6b9baf67ce60100011fd138066140090 = typing.Union[INSTANCEMODELREFERENCE,typing.Union[bool, date, datetime, dict, float, int, list, str, None]]
