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


class PersonPublicRepresentationD8f2aecf3d63100016a77ab413a20235(
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
                    
                    
                    class instantMessengers(
                        schemas.ListSchema
                    ):
                    
                    
                        class MetaOapg:
                            
                            @staticmethod
                            def items() -> typing.Type['InstantMessengerAccount33e26848dc00100036f723337ebb0132']:
                                return InstantMessengerAccount33e26848dc00100036f723337ebb0132
                    
                        def __new__(
                            cls,
                            arg: typing.Union[typing.Tuple['InstantMessengerAccount33e26848dc00100036f723337ebb0132'], typing.List['InstantMessengerAccount33e26848dc00100036f723337ebb0132']],
                            _configuration: typing.Optional[schemas.Configuration] = None,
                        ) -> 'instantMessengers':
                            return super().__new__(
                                cls,
                                arg,
                                _configuration=_configuration,
                            )
                    
                        def __getitem__(self, i: int) -> 'InstantMessengerAccount33e26848dc00100036f723337ebb0132':
                            return super().__getitem__(i)
                    
                    
                    class phoneNumbers(
                        schemas.ListSchema
                    ):
                    
                    
                        class MetaOapg:
                            
                            @staticmethod
                            def items() -> typing.Type['PhoneReferenceDf014bc8b5fa10000af0fe7cb0ab00dd']:
                                return PhoneReferenceDf014bc8b5fa10000af0fe7cb0ab00dd
                    
                        def __new__(
                            cls,
                            arg: typing.Union[typing.Tuple['PhoneReferenceDf014bc8b5fa10000af0fe7cb0ab00dd'], typing.List['PhoneReferenceDf014bc8b5fa10000af0fe7cb0ab00dd']],
                            _configuration: typing.Optional[schemas.Configuration] = None,
                        ) -> 'phoneNumbers':
                            return super().__new__(
                                cls,
                                arg,
                                _configuration=_configuration,
                            )
                    
                        def __getitem__(self, i: int) -> 'PhoneReferenceDf014bc8b5fa10000af0fe7cb0ab00dd':
                            return super().__getitem__(i)
                    
                    
                    class addresses(
                        schemas.ListSchema
                    ):
                    
                    
                        class MetaOapg:
                            
                            @staticmethod
                            def items() -> typing.Type['AddressReference9c3ab7b846e4100009e5ec55fa530024']:
                                return AddressReference9c3ab7b846e4100009e5ec55fa530024
                    
                        def __new__(
                            cls,
                            arg: typing.Union[typing.Tuple['AddressReference9c3ab7b846e4100009e5ec55fa530024'], typing.List['AddressReference9c3ab7b846e4100009e5ec55fa530024']],
                            _configuration: typing.Optional[schemas.Configuration] = None,
                        ) -> 'addresses':
                            return super().__new__(
                                cls,
                                arg,
                                _configuration=_configuration,
                            )
                    
                        def __getitem__(self, i: int) -> 'AddressReference9c3ab7b846e4100009e5ec55fa530024':
                            return super().__getitem__(i)
                    
                    
                    class webAddresses(
                        schemas.ListSchema
                    ):
                    
                    
                        class MetaOapg:
                            
                            @staticmethod
                            def items() -> typing.Type['WebAddress33e26848dc0010003893a0202ced0165']:
                                return WebAddress33e26848dc0010003893a0202ced0165
                    
                        def __new__(
                            cls,
                            arg: typing.Union[typing.Tuple['WebAddress33e26848dc0010003893a0202ced0165'], typing.List['WebAddress33e26848dc0010003893a0202ced0165']],
                            _configuration: typing.Optional[schemas.Configuration] = None,
                        ) -> 'webAddresses':
                            return super().__new__(
                                cls,
                                arg,
                                _configuration=_configuration,
                            )
                    
                        def __getitem__(self, i: int) -> 'WebAddress33e26848dc0010003893a0202ced0165':
                            return super().__getitem__(i)
                    
                    
                    class emails(
                        schemas.ListSchema
                    ):
                    
                    
                        class MetaOapg:
                            
                            @staticmethod
                            def items() -> typing.Type['EmailReference9c3ab7b846e41000327e788d9664012a']:
                                return EmailReference9c3ab7b846e41000327e788d9664012a
                    
                        def __new__(
                            cls,
                            arg: typing.Union[typing.Tuple['EmailReference9c3ab7b846e41000327e788d9664012a'], typing.List['EmailReference9c3ab7b846e41000327e788d9664012a']],
                            _configuration: typing.Optional[schemas.Configuration] = None,
                        ) -> 'emails':
                            return super().__new__(
                                cls,
                                arg,
                                _configuration=_configuration,
                            )
                    
                        def __getitem__(self, i: int) -> 'EmailReference9c3ab7b846e41000327e788d9664012a':
                            return super().__getitem__(i)
                    __annotations__ = {
                        "instantMessengers": instantMessengers,
                        "phoneNumbers": phoneNumbers,
                        "addresses": addresses,
                        "webAddresses": webAddresses,
                        "emails": emails,
                    }
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["instantMessengers"]) -> MetaOapg.properties.instantMessengers: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["phoneNumbers"]) -> MetaOapg.properties.phoneNumbers: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["addresses"]) -> MetaOapg.properties.addresses: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["webAddresses"]) -> MetaOapg.properties.webAddresses: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["emails"]) -> MetaOapg.properties.emails: ...
            
            @typing.overload
            def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
            
            def __getitem__(self, name: typing.Union[typing_extensions.Literal["instantMessengers", "phoneNumbers", "addresses", "webAddresses", "emails", ], str]):
                # dict_instance[name] accessor
                return super().__getitem__(name)
            
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["instantMessengers"]) -> typing.Union[MetaOapg.properties.instantMessengers, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["phoneNumbers"]) -> typing.Union[MetaOapg.properties.phoneNumbers, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["addresses"]) -> typing.Union[MetaOapg.properties.addresses, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["webAddresses"]) -> typing.Union[MetaOapg.properties.webAddresses, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["emails"]) -> typing.Union[MetaOapg.properties.emails, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
            
            def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["instantMessengers", "phoneNumbers", "addresses", "webAddresses", "emails", ], str]):
                return super().get_item_oapg(name)
            
        
            def __new__(
                cls,
                *args: typing.Union[dict, frozendict.frozendict, ],
                instantMessengers: typing.Union[MetaOapg.properties.instantMessengers, list, tuple, schemas.Unset] = schemas.unset,
                phoneNumbers: typing.Union[MetaOapg.properties.phoneNumbers, list, tuple, schemas.Unset] = schemas.unset,
                addresses: typing.Union[MetaOapg.properties.addresses, list, tuple, schemas.Unset] = schemas.unset,
                webAddresses: typing.Union[MetaOapg.properties.webAddresses, list, tuple, schemas.Unset] = schemas.unset,
                emails: typing.Union[MetaOapg.properties.emails, list, tuple, schemas.Unset] = schemas.unset,
                _configuration: typing.Optional[schemas.Configuration] = None,
                **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
            ) -> 'all_of_0':
                return super().__new__(
                    cls,
                    *args,
                    instantMessengers=instantMessengers,
                    phoneNumbers=phoneNumbers,
                    addresses=addresses,
                    webAddresses=webAddresses,
                    emails=emails,
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
    ) -> 'PersonPublicRepresentationD8f2aecf3d63100016a77ab413a20235':
        return super().__new__(
            cls,
            *args,
            _configuration=_configuration,
            **kwargs,
        )

from workday_person_python_sdk.model.address_reference9c3ab7b846e4100009e5ec55fa530024 import AddressReference9c3ab7b846e4100009e5ec55fa530024
from workday_person_python_sdk.model.email_reference9c3ab7b846e41000327e788d9664012a import EmailReference9c3ab7b846e41000327e788d9664012a
from workday_person_python_sdk.model.instant_messenger_account33e26848dc00100036f723337ebb0132 import InstantMessengerAccount33e26848dc00100036f723337ebb0132
from workday_person_python_sdk.model.phone_reference_df014bc8b5fa10000af0fe7cb0ab00dd import PhoneReferenceDf014bc8b5fa10000af0fe7cb0ab00dd
from workday_person_python_sdk.model.web_address33e26848dc0010003893a0202ced0165 import WebAddress33e26848dc0010003893a0202ced0165