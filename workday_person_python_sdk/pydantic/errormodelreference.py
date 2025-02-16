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


class ERRORMODELREFERENCE(BaseModel):
    # A description of the error
    error: str = Field(alias='error')

    # The code that corresponds to the error message. Use the error code to drive programmatic error-handling behavior. Don't use error message strings for this purpose because they are subject to change
    code: typing.Optional[str] = Field(None, alias='code')

    # The field related to the error
    field: typing.Optional[str] = Field(None, alias='field')

    # The path of the field related to the error
    path: typing.Optional[str] = Field(None, alias='path')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
