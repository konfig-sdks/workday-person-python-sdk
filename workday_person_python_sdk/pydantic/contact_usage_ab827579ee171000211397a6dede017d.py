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

from workday_person_python_sdk.pydantic.usage_behavior33e26848dc0010003a3c3827858901b4 import UsageBehavior33e26848dc0010003a3c3827858901b4
from workday_person_python_sdk.pydantic.usage_type901718dd5e7910000cb06dace3950299 import UsageType901718dd5e7910000cb06dace3950299

ContactUsageAb827579ee171000211397a6dede017d = typing.Union[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]]