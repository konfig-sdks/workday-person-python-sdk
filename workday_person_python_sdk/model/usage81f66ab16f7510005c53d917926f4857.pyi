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


class Usage81f66ab16f7510005c53d917926f4857(
    schemas.ComposedSchema,
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Address Instance Referenced
    """


    class MetaOapg:
        all_of_1 = schemas.AnyTypeSchema
        
        @classmethod
        @functools.lru_cache()
        def all_of(cls):
            # we need this here to make our import statements work
            # we must store _composed_schemas in here so the code is only run
            # when we invoke this method. If we kept this at the class
            # level we would get an error because the class level
            # code would be run when this module is imported, and these composed
            # classes don't exist yet because their module has not finished
            # loading
            return [
                HomeContactUsageC1bb9f46f65210002d3c341a5dc400b8,
                cls.all_of_1,
            ]


    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'Usage81f66ab16f7510005c53d917926f4857':
        return super().__new__(
            cls,
            *args,
            _configuration=_configuration,
            **kwargs,
        )

from workday_person_python_sdk.model.home_contact_usage_c1bb9f46f65210002d3c341a5dc400b8 import HomeContactUsageC1bb9f46f65210002d3c341a5dc400b8
