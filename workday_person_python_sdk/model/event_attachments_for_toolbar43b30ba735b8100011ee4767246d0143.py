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


class EventAttachmentsForToolbar43b30ba735b8100011ee4767246d0143(
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
                    description = schemas.StrSchema
                
                    @staticmethod
                    def contentType() -> typing.Type['ContentType43b30ba735b8100011ee47993f11014a']:
                        return ContentType43b30ba735b8100011ee47993f11014a
                    fileLength = schemas.IntSchema
                    uploadDate = schemas.DateSchema
                    
                    
                    class fileName(
                        schemas.StrSchema
                    ):
                    
                    
                        class MetaOapg:
                            max_length = 255
                
                    @staticmethod
                    def uploadedBy() -> typing.Type['UploadedByB32ff437243510000e22e06470370160']:
                        return UploadedByB32ff437243510000e22e06470370160
                
                    @staticmethod
                    def category() -> typing.Type['Category43b30ba735b8100011ee4781a9d50146']:
                        return Category43b30ba735b8100011ee4781a9d50146
                    id = schemas.StrSchema
                    __annotations__ = {
                        "description": description,
                        "contentType": contentType,
                        "fileLength": fileLength,
                        "uploadDate": uploadDate,
                        "fileName": fileName,
                        "uploadedBy": uploadedBy,
                        "category": category,
                        "id": id,
                    }
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["description"]) -> MetaOapg.properties.description: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["contentType"]) -> 'ContentType43b30ba735b8100011ee47993f11014a': ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["fileLength"]) -> MetaOapg.properties.fileLength: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["uploadDate"]) -> MetaOapg.properties.uploadDate: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["fileName"]) -> MetaOapg.properties.fileName: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["uploadedBy"]) -> 'UploadedByB32ff437243510000e22e06470370160': ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["category"]) -> 'Category43b30ba735b8100011ee4781a9d50146': ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
            
            @typing.overload
            def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
            
            def __getitem__(self, name: typing.Union[typing_extensions.Literal["description", "contentType", "fileLength", "uploadDate", "fileName", "uploadedBy", "category", "id", ], str]):
                # dict_instance[name] accessor
                return super().__getitem__(name)
            
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["description"]) -> typing.Union[MetaOapg.properties.description, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["contentType"]) -> typing.Union['ContentType43b30ba735b8100011ee47993f11014a', schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["fileLength"]) -> typing.Union[MetaOapg.properties.fileLength, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["uploadDate"]) -> typing.Union[MetaOapg.properties.uploadDate, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["fileName"]) -> typing.Union[MetaOapg.properties.fileName, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["uploadedBy"]) -> typing.Union['UploadedByB32ff437243510000e22e06470370160', schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["category"]) -> typing.Union['Category43b30ba735b8100011ee4781a9d50146', schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
            
            def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["description", "contentType", "fileLength", "uploadDate", "fileName", "uploadedBy", "category", "id", ], str]):
                return super().get_item_oapg(name)
            
        
            def __new__(
                cls,
                *args: typing.Union[dict, frozendict.frozendict, ],
                description: typing.Union[MetaOapg.properties.description, str, schemas.Unset] = schemas.unset,
                contentType: typing.Union['ContentType43b30ba735b8100011ee47993f11014a', schemas.Unset] = schemas.unset,
                fileLength: typing.Union[MetaOapg.properties.fileLength, decimal.Decimal, int, schemas.Unset] = schemas.unset,
                uploadDate: typing.Union[MetaOapg.properties.uploadDate, str, date, schemas.Unset] = schemas.unset,
                fileName: typing.Union[MetaOapg.properties.fileName, str, schemas.Unset] = schemas.unset,
                uploadedBy: typing.Union['UploadedByB32ff437243510000e22e06470370160', schemas.Unset] = schemas.unset,
                category: typing.Union['Category43b30ba735b8100011ee4781a9d50146', schemas.Unset] = schemas.unset,
                id: typing.Union[MetaOapg.properties.id, str, schemas.Unset] = schemas.unset,
                _configuration: typing.Optional[schemas.Configuration] = None,
                **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
            ) -> 'all_of_0':
                return super().__new__(
                    cls,
                    *args,
                    description=description,
                    contentType=contentType,
                    fileLength=fileLength,
                    uploadDate=uploadDate,
                    fileName=fileName,
                    uploadedBy=uploadedBy,
                    category=category,
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
    ) -> 'EventAttachmentsForToolbar43b30ba735b8100011ee4767246d0143':
        return super().__new__(
            cls,
            *args,
            _configuration=_configuration,
            **kwargs,
        )

from workday_person_python_sdk.model.category43b30ba735b8100011ee4781a9d50146 import Category43b30ba735b8100011ee4781a9d50146
from workday_person_python_sdk.model.content_type43b30ba735b8100011ee47993f11014a import ContentType43b30ba735b8100011ee47993f11014a
from workday_person_python_sdk.model.uploaded_by_b32ff437243510000e22e06470370160 import UploadedByB32ff437243510000e22e06470370160
