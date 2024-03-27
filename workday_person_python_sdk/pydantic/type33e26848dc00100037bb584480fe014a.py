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

from workday_person_python_sdk.pydantic.instant_messenger_type_ab827579ee17100023fd6abda45c01b9 import InstantMessengerTypeAb827579ee17100023fd6abda45c01b9

Type33e26848dc00100037bb584480fe014a = typing.Union[InstantMessengerTypeAb827579ee17100023fd6abda45c01b9,typing.Union[bool, date, datetime, dict, float, int, list, str, None]]
