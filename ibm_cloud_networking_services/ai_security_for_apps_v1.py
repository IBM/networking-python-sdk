# coding: utf-8

# (C) Copyright IBM Corp. 2026.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# IBM OpenAPI SDK Code Generator Version: 3.117.0-7f07c563-20260915-094553

"""
AI Security for Apps

API Version: 1.0.0
"""

from datetime import datetime
from enum import Enum
from typing import Dict, List, Optional
import json

from ibm_cloud_sdk_core import BaseService, DetailedResponse
from ibm_cloud_sdk_core.authenticators.authenticator import Authenticator
from ibm_cloud_sdk_core.get_authenticator import get_authenticator_from_environment
from ibm_cloud_sdk_core.utils import convert_list, convert_model, datetime_to_string, string_to_datetime

from .common import get_sdk_headers

##############################################################################
# Service
##############################################################################


class AiSecurityForAppsV1(BaseService):
    """The AI Security for Apps V1 service."""

    DEFAULT_SERVICE_URL = 'https://api.cis.cloud.ibm.com'
    DEFAULT_SERVICE_NAME = 'ai_security_for_apps'

    @classmethod
    def new_instance(
        cls,
        crn: str,
        zone_identifier: str,
        service_name: str = DEFAULT_SERVICE_NAME,
    ) -> 'AiSecurityForAppsV1':
        """
        Return a new client for the AI Security for Apps service using the
               specified parameters and external configuration.

        :param str crn: Full url-encoded CRN of the service instance.

        :param str zone_identifier: Zone identifier to identify the zone.
        """
        if crn is None:
            raise ValueError('crn must be provided')
        if zone_identifier is None:
            raise ValueError('zone_identifier must be provided')

        authenticator = get_authenticator_from_environment(service_name)
        service = cls(
            crn,
            zone_identifier,
            authenticator
            )
        service.configure_service(service_name)
        return service

    def __init__(
        self,
        crn: str,
        zone_identifier: str,
        authenticator: Authenticator = None,
    ) -> None:
        """
        Construct a new client for the AI Security for Apps service.

        :param str crn: Full url-encoded CRN of the service instance.

        :param str zone_identifier: Zone identifier to identify the zone.

        :param Authenticator authenticator: The authenticator specifies the authentication mechanism.
               Get up to date information from https://github.com/IBM/python-sdk-core/blob/main/README.md
               about initializing the authenticator of your choice.
        """
        if crn is None:
            raise ValueError('crn must be provided')
        if zone_identifier is None:
            raise ValueError('zone_identifier must be provided')

        BaseService.__init__(self, service_url=self.DEFAULT_SERVICE_URL, authenticator=authenticator)
        self.crn = crn
        self.zone_identifier = zone_identifier

    #########################
    # aISecuritySettings
    #########################

    def get_ai_security_settings(
        self,
        **kwargs,
    ) -> DetailedResponse:
        """
        Get AI Security for Apps settings.

        Get AI Security for Apps enabled/disabled setting for a given zone.

        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `AiSecuritySettingsResp` object
        """

        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='get_ai_security_settings',
        )
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['crn', 'zone_identifier']
        path_param_values = self.encode_path_vars(self.crn, self.zone_identifier)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/{crn}/zones/{zone_identifier}/ai_security/settings'.format(**path_param_dict)
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
        )

        response = self.send(request, **kwargs)
        return response

    def replace_zone_ai_security_settings(
        self,
        *,
        enabled: Optional[bool] = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Update AI Security for Apps settings.

        Enable or disable AI Security for Apps for a given zone.

        :param bool enabled: (optional) Set to true to enable AI Security for Apps,
               false to disable.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `AiSecuritySettingsResp` object
        """

        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='replace_zone_ai_security_settings',
        )
        headers.update(sdk_headers)

        data = {
            'enabled': enabled,
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['crn', 'zone_identifier']
        path_param_values = self.encode_path_vars(self.crn, self.zone_identifier)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/{crn}/zones/{zone_identifier}/ai_security/settings'.format(**path_param_dict)
        request = self.prepare_request(
            method='PUT',
            url=url,
            headers=headers,
            data=data,
        )

        response = self.send(request, **kwargs)
        return response

    #########################
    # aPIGatewayDiscovery
    #########################

    def get_api_gateway_discovery(
        self,
        **kwargs,
    ) -> DetailedResponse:
        """
        Get API Gateway discovery.

        Retrieve discovered operations for a zone rendered as OpenAPI schemas. Use this to
        identify AI-powered endpoints, save them to Endpoint Management, and label them to
        enable AI Security for Apps scanning.

        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ApiGatewayDiscoveryResp` object
        """

        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='get_api_gateway_discovery',
        )
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['crn', 'zone_identifier']
        path_param_values = self.encode_path_vars(self.crn, self.zone_identifier)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/{crn}/zones/{zone_identifier}/api_gateway/discovery'.format(**path_param_dict)
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
        )

        response = self.send(request, **kwargs)
        return response

    #########################
    # aPIGatewayDiscoveryOperations
    #########################

    def list_api_gateway_discovery_operations(
        self,
        *,
        diff: Optional[bool] = None,
        direction: Optional[str] = None,
        endpoint: Optional[str] = None,
        host: Optional[List[str]] = None,
        method: Optional[List[str]] = None,
        order: Optional[str] = None,
        origin: Optional[str] = None,
        state: Optional[str] = None,
        page: Optional[int] = None,
        per_page: Optional[int] = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        List API Gateway discovery operations.

        Retrieve the most up-to-date list of discovered operations for a zone.

        :param bool diff: (optional) When true, only return operations not yet
               saved into API Shield Endpoint Management.
        :param str direction: (optional) Direction to order results.
        :param str endpoint: (optional) Filter results to only include endpoints
               containing this pattern.
        :param List[str] host: (optional) Filter results to only include the
               specified hosts.
        :param List[str] method: (optional) Filter results to only include the
               specified HTTP methods.
        :param str order: (optional) Field to order results by.
        :param str origin: (optional) Filter by discovery engine source.
        :param str state: (optional) Filter results by discovery state
               (review/saved/ignored).
        :param int page: (optional) Page number of paginated results.
        :param int per_page: (optional) Maximum number of results per page.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `DiscoveryOperationsListResp` object
        """

        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='list_api_gateway_discovery_operations',
        )
        headers.update(sdk_headers)

        params = {
            'diff': diff,
            'direction': direction,
            'endpoint': endpoint,
            'host': convert_list(host),
            'method': convert_list(method),
            'order': order,
            'origin': origin,
            'state': state,
            'page': page,
            'per_page': per_page,
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['crn', 'zone_identifier']
        path_param_values = self.encode_path_vars(self.crn, self.zone_identifier)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/{crn}/zones/{zone_identifier}/api_gateway/discovery/operations'.format(**path_param_dict)
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
        )

        response = self.send(request, **kwargs)
        return response

    def update_zone_api_gateway_discovery_operation(
        self,
        *,
        request_body: Optional[dict] = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Bulk update discovered operation states.

        Bulk update the state of one or more discovered operations. Use to mark operations
        as saved (promoting to Endpoint Management) or ignored.

        :param dict request_body: (optional) List of operation state updates.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `DiscoveryOperationsPatchResp` object
        """

        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='update_zone_api_gateway_discovery_operation',
        )
        headers.update(sdk_headers)

        data = json.dumps(request_body)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['crn', 'zone_identifier']
        path_param_values = self.encode_path_vars(self.crn, self.zone_identifier)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/{crn}/zones/{zone_identifier}/api_gateway/discovery/operations'.format(**path_param_dict)
        request = self.prepare_request(
            method='PATCH',
            url=url,
            headers=headers,
            data=data,
        )

        response = self.send(request, **kwargs)
        return response

    #########################
    # aPIGatewayOperations
    #########################

    def create_zone_api_gateway_operation(
        self,
        *,
        api_gateway_operation: Optional[List['ApiGatewayOperation']] = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Create API Gateway operations in bulk.

        Create API Gateway operations in bulk for a zone, saving them to Endpoint
        Management.

        :param List[ApiGatewayOperation] api_gateway_operation: (optional) List of
               operations to create.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ApiGatewayOperationsResp` object
        """

        if api_gateway_operation is not None:
            api_gateway_operation = [convert_model(x) for x in api_gateway_operation]
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='create_zone_api_gateway_operation',
        )
        headers.update(sdk_headers)

        data = json.dumps(api_gateway_operation)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['crn', 'zone_identifier']
        path_param_values = self.encode_path_vars(self.crn, self.zone_identifier)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/{crn}/zones/{zone_identifier}/api_gateway/operations'.format(**path_param_dict)
        request = self.prepare_request(
            method='POST',
            url=url,
            headers=headers,
            data=data,
        )

        response = self.send(request, **kwargs)
        return response

    def create_api_gateway_operation_item(
        self,
        *,
        method: Optional[str] = None,
        host: Optional[str] = None,
        endpoint: Optional[str] = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Create a single API Gateway operation.

        Create a single API Gateway operation for a zone, saving it to Endpoint
        Management.

        :param str method: (optional) The HTTP method for the operation.
        :param str host: (optional) RFC3986-compliant host.
        :param str endpoint: (optional) The endpoint path. Must start with /.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ApiGatewayOperationItemResp` object
        """

        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='create_api_gateway_operation_item',
        )
        headers.update(sdk_headers)

        data = {
            'method': method,
            'host': host,
            'endpoint': endpoint,
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['crn', 'zone_identifier']
        path_param_values = self.encode_path_vars(self.crn, self.zone_identifier)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/{crn}/zones/{zone_identifier}/api_gateway/operations/item'.format(**path_param_dict)
        request = self.prepare_request(
            method='POST',
            url=url,
            headers=headers,
            data=data,
        )

        response = self.send(request, **kwargs)
        return response

    def update_api_gateway_operation_labels(
        self,
        *,
        selector: Optional['ApiGatewayOperationsLabelsInputSelector'] = None,
        user: Optional['ApiGatewayOperationsLabelsInputUser'] = None,
        managed: Optional['ApiGatewayOperationsLabelsInputManaged'] = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Add or remove labels from API Gateway operations.

        Add or remove labels from one or more API Gateway operations. Apply the built-in
        LLM label to endpoints that receive LLM traffic to enable IBM AI Security for Apps
        to scan those endpoints for prompt injection, PII, and unsafe topics.

        :param ApiGatewayOperationsLabelsInputSelector selector: (optional)
               Selector specifying which operations to label.
        :param ApiGatewayOperationsLabelsInputUser user: (optional) User-defined
               labels to apply.
        :param ApiGatewayOperationsLabelsInputManaged managed: (optional) Managed
               labels to apply (e.g. cf-llm).
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ApiGatewayOperationsLabelsResp` object
        """

        if selector is not None:
            selector = convert_model(selector)
        if user is not None:
            user = convert_model(user)
        if managed is not None:
            managed = convert_model(managed)
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='update_api_gateway_operation_labels',
        )
        headers.update(sdk_headers)

        data = {
            'selector': selector,
            'user': user,
            'managed': managed,
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['crn', 'zone_identifier']
        path_param_values = self.encode_path_vars(self.crn, self.zone_identifier)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/{crn}/zones/{zone_identifier}/api_gateway/operations/labels'.format(**path_param_dict)
        request = self.prepare_request(
            method='POST',
            url=url,
            headers=headers,
            data=data,
        )

        response = self.send(request, **kwargs)
        return response

    def get_zone_api_gateway_operation(
        self,
        operation_id: str,
        **kwargs,
    ) -> DetailedResponse:
        """
        Retrieve information about an operation.

        Retrieve information about a specific operation on a zone.

        :param str operation_id: UUID of the API Gateway operation.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ApiGatewayOperationItemResp` object
        """

        if not operation_id:
            raise ValueError('operation_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='get_zone_api_gateway_operation',
        )
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['crn', 'zone_identifier', 'operation_id']
        path_param_values = self.encode_path_vars(self.crn, self.zone_identifier, operation_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/{crn}/zones/{zone_identifier}/api_gateway/operations/{operation_id}'.format(**path_param_dict)
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
        )

        response = self.send(request, **kwargs)
        return response

    def delete_zone_api_gateway_operation(
        self,
        operation_id: str,
        **kwargs,
    ) -> DetailedResponse:
        """
        Delete an operation.

        Delete an operation from a zone.

        :param str operation_id: UUID of the API Gateway operation.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if not operation_id:
            raise ValueError('operation_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='delete_zone_api_gateway_operation',
        )
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']

        path_param_keys = ['crn', 'zone_identifier', 'operation_id']
        path_param_values = self.encode_path_vars(self.crn, self.zone_identifier, operation_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/{crn}/zones/{zone_identifier}/api_gateway/operations/{operation_id}'.format(**path_param_dict)
        request = self.prepare_request(
            method='DELETE',
            url=url,
            headers=headers,
        )

        response = self.send(request, **kwargs)
        return response

    #########################
    # aPIGatewaySchemas
    #########################

    def get_api_gateway_schemas(
        self,
        **kwargs,
    ) -> DetailedResponse:
        """
        Get API Gateway schemas.

        Retrieve API Gateway schemas for a specified zone rendered as OpenAPI schemas.

        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ApiGatewaySchemasResp` object
        """

        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='get_api_gateway_schemas',
        )
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['crn', 'zone_identifier']
        path_param_values = self.encode_path_vars(self.crn, self.zone_identifier)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/{crn}/zones/{zone_identifier}/api_gateway/schemas'.format(**path_param_dict)
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
        )

        response = self.send(request, **kwargs)
        return response


class ListApiGatewayDiscoveryOperationsEnums:
    """
    Enums for list_api_gateway_discovery_operations parameters.
    """

    class Direction(str, Enum):
        """
        Direction to order results.
        """

        ASC = 'asc'
        DESC = 'desc'
    class Order(str, Enum):
        """
        Field to order results by.
        """

        HOST = 'host'
        METHOD = 'method'
        ENDPOINT = 'endpoint'
        TRAFFIC_STATS_REQUESTS = 'traffic_stats.requests'
        TRAFFIC_STATS_LAST_UPDATED = 'traffic_stats.last_updated'
    class Origin(str, Enum):
        """
        Filter by discovery engine source.
        """

        ML = 'ML'
        SESSIONIDENTIFIER = 'SessionIdentifier'
        LABELDISCOVERY = 'LabelDiscovery'
    class State(str, Enum):
        """
        Filter results by discovery state (review/saved/ignored).
        """

        REVIEW = 'review'
        SAVED = 'saved'
        IGNORED = 'ignored'


##############################################################################
# Models
##############################################################################


class AiSecuritySettingsRespResult:
    """
    Container for response information.

    :param bool enabled: (optional) Whether AI Security for Apps is enabled on the
          zone.
    """

    def __init__(
        self,
        *,
        enabled: Optional[bool] = None,
    ) -> None:
        """
        Initialize a AiSecuritySettingsRespResult object.

        :param bool enabled: (optional) Whether AI Security for Apps is enabled on
               the zone.
        """
        self.enabled = enabled

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'AiSecuritySettingsRespResult':
        """Initialize a AiSecuritySettingsRespResult object from a json dictionary."""
        args = {}
        if (enabled := _dict.get('enabled')) is not None:
            args['enabled'] = enabled
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a AiSecuritySettingsRespResult object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'enabled') and self.enabled is not None:
            _dict['enabled'] = self.enabled
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this AiSecuritySettingsRespResult object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'AiSecuritySettingsRespResult') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'AiSecuritySettingsRespResult') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ApiGatewayOperationItemRespResult:
    """
    ApiGatewayOperationItemRespResult.

    :param str operation_id: (optional) UUID of the created operation.
    :param str method: (optional)
    :param str host: (optional)
    :param str endpoint: (optional)
    """

    def __init__(
        self,
        *,
        operation_id: Optional[str] = None,
        method: Optional[str] = None,
        host: Optional[str] = None,
        endpoint: Optional[str] = None,
    ) -> None:
        """
        Initialize a ApiGatewayOperationItemRespResult object.

        :param str operation_id: (optional) UUID of the created operation.
        :param str method: (optional)
        :param str host: (optional)
        :param str endpoint: (optional)
        """
        self.operation_id = operation_id
        self.method = method
        self.host = host
        self.endpoint = endpoint

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ApiGatewayOperationItemRespResult':
        """Initialize a ApiGatewayOperationItemRespResult object from a json dictionary."""
        args = {}
        if (operation_id := _dict.get('operation_id')) is not None:
            args['operation_id'] = operation_id
        if (method := _dict.get('method')) is not None:
            args['method'] = method
        if (host := _dict.get('host')) is not None:
            args['host'] = host
        if (endpoint := _dict.get('endpoint')) is not None:
            args['endpoint'] = endpoint
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ApiGatewayOperationItemRespResult object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'operation_id') and self.operation_id is not None:
            _dict['operation_id'] = self.operation_id
        if hasattr(self, 'method') and self.method is not None:
            _dict['method'] = self.method
        if hasattr(self, 'host') and self.host is not None:
            _dict['host'] = self.host
        if hasattr(self, 'endpoint') and self.endpoint is not None:
            _dict['endpoint'] = self.endpoint
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ApiGatewayOperationItemRespResult object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ApiGatewayOperationItemRespResult') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ApiGatewayOperationItemRespResult') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ApiGatewayOperationsLabelsInputManaged:
    """
    Managed labels to apply (e.g. cf-llm).

    :param List[str] labels: (optional) Array of managed label strings.
    """

    def __init__(
        self,
        *,
        labels: Optional[List[str]] = None,
    ) -> None:
        """
        Initialize a ApiGatewayOperationsLabelsInputManaged object.

        :param List[str] labels: (optional) Array of managed label strings.
        """
        self.labels = labels

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ApiGatewayOperationsLabelsInputManaged':
        """Initialize a ApiGatewayOperationsLabelsInputManaged object from a json dictionary."""
        args = {}
        if (labels := _dict.get('labels')) is not None:
            args['labels'] = labels
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ApiGatewayOperationsLabelsInputManaged object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'labels') and self.labels is not None:
            _dict['labels'] = self.labels
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ApiGatewayOperationsLabelsInputManaged object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ApiGatewayOperationsLabelsInputManaged') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ApiGatewayOperationsLabelsInputManaged') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ApiGatewayOperationsLabelsInputSelector:
    """
    Selector specifying which operations to label.

    :param ApiGatewayOperationsLabelsInputSelectorInclude include: Operations to
          include in the label operation.
    """

    def __init__(
        self,
        include: 'ApiGatewayOperationsLabelsInputSelectorInclude',
    ) -> None:
        """
        Initialize a ApiGatewayOperationsLabelsInputSelector object.

        :param ApiGatewayOperationsLabelsInputSelectorInclude include: Operations
               to include in the label operation.
        """
        self.include = include

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ApiGatewayOperationsLabelsInputSelector':
        """Initialize a ApiGatewayOperationsLabelsInputSelector object from a json dictionary."""
        args = {}
        if (include := _dict.get('include')) is not None:
            args['include'] = ApiGatewayOperationsLabelsInputSelectorInclude.from_dict(include)
        else:
            raise ValueError('Required property \'include\' not present in ApiGatewayOperationsLabelsInputSelector JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ApiGatewayOperationsLabelsInputSelector object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'include') and self.include is not None:
            if isinstance(self.include, dict):
                _dict['include'] = self.include
            else:
                _dict['include'] = self.include.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ApiGatewayOperationsLabelsInputSelector object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ApiGatewayOperationsLabelsInputSelector') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ApiGatewayOperationsLabelsInputSelector') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ApiGatewayOperationsLabelsInputSelectorInclude:
    """
    Operations to include in the label operation.

    :param List[str] operation_ids: (optional) Array of operation UUIDs to label.
    """

    def __init__(
        self,
        *,
        operation_ids: Optional[List[str]] = None,
    ) -> None:
        """
        Initialize a ApiGatewayOperationsLabelsInputSelectorInclude object.

        :param List[str] operation_ids: (optional) Array of operation UUIDs to
               label.
        """
        self.operation_ids = operation_ids

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ApiGatewayOperationsLabelsInputSelectorInclude':
        """Initialize a ApiGatewayOperationsLabelsInputSelectorInclude object from a json dictionary."""
        args = {}
        if (operation_ids := _dict.get('operation_ids')) is not None:
            args['operation_ids'] = operation_ids
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ApiGatewayOperationsLabelsInputSelectorInclude object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'operation_ids') and self.operation_ids is not None:
            _dict['operation_ids'] = self.operation_ids
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ApiGatewayOperationsLabelsInputSelectorInclude object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ApiGatewayOperationsLabelsInputSelectorInclude') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ApiGatewayOperationsLabelsInputSelectorInclude') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ApiGatewayOperationsLabelsInputUser:
    """
    User-defined labels to apply.

    :param List[str] labels: (optional) Array of user-defined label strings.
    """

    def __init__(
        self,
        *,
        labels: Optional[List[str]] = None,
    ) -> None:
        """
        Initialize a ApiGatewayOperationsLabelsInputUser object.

        :param List[str] labels: (optional) Array of user-defined label strings.
        """
        self.labels = labels

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ApiGatewayOperationsLabelsInputUser':
        """Initialize a ApiGatewayOperationsLabelsInputUser object from a json dictionary."""
        args = {}
        if (labels := _dict.get('labels')) is not None:
            args['labels'] = labels
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ApiGatewayOperationsLabelsInputUser object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'labels') and self.labels is not None:
            _dict['labels'] = self.labels
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ApiGatewayOperationsLabelsInputUser object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ApiGatewayOperationsLabelsInputUser') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ApiGatewayOperationsLabelsInputUser') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ApiGatewayOperationsLabelsRespResultItem:
    """
    ApiGatewayOperationsLabelsRespResultItem.

    :param str operation_id: (optional)
    :param List[str] labels: (optional)
    """

    def __init__(
        self,
        *,
        operation_id: Optional[str] = None,
        labels: Optional[List[str]] = None,
    ) -> None:
        """
        Initialize a ApiGatewayOperationsLabelsRespResultItem object.

        :param str operation_id: (optional)
        :param List[str] labels: (optional)
        """
        self.operation_id = operation_id
        self.labels = labels

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ApiGatewayOperationsLabelsRespResultItem':
        """Initialize a ApiGatewayOperationsLabelsRespResultItem object from a json dictionary."""
        args = {}
        if (operation_id := _dict.get('operation_id')) is not None:
            args['operation_id'] = operation_id
        if (labels := _dict.get('labels')) is not None:
            args['labels'] = labels
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ApiGatewayOperationsLabelsRespResultItem object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'operation_id') and self.operation_id is not None:
            _dict['operation_id'] = self.operation_id
        if hasattr(self, 'labels') and self.labels is not None:
            _dict['labels'] = self.labels
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ApiGatewayOperationsLabelsRespResultItem object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ApiGatewayOperationsLabelsRespResultItem') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ApiGatewayOperationsLabelsRespResultItem') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ApiGatewayOperationsRespResultItem:
    """
    ApiGatewayOperationsRespResultItem.

    :param str operation_id: (optional) UUID of the created operation.
    :param str method: (optional)
    :param str host: (optional)
    :param str endpoint: (optional)
    """

    def __init__(
        self,
        *,
        operation_id: Optional[str] = None,
        method: Optional[str] = None,
        host: Optional[str] = None,
        endpoint: Optional[str] = None,
    ) -> None:
        """
        Initialize a ApiGatewayOperationsRespResultItem object.

        :param str operation_id: (optional) UUID of the created operation.
        :param str method: (optional)
        :param str host: (optional)
        :param str endpoint: (optional)
        """
        self.operation_id = operation_id
        self.method = method
        self.host = host
        self.endpoint = endpoint

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ApiGatewayOperationsRespResultItem':
        """Initialize a ApiGatewayOperationsRespResultItem object from a json dictionary."""
        args = {}
        if (operation_id := _dict.get('operation_id')) is not None:
            args['operation_id'] = operation_id
        if (method := _dict.get('method')) is not None:
            args['method'] = method
        if (host := _dict.get('host')) is not None:
            args['host'] = host
        if (endpoint := _dict.get('endpoint')) is not None:
            args['endpoint'] = endpoint
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ApiGatewayOperationsRespResultItem object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'operation_id') and self.operation_id is not None:
            _dict['operation_id'] = self.operation_id
        if hasattr(self, 'method') and self.method is not None:
            _dict['method'] = self.method
        if hasattr(self, 'host') and self.host is not None:
            _dict['host'] = self.host
        if hasattr(self, 'endpoint') and self.endpoint is not None:
            _dict['endpoint'] = self.endpoint
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ApiGatewayOperationsRespResultItem object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ApiGatewayOperationsRespResultItem') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ApiGatewayOperationsRespResultItem') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class DiscoveryOperationFeatures:
    """
    DiscoveryOperationFeatures.

    :param DiscoveryOperationFeaturesTrafficStats traffic_stats: (optional)
    """

    def __init__(
        self,
        *,
        traffic_stats: Optional['DiscoveryOperationFeaturesTrafficStats'] = None,
    ) -> None:
        """
        Initialize a DiscoveryOperationFeatures object.

        :param DiscoveryOperationFeaturesTrafficStats traffic_stats: (optional)
        """
        self.traffic_stats = traffic_stats

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'DiscoveryOperationFeatures':
        """Initialize a DiscoveryOperationFeatures object from a json dictionary."""
        args = {}
        if (traffic_stats := _dict.get('traffic_stats')) is not None:
            args['traffic_stats'] = DiscoveryOperationFeaturesTrafficStats.from_dict(traffic_stats)
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a DiscoveryOperationFeatures object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'traffic_stats') and self.traffic_stats is not None:
            if isinstance(self.traffic_stats, dict):
                _dict['traffic_stats'] = self.traffic_stats
            else:
                _dict['traffic_stats'] = self.traffic_stats.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this DiscoveryOperationFeatures object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'DiscoveryOperationFeatures') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'DiscoveryOperationFeatures') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class DiscoveryOperationFeaturesTrafficStats:
    """
    DiscoveryOperationFeaturesTrafficStats.

    :param datetime last_updated: (optional)
    :param int period_seconds: (optional) The period in seconds over which
          statistics were computed.
    :param float requests: (optional) The average number of requests seen during
          this period.
    """

    def __init__(
        self,
        *,
        last_updated: Optional[datetime] = None,
        period_seconds: Optional[int] = None,
        requests: Optional[float] = None,
    ) -> None:
        """
        Initialize a DiscoveryOperationFeaturesTrafficStats object.

        :param datetime last_updated: (optional)
        :param int period_seconds: (optional) The period in seconds over which
               statistics were computed.
        :param float requests: (optional) The average number of requests seen
               during this period.
        """
        self.last_updated = last_updated
        self.period_seconds = period_seconds
        self.requests = requests

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'DiscoveryOperationFeaturesTrafficStats':
        """Initialize a DiscoveryOperationFeaturesTrafficStats object from a json dictionary."""
        args = {}
        if (last_updated := _dict.get('last_updated')) is not None:
            args['last_updated'] = string_to_datetime(last_updated)
        if (period_seconds := _dict.get('period_seconds')) is not None:
            args['period_seconds'] = period_seconds
        if (requests := _dict.get('requests')) is not None:
            args['requests'] = requests
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a DiscoveryOperationFeaturesTrafficStats object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'last_updated') and self.last_updated is not None:
            _dict['last_updated'] = datetime_to_string(self.last_updated)
        if hasattr(self, 'period_seconds') and self.period_seconds is not None:
            _dict['period_seconds'] = self.period_seconds
        if hasattr(self, 'requests') and self.requests is not None:
            _dict['requests'] = self.requests
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this DiscoveryOperationFeaturesTrafficStats object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'DiscoveryOperationFeaturesTrafficStats') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'DiscoveryOperationFeaturesTrafficStats') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class AiSecuritySettingsResp:
    """
    AI Security for Apps settings response.

    :param bool success: Was operation successful.
    :param List[List[str]] errors: Array of errors encountered.
    :param List[List[str]] messages: Array of messages returned.
    :param AiSecuritySettingsRespResult result: Container for response information.
    """

    def __init__(
        self,
        success: bool,
        errors: List[List[str]],
        messages: List[List[str]],
        result: 'AiSecuritySettingsRespResult',
    ) -> None:
        """
        Initialize a AiSecuritySettingsResp object.

        :param bool success: Was operation successful.
        :param List[List[str]] errors: Array of errors encountered.
        :param List[List[str]] messages: Array of messages returned.
        :param AiSecuritySettingsRespResult result: Container for response
               information.
        """
        self.success = success
        self.errors = errors
        self.messages = messages
        self.result = result

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'AiSecuritySettingsResp':
        """Initialize a AiSecuritySettingsResp object from a json dictionary."""
        args = {}
        if (success := _dict.get('success')) is not None:
            args['success'] = success
        else:
            raise ValueError('Required property \'success\' not present in AiSecuritySettingsResp JSON')
        if (errors := _dict.get('errors')) is not None:
            args['errors'] = errors
        else:
            raise ValueError('Required property \'errors\' not present in AiSecuritySettingsResp JSON')
        if (messages := _dict.get('messages')) is not None:
            args['messages'] = messages
        else:
            raise ValueError('Required property \'messages\' not present in AiSecuritySettingsResp JSON')
        if (result := _dict.get('result')) is not None:
            args['result'] = AiSecuritySettingsRespResult.from_dict(result)
        else:
            raise ValueError('Required property \'result\' not present in AiSecuritySettingsResp JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a AiSecuritySettingsResp object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'success') and self.success is not None:
            _dict['success'] = self.success
        if hasattr(self, 'errors') and self.errors is not None:
            _dict['errors'] = self.errors
        if hasattr(self, 'messages') and self.messages is not None:
            _dict['messages'] = self.messages
        if hasattr(self, 'result') and self.result is not None:
            if isinstance(self.result, dict):
                _dict['result'] = self.result
            else:
                _dict['result'] = self.result.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this AiSecuritySettingsResp object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'AiSecuritySettingsResp') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'AiSecuritySettingsResp') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ApiGatewayDiscoveryResp:
    """
    API Gateway discovery response (OpenAPI schema format).

    :param bool success: Was operation successful.
    :param List[List[str]] errors: Array of errors encountered.
    :param List[List[str]] messages: Array of messages returned.
    :param dict result: Discovered operations rendered as an OpenAPI schema
          document.
    """

    def __init__(
        self,
        success: bool,
        errors: List[List[str]],
        messages: List[List[str]],
        result: dict,
    ) -> None:
        """
        Initialize a ApiGatewayDiscoveryResp object.

        :param bool success: Was operation successful.
        :param List[List[str]] errors: Array of errors encountered.
        :param List[List[str]] messages: Array of messages returned.
        :param dict result: Discovered operations rendered as an OpenAPI schema
               document.
        """
        self.success = success
        self.errors = errors
        self.messages = messages
        self.result = result

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ApiGatewayDiscoveryResp':
        """Initialize a ApiGatewayDiscoveryResp object from a json dictionary."""
        args = {}
        if (success := _dict.get('success')) is not None:
            args['success'] = success
        else:
            raise ValueError('Required property \'success\' not present in ApiGatewayDiscoveryResp JSON')
        if (errors := _dict.get('errors')) is not None:
            args['errors'] = errors
        else:
            raise ValueError('Required property \'errors\' not present in ApiGatewayDiscoveryResp JSON')
        if (messages := _dict.get('messages')) is not None:
            args['messages'] = messages
        else:
            raise ValueError('Required property \'messages\' not present in ApiGatewayDiscoveryResp JSON')
        if (result := _dict.get('result')) is not None:
            args['result'] = result
        else:
            raise ValueError('Required property \'result\' not present in ApiGatewayDiscoveryResp JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ApiGatewayDiscoveryResp object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'success') and self.success is not None:
            _dict['success'] = self.success
        if hasattr(self, 'errors') and self.errors is not None:
            _dict['errors'] = self.errors
        if hasattr(self, 'messages') and self.messages is not None:
            _dict['messages'] = self.messages
        if hasattr(self, 'result') and self.result is not None:
            _dict['result'] = self.result
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ApiGatewayDiscoveryResp object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ApiGatewayDiscoveryResp') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ApiGatewayDiscoveryResp') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ApiGatewayOperation:
    """
    An API Gateway operation definition.

    :param str method: The HTTP method for the operation.
    :param str host: RFC3986-compliant host.
    :param str endpoint: The endpoint path. Must start with /.
    """

    def __init__(
        self,
        method: str,
        host: str,
        endpoint: str,
    ) -> None:
        """
        Initialize a ApiGatewayOperation object.

        :param str method: The HTTP method for the operation.
        :param str host: RFC3986-compliant host.
        :param str endpoint: The endpoint path. Must start with /.
        """
        self.method = method
        self.host = host
        self.endpoint = endpoint

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ApiGatewayOperation':
        """Initialize a ApiGatewayOperation object from a json dictionary."""
        args = {}
        if (method := _dict.get('method')) is not None:
            args['method'] = method
        else:
            raise ValueError('Required property \'method\' not present in ApiGatewayOperation JSON')
        if (host := _dict.get('host')) is not None:
            args['host'] = host
        else:
            raise ValueError('Required property \'host\' not present in ApiGatewayOperation JSON')
        if (endpoint := _dict.get('endpoint')) is not None:
            args['endpoint'] = endpoint
        else:
            raise ValueError('Required property \'endpoint\' not present in ApiGatewayOperation JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ApiGatewayOperation object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'method') and self.method is not None:
            _dict['method'] = self.method
        if hasattr(self, 'host') and self.host is not None:
            _dict['host'] = self.host
        if hasattr(self, 'endpoint') and self.endpoint is not None:
            _dict['endpoint'] = self.endpoint
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ApiGatewayOperation object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ApiGatewayOperation') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ApiGatewayOperation') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class MethodEnum(str, Enum):
        """
        The HTTP method for the operation.
        """

        GET = 'GET'
        POST = 'POST'
        PUT = 'PUT'
        PATCH = 'PATCH'
        DELETE = 'DELETE'
        HEAD = 'HEAD'
        OPTIONS = 'OPTIONS'



class ApiGatewayOperationItemResp:
    """
    Single API Gateway operation create response.

    :param bool success: Was operation successful.
    :param List[List[str]] errors: Array of errors encountered.
    :param List[List[str]] messages: Array of messages returned.
    :param ApiGatewayOperationItemRespResult result:
    """

    def __init__(
        self,
        success: bool,
        errors: List[List[str]],
        messages: List[List[str]],
        result: 'ApiGatewayOperationItemRespResult',
    ) -> None:
        """
        Initialize a ApiGatewayOperationItemResp object.

        :param bool success: Was operation successful.
        :param List[List[str]] errors: Array of errors encountered.
        :param List[List[str]] messages: Array of messages returned.
        :param ApiGatewayOperationItemRespResult result:
        """
        self.success = success
        self.errors = errors
        self.messages = messages
        self.result = result

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ApiGatewayOperationItemResp':
        """Initialize a ApiGatewayOperationItemResp object from a json dictionary."""
        args = {}
        if (success := _dict.get('success')) is not None:
            args['success'] = success
        else:
            raise ValueError('Required property \'success\' not present in ApiGatewayOperationItemResp JSON')
        if (errors := _dict.get('errors')) is not None:
            args['errors'] = errors
        else:
            raise ValueError('Required property \'errors\' not present in ApiGatewayOperationItemResp JSON')
        if (messages := _dict.get('messages')) is not None:
            args['messages'] = messages
        else:
            raise ValueError('Required property \'messages\' not present in ApiGatewayOperationItemResp JSON')
        if (result := _dict.get('result')) is not None:
            args['result'] = ApiGatewayOperationItemRespResult.from_dict(result)
        else:
            raise ValueError('Required property \'result\' not present in ApiGatewayOperationItemResp JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ApiGatewayOperationItemResp object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'success') and self.success is not None:
            _dict['success'] = self.success
        if hasattr(self, 'errors') and self.errors is not None:
            _dict['errors'] = self.errors
        if hasattr(self, 'messages') and self.messages is not None:
            _dict['messages'] = self.messages
        if hasattr(self, 'result') and self.result is not None:
            if isinstance(self.result, dict):
                _dict['result'] = self.result
            else:
                _dict['result'] = self.result.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ApiGatewayOperationItemResp object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ApiGatewayOperationItemResp') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ApiGatewayOperationItemResp') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ApiGatewayOperationsLabelsResp:
    """
    API Gateway operations labels update response.

    :param bool success: Was operation successful.
    :param List[List[str]] errors: Array of errors encountered.
    :param List[List[str]] messages: Array of messages returned.
    :param List[ApiGatewayOperationsLabelsRespResultItem] result: List of operations
          with their updated label sets.
    """

    def __init__(
        self,
        success: bool,
        errors: List[List[str]],
        messages: List[List[str]],
        result: List['ApiGatewayOperationsLabelsRespResultItem'],
    ) -> None:
        """
        Initialize a ApiGatewayOperationsLabelsResp object.

        :param bool success: Was operation successful.
        :param List[List[str]] errors: Array of errors encountered.
        :param List[List[str]] messages: Array of messages returned.
        :param List[ApiGatewayOperationsLabelsRespResultItem] result: List of
               operations with their updated label sets.
        """
        self.success = success
        self.errors = errors
        self.messages = messages
        self.result = result

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ApiGatewayOperationsLabelsResp':
        """Initialize a ApiGatewayOperationsLabelsResp object from a json dictionary."""
        args = {}
        if (success := _dict.get('success')) is not None:
            args['success'] = success
        else:
            raise ValueError('Required property \'success\' not present in ApiGatewayOperationsLabelsResp JSON')
        if (errors := _dict.get('errors')) is not None:
            args['errors'] = errors
        else:
            raise ValueError('Required property \'errors\' not present in ApiGatewayOperationsLabelsResp JSON')
        if (messages := _dict.get('messages')) is not None:
            args['messages'] = messages
        else:
            raise ValueError('Required property \'messages\' not present in ApiGatewayOperationsLabelsResp JSON')
        if (result := _dict.get('result')) is not None:
            args['result'] = [ApiGatewayOperationsLabelsRespResultItem.from_dict(v) for v in result]
        else:
            raise ValueError('Required property \'result\' not present in ApiGatewayOperationsLabelsResp JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ApiGatewayOperationsLabelsResp object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'success') and self.success is not None:
            _dict['success'] = self.success
        if hasattr(self, 'errors') and self.errors is not None:
            _dict['errors'] = self.errors
        if hasattr(self, 'messages') and self.messages is not None:
            _dict['messages'] = self.messages
        if hasattr(self, 'result') and self.result is not None:
            result_list = []
            for v in self.result:
                if isinstance(v, dict):
                    result_list.append(v)
                else:
                    result_list.append(v.to_dict())
            _dict['result'] = result_list
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ApiGatewayOperationsLabelsResp object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ApiGatewayOperationsLabelsResp') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ApiGatewayOperationsLabelsResp') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ApiGatewayOperationsResp:
    """
    API Gateway bulk operations create response.

    :param bool success: Was operation successful.
    :param List[List[str]] errors: Array of errors encountered.
    :param List[List[str]] messages: Array of messages returned.
    :param List[ApiGatewayOperationsRespResultItem] result: List of created
          operations.
    """

    def __init__(
        self,
        success: bool,
        errors: List[List[str]],
        messages: List[List[str]],
        result: List['ApiGatewayOperationsRespResultItem'],
    ) -> None:
        """
        Initialize a ApiGatewayOperationsResp object.

        :param bool success: Was operation successful.
        :param List[List[str]] errors: Array of errors encountered.
        :param List[List[str]] messages: Array of messages returned.
        :param List[ApiGatewayOperationsRespResultItem] result: List of created
               operations.
        """
        self.success = success
        self.errors = errors
        self.messages = messages
        self.result = result

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ApiGatewayOperationsResp':
        """Initialize a ApiGatewayOperationsResp object from a json dictionary."""
        args = {}
        if (success := _dict.get('success')) is not None:
            args['success'] = success
        else:
            raise ValueError('Required property \'success\' not present in ApiGatewayOperationsResp JSON')
        if (errors := _dict.get('errors')) is not None:
            args['errors'] = errors
        else:
            raise ValueError('Required property \'errors\' not present in ApiGatewayOperationsResp JSON')
        if (messages := _dict.get('messages')) is not None:
            args['messages'] = messages
        else:
            raise ValueError('Required property \'messages\' not present in ApiGatewayOperationsResp JSON')
        if (result := _dict.get('result')) is not None:
            args['result'] = [ApiGatewayOperationsRespResultItem.from_dict(v) for v in result]
        else:
            raise ValueError('Required property \'result\' not present in ApiGatewayOperationsResp JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ApiGatewayOperationsResp object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'success') and self.success is not None:
            _dict['success'] = self.success
        if hasattr(self, 'errors') and self.errors is not None:
            _dict['errors'] = self.errors
        if hasattr(self, 'messages') and self.messages is not None:
            _dict['messages'] = self.messages
        if hasattr(self, 'result') and self.result is not None:
            result_list = []
            for v in self.result:
                if isinstance(v, dict):
                    result_list.append(v)
                else:
                    result_list.append(v.to_dict())
            _dict['result'] = result_list
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ApiGatewayOperationsResp object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ApiGatewayOperationsResp') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ApiGatewayOperationsResp') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ApiGatewaySchemasResp:
    """
    API Gateway schemas response (OpenAPI schema format).

    :param bool success: Was operation successful.
    :param List[List[str]] errors: Array of errors encountered.
    :param List[List[str]] messages: Array of messages returned.
    :param dict result: API Gateway schemas rendered as an OpenAPI schema document.
    """

    def __init__(
        self,
        success: bool,
        errors: List[List[str]],
        messages: List[List[str]],
        result: dict,
    ) -> None:
        """
        Initialize a ApiGatewaySchemasResp object.

        :param bool success: Was operation successful.
        :param List[List[str]] errors: Array of errors encountered.
        :param List[List[str]] messages: Array of messages returned.
        :param dict result: API Gateway schemas rendered as an OpenAPI schema
               document.
        """
        self.success = success
        self.errors = errors
        self.messages = messages
        self.result = result

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ApiGatewaySchemasResp':
        """Initialize a ApiGatewaySchemasResp object from a json dictionary."""
        args = {}
        if (success := _dict.get('success')) is not None:
            args['success'] = success
        else:
            raise ValueError('Required property \'success\' not present in ApiGatewaySchemasResp JSON')
        if (errors := _dict.get('errors')) is not None:
            args['errors'] = errors
        else:
            raise ValueError('Required property \'errors\' not present in ApiGatewaySchemasResp JSON')
        if (messages := _dict.get('messages')) is not None:
            args['messages'] = messages
        else:
            raise ValueError('Required property \'messages\' not present in ApiGatewaySchemasResp JSON')
        if (result := _dict.get('result')) is not None:
            args['result'] = result
        else:
            raise ValueError('Required property \'result\' not present in ApiGatewaySchemasResp JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ApiGatewaySchemasResp object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'success') and self.success is not None:
            _dict['success'] = self.success
        if hasattr(self, 'errors') and self.errors is not None:
            _dict['errors'] = self.errors
        if hasattr(self, 'messages') and self.messages is not None:
            _dict['messages'] = self.messages
        if hasattr(self, 'result') and self.result is not None:
            _dict['result'] = self.result
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ApiGatewaySchemasResp object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ApiGatewaySchemasResp') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ApiGatewaySchemasResp') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class DiscoveryOperation:
    """
    A discovered API operation.

    :param str id: (optional) UUID of the discovered operation.
    :param str endpoint: (optional) The endpoint path. May contain path parameter
          templates in curly braces (e.g. /api/user/{var1}/details).
    :param str host: (optional) RFC3986-compliant host.
    :param str method: (optional) The HTTP method used to access the endpoint.
    :param datetime last_updated: (optional)
    :param List[str] origin: (optional) API discovery engine(s) that discovered this
          operation.
    :param str state: (optional) State of the operation in API Discovery. review -
          not yet saved to Endpoint Management; saved - saved to Endpoint Management;
          ignored - marked as ignored.
    :param DiscoveryOperationFeatures features: (optional)
    """

    def __init__(
        self,
        *,
        id: Optional[str] = None,
        endpoint: Optional[str] = None,
        host: Optional[str] = None,
        method: Optional[str] = None,
        last_updated: Optional[datetime] = None,
        origin: Optional[List[str]] = None,
        state: Optional[str] = None,
        features: Optional['DiscoveryOperationFeatures'] = None,
    ) -> None:
        """
        Initialize a DiscoveryOperation object.

        :param str id: (optional) UUID of the discovered operation.
        :param str endpoint: (optional) The endpoint path. May contain path
               parameter templates in curly braces (e.g. /api/user/{var1}/details).
        :param str host: (optional) RFC3986-compliant host.
        :param str method: (optional) The HTTP method used to access the endpoint.
        :param datetime last_updated: (optional)
        :param List[str] origin: (optional) API discovery engine(s) that discovered
               this operation.
        :param str state: (optional) State of the operation in API Discovery.
               review - not yet saved to Endpoint Management; saved - saved to Endpoint
               Management; ignored - marked as ignored.
        :param DiscoveryOperationFeatures features: (optional)
        """
        self.id = id
        self.endpoint = endpoint
        self.host = host
        self.method = method
        self.last_updated = last_updated
        self.origin = origin
        self.state = state
        self.features = features

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'DiscoveryOperation':
        """Initialize a DiscoveryOperation object from a json dictionary."""
        args = {}
        if (id := _dict.get('id')) is not None:
            args['id'] = id
        if (endpoint := _dict.get('endpoint')) is not None:
            args['endpoint'] = endpoint
        if (host := _dict.get('host')) is not None:
            args['host'] = host
        if (method := _dict.get('method')) is not None:
            args['method'] = method
        if (last_updated := _dict.get('last_updated')) is not None:
            args['last_updated'] = string_to_datetime(last_updated)
        if (origin := _dict.get('origin')) is not None:
            args['origin'] = origin
        if (state := _dict.get('state')) is not None:
            args['state'] = state
        if (features := _dict.get('features')) is not None:
            args['features'] = DiscoveryOperationFeatures.from_dict(features)
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a DiscoveryOperation object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        if hasattr(self, 'endpoint') and self.endpoint is not None:
            _dict['endpoint'] = self.endpoint
        if hasattr(self, 'host') and self.host is not None:
            _dict['host'] = self.host
        if hasattr(self, 'method') and self.method is not None:
            _dict['method'] = self.method
        if hasattr(self, 'last_updated') and self.last_updated is not None:
            _dict['last_updated'] = datetime_to_string(self.last_updated)
        if hasattr(self, 'origin') and self.origin is not None:
            _dict['origin'] = self.origin
        if hasattr(self, 'state') and self.state is not None:
            _dict['state'] = self.state
        if hasattr(self, 'features') and self.features is not None:
            if isinstance(self.features, dict):
                _dict['features'] = self.features
            else:
                _dict['features'] = self.features.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this DiscoveryOperation object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'DiscoveryOperation') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'DiscoveryOperation') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class MethodEnum(str, Enum):
        """
        The HTTP method used to access the endpoint.
        """

        GET = 'GET'
        POST = 'POST'
        HEAD = 'HEAD'
        OPTIONS = 'OPTIONS'
        PUT = 'PUT'
        DELETE = 'DELETE'
        CONNECT = 'CONNECT'
        PATCH = 'PATCH'
        TRACE = 'TRACE'


    class OriginEnum(str, Enum):
        """
        origin.
        """

        ML = 'ML'
        SESSIONIDENTIFIER = 'SessionIdentifier'
        LABELDISCOVERY = 'LabelDiscovery'


    class StateEnum(str, Enum):
        """
        State of the operation in API Discovery. review - not yet saved to Endpoint
        Management; saved - saved to Endpoint Management; ignored - marked as ignored.
        """

        REVIEW = 'review'
        SAVED = 'saved'
        IGNORED = 'ignored'



