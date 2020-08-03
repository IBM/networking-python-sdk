# coding: utf-8

# (C) Copyright IBM Corp. 2020.
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

"""
Routing
"""

from datetime import datetime
from typing import Dict, List
import json

from ibm_cloud_sdk_core import BaseService, DetailedResponse
from ibm_cloud_sdk_core.authenticators.authenticator import Authenticator
from ibm_cloud_sdk_core.get_authenticator import get_authenticator_from_environment
from ibm_cloud_sdk_core.utils import datetime_to_string, string_to_datetime

from .common import get_sdk_headers

##############################################################################
# Service
##############################################################################

class RoutingV1(BaseService):
    """The Routing V1 service."""

    DEFAULT_SERVICE_URL = 'https://api.cis.cloud.ibm.com'
    DEFAULT_SERVICE_NAME = 'routing'

    @classmethod
    def new_instance(cls,
                     crn: str,
                     zone_identifier: str,
                     service_name: str = DEFAULT_SERVICE_NAME,
                    ) -> 'RoutingV1':
        """
        Return a new client for the Routing service using the specified parameters
               and external configuration.

        :param str crn: Full url-encoded cloud resource name (CRN) of resource
               instance.

        :param str zone_identifier: Zone identifier.
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

    def __init__(self,
                 crn: str,
                 zone_identifier: str,
                 authenticator: Authenticator = None,
                ) -> None:
        """
        Construct a new client for the Routing service.

        :param str crn: Full url-encoded cloud resource name (CRN) of resource
               instance.

        :param str zone_identifier: Zone identifier.

        :param Authenticator authenticator: The authenticator specifies the authentication mechanism.
               Get up to date information from https://github.com/IBM/python-sdk-core/blob/master/README.md
               about initializing the authenticator of your choice.
        """
        if crn is None:
            raise ValueError('crn must be provided')
        if zone_identifier is None:
            raise ValueError('zone_identifier must be provided')

        BaseService.__init__(self,
                             service_url=self.DEFAULT_SERVICE_URL,
                             authenticator=authenticator)
        self.crn = crn
        self.zone_identifier = zone_identifier


    #########################
    # Routing
    #########################


    def get_smart_routing(self,
        **kwargs
    ) -> DetailedResponse:
        """
        Get Routing feature smart routing setting.

        Get Routing feature smart routing setting for a zone.

        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `SmartRoutingResp` object
        """

        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='get_smart_routing')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v1/{0}/zones/{1}/routing/smart_routing'.format(
            *self.encode_path_vars(self.crn, self.zone_identifier))
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response


    def update_smart_routing(self,
        *,
        value: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Update Routing feature smart route setting.

        Update Routing feature smart route setting for a zone.

        :param str value: (optional) Value.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `SmartRoutingResp` object
        """

        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='update_smart_routing')
        headers.update(sdk_headers)

        data = {
            'value': value
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v1/{0}/zones/{1}/routing/smart_routing'.format(
            *self.encode_path_vars(self.crn, self.zone_identifier))
        request = self.prepare_request(method='PATCH',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request)
        return response


##############################################################################
# Models
##############################################################################


class SmartRoutingRespResult():
    """
    Container for response information.

    :attr str id: ID.
    :attr str value: Value.
    :attr bool editable: Editable.
    :attr datetime modified_on: Modified date.
    """

    def __init__(self,
                 id: str,
                 value: str,
                 editable: bool,
                 modified_on: datetime) -> None:
        """
        Initialize a SmartRoutingRespResult object.

        :param str id: ID.
        :param str value: Value.
        :param bool editable: Editable.
        :param datetime modified_on: Modified date.
        """
        self.id = id
        self.value = value
        self.editable = editable
        self.modified_on = modified_on

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'SmartRoutingRespResult':
        """Initialize a SmartRoutingRespResult object from a json dictionary."""
        args = {}
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        else:
            raise ValueError('Required property \'id\' not present in SmartRoutingRespResult JSON')
        if 'value' in _dict:
            args['value'] = _dict.get('value')
        else:
            raise ValueError('Required property \'value\' not present in SmartRoutingRespResult JSON')
        if 'editable' in _dict:
            args['editable'] = _dict.get('editable')
        else:
            raise ValueError('Required property \'editable\' not present in SmartRoutingRespResult JSON')
        if 'modified_on' in _dict:
            args['modified_on'] = string_to_datetime(_dict.get('modified_on'))
        else:
            raise ValueError('Required property \'modified_on\' not present in SmartRoutingRespResult JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a SmartRoutingRespResult object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        if hasattr(self, 'value') and self.value is not None:
            _dict['value'] = self.value
        if hasattr(self, 'editable') and self.editable is not None:
            _dict['editable'] = self.editable
        if hasattr(self, 'modified_on') and self.modified_on is not None:
            _dict['modified_on'] = datetime_to_string(self.modified_on)
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this SmartRoutingRespResult object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'SmartRoutingRespResult') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'SmartRoutingRespResult') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class SmartRoutingResp():
    """
    smart routing response.

    :attr SmartRoutingRespResult result: Container for response information.
    :attr bool success: Was the get successful.
    :attr List[List[str]] errors: Array of errors encountered.
    :attr List[List[str]] messages: Array of messages returned.
    """

    def __init__(self,
                 result: 'SmartRoutingRespResult',
                 success: bool,
                 errors: List[List[str]],
                 messages: List[List[str]]) -> None:
        """
        Initialize a SmartRoutingResp object.

        :param SmartRoutingRespResult result: Container for response information.
        :param bool success: Was the get successful.
        :param List[List[str]] errors: Array of errors encountered.
        :param List[List[str]] messages: Array of messages returned.
        """
        self.result = result
        self.success = success
        self.errors = errors
        self.messages = messages

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'SmartRoutingResp':
        """Initialize a SmartRoutingResp object from a json dictionary."""
        args = {}
        if 'result' in _dict:
            args['result'] = SmartRoutingRespResult.from_dict(_dict.get('result'))
        else:
            raise ValueError('Required property \'result\' not present in SmartRoutingResp JSON')
        if 'success' in _dict:
            args['success'] = _dict.get('success')
        else:
            raise ValueError('Required property \'success\' not present in SmartRoutingResp JSON')
        if 'errors' in _dict:
            args['errors'] = _dict.get('errors')
        else:
            raise ValueError('Required property \'errors\' not present in SmartRoutingResp JSON')
        if 'messages' in _dict:
            args['messages'] = _dict.get('messages')
        else:
            raise ValueError('Required property \'messages\' not present in SmartRoutingResp JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a SmartRoutingResp object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'result') and self.result is not None:
            _dict['result'] = self.result.to_dict()
        if hasattr(self, 'success') and self.success is not None:
            _dict['success'] = self.success
        if hasattr(self, 'errors') and self.errors is not None:
            _dict['errors'] = self.errors
        if hasattr(self, 'messages') and self.messages is not None:
            _dict['messages'] = self.messages
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this SmartRoutingResp object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'SmartRoutingResp') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'SmartRoutingResp') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other
