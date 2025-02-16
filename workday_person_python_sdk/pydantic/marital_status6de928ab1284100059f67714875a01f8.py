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

from workday_person_python_sdk.pydantic.marital_status_information6de928ab1284100059f5dc52629b01f4 import MaritalStatusInformation6de928ab1284100059f5dc52629b01f4

MaritalStatus6de928ab1284100059f67714875a01f8 = typing.Union[MaritalStatusInformation6de928ab1284100059f5dc52629b01f4,typing.Union[bool, date, datetime, dict, float, int, list, str, None]]
