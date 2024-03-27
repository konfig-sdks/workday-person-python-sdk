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

from workday_person_python_sdk.type.usage_type901718dd5e7910000cc03935c73e029c import UsageType901718dd5e7910000cc03935c73e029c

UsageTypeC1bb9f46f65210002d3c343d773200bc = typing.Union[UsageType901718dd5e7910000cc03935c73e029c,typing.Union[bool, date, datetime, dict, float, int, list, str, None]]
