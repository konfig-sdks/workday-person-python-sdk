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

from workday_person_python_sdk.pydantic.certification_basis6de928ab128410005c56a638b9d4024c import CertificationBasis6de928ab128410005c56a638b9d4024c
from workday_person_python_sdk.pydantic.disability6de928ab128410005c56a64ec69f024f import Disability6de928ab128410005c56a64ec69f024f
from workday_person_python_sdk.pydantic.grade6de928ab128410005c56a5feed2e0244 import Grade6de928ab128410005c56a5feed2e0244
from workday_person_python_sdk.pydantic.worker_document15d8b82e323110000e0117c92d9803b2 import WorkerDocument15d8b82e323110000e0117c92d9803b2

DisabilityStatus6de928ab128410005c56a5a5299c0239 = typing.Union[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]]
