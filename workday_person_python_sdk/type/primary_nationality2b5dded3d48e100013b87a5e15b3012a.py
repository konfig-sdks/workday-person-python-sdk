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

from workday_person_python_sdk.type.country_and_nationality06544db2578d10000ec1cd4257350000 import CountryAndNationality06544db2578d10000ec1cd4257350000

PrimaryNationality2b5dded3d48e100013b87a5e15b3012a = typing.Union[CountryAndNationality06544db2578d10000ec1cd4257350000,typing.Union[bool, date, datetime, dict, float, int, list, str, None]]