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

from workday_person_python_sdk.pydantic.work_contact_usage81f66ab16f7510005c60769e6db24871 import WorkContactUsage81f66ab16f7510005c60769e6db24871

UsageC1bb9f46f65210002d2fa2e7babe00a8 = typing.Union[WorkContactUsage81f66ab16f7510005c60769e6db24871,typing.Union[bool, date, datetime, dict, float, int, list, str, None]]