class DiscoveryOperationsListResp:
    """
    API Gateway discovery operations list response.

    :param bool success: Was operation successful.
    :param List[List[str]] errors: Array of errors encountered.
    :param List[List[str]] messages: Array of messages returned.
    :param List[DiscoveryOperation] result:
    :param ResultInfo result_info: (optional)
    """

    def __init__(
        self,
        success: bool,
        errors: List[List[str]],
        messages: List[List[str]],
        result: List['DiscoveryOperation'],
        *,
        result_info: Optional['ResultInfo'] = None,
    ) -> None:
        """
        Initialize a DiscoveryOperationsListResp object.

        :param bool success: Was operation successful.
        :param List[List[str]] errors: Array of errors encountered.
        :param List[List[str]] messages: Array of messages returned.
        :param List[DiscoveryOperation] result:
        :param ResultInfo result_info: (optional)
        """
        self.success = success
        self.errors = errors
        self.messages = messages
        self.result = result
        self.result_info = result_info

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'DiscoveryOperationsListResp':
        """Initialize a DiscoveryOperationsListResp object from a json dictionary."""
        args = {}
        if (success := _dict.get('success')) is not None:
            args['success'] = success
        else:
            raise ValueError('Required property \'success\' not present in DiscoveryOperationsListResp JSON')
        if (errors := _dict.get('errors')) is not None:
            args['errors'] = errors
        else:
            raise ValueError('Required property \'errors\' not present in DiscoveryOperationsListResp JSON')
        if (messages := _dict.get('messages')) is not None:
            args['messages'] = messages
        else:
            raise ValueError('Required property \'messages\' not present in DiscoveryOperationsListResp JSON')
        if (result := _dict.get('result')) is not None:
            args['result'] = [DiscoveryOperation.from_dict(v) for v in result]
        else:
            raise ValueError('Required property \'result\' not present in DiscoveryOperationsListResp JSON')
        if (result_info := _dict.get('result_info')) is not None:
            args['result_info'] = ResultInfo.from_dict(result_info)
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a DiscoveryOperationsListResp object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'success') and self.success is not None:
            _dict['success'] = self.success
        if hasattr(self, 'errors') and self.errors is not None:
            _dict['errors'] = self.errors
        if hasattr(self, 'messages') and self.messages is not None:
            _dict['messages'] = self.messages
        if hasattr(self, 'result') and self.result is not None:
            result_list = []
            for v in self.result:
                if isinstance(v, dict):
                    result_list.append(v)
                else:
                    result_list.append(v.to_dict())
            _dict['result'] = result_list
        if hasattr(self, 'result_info') and self.result_info is not None:
            if isinstance(self.result_info, dict):
                _dict['result_info'] = self.result_info
            else:
                _dict['result_info'] = self.result_info.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this DiscoveryOperationsListResp object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'DiscoveryOperationsListResp') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'DiscoveryOperationsListResp') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class DiscoveryOperationsPatchResp:
    """
    API Gateway discovery operations bulk patch response.

    :param bool success: Was operation successful.
    :param List[List[str]] errors: Array of errors encountered.
    :param List[List[str]] messages: Array of messages returned.
    :param List[DiscoveryOperation] result:
    """

    def __init__(
        self,
        success: bool,
        errors: List[List[str]],
        messages: List[List[str]],
        result: List['DiscoveryOperation'],
    ) -> None:
        """
        Initialize a DiscoveryOperationsPatchResp object.

        :param bool success: Was operation successful.
        :param List[List[str]] errors: Array of errors encountered.
        :param List[List[str]] messages: Array of messages returned.
        :param List[DiscoveryOperation] result:
        """
        self.success = success
        self.errors = errors
        self.messages = messages
        self.result = result

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'DiscoveryOperationsPatchResp':
        """Initialize a DiscoveryOperationsPatchResp object from a json dictionary."""
        args = {}
        if (success := _dict.get('success')) is not None:
            args['success'] = success
        else:
            raise ValueError('Required property \'success\' not present in DiscoveryOperationsPatchResp JSON')
        if (errors := _dict.get('errors')) is not None:
            args['errors'] = errors
        else:
            raise ValueError('Required property \'errors\' not present in DiscoveryOperationsPatchResp JSON')
        if (messages := _dict.get('messages')) is not None:
            args['messages'] = messages
        else:
            raise ValueError('Required property \'messages\' not present in DiscoveryOperationsPatchResp JSON')
        if (result := _dict.get('result')) is not None:
            args['result'] = [DiscoveryOperation.from_dict(v) for v in result]
        else:
            raise ValueError('Required property \'result\' not present in DiscoveryOperationsPatchResp JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a DiscoveryOperationsPatchResp object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'success') and self.success is not None:
            _dict['success'] = self.success
        if hasattr(self, 'errors') and self.errors is not None:
            _dict['errors'] = self.errors
        if hasattr(self, 'messages') and self.messages is not None:
            _dict['messages'] = self.messages
        if hasattr(self, 'result') and self.result is not None:
            result_list = []
            for v in self.result:
                if isinstance(v, dict):
                    result_list.append(v)
                else:
                    result_list.append(v.to_dict())
            _dict['result'] = result_list
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this DiscoveryOperationsPatchResp object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'DiscoveryOperationsPatchResp') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'DiscoveryOperationsPatchResp') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ResultInfo:
    """
    ResultInfo.

    :param int count: (optional) Total number of results for the requested service.
    :param int page: (optional) Current page within paginated list of results.
    :param int per_page: (optional) Number of results per page.
    :param int total_count: (optional) Total number of results.
    """

    def __init__(
        self,
        *,
        count: Optional[int] = None,
        page: Optional[int] = None,
        per_page: Optional[int] = None,
        total_count: Optional[int] = None,
    ) -> None:
        """
        Initialize a ResultInfo object.

        :param int count: (optional) Total number of results for the requested
               service.
        :param int page: (optional) Current page within paginated list of results.
        :param int per_page: (optional) Number of results per page.
        :param int total_count: (optional) Total number of results.
        """
        self.count = count
        self.page = page
        self.per_page = per_page
        self.total_count = total_count

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ResultInfo':
        """Initialize a ResultInfo object from a json dictionary."""
        args = {}
        if (count := _dict.get('count')) is not None:
            args['count'] = count
        if (page := _dict.get('page')) is not None:
            args['page'] = page
        if (per_page := _dict.get('per_page')) is not None:
            args['per_page'] = per_page
        if (total_count := _dict.get('total_count')) is not None:
            args['total_count'] = total_count
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ResultInfo object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'count') and self.count is not None:
            _dict['count'] = self.count
        if hasattr(self, 'page') and self.page is not None:
            _dict['page'] = self.page
        if hasattr(self, 'per_page') and self.per_page is not None:
            _dict['per_page'] = self.per_page
        if hasattr(self, 'total_count') and self.total_count is not None:
            _dict['total_count'] = self.total_count
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ResultInfo object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ResultInfo') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ResultInfo') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other
