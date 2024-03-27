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

from workday_person_python_sdk.type.blood_type6de928ab1284100056beb6e9884101cd import BloodType6de928ab1284100056beb6e9884101cd

BloodTypeA63806bf8576100013fa9dcbb7dc0111 = typing.Union[BloodType6de928ab1284100056beb6e9884101cd,typing.Union[bool, date, datetime, dict, float, int, list, str, None]]