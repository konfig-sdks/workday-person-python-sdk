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

from workday_person_python_sdk.pydantic.aboriginal_indigenous_identification37580627f49d10002587d93d0a820000 import AboriginalIndigenousIdentification37580627f49d10002587d93d0a820000

AboriginalIndigenousIdentification37580627f49d1000258f815dc9c00001 = typing.Union[AboriginalIndigenousIdentification37580627f49d10002587d93d0a820000,typing.Union[bool, date, datetime, dict, float, int, list, str, None]]