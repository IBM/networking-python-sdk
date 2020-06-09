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
DNS Zones
"""

from datetime import datetime
from enum import Enum
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

class DnsZonesV1(BaseService):
    """The DNS Zones V1 service."""

    DEFAULT_SERVICE_URL = 'https://api.dns-svcs.cloud.ibm.com/v1'
    DEFAULT_SERVICE_NAME = 'dns_zones'

    @classmethod
    def new_instance(cls,
                     service_name: str = DEFAULT_SERVICE_NAME,
                    ) -> 'DnsZonesV1':
        """
        Return a new client for the DNS Zones service using the specified
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
        Construct a new client for the DNS Zones service.

        :param Authenticator authenticator: The authenticator specifies the authentication mechanism.
               Get up to date information from https://github.com/IBM/python-sdk-core/blob/master/README.md
               about initializing the authenticator of your choice.
        """
        BaseService.__init__(self,
                             service_url=self.DEFAULT_SERVICE_URL,
                             authenticator=authenticator)


    #########################
    # DNS Zones
    #########################


    def list_dnszones(self, instance_id: str, *, x_correlation_id: str = None, offset: int = None, limit: int = None, vpc_id: str = None, **kwargs) -> DetailedResponse:
        """
        List DNS zones.

        List the DNS zones for a given service instance.

        :param str instance_id: The unique identifier of a service instance.
        :param str x_correlation_id: (optional) Uniquely identifying a request.
        :param int offset: (optional) Specify how many DNS zones to skip over, the
               default value is 0.
        :param int limit: (optional) Specify how many DNS zones are returned, the
               default value is 10.
        :param str vpc_id: (optional) Specify the VPC instance id.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ListDnszones` object
        """

        if instance_id is None:
            raise ValueError('instance_id must be provided')
        headers = {
            'X-Correlation-ID': x_correlation_id
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME, service_version='V1', operation_id='list_dnszones')
        headers.update(sdk_headers)

        params = {
            'offset': offset,
            'limit': limit,
            'vpc_id': vpc_id
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/instances/{0}/dnszones'.format(*self.encode_path_vars(instance_id))
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers,
                                       params=params)

        response = self.send(request)
        return response


    def create_dnszone(self, instance_id: str, *, name: str = None, description: str = None, label: str = None, x_correlation_id: str = None, **kwargs) -> DetailedResponse:
        """
        Create a DNS zone.

        Create a DNS zone for a given service instance.

        :param str instance_id: The unique identifier of a service instance.
        :param str name: (optional) Name of DNS zone.
        :param str description: (optional) The text describing the purpose of a DNS
               zone.
        :param str label: (optional) The label of a DNS zone.
        :param str x_correlation_id: (optional) Uniquely identifying a request.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `Dnszone` object
        """

        if instance_id is None:
            raise ValueError('instance_id must be provided')
        headers = {
            'X-Correlation-ID': x_correlation_id
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME, service_version='V1', operation_id='create_dnszone')
        headers.update(sdk_headers)

        data = {
            'name': name,
            'description': description,
            'label': label
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/instances/{0}/dnszones'.format(*self.encode_path_vars(instance_id))
        request = self.prepare_request(method='POST',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request)
        return response


    def delete_dnszone(self, instance_id: str, dnszone_id: str, *, x_correlation_id: str = None, **kwargs) -> DetailedResponse:
        """
        Delete a DNS zone.

        Delete a DNS zone.

        :param str instance_id: The unique identifier of a service instance.
        :param str dnszone_id: The unique identifier of a DNS zone.
        :param str x_correlation_id: (optional) Uniquely identifying a request.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if instance_id is None:
            raise ValueError('instance_id must be provided')
        if dnszone_id is None:
            raise ValueError('dnszone_id must be provided')
        headers = {
            'X-Correlation-ID': x_correlation_id
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME, service_version='V1', operation_id='delete_dnszone')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/instances/{0}/dnszones/{1}'.format(*self.encode_path_vars(instance_id, dnszone_id))
        request = self.prepare_request(method='DELETE',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response


    def get_dnszone(self, instance_id: str, dnszone_id: str, *, x_correlation_id: str = None, **kwargs) -> DetailedResponse:
        """
        Get a DNS zone.

        Get details of a DNS zone.

        :param str instance_id: The unique identifier of a service instance.
        :param str dnszone_id: The unique identifier of a DNS zone.
        :param str x_correlation_id: (optional) Uniquely identifying a request.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `Dnszone` object
        """

        if instance_id is None:
            raise ValueError('instance_id must be provided')
        if dnszone_id is None:
            raise ValueError('dnszone_id must be provided')
        headers = {
            'X-Correlation-ID': x_correlation_id
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME, service_version='V1', operation_id='get_dnszone')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/instances/{0}/dnszones/{1}'.format(*self.encode_path_vars(instance_id, dnszone_id))
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response


    def update_dnszone(self, instance_id: str, dnszone_id: str, *, description: str = None, label: str = None, x_correlation_id: str = None, **kwargs) -> DetailedResponse:
        """
        Update the properties of a DNS zone.

        Update the properties of a DNS zone.

        :param str instance_id: The unique identifier of a service instance.
        :param str dnszone_id: The unique identifier of a DNS zone.
        :param str description: (optional) The text describing the purpose of a DNS
               zone.
        :param str label: (optional) The label of a DNS zone.
        :param str x_correlation_id: (optional) Uniquely identifying a request.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `Dnszone` object
        """

        if instance_id is None:
            raise ValueError('instance_id must be provided')
        if dnszone_id is None:
            raise ValueError('dnszone_id must be provided')
        headers = {
            'X-Correlation-ID': x_correlation_id
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME, service_version='V1', operation_id='update_dnszone')
        headers.update(sdk_headers)

        data = {
            'description': description,
            'label': label
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/instances/{0}/dnszones/{1}'.format(*self.encode_path_vars(instance_id, dnszone_id))
        request = self.prepare_request(method='PATCH',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request)
        return response
