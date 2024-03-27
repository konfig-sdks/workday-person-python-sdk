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

from workday_person_python_sdk.type.country_predefined_name_component_ab5c028f50b310001b9916066f1f0250 import CountryPredefinedNameComponentAb5c028f50b310001b9916066f1f0250

HonorarySuffixE08d883b5eae10000403d7acba9602e5 = typing.Union[CountryPredefinedNameComponentAb5c028f50b310001b9916066f1f0250,typing.Union[bool, date, datetime, dict, float, int, list, str, None]]
