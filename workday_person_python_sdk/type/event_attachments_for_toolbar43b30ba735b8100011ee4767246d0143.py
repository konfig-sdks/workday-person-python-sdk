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

from workday_person_python_sdk.type.category43b30ba735b8100011ee4781a9d50146 import Category43b30ba735b8100011ee4781a9d50146
from workday_person_python_sdk.type.content_type43b30ba735b8100011ee47993f11014a import ContentType43b30ba735b8100011ee47993f11014a
from workday_person_python_sdk.type.uploaded_by_b32ff437243510000e22e06470370160 import UploadedByB32ff437243510000e22e06470370160

EventAttachmentsForToolbar43b30ba735b8100011ee4767246d0143 = typing.Union[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]]