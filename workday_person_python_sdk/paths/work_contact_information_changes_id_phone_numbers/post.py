# coding: utf-8

"""
    person

    The Person REST APIs enable you to access information about the worker person, including country-specific configuration information about name components.

    The version of the OpenAPI document: v4
    Generated by: https://konfigthis.com
"""

from dataclasses import dataclass
import typing_extensions
import urllib3
from pydantic import RootModel
from workday_person_python_sdk.request_before_hook import request_before_hook
import json
from urllib3._collections import HTTPHeaderDict

from workday_person_python_sdk.api_response import AsyncGeneratorResponse
from workday_person_python_sdk import api_client, exceptions
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

from workday_person_python_sdk.model.country_phone_code1089da0ab90910000f7089365467088c import CountryPhoneCode1089da0ab90910000f7089365467088c as CountryPhoneCode1089da0ab90910000f7089365467088cSchema
from workday_person_python_sdk.model.errormodelreference import ERRORMODELREFERENCE as ERRORMODELREFERENCESchema
from workday_person_python_sdk.model.device_type1089da0ab90910000f7089256c7b0888 import DeviceType1089da0ab90910000f7089256c7b0888 as DeviceType1089da0ab90910000f7089256c7b0888Schema
from workday_person_python_sdk.model.usage1089da0ab90910000f70892f2de3088a import Usage1089da0ab90910000f70892f2de3088a as Usage1089da0ab90910000f70892f2de3088aSchema
from workday_person_python_sdk.model.phone_reference1089da0ab90910000f70891a998b0887 import PhoneReference1089da0ab90910000f70891a998b0887 as PhoneReference1089da0ab90910000f70891a998b0887Schema
from workday_person_python_sdk.model.validationerrormodelreference import VALIDATIONERRORMODELREFERENCE as VALIDATIONERRORMODELREFERENCESchema

from workday_person_python_sdk.type.phone_reference1089da0ab90910000f70891a998b0887 import PhoneReference1089da0ab90910000f70891a998b0887
from workday_person_python_sdk.type.validationerrormodelreference import VALIDATIONERRORMODELREFERENCE
from workday_person_python_sdk.type.errormodelreference import ERRORMODELREFERENCE
from workday_person_python_sdk.type.device_type1089da0ab90910000f7089256c7b0888 import DeviceType1089da0ab90910000f7089256c7b0888
from workday_person_python_sdk.type.usage1089da0ab90910000f70892f2de3088a import Usage1089da0ab90910000f70892f2de3088a
from workday_person_python_sdk.type.country_phone_code1089da0ab90910000f7089365467088c import CountryPhoneCode1089da0ab90910000f7089365467088c

from ...api_client import Dictionary
from workday_person_python_sdk.pydantic.usage1089da0ab90910000f70892f2de3088a import Usage1089da0ab90910000f70892f2de3088a as Usage1089da0ab90910000f70892f2de3088aPydantic
from workday_person_python_sdk.pydantic.country_phone_code1089da0ab90910000f7089365467088c import CountryPhoneCode1089da0ab90910000f7089365467088c as CountryPhoneCode1089da0ab90910000f7089365467088cPydantic
from workday_person_python_sdk.pydantic.device_type1089da0ab90910000f7089256c7b0888 import DeviceType1089da0ab90910000f7089256c7b0888 as DeviceType1089da0ab90910000f7089256c7b0888Pydantic
from workday_person_python_sdk.pydantic.phone_reference1089da0ab90910000f70891a998b0887 import PhoneReference1089da0ab90910000f70891a998b0887 as PhoneReference1089da0ab90910000f70891a998b0887Pydantic
from workday_person_python_sdk.pydantic.errormodelreference import ERRORMODELREFERENCE as ERRORMODELREFERENCEPydantic
from workday_person_python_sdk.pydantic.validationerrormodelreference import VALIDATIONERRORMODELREFERENCE as VALIDATIONERRORMODELREFERENCEPydantic

