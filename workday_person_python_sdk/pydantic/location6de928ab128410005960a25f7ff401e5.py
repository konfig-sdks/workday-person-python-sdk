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

from workday_person_python_sdk.pydantic.location_aaeb64c958b2100011f0c7fc94120224 import LocationAaeb64c958b2100011f0c7fc94120224

Location6de928ab128410005960a25f7ff401e5 = typing.Union[LocationAaeb64c958b2100011f0c7fc94120224,typing.Union[bool, date, datetime, dict, float, int, list, str, None]]