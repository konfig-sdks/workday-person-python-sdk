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


class PhoneNumberValidationDb1991f2fb091000169c5dfa023800b8(
    schemas.ComposedSchema,
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        
        class all_of_0(
            schemas.DictSchema
        ):
        
        
            class MetaOapg:
                
                class properties:
                
                    @staticmethod
                    def deviceType() -> typing.Type['DeviceTypeDb1991f2fb091000169c5e28fc0400bb']:
                        return DeviceTypeDb1991f2fb091000169c5e28fc0400bb
                    completePhoneNumber = schemas.StrSchema
                
                    @staticmethod
                    def countryPhoneCode() -> typing.Type['CountryPhoneCodeDb1991f2fb091000169c5e0cb7c200b9']:
                        return CountryPhoneCodeDb1991f2fb091000169c5e0cb7c200b9
                    __annotations__ = {
                        "deviceType": deviceType,
                        "completePhoneNumber": completePhoneNumber,
                        "countryPhoneCode": countryPhoneCode,
                    }
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["deviceType"]) -> 'DeviceTypeDb1991f2fb091000169c5e28fc0400bb': ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["completePhoneNumber"]) -> MetaOapg.properties.completePhoneNumber: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["countryPhoneCode"]) -> 'CountryPhoneCodeDb1991f2fb091000169c5e0cb7c200b9': ...
            
            @typing.overload
            def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
            
            def __getitem__(self, name: typing.Union[typing_extensions.Literal["deviceType", "completePhoneNumber", "countryPhoneCode", ], str]):
                # dict_instance[name] accessor
                return super().__getitem__(name)
            
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["deviceType"]) -> typing.Union['DeviceTypeDb1991f2fb091000169c5e28fc0400bb', schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["completePhoneNumber"]) -> typing.Union[MetaOapg.properties.completePhoneNumber, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["countryPhoneCode"]) -> typing.Union['CountryPhoneCodeDb1991f2fb091000169c5e0cb7c200b9', schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
            
            def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["deviceType", "completePhoneNumber", "countryPhoneCode", ], str]):
                return super().get_item_oapg(name)
            
        
            def __new__(
                cls,
                *args: typing.Union[dict, frozendict.frozendict, ],
                deviceType: typing.Union['DeviceTypeDb1991f2fb091000169c5e28fc0400bb', schemas.Unset] = schemas.unset,
                completePhoneNumber: typing.Union[MetaOapg.properties.completePhoneNumber, str, schemas.Unset] = schemas.unset,
                countryPhoneCode: typing.Union['CountryPhoneCodeDb1991f2fb091000169c5e0cb7c200b9', schemas.Unset] = schemas.unset,
                _configuration: typing.Optional[schemas.Configuration] = None,
                **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
            ) -> 'all_of_0':
                return super().__new__(
                    cls,
                    *args,
                    deviceType=deviceType,
                    completePhoneNumber=completePhoneNumber,
                    countryPhoneCode=countryPhoneCode,
                    _configuration=_configuration,
                    **kwargs,
                )
        
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
                cls.all_of_0,
            ]


    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'PhoneNumberValidationDb1991f2fb091000169c5dfa023800b8':
        return super().__new__(
            cls,
            *args,
            _configuration=_configuration,
            **kwargs,
        )

from workday_person_python_sdk.model.country_phone_code_db1991f2fb091000169c5e0cb7c200b9 import CountryPhoneCodeDb1991f2fb091000169c5e0cb7c200b9
from workday_person_python_sdk.model.device_type_db1991f2fb091000169c5e28fc0400bb import DeviceTypeDb1991f2fb091000169c5e28fc0400bb