from . import path

# Path params
IDSchema = schemas.StrSchema
RequestRequiredPathParams = typing_extensions.TypedDict(
    'RequestRequiredPathParams',
    {
        'ID': typing.Union[IDSchema, str, ],
    }
)
RequestOptionalPathParams = typing_extensions.TypedDict(
    'RequestOptionalPathParams',
    {
    },
    total=False
)


class RequestPathParams(RequestRequiredPathParams, RequestOptionalPathParams):
    pass


request_path_id = api_client.PathParameter(
    name="ID",
    style=api_client.ParameterStyle.SIMPLE,
    schema=IDSchema,
    required=True,
)
# body param
SchemaForRequestBodyApplicationJson = PhoneReference1089da0ab90910000f70891a998b0887Schema


request_body_phone_reference1089da0ab90910000f70891a998b0887 = api_client.RequestBody(
    content={
        'application/json': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJson),
    },
    required=True,
)
SchemaFor201ResponseBodyApplicationJson = PhoneReference1089da0ab90910000f70891a998b0887Schema


@dataclass
class ApiResponseFor201(api_client.ApiResponse):
    body: PhoneReference1089da0ab90910000f70891a998b0887


@dataclass
class ApiResponseFor201Async(api_client.AsyncApiResponse):
    body: PhoneReference1089da0ab90910000f70891a998b0887


_response_for_201 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor201,
    response_cls_async=ApiResponseFor201Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor201ResponseBodyApplicationJson),
    },
)
SchemaFor400ResponseBodyApplicationJson = VALIDATIONERRORMODELREFERENCESchema


@dataclass
class ApiResponseFor400(api_client.ApiResponse):
    body: VALIDATIONERRORMODELREFERENCE


@dataclass
class ApiResponseFor400Async(api_client.AsyncApiResponse):
    body: VALIDATIONERRORMODELREFERENCE


_response_for_400 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor400,
    response_cls_async=ApiResponseFor400Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor400ResponseBodyApplicationJson),
    },
)
SchemaFor401ResponseBodyApplicationJson = VALIDATIONERRORMODELREFERENCESchema


@dataclass
class ApiResponseFor401(api_client.ApiResponse):
    body: VALIDATIONERRORMODELREFERENCE


@dataclass
class ApiResponseFor401Async(api_client.AsyncApiResponse):
    body: VALIDATIONERRORMODELREFERENCE


_response_for_401 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor401,
    response_cls_async=ApiResponseFor401Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor401ResponseBodyApplicationJson),
    },
)
SchemaFor403ResponseBodyApplicationJson = VALIDATIONERRORMODELREFERENCESchema


@dataclass
class ApiResponseFor403(api_client.ApiResponse):
    body: VALIDATIONERRORMODELREFERENCE


@dataclass
class ApiResponseFor403Async(api_client.AsyncApiResponse):
    body: VALIDATIONERRORMODELREFERENCE


_response_for_403 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor403,
    response_cls_async=ApiResponseFor403Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor403ResponseBodyApplicationJson),
    },
)
SchemaFor404ResponseBodyApplicationJson = VALIDATIONERRORMODELREFERENCESchema


@dataclass
class ApiResponseFor404(api_client.ApiResponse):
    body: VALIDATIONERRORMODELREFERENCE


@dataclass
class ApiResponseFor404Async(api_client.AsyncApiResponse):
    body: VALIDATIONERRORMODELREFERENCE


_response_for_404 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor404,
    response_cls_async=ApiResponseFor404Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor404ResponseBodyApplicationJson),
    },
)
SchemaFor0ResponseBodyApplicationJson = ERRORMODELREFERENCESchema


@dataclass
class ApiResponseForDefault(api_client.ApiResponse):
    body: ERRORMODELREFERENCE


@dataclass
class ApiResponseForDefaultAsync(api_client.AsyncApiResponse):
    body: ERRORMODELREFERENCE


