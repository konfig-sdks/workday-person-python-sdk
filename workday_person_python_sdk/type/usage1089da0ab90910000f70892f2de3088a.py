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

from workday_person_python_sdk.type.contact_usage1089da0ab90910000fa7748617db0898 import ContactUsage1089da0ab90910000fa7748617db0898

Usage1089da0ab90910000f70892f2de3088a = typing.Union[ContactUsage1089da0ab90910000fa7748617db0898,typing.Union[bool, date, datetime, dict, float, int, list, str, None]]
