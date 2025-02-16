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

from workday_person_python_sdk.type.local_name_ab5c028f50b310001cb4684782660256 import LocalNameAb5c028f50b310001cb4684782660256

LocalPersonNameE08d883b5eae10000403d7cd713c02ec = typing.Union[LocalNameAb5c028f50b310001cb4684782660256,typing.Union[bool, date, datetime, dict, float, int, list, str, None]]