_response_for_default = api_client.OpenApiResponse(
    response_cls=ApiResponseForDefault,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor0ResponseBodyApplicationJson),
    },
)
_status_code_to_response = {
    '201': _response_for_201,
    '400': _response_for_400,
    '401': _response_for_401,
    '403': _response_for_403,
    '404': _response_for_404,
    'default': _response_for_default,
}
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):

    def _create_phone_number_mapped_args(
        self,
        id: str,
        extension: typing.Optional[str] = None,
        complete_phone_number: typing.Optional[str] = None,
        country_phone_code: typing.Optional[CountryPhoneCode1089da0ab90910000f7089365467088c] = None,
        device_type: typing.Optional[DeviceType1089da0ab90910000f7089256c7b0888] = None,
        usage: typing.Optional[Usage1089da0ab90910000f70892f2de3088a] = None,
        descriptor: typing.Optional[str] = None,
        id: typing.Optional[str] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _path_params = {}
        _body = {}
        if extension is not None:
            _body["extension"] = extension
        if complete_phone_number is not None:
            _body["completePhoneNumber"] = complete_phone_number
        if country_phone_code is not None:
            _body["countryPhoneCode"] = country_phone_code
        if device_type is not None:
            _body["deviceType"] = device_type
        if usage is not None:
            _body["usage"] = usage
        if descriptor is not None:
            _body["descriptor"] = descriptor
        if id is not None:
            _body["id"] = id
        args.body = _body
        if id is not None:
            _path_params["ID"] = id
        args.path = _path_params
        return args

    async def _acreate_phone_number_oapg(
        self,
        body: typing.Any = None,
            path_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/json',
        stream: bool = False,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor201Async,
        ApiResponseForDefaultAsync,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        """
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_id,
        ):
            parameter_data = path_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _path_params.update(serialized_data)
    
        for k, v in _path_params.items():
            used_path = used_path.replace('{%s}' % k, v)
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'post'.upper()
        _headers.add('Content-Type', content_type)
    
        if body is schemas.unset:
            raise exceptions.ApiValueError(
                'The required body parameter has an invalid value of: unset. Set a valid value instead')
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/workContactInformationChanges/{ID}/phoneNumbers',
            body=body,
            headers=_headers,
        )
        serialized_data = request_body_phone_reference1089da0ab90910000f70891a998b0887.serialize(body, content_type)
        if 'fields' in serialized_data:
            _fields = serialized_data['fields']
        elif 'body' in serialized_data:
            _body = serialized_data['body']
    
        response = await self.api_client.async_call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            fields=_fields,
            serialized_body=_body,
            body=body,
            timeout=timeout,
            **kwargs
        )
    
        if stream:
            if not 200 <= response.http_response.status <= 299:
                body = (await response.http_response.content.read()).decode("utf-8")
                raise exceptions.ApiStreamingException(
                    status=response.http_response.status,
                    reason=response.http_response.reason,
                    body=body,
                )
    
            async def stream_iterator():
                """
                iterates over response.http_response.content and closes connection once iteration has finished
                """
                async for line in response.http_response.content:
                    if line == b'\r\n':
                        continue
                    yield line
                response.http_response.close()
                await response.session.close()
            return AsyncGeneratorResponse(
                content=stream_iterator(),
                headers=response.http_response.headers,
                status=response.http_response.status,
                response=response.http_response
            )
    
        response_for_status = _status_code_to_response.get(str(response.http_response.status))
        if response_for_status:
            api_response = await response_for_status.deserialize_async(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
        else:
            default_response = _status_code_to_response.get('default')
            if default_response:
                api_response = default_response.deserialize(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
            else:
                api_response = api_client.ApiResponseWithoutDeserializationAsync(
                    response=response.http_response,
                    round_trip_time=response.round_trip_time,
                    status=response.http_response.status,
                    headers=response.http_response.headers,
                )
    
        if not 200 <= api_response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)
    
        # cleanup session / response
        response.http_response.close()
        await response.session.close()
    
        return api_response


    def _create_phone_number_oapg(
        self,
        body: typing.Any = None,
            path_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/json',
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor201,
        ApiResponseForDefault,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_id,
        ):
            parameter_data = path_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _path_params.update(serialized_data)
    
        for k, v in _path_params.items():
            used_path = used_path.replace('{%s}' % k, v)
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'post'.upper()
        _headers.add('Content-Type', content_type)
    
        if body is schemas.unset:
            raise exceptions.ApiValueError(
                'The required body parameter has an invalid value of: unset. Set a valid value instead')
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/workContactInformationChanges/{ID}/phoneNumbers',
            body=body,
            headers=_headers,
        )
        serialized_data = request_body_phone_reference1089da0ab90910000f70891a998b0887.serialize(body, content_type)
        if 'fields' in serialized_data:
            _fields = serialized_data['fields']
        elif 'body' in serialized_data:
            _body = serialized_data['body']
    
        response = self.api_client.call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            fields=_fields,
            serialized_body=_body,
            body=body,
            timeout=timeout,
        )
    
        response_for_status = _status_code_to_response.get(str(response.http_response.status))
        if response_for_status:
            api_response = response_for_status.deserialize(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
        else:
            default_response = _status_code_to_response.get('default')
            if default_response:
                api_response = default_response.deserialize(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
            else:
                api_response = api_client.ApiResponseWithoutDeserialization(
                    response=response.http_response,
                    round_trip_time=response.round_trip_time,
                    status=response.http_response.status,
                    headers=response.http_response.headers,
                )
    
        if not 200 <= api_response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)
    
        return api_response


class CreatePhoneNumberRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def acreate_phone_number(
        self,
        id: str,
        extension: typing.Optional[str] = None,
        complete_phone_number: typing.Optional[str] = None,
        country_phone_code: typing.Optional[CountryPhoneCode1089da0ab90910000f7089365467088c] = None,
        device_type: typing.Optional[DeviceType1089da0ab90910000f7089256c7b0888] = None,
        usage: typing.Optional[Usage1089da0ab90910000f70892f2de3088a] = None,
        descriptor: typing.Optional[str] = None,
        id: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor201Async,
        ApiResponseForDefaultAsync,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._create_phone_number_mapped_args(
            body=body,
            id=id,
            extension=extension,
            complete_phone_number=complete_phone_number,
            country_phone_code=country_phone_code,
            device_type=device_type,
            usage=usage,
            descriptor=descriptor,
            id=id,
        )
        return await self._acreate_phone_number_oapg(
            body=args.body,
            path_params=args.path,
            **kwargs,
        )
    
    def create_phone_number(
        self,
        id: str,
        extension: typing.Optional[str] = None,
        complete_phone_number: typing.Optional[str] = None,
        country_phone_code: typing.Optional[CountryPhoneCode1089da0ab90910000f7089365467088c] = None,
        device_type: typing.Optional[DeviceType1089da0ab90910000f7089256c7b0888] = None,
        usage: typing.Optional[Usage1089da0ab90910000f70892f2de3088a] = None,
        descriptor: typing.Optional[str] = None,
        id: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor201,
        ApiResponseForDefault,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._create_phone_number_mapped_args(
            body=body,
            id=id,
            extension=extension,
            complete_phone_number=complete_phone_number,
            country_phone_code=country_phone_code,
            device_type=device_type,
            usage=usage,
            descriptor=descriptor,
            id=id,
        )
        return self._create_phone_number_oapg(
            body=args.body,
            path_params=args.path,
        )

class CreatePhoneNumber(BaseApi):

    async def acreate_phone_number(
        self,
        id: str,
        extension: typing.Optional[str] = None,
        complete_phone_number: typing.Optional[str] = None,
        country_phone_code: typing.Optional[CountryPhoneCode1089da0ab90910000f7089365467088c] = None,
        device_type: typing.Optional[DeviceType1089da0ab90910000f7089256c7b0888] = None,
        usage: typing.Optional[Usage1089da0ab90910000f70892f2de3088a] = None,
        descriptor: typing.Optional[str] = None,
        id: typing.Optional[str] = None,
        validate: bool = False,
        **kwargs,
    ) -> PhoneReference1089da0ab90910000f70891a998b0887Pydantic:
        raw_response = await self.raw.acreate_phone_number(
            body=body,
            id=id,
            extension=extension,
            complete_phone_number=complete_phone_number,
            country_phone_code=country_phone_code,
            device_type=device_type,
            usage=usage,
            descriptor=descriptor,
            id=id,
            **kwargs,
        )
        if validate:
            return RootModel[PhoneReference1089da0ab90910000f70891a998b0887Pydantic](raw_response.body).root
        return api_client.construct_model_instance(PhoneReference1089da0ab90910000f70891a998b0887Pydantic, raw_response.body)
    
    
    def create_phone_number(
        self,
        id: str,
        extension: typing.Optional[str] = None,
        complete_phone_number: typing.Optional[str] = None,
        country_phone_code: typing.Optional[CountryPhoneCode1089da0ab90910000f7089365467088c] = None,
        device_type: typing.Optional[DeviceType1089da0ab90910000f7089256c7b0888] = None,
        usage: typing.Optional[Usage1089da0ab90910000f70892f2de3088a] = None,
        descriptor: typing.Optional[str] = None,
        id: typing.Optional[str] = None,
        validate: bool = False,
    ) -> PhoneReference1089da0ab90910000f70891a998b0887Pydantic:
        raw_response = self.raw.create_phone_number(
            body=body,
            id=id,
            extension=extension,
            complete_phone_number=complete_phone_number,
            country_phone_code=country_phone_code,
            device_type=device_type,
            usage=usage,
            descriptor=descriptor,
            id=id,
        )
        if validate:
            return RootModel[PhoneReference1089da0ab90910000f70891a998b0887Pydantic](raw_response.body).root
        return api_client.construct_model_instance(PhoneReference1089da0ab90910000f70891a998b0887Pydantic, raw_response.body)


class ApiForpost(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def apost(
        self,
        id: str,
        extension: typing.Optional[str] = None,
        complete_phone_number: typing.Optional[str] = None,
        country_phone_code: typing.Optional[CountryPhoneCode1089da0ab90910000f7089365467088c] = None,
        device_type: typing.Optional[DeviceType1089da0ab90910000f7089256c7b0888] = None,
        usage: typing.Optional[Usage1089da0ab90910000f70892f2de3088a] = None,
        descriptor: typing.Optional[str] = None,
        id: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor201Async,
        ApiResponseForDefaultAsync,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._create_phone_number_mapped_args(
            body=body,
            id=id,
            extension=extension,
            complete_phone_number=complete_phone_number,
            country_phone_code=country_phone_code,
            device_type=device_type,
            usage=usage,
            descriptor=descriptor,
            id=id,
        )
        return await self._acreate_phone_number_oapg(
            body=args.body,
            path_params=args.path,
            **kwargs,
        )
    
    def post(
        self,
        id: str,
        extension: typing.Optional[str] = None,
        complete_phone_number: typing.Optional[str] = None,
        country_phone_code: typing.Optional[CountryPhoneCode1089da0ab90910000f7089365467088c] = None,
        device_type: typing.Optional[DeviceType1089da0ab90910000f7089256c7b0888] = None,
        usage: typing.Optional[Usage1089da0ab90910000f70892f2de3088a] = None,
        descriptor: typing.Optional[str] = None,
        id: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor201,
        ApiResponseForDefault,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._create_phone_number_mapped_args(
            body=body,
            id=id,
            extension=extension,
            complete_phone_number=complete_phone_number,
            country_phone_code=country_phone_code,
            device_type=device_type,
            usage=usage,
            descriptor=descriptor,
            id=id,
        )
        return self._create_phone_number_oapg(
            body=args.body,
            path_params=args.path,
        )

