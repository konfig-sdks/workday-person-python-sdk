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

from workday_person_python_sdk.pydantic.country8beeb162738910001433a1ef009a01d0 import Country8beeb162738910001433a1ef009a01d0

CountryC1bb9f46f65210002d2fa329fe6700b4 = typing.Union[Country8beeb162738910001433a1ef009a01d0,typing.Union[bool, date, datetime, dict, float, int, list, str, None]]
