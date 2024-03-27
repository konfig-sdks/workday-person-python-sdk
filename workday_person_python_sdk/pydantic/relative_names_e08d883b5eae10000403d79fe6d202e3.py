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

from workday_person_python_sdk.pydantic.academic_suffix_e08d883b5eae10000403d7c0735402e9 import AcademicSuffixE08d883b5eae10000403d7c0735402e9
from workday_person_python_sdk.pydantic.country_e08d883b5eae10000403d7c8e60502eb import CountryE08d883b5eae10000403d7c8e60502eb
from workday_person_python_sdk.pydantic.hereditary_suffix_e08d883b5eae10000403d7efe24b02f3 import HereditarySuffixE08d883b5eae10000403d7efe24b02f3
from workday_person_python_sdk.pydantic.honorary_suffix_e08d883b5eae10000403d7acba9602e5 import HonorarySuffixE08d883b5eae10000403d7acba9602e5
from workday_person_python_sdk.pydantic.local_person_name_e08d883b5eae10000403d7cd713c02ec import LocalPersonNameE08d883b5eae10000403d7cd713c02ec
from workday_person_python_sdk.pydantic.professional_suffix_e08d883b5eae10000403d7e2171f02f0 import ProfessionalSuffixE08d883b5eae10000403d7e2171f02f0
from workday_person_python_sdk.pydantic.relative_type_e08d883b5eae1000040cc1231a5902f5 import RelativeTypeE08d883b5eae1000040cc1231a5902f5
from workday_person_python_sdk.pydantic.religious_suffix_e08d883b5eae10000403d7eb401e02f2 import ReligiousSuffixE08d883b5eae10000403d7eb401e02f2
from workday_person_python_sdk.pydantic.royal_suffix_e08d883b5eae10000403d7d259db02ed import RoyalSuffixE08d883b5eae10000403d7d259db02ed
from workday_person_python_sdk.pydantic.salutation_suffix_e08d883b5eae10000403d7d736c102ee import SalutationSuffixE08d883b5eae10000403d7d736c102ee
from workday_person_python_sdk.pydantic.social_suffix_e08d883b5eae10000403d7dc081502ef import SocialSuffixE08d883b5eae10000403d7dc081502ef
from workday_person_python_sdk.pydantic.title_e08d883b5eae10000403d7b62abb02e7 import TitleE08d883b5eae10000403d7b62abb02e7

RelativeNamesE08d883b5eae10000403d79fe6d202e3 = typing.Union[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]]