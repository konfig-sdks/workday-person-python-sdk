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

from workday_person_python_sdk.type.country6de928ab12841000549fe6404b2101c3 import Country6de928ab12841000549fe6404b2101c3
from workday_person_python_sdk.type.region6de928ab12841000549fe6375a9301c2 import Region6de928ab12841000549fe6375a9301c2

PlaceOfBirth6de928ab12841000549fe623b1ab01c0 = typing.Union[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]]