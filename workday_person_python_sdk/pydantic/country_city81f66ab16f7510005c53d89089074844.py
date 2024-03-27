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
from pydantic import BaseModel, Field, RootModel, ConfigDict

from workday_person_python_sdk.pydantic.city_ab827579ee1710002095f51c0e3f0178 import CityAb827579ee1710002095f51c0e3f0178

CountryCity81f66ab16f7510005c53d89089074844 = typing.Union[CityAb827579ee1710002095f51c0e3f0178,typing.Union[bool, date, datetime, dict, float, int, list, str, None]]
