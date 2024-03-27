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

from workday_person_python_sdk.type.country_a58f621b14ee1000146a3350196300e7 import CountryA58f621b14ee1000146a3350196300e7
from workday_person_python_sdk.type.country_city_a58f621b14ee1000146a333da1c900e6 import CountryCityA58f621b14ee1000146a333da1c900e6
from workday_person_python_sdk.type.country_region_a58f621b14ee100014b01c1cbabe00f4 import CountryRegionA58f621b14ee100014b01c1cbabe00f4
from workday_person_python_sdk.type.usage_a58f621b14ee100014b01c034eeb00f3 import UsageA58f621b14ee100014b01c034eeb00f3

AddressReference9c3ab7b846e4100009e5ec55fa530024 = typing.Union[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]]
