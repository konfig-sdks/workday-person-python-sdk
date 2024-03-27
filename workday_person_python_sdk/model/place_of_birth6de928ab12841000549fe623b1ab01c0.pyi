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


class PlaceOfBirth6de928ab12841000549fe623b1ab01c0(
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
                    city = schemas.StrSchema
                
                    @staticmethod
                    def country() -> typing.Type['Country6de928ab12841000549fe6404b2101c3']:
                        return Country6de928ab12841000549fe6404b2101c3
                
                    @staticmethod
                    def region() -> typing.Type['Region6de928ab12841000549fe6375a9301c2']:
                        return Region6de928ab12841000549fe6375a9301c2
                    __annotations__ = {
                        "city": city,
                        "country": country,
                        "region": region,
                    }
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["city"]) -> MetaOapg.properties.city: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["country"]) -> 'Country6de928ab12841000549fe6404b2101c3': ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["region"]) -> 'Region6de928ab12841000549fe6375a9301c2': ...
            
            @typing.overload
            def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
            
            def __getitem__(self, name: typing.Union[typing_extensions.Literal["city", "country", "region", ], str]):
                # dict_instance[name] accessor
                return super().__getitem__(name)
            
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["city"]) -> typing.Union[MetaOapg.properties.city, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["country"]) -> typing.Union['Country6de928ab12841000549fe6404b2101c3', schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["region"]) -> typing.Union['Region6de928ab12841000549fe6375a9301c2', schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
            
            def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["city", "country", "region", ], str]):
                return super().get_item_oapg(name)
            
        
            def __new__(
                cls,
                *args: typing.Union[dict, frozendict.frozendict, ],
                city: typing.Union[MetaOapg.properties.city, str, schemas.Unset] = schemas.unset,
                country: typing.Union['Country6de928ab12841000549fe6404b2101c3', schemas.Unset] = schemas.unset,
                region: typing.Union['Region6de928ab12841000549fe6375a9301c2', schemas.Unset] = schemas.unset,
                _configuration: typing.Optional[schemas.Configuration] = None,
                **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
            ) -> 'all_of_0':
                return super().__new__(
                    cls,
                    *args,
                    city=city,
                    country=country,
                    region=region,
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
    ) -> 'PlaceOfBirth6de928ab12841000549fe623b1ab01c0':
        return super().__new__(
            cls,
            *args,
            _configuration=_configuration,
            **kwargs,
        )

from workday_person_python_sdk.model.country6de928ab12841000549fe6404b2101c3 import Country6de928ab12841000549fe6404b2101c3
from workday_person_python_sdk.model.region6de928ab12841000549fe6375a9301c2 import Region6de928ab12841000549fe6375a9301c2
