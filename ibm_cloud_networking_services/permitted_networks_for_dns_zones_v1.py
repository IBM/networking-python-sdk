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
Permitted Networks for DNS Zones
"""

from datetime import datetime
from enum import Enum
from typing import Dict, List
import json

from ibm_cloud_sdk_core import BaseService, DetailedResponse
from ibm_cloud_sdk_core.authenticators.authenticator import Authenticator
from ibm_cloud_sdk_core.get_authenticator import get_authenticator_from_environment
from ibm_cloud_sdk_core.utils import convert_model, datetime_to_string, string_to_datetime

from .common import get_sdk_headers

##############################################################################
# Service
##############################################################################

class PermittedNetworksForDnsZonesV1(BaseService):
    """The Permitted Networks for DNS Zones V1 service."""

    DEFAULT_SERVICE_URL = 'https://api.dns-svcs.cloud.ibm.com/v1'
    DEFAULT_SERVICE_NAME = 'permitted_networks_for_dns_zones'

    @classmethod
    def new_instance(cls,
                     service_name: str = DEFAULT_SERVICE_NAME,
                    ) -> 'PermittedNetworksForDnsZonesV1':
        """
        Return a new client for the Permitted Networks for DNS Zones service using
               the specified parameters and external configuration.
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
        Construct a new client for the Permitted Networks for DNS Zones service.

        :param Authenticator authenticator: The authenticator specifies the authentication mechanism.
               Get up to date information from https://github.com/IBM/python-sdk-core/blob/master/README.md
               about initializing the authenticator of your choice.
        """
        BaseService.__init__(self,
                             service_url=self.DEFAULT_SERVICE_URL,
                             authenticator=authenticator)


    #########################
    # Permitted Network
    #########################


    def list_permitted_networks(self, instance_id: str, dnszone_id: str, *, x_correlation_id: str = None, offset: str = None, limit: str = None, **kwargs) -> DetailedResponse:
        """
        List permitted networks.

        List the permitted networks for a given DNS zone.

        :param str instance_id: The unique identifier of a service instance.
        :param str dnszone_id: The unique identifier of a DNS zone.
        :param str x_correlation_id: (optional) Uniquely identifying a request.
        :param str offset: (optional) Specify how many permitted networks to skip
               over, the default value is 0.
        :param str limit: (optional) Specify how many permitted networks are
               returned, the default value is 10.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ListPermittedNetworks` object
        """

        if instance_id is None:
            raise ValueError('instance_id must be provided')
        if dnszone_id is None:
            raise ValueError('dnszone_id must be provided')
        headers = {
            'X-Correlation-ID': x_correlation_id
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME, service_version='V1', operation_id='list_permitted_networks')
        headers.update(sdk_headers)

        params = {
            'offset': offset,
            'limit': limit
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/instances/{0}/dnszones/{1}/permitted_networks'.format(*self.encode_path_vars(instance_id, dnszone_id))
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers,
                                       params=params)

        response = self.send(request)
        return response


    def create_permitted_network(self, instance_id: str, dnszone_id: str, *, type: str = None, permitted_network: 'PermittedNetworkVpc' = None, x_correlation_id: str = None, **kwargs) -> DetailedResponse:
        """
        Create a permitted network.

        Create a permitted network for a given DNS zone.

        :param str instance_id: The unique identifier of a service instance.
        :param str dnszone_id: The unique identifier of a DNS zone.
        :param str type: (optional) The type of a permitted network.
        :param PermittedNetworkVpc permitted_network: (optional) Permitted network
               data for VPC.
        :param str x_correlation_id: (optional) Uniquely identifying a request.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `PermittedNetwork` object
        """

        if instance_id is None:
            raise ValueError('instance_id must be provided')
        if dnszone_id is None:
            raise ValueError('dnszone_id must be provided')
        if permitted_network is not None:
            permitted_network = convert_model(permitted_network)
        headers = {
            'X-Correlation-ID': x_correlation_id
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME, service_version='V1', operation_id='create_permitted_network')
        headers.update(sdk_headers)

        data = {
            'type': type,
            'permitted_network': permitted_network
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/instances/{0}/dnszones/{1}/permitted_networks'.format(*self.encode_path_vars(instance_id, dnszone_id))
        request = self.prepare_request(method='POST',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request)
        return response


    def delete_permitted_network(self, instance_id: str, dnszone_id: str, permitted_network_id: str, *, x_correlation_id: str = None, **kwargs) -> DetailedResponse:
        """
        Remove a permitted network.

        Remove a permitted network.

        :param str instance_id: The unique identifier of a service instance.
        :param str dnszone_id: The unique identifier of a DNS zone.
        :param str permitted_network_id: The unique identifier of a permitted
               network.
        :param str x_correlation_id: (optional) Uniquely identifying a request.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `PermittedNetwork` object
        """

        if instance_id is None:
            raise ValueError('instance_id must be provided')
        if dnszone_id is None:
            raise ValueError('dnszone_id must be provided')
        if permitted_network_id is None:
            raise ValueError('permitted_network_id must be provided')
        headers = {
            'X-Correlation-ID': x_correlation_id
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME, service_version='V1', operation_id='delete_permitted_network')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/instances/{0}/dnszones/{1}/permitted_networks/{2}'.format(*self.encode_path_vars(instance_id, dnszone_id, permitted_network_id))
        request = self.prepare_request(method='DELETE',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response


    def get_permitted_network(self, instance_id: str, dnszone_id: str, permitted_network_id: str, *, x_correlation_id: str = None, **kwargs) -> DetailedResponse:
        """
        Get a permitted network.

        Get details of a permitted network.

        :param str instance_id: The unique identifier of a service instance.
        :param str dnszone_id: The unique identifier of a DNS zone.
        :param str permitted_network_id: The unique identifier of a permitted
               network.
        :param str x_correlation_id: (optional) Uniquely identifying a request.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `PermittedNetwork` object
        """

        if instance_id is None:
            raise ValueError('instance_id must be provided')
        if dnszone_id is None:
            raise ValueError('dnszone_id must be provided')
        if permitted_network_id is None:
            raise ValueError('permitted_network_id must be provided')
        headers = {
            'X-Correlation-ID': x_correlation_id
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME, service_version='V1', operation_id='get_permitted_network')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/instances/{0}/dnszones/{1}/permitted_networks/{2}'.format(*self.encode_path_vars(instance_id, dnszone_id, permitted_network_id))
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response

