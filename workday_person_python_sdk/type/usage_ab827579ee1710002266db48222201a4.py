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

from workday_person_python_sdk.type.contact_usage_ab827579ee171000211397a6dede017d import ContactUsageAb827579ee171000211397a6dede017d

UsageAb827579ee1710002266db48222201a4 = typing.Union[ContactUsageAb827579ee171000211397a6dede017d,typing.Union[bool, date, datetime, dict, float, int, list, str, None]]
