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


class VeteransPreference898f4bc8578c100010cc072a1b140000(
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
                    militaryServicePreferenceName = schemas.StrSchema
                    militaryServicePreferenceCode = schemas.StrSchema
                    inactive = schemas.BoolSchema
                    militaryServicePreferenceDescription = schemas.StrSchema
                    descriptor = schemas.StrSchema
                    id = schemas.StrSchema
                    __annotations__ = {
                        "militaryServicePreferenceName": militaryServicePreferenceName,
                        "militaryServicePreferenceCode": militaryServicePreferenceCode,
                        "inactive": inactive,
                        "militaryServicePreferenceDescription": militaryServicePreferenceDescription,
                        "descriptor": descriptor,
                        "id": id,
                    }
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["militaryServicePreferenceName"]) -> MetaOapg.properties.militaryServicePreferenceName: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["militaryServicePreferenceCode"]) -> MetaOapg.properties.militaryServicePreferenceCode: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["inactive"]) -> MetaOapg.properties.inactive: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["militaryServicePreferenceDescription"]) -> MetaOapg.properties.militaryServicePreferenceDescription: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["descriptor"]) -> MetaOapg.properties.descriptor: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
            
            @typing.overload
            def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
            
            def __getitem__(self, name: typing.Union[typing_extensions.Literal["militaryServicePreferenceName", "militaryServicePreferenceCode", "inactive", "militaryServicePreferenceDescription", "descriptor", "id", ], str]):
                # dict_instance[name] accessor
                return super().__getitem__(name)
            
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["militaryServicePreferenceName"]) -> typing.Union[MetaOapg.properties.militaryServicePreferenceName, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["militaryServicePreferenceCode"]) -> typing.Union[MetaOapg.properties.militaryServicePreferenceCode, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["inactive"]) -> typing.Union[MetaOapg.properties.inactive, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["militaryServicePreferenceDescription"]) -> typing.Union[MetaOapg.properties.militaryServicePreferenceDescription, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["descriptor"]) -> typing.Union[MetaOapg.properties.descriptor, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
            
            def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["militaryServicePreferenceName", "militaryServicePreferenceCode", "inactive", "militaryServicePreferenceDescription", "descriptor", "id", ], str]):
                return super().get_item_oapg(name)
            
        
            def __new__(
                cls,
                *args: typing.Union[dict, frozendict.frozendict, ],
                militaryServicePreferenceName: typing.Union[MetaOapg.properties.militaryServicePreferenceName, str, schemas.Unset] = schemas.unset,
                militaryServicePreferenceCode: typing.Union[MetaOapg.properties.militaryServicePreferenceCode, str, schemas.Unset] = schemas.unset,
                inactive: typing.Union[MetaOapg.properties.inactive, bool, schemas.Unset] = schemas.unset,
                militaryServicePreferenceDescription: typing.Union[MetaOapg.properties.militaryServicePreferenceDescription, str, schemas.Unset] = schemas.unset,
                descriptor: typing.Union[MetaOapg.properties.descriptor, str, schemas.Unset] = schemas.unset,
                id: typing.Union[MetaOapg.properties.id, str, schemas.Unset] = schemas.unset,
                _configuration: typing.Optional[schemas.Configuration] = None,
                **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
            ) -> 'all_of_0':
                return super().__new__(
                    cls,
                    *args,
                    militaryServicePreferenceName=militaryServicePreferenceName,
                    militaryServicePreferenceCode=militaryServicePreferenceCode,
                    inactive=inactive,
                    militaryServicePreferenceDescription=militaryServicePreferenceDescription,
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
    ) -> 'VeteransPreference898f4bc8578c100010cc072a1b140000':
        return super().__new__(
            cls,
            *args,
            _configuration=_configuration,
            **kwargs,
        )
