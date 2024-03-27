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

from workday_person_python_sdk.pydantic.disability15d8b82e323110000d98d0fc4d9903a5 import Disability15d8b82e323110000d98d0fc4d9903a5

Disability6de928ab128410005c56a64ec69f024f = typing.Union[Disability15d8b82e323110000d98d0fc4d9903a5,typing.Union[bool, date, datetime, dict, float, int, list, str, None]]
