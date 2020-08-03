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
This document describes CIS WAF API.
"""

from typing import Dict, List
import json

from ibm_cloud_sdk_core import BaseService, DetailedResponse
from ibm_cloud_sdk_core.authenticators.authenticator import Authenticator
from ibm_cloud_sdk_core.get_authenticator import get_authenticator_from_environment

from .common import get_sdk_headers

##############################################################################
# Service
##############################################################################

class WafApiV1(BaseService):
    """The WAF API V1 service."""

    DEFAULT_SERVICE_URL = 'https://api.cis.cloud.ibm.com'
    DEFAULT_SERVICE_NAME = 'waf_api'

    @classmethod
    def new_instance(cls,
                     crn: str,
                     zone_id: str,
                     service_name: str = DEFAULT_SERVICE_NAME,
                    ) -> 'WafApiV1':
        """
        Return a new client for the WAF API service using the specified parameters
               and external configuration.

        :param str crn: cloud resource name.

        :param str zone_id: zone id.
        """
        if crn is None:
            raise ValueError('crn must be provided')
        if zone_id is None:
            raise ValueError('zone_id must be provided')

        authenticator = get_authenticator_from_environment(service_name)
        service = cls(
            crn,
            zone_id,
            authenticator
            )
        service.configure_service(service_name)
        return service

    def __init__(self,
                 crn: str,
                 zone_id: str,
                 authenticator: Authenticator = None,
                ) -> None:
        """
        Construct a new client for the WAF API service.

        :param str crn: cloud resource name.

        :param str zone_id: zone id.

        :param Authenticator authenticator: The authenticator specifies the authentication mechanism.
               Get up to date information from https://github.com/IBM/python-sdk-core/blob/master/README.md
               about initializing the authenticator of your choice.
        """
        if crn is None:
            raise ValueError('crn must be provided')
        if zone_id is None:
            raise ValueError('zone_id must be provided')

        BaseService.__init__(self,
                             service_url=self.DEFAULT_SERVICE_URL,
                             authenticator=authenticator)
        self.crn = crn
        self.zone_id = zone_id


    #########################
    # WAF
    #########################


    def get_waf_settings(self,
        **kwargs
    ) -> DetailedResponse:
        """
        Get WAF setting.

        Get WAF of a specific zone.

        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `WafResponse` object
        """

        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='get_waf_settings')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v1/{0}/zones/{1}/settings/waf'.format(
            *self.encode_path_vars(self.crn, self.zone_id))
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response


    def update_waf_settings(self,
        *,
        value: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Set WAF setting.

        Set WAF (on | off) for a specific zone.

        :param str value: (optional) value.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `WafResponse` object
        """

        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='update_waf_settings')
        headers.update(sdk_headers)

        data = {
            'value': value
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v1/{0}/zones/{1}/settings/waf'.format(
            *self.encode_path_vars(self.crn, self.zone_id))
        request = self.prepare_request(method='PATCH',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request)
        return response


##############################################################################
# Models
##############################################################################


class WafResponseResult():
    """
    result.

    :attr str id: (optional) id.
    :attr str value: (optional) value.
    :attr bool editable: (optional) editable.
    :attr str modified_on: (optional) modified date.
    """

    def __init__(self,
                 *,
                 id: str = None,
                 value: str = None,
                 editable: bool = None,
                 modified_on: str = None) -> None:
        """
        Initialize a WafResponseResult object.

        :param str id: (optional) id.
        :param str value: (optional) value.
        :param bool editable: (optional) editable.
        :param str modified_on: (optional) modified date.
        """
        self.id = id
        self.value = value
        self.editable = editable
        self.modified_on = modified_on

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'WafResponseResult':
        """Initialize a WafResponseResult object from a json dictionary."""
        args = {}
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        if 'value' in _dict:
            args['value'] = _dict.get('value')
        if 'editable' in _dict:
            args['editable'] = _dict.get('editable')
        if 'modified_on' in _dict:
            args['modified_on'] = _dict.get('modified_on')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a WafResponseResult object from a json dictionary."""
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
            _dict['modified_on'] = self.modified_on
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this WafResponseResult object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'WafResponseResult') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'WafResponseResult') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class WafResponse():
    """
    waf response.

    :attr bool success: success.
    :attr List[List[str]] errors: errors.
    :attr List[List[str]] messages: messages.
    :attr WafResponseResult result: result.
    """

    def __init__(self,
                 success: bool,
                 errors: List[List[str]],
                 messages: List[List[str]],
                 result: 'WafResponseResult') -> None:
        """
        Initialize a WafResponse object.

        :param bool success: success.
        :param List[List[str]] errors: errors.
        :param List[List[str]] messages: messages.
        :param WafResponseResult result: result.
        """
        self.success = success
        self.errors = errors
        self.messages = messages
        self.result = result

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'WafResponse':
        """Initialize a WafResponse object from a json dictionary."""
        args = {}
        if 'success' in _dict:
            args['success'] = _dict.get('success')
        else:
            raise ValueError('Required property \'success\' not present in WafResponse JSON')
        if 'errors' in _dict:
            args['errors'] = _dict.get('errors')
        else:
            raise ValueError('Required property \'errors\' not present in WafResponse JSON')
        if 'messages' in _dict:
            args['messages'] = _dict.get('messages')
        else:
            raise ValueError('Required property \'messages\' not present in WafResponse JSON')
        if 'result' in _dict:
            args['result'] = WafResponseResult.from_dict(_dict.get('result'))
        else:
            raise ValueError('Required property \'result\' not present in WafResponse JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a WafResponse object from a json dictionary."""
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
            _dict['result'] = self.result.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this WafResponse object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'WafResponse') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'WafResponse') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other
