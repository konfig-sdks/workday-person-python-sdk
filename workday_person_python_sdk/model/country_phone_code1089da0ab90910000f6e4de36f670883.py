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


class CountryPhoneCode1089da0ab90910000f6e4de36f670883(
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
                    countryPhoneCode = schemas.StrSchema
                
                    @staticmethod
                    def country() -> typing.Type['Country1089da0ab90910000f6e4df524710885']:
                        return Country1089da0ab90910000f6e4df524710885
                    descriptor = schemas.StrSchema
                    id = schemas.StrSchema
                    __annotations__ = {
                        "countryPhoneCode": countryPhoneCode,
                        "country": country,
                        "descriptor": descriptor,
                        "id": id,
                    }
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["countryPhoneCode"]) -> MetaOapg.properties.countryPhoneCode: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["country"]) -> 'Country1089da0ab90910000f6e4df524710885': ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["descriptor"]) -> MetaOapg.properties.descriptor: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
            
            @typing.overload
            def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
            
            def __getitem__(self, name: typing.Union[typing_extensions.Literal["countryPhoneCode", "country", "descriptor", "id", ], str]):
                # dict_instance[name] accessor
                return super().__getitem__(name)
            
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["countryPhoneCode"]) -> typing.Union[MetaOapg.properties.countryPhoneCode, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["country"]) -> typing.Union['Country1089da0ab90910000f6e4df524710885', schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["descriptor"]) -> typing.Union[MetaOapg.properties.descriptor, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
            
            def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["countryPhoneCode", "country", "descriptor", "id", ], str]):
                return super().get_item_oapg(name)
            
        
            def __new__(
                cls,
                *args: typing.Union[dict, frozendict.frozendict, ],
                countryPhoneCode: typing.Union[MetaOapg.properties.countryPhoneCode, str, schemas.Unset] = schemas.unset,
                country: typing.Union['Country1089da0ab90910000f6e4df524710885', schemas.Unset] = schemas.unset,
                descriptor: typing.Union[MetaOapg.properties.descriptor, str, schemas.Unset] = schemas.unset,
                id: typing.Union[MetaOapg.properties.id, str, schemas.Unset] = schemas.unset,
                _configuration: typing.Optional[schemas.Configuration] = None,
                **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
            ) -> 'all_of_0':
                return super().__new__(
                    cls,
                    *args,
                    countryPhoneCode=countryPhoneCode,
                    country=country,
                    descriptor=descriptor,
                    id=id,
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
    ) -> 'CountryPhoneCode1089da0ab90910000f6e4de36f670883':
        return super().__new__(
            cls,
            *args,
            _configuration=_configuration,
            **kwargs,
        )

from workday_person_python_sdk.model.country1089da0ab90910000f6e4df524710885 import Country1089da0ab90910000f6e4df524710885
