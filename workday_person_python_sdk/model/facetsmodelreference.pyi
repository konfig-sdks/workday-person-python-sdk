# coding: utf-8

"""
    person

    The Person REST APIs enable you to access information about the worker person, including country-specific configuration information about name components.

    The version of the OpenAPI document: v4
    Generated by: https://konfigthis.com
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from workday_person_python_sdk import schemas  # noqa: F401


class FACETSMODELREFERENCE(
    schemas.ListSchema
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        @staticmethod
        def items() -> typing.Type['FACETSMODELREFERENCEItem']:
            return FACETSMODELREFERENCEItem

    def __new__(
        cls,
        arg: typing.Union[typing.Tuple['FACETSMODELREFERENCEItem'], typing.List['FACETSMODELREFERENCEItem']],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'FACETSMODELREFERENCE':
        return super().__new__(
            cls,
            arg,
            _configuration=_configuration,
        )

    def __getitem__(self, i: int) -> 'FACETSMODELREFERENCEItem':
        return super().__getitem__(i)

from workday_person_python_sdk.model.facetsmodelreference_item import FACETSMODELREFERENCEItem