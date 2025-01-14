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

from workday_person_python_sdk.pydantic.military_discharge_type_reference_b26f12db214d100010f22b23c4e70000 import MilitaryDischargeTypeReferenceB26f12db214d100010f22b23c4e70000
from workday_person_python_sdk.pydantic.military_service_reference6de928ab128410005b41e4b2f27d021e import MilitaryServiceReference6de928ab128410005b41e4b2f27d021e
from workday_person_python_sdk.pydantic.rank6de928ab128410005b41e4ba56a6021f import Rank6de928ab128410005b41e4ba56a6021f
from workday_person_python_sdk.pydantic.status6de928ab128410005b41e4a4e4d2021c import Status6de928ab128410005b41e4a4e4d2021c
from workday_person_python_sdk.pydantic.type6de928ab128410005b41e4ac0ec5021d import Type6de928ab128410005b41e4ac0ec5021d

MilitaryService6de928ab128410005b41e47e6d890218 = typing.Union[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]]
