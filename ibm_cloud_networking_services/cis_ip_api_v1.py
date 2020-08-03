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
This document describes CIS IP API.
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

class CisIpApiV1(BaseService):
    """The CIS IP API V1 service."""

    DEFAULT_SERVICE_URL = 'https://api.cis.cloud.ibm.com'
    DEFAULT_SERVICE_NAME = 'cis_ip_api'

    @classmethod
    def new_instance(cls,
                     service_name: str = DEFAULT_SERVICE_NAME,
                    ) -> 'CisIpApiV1':
        """
        Return a new client for the CIS IP API service using the specified
               parameters and external configuration.
        """
        authenticator = get_authenticator_from_environment(service_name)
        service = cls(
            authenticator
            )
        service.configure_service(service_name)
        return service

    def __init__(self,
                 authenticator: Authenticator = None,
                ) -> None:
        """
        Construct a new client for the CIS IP API service.

        :param Authenticator authenticator: The authenticator specifies the authentication mechanism.
               Get up to date information from https://github.com/IBM/python-sdk-core/blob/master/README.md
               about initializing the authenticator of your choice.
        """
        BaseService.__init__(self,
                             service_url=self.DEFAULT_SERVICE_URL,
                             authenticator=authenticator)


    #########################
    # IP
    #########################


    def list_ips(self,
        **kwargs
    ) -> DetailedResponse:
        """
        List of all IP addresses used by the CIS proxy.

        List of all IP addresses used by the CIS proxy.

        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `IpResponse` object
        """

        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='list_ips')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v1/ips'
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response


##############################################################################
# Models
##############################################################################


class IpResponseResult():
    """
    Container for response information.

    :attr List[str] ipv4_cidrs: (optional) List of IPv4 CIDR addresses.
    :attr List[str] ipv6_cidrs: (optional) List of IPv6 CIDR addresses.
    """

    def __init__(self,
                 *,
                 ipv4_cidrs: List[str] = None,
                 ipv6_cidrs: List[str] = None) -> None:
        """
        Initialize a IpResponseResult object.

        :param List[str] ipv4_cidrs: (optional) List of IPv4 CIDR addresses.
        :param List[str] ipv6_cidrs: (optional) List of IPv6 CIDR addresses.
        """
        self.ipv4_cidrs = ipv4_cidrs
        self.ipv6_cidrs = ipv6_cidrs

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'IpResponseResult':
        """Initialize a IpResponseResult object from a json dictionary."""
        args = {}
        if 'ipv4_cidrs' in _dict:
            args['ipv4_cidrs'] = _dict.get('ipv4_cidrs')
        if 'ipv6_cidrs' in _dict:
            args['ipv6_cidrs'] = _dict.get('ipv6_cidrs')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a IpResponseResult object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'ipv4_cidrs') and self.ipv4_cidrs is not None:
            _dict['ipv4_cidrs'] = self.ipv4_cidrs
        if hasattr(self, 'ipv6_cidrs') and self.ipv6_cidrs is not None:
            _dict['ipv6_cidrs'] = self.ipv6_cidrs
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this IpResponseResult object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'IpResponseResult') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'IpResponseResult') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class IpResponse():
    """
    ip response.

    :attr bool success: Was operation successful.
    :attr List[List[str]] errors: errors.
    :attr List[List[str]] messages: messages.
    :attr IpResponseResult result: Container for response information.
    """

    def __init__(self,
                 success: bool,
                 errors: List[List[str]],
                 messages: List[List[str]],
                 result: 'IpResponseResult') -> None:
        """
        Initialize a IpResponse object.

        :param bool success: Was operation successful.
        :param List[List[str]] errors: errors.
        :param List[List[str]] messages: messages.
        :param IpResponseResult result: Container for response information.
        """
        self.success = success
        self.errors = errors
        self.messages = messages
        self.result = result

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'IpResponse':
        """Initialize a IpResponse object from a json dictionary."""
        args = {}
        if 'success' in _dict:
            args['success'] = _dict.get('success')
        else:
            raise ValueError('Required property \'success\' not present in IpResponse JSON')
        if 'errors' in _dict:
            args['errors'] = _dict.get('errors')
        else:
            raise ValueError('Required property \'errors\' not present in IpResponse JSON')
        if 'messages' in _dict:
            args['messages'] = _dict.get('messages')
        else:
            raise ValueError('Required property \'messages\' not present in IpResponse JSON')
        if 'result' in _dict:
            args['result'] = IpResponseResult.from_dict(_dict.get('result'))
        else:
            raise ValueError('Required property \'result\' not present in IpResponse JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a IpResponse object from a json dictionary."""
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
        """Return a `str` version of this IpResponse object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'IpResponse') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'IpResponse') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other
