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

# IBM OpenAPI SDK Code Generator Version: 3.20.0-debb9f29-20201203-202043
 
"""
DNS Services API
"""

from enum import Enum
from typing import Dict, List
import json

from ibm_cloud_sdk_core import BaseService, DetailedResponse
from ibm_cloud_sdk_core.authenticators.authenticator import Authenticator
from ibm_cloud_sdk_core.get_authenticator import get_authenticator_from_environment
from ibm_cloud_sdk_core.utils import convert_model

from .common import get_sdk_headers

##############################################################################
# Service
##############################################################################

class DnsSvcsV1(BaseService):
    """The DNS Svcs V1 service."""

    DEFAULT_SERVICE_URL = 'https://api.dns-svcs.cloud.ibm.com/v1'
    DEFAULT_SERVICE_NAME = 'dns_svcs'

    @classmethod
    def new_instance(cls,
                     service_name: str = DEFAULT_SERVICE_NAME,
                    ) -> 'DnsSvcsV1':
        """
        Return a new client for the DNS Svcs service using the specified parameters
               and external configuration.
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
        Construct a new client for the DNS Svcs service.

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


    def list_dnszones(self,
        instance_id: str,
        *,
        x_correlation_id: str = None,
        offset: int = None,
        limit: int = None,
        **kwargs
    ) -> DetailedResponse:
        """
        List DNS zones.

        List the DNS zones for a given service instance.

        :param str instance_id: The unique identifier of a service instance.
        :param str x_correlation_id: (optional) Uniquely identifying a request.
        :param int offset: (optional) Specify how many resource records to skip
               over, the default value is 0.
        :param int limit: (optional) Specify how many resource records are
               returned, the default value is 200.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ListDnszones` object
        """

        if instance_id is None:
            raise ValueError('instance_id must be provided')
        headers = {
            'X-Correlation-ID': x_correlation_id
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='list_dnszones')
        headers.update(sdk_headers)

        params = {
            'offset': offset,
            'limit': limit
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        path_param_keys = ['instance_id']
        path_param_values = self.encode_path_vars(instance_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/instances/{instance_id}/dnszones'.format(**path_param_dict)
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers,
                                       params=params)

        response = self.send(request)
        return response


    def create_dnszone(self,
        instance_id: str,
        *,
        name: str = None,
        description: str = None,
        label: str = None,
        x_correlation_id: str = None,
        **kwargs
    ) -> DetailedResponse:
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
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='create_dnszone')
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
        headers['Accept'] = 'application/json'

        path_param_keys = ['instance_id']
        path_param_values = self.encode_path_vars(instance_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/instances/{instance_id}/dnszones'.format(**path_param_dict)
        request = self.prepare_request(method='POST',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request)
        return response


    def delete_dnszone(self,
        instance_id: str,
        dnszone_id: str,
        *,
        x_correlation_id: str = None,
        **kwargs
    ) -> DetailedResponse:
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
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='delete_dnszone')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        path_param_keys = ['instance_id', 'dnszone_id']
        path_param_values = self.encode_path_vars(instance_id, dnszone_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/instances/{instance_id}/dnszones/{dnszone_id}'.format(**path_param_dict)
        request = self.prepare_request(method='DELETE',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response


    def get_dnszone(self,
        instance_id: str,
        dnszone_id: str,
        *,
        x_correlation_id: str = None,
        **kwargs
    ) -> DetailedResponse:
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
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='get_dnszone')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        path_param_keys = ['instance_id', 'dnszone_id']
        path_param_values = self.encode_path_vars(instance_id, dnszone_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/instances/{instance_id}/dnszones/{dnszone_id}'.format(**path_param_dict)
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response


    def update_dnszone(self,
        instance_id: str,
        dnszone_id: str,
        *,
        description: str = None,
        label: str = None,
        x_correlation_id: str = None,
        **kwargs
    ) -> DetailedResponse:
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
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='update_dnszone')
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
        headers['Accept'] = 'application/json'

        path_param_keys = ['instance_id', 'dnszone_id']
        path_param_values = self.encode_path_vars(instance_id, dnszone_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/instances/{instance_id}/dnszones/{dnszone_id}'.format(**path_param_dict)
        request = self.prepare_request(method='PATCH',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request)
        return response

    #########################
    # Resource Records
    #########################


    def list_resource_records(self,
        instance_id: str,
        dnszone_id: str,
        *,
        x_correlation_id: str = None,
        offset: int = None,
        limit: int = None,
        **kwargs
    ) -> DetailedResponse:
        """
        List Resource Records.

        List the Resource Records for a given DNS zone.

        :param str instance_id: The unique identifier of a service instance.
        :param str dnszone_id: The unique identifier of a DNS zone.
        :param str x_correlation_id: (optional) Uniquely identifying a request.
        :param int offset: (optional) Specify how many resource records to skip
               over, the default value is 0.
        :param int limit: (optional) Specify how many resource records are
               returned, the default value is 200.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ListResourceRecords` object
        """

        if instance_id is None:
            raise ValueError('instance_id must be provided')
        if dnszone_id is None:
            raise ValueError('dnszone_id must be provided')
        headers = {
            'X-Correlation-ID': x_correlation_id
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='list_resource_records')
        headers.update(sdk_headers)

        params = {
            'offset': offset,
            'limit': limit
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        path_param_keys = ['instance_id', 'dnszone_id']
        path_param_values = self.encode_path_vars(instance_id, dnszone_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/instances/{instance_id}/dnszones/{dnszone_id}/resource_records'.format(**path_param_dict)
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers,
                                       params=params)

        response = self.send(request)
        return response


    def create_resource_record(self,
        instance_id: str,
        dnszone_id: str,
        *,
        type: str = None,
        name: str = None,
        rdata: 'ResourceRecordInputRdata' = None,
        ttl: int = None,
        service: str = None,
        protocol: str = None,
        x_correlation_id: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Create a resource record.

        Create a resource record for a given DNS zone.

        :param str instance_id: The unique identifier of a service instance.
        :param str dnszone_id: The unique identifier of a DNS zone.
        :param str type: (optional) Type of the resource record.
        :param str name: (optional) Name of the resource record.
        :param ResourceRecordInputRdata rdata: (optional) Content of the resource
               record.
        :param int ttl: (optional) Time to live in second.
        :param str service: (optional) Only used for SRV record.
        :param str protocol: (optional) Only used for SRV record.
        :param str x_correlation_id: (optional) Uniquely identifying a request.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ResourceRecord` object
        """

        if instance_id is None:
            raise ValueError('instance_id must be provided')
        if dnszone_id is None:
            raise ValueError('dnszone_id must be provided')
        if rdata is not None:
            rdata = convert_model(rdata)
        headers = {
            'X-Correlation-ID': x_correlation_id
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='create_resource_record')
        headers.update(sdk_headers)

        data = {
            'type': type,
            'name': name,
            'rdata': rdata,
            'ttl': ttl,
            'service': service,
            'protocol': protocol
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        path_param_keys = ['instance_id', 'dnszone_id']
        path_param_values = self.encode_path_vars(instance_id, dnszone_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/instances/{instance_id}/dnszones/{dnszone_id}/resource_records'.format(**path_param_dict)
        request = self.prepare_request(method='POST',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request)
        return response


    def delete_resource_record(self,
        instance_id: str,
        dnszone_id: str,
        record_id: str,
        *,
        x_correlation_id: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Delete a resource record.

        Delete a resource record.

        :param str instance_id: The unique identifier of a service instance.
        :param str dnszone_id: The unique identifier of a DNS zone.
        :param str record_id: The unique identifier of a resource record.
        :param str x_correlation_id: (optional) Uniquely identifying a request.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if instance_id is None:
            raise ValueError('instance_id must be provided')
        if dnszone_id is None:
            raise ValueError('dnszone_id must be provided')
        if record_id is None:
            raise ValueError('record_id must be provided')
        headers = {
            'X-Correlation-ID': x_correlation_id
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='delete_resource_record')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        path_param_keys = ['instance_id', 'dnszone_id', 'record_id']
        path_param_values = self.encode_path_vars(instance_id, dnszone_id, record_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/instances/{instance_id}/dnszones/{dnszone_id}/resource_records/{record_id}'.format(**path_param_dict)
        request = self.prepare_request(method='DELETE',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response


    def get_resource_record(self,
        instance_id: str,
        dnszone_id: str,
        record_id: str,
        *,
        x_correlation_id: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Get a resource record.

        Get details of a resource record.

        :param str instance_id: The unique identifier of a service instance.
        :param str dnszone_id: The unique identifier of a DNS zone.
        :param str record_id: The unique identifier of a resource record.
        :param str x_correlation_id: (optional) Uniquely identifying a request.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ResourceRecord` object
        """

        if instance_id is None:
            raise ValueError('instance_id must be provided')
        if dnszone_id is None:
            raise ValueError('dnszone_id must be provided')
        if record_id is None:
            raise ValueError('record_id must be provided')
        headers = {
            'X-Correlation-ID': x_correlation_id
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='get_resource_record')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        path_param_keys = ['instance_id', 'dnszone_id', 'record_id']
        path_param_values = self.encode_path_vars(instance_id, dnszone_id, record_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/instances/{instance_id}/dnszones/{dnszone_id}/resource_records/{record_id}'.format(**path_param_dict)
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response


    def update_resource_record(self,
        instance_id: str,
        dnszone_id: str,
        record_id: str,
        *,
        name: str = None,
        rdata: 'ResourceRecordUpdateInputRdata' = None,
        ttl: int = None,
        service: str = None,
        protocol: str = None,
        x_correlation_id: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Update the properties of a resource record.

        Update the properties of a resource record.

        :param str instance_id: The unique identifier of a service instance.
        :param str dnszone_id: The unique identifier of a DNS zone.
        :param str record_id: The unique identifier of a resource record.
        :param str name: (optional) Name of the resource record.
        :param ResourceRecordUpdateInputRdata rdata: (optional) Content of the
               resource record.
        :param int ttl: (optional) Time to live in second.
        :param str service: (optional) Only used for SRV record.
        :param str protocol: (optional) Only used for SRV record.
        :param str x_correlation_id: (optional) Uniquely identifying a request.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ResourceRecord` object
        """

        if instance_id is None:
            raise ValueError('instance_id must be provided')
        if dnszone_id is None:
            raise ValueError('dnszone_id must be provided')
        if record_id is None:
            raise ValueError('record_id must be provided')
        if rdata is not None:
            rdata = convert_model(rdata)
        headers = {
            'X-Correlation-ID': x_correlation_id
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='update_resource_record')
        headers.update(sdk_headers)

        data = {
            'name': name,
            'rdata': rdata,
            'ttl': ttl,
            'service': service,
            'protocol': protocol
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        path_param_keys = ['instance_id', 'dnszone_id', 'record_id']
        path_param_values = self.encode_path_vars(instance_id, dnszone_id, record_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/instances/{instance_id}/dnszones/{dnszone_id}/resource_records/{record_id}'.format(**path_param_dict)
        request = self.prepare_request(method='PUT',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request)
        return response

    #########################
    # Permitted Network
    #########################


    def list_permitted_networks(self,
        instance_id: str,
        dnszone_id: str,
        *,
        x_correlation_id: str = None,
        offset: int = None,
        limit: int = None,
        **kwargs
    ) -> DetailedResponse:
        """
        List permitted networks.

        List the permitted networks for a given DNS zone.

        :param str instance_id: The unique identifier of a service instance.
        :param str dnszone_id: The unique identifier of a DNS zone.
        :param str x_correlation_id: (optional) Uniquely identifying a request.
        :param int offset: (optional) Specify how many resource records to skip
               over, the default value is 0.
        :param int limit: (optional) Specify how many resource records are
               returned, the default value is 200.
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
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='list_permitted_networks')
        headers.update(sdk_headers)

        params = {
            'offset': offset,
            'limit': limit
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        path_param_keys = ['instance_id', 'dnszone_id']
        path_param_values = self.encode_path_vars(instance_id, dnszone_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/instances/{instance_id}/dnszones/{dnszone_id}/permitted_networks'.format(**path_param_dict)
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers,
                                       params=params)

        response = self.send(request)
        return response


    def create_permitted_network(self,
        instance_id: str,
        dnszone_id: str,
        *,
        type: str = None,
        permitted_network: 'PermittedNetworkVpc' = None,
        x_correlation_id: str = None,
        **kwargs
    ) -> DetailedResponse:
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
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='create_permitted_network')
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
        headers['Accept'] = 'application/json'

        path_param_keys = ['instance_id', 'dnszone_id']
        path_param_values = self.encode_path_vars(instance_id, dnszone_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/instances/{instance_id}/dnszones/{dnszone_id}/permitted_networks'.format(**path_param_dict)
        request = self.prepare_request(method='POST',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request)
        return response


    def delete_permitted_network(self,
        instance_id: str,
        dnszone_id: str,
        permitted_network_id: str,
        *,
        x_correlation_id: str = None,
        **kwargs
    ) -> DetailedResponse:
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
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='delete_permitted_network')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        path_param_keys = ['instance_id', 'dnszone_id', 'permitted_network_id']
        path_param_values = self.encode_path_vars(instance_id, dnszone_id, permitted_network_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/instances/{instance_id}/dnszones/{dnszone_id}/permitted_networks/{permitted_network_id}'.format(**path_param_dict)
        request = self.prepare_request(method='DELETE',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response


    def get_permitted_network(self,
        instance_id: str,
        dnszone_id: str,
        permitted_network_id: str,
        *,
        x_correlation_id: str = None,
        **kwargs
    ) -> DetailedResponse:
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
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='get_permitted_network')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        path_param_keys = ['instance_id', 'dnszone_id', 'permitted_network_id']
        path_param_values = self.encode_path_vars(instance_id, dnszone_id, permitted_network_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/instances/{instance_id}/dnszones/{dnszone_id}/permitted_networks/{permitted_network_id}'.format(**path_param_dict)
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response

    #########################
    # Global Load Balancers
    #########################


    def list_load_balancers(self,
        instance_id: str,
        dnszone_id: str,
        *,
        x_correlation_id: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        List load balancers.

        List the Global Load Balancers for a given DNS zone.

        :param str instance_id: The unique identifier of a service instance.
        :param str dnszone_id: The unique identifier of a DNS zone.
        :param str x_correlation_id: (optional) Uniquely identifying a request.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ListLoadBalancers` object
        """

        if instance_id is None:
            raise ValueError('instance_id must be provided')
        if dnszone_id is None:
            raise ValueError('dnszone_id must be provided')
        headers = {
            'X-Correlation-ID': x_correlation_id
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='list_load_balancers')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        path_param_keys = ['instance_id', 'dnszone_id']
        path_param_values = self.encode_path_vars(instance_id, dnszone_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/instances/{instance_id}/dnszones/{dnszone_id}/load_balancers'.format(**path_param_dict)
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response


    def create_load_balancer(self,
        instance_id: str,
        dnszone_id: str,
        *,
        name: str = None,
        fallback_pool: str = None,
        default_pools: List[str] = None,
        description: str = None,
        enabled: bool = None,
        ttl: int = None,
        az_pools: List['LoadBalancerAzPoolsItem'] = None,
        x_correlation_id: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Create a load balancer.

        Create a load balancer for a given DNS zone.

        :param str instance_id: The unique identifier of a service instance.
        :param str dnszone_id: The unique identifier of a DNS zone.
        :param str name: (optional) Name of the load balancer.
        :param str fallback_pool: (optional) The pool ID to use when all other
               pools are detected as unhealthy.
        :param List[str] default_pools: (optional) A list of pool IDs ordered by
               their failover priority. Pools defined here are used by default, or when
               region_pools are not configured for a given region.
        :param str description: (optional) Descriptive text of the load balancer.
        :param bool enabled: (optional) Whether the load balancer is enabled.
        :param int ttl: (optional) Time to live in second.
        :param List[LoadBalancerAzPoolsItem] az_pools: (optional) Map availability
               zones to pool IDs.
        :param str x_correlation_id: (optional) Uniquely identifying a request.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `LoadBalancer` object
        """

        if instance_id is None:
            raise ValueError('instance_id must be provided')
        if dnszone_id is None:
            raise ValueError('dnszone_id must be provided')
        if az_pools is not None:
            az_pools = [convert_model(x) for x in az_pools]
        headers = {
            'X-Correlation-ID': x_correlation_id
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='create_load_balancer')
        headers.update(sdk_headers)

        data = {
            'name': name,
            'fallback_pool': fallback_pool,
            'default_pools': default_pools,
            'description': description,
            'enabled': enabled,
            'ttl': ttl,
            'az_pools': az_pools
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        path_param_keys = ['instance_id', 'dnszone_id']
        path_param_values = self.encode_path_vars(instance_id, dnszone_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/instances/{instance_id}/dnszones/{dnszone_id}/load_balancers'.format(**path_param_dict)
        request = self.prepare_request(method='POST',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request)
        return response


    def delete_load_balancer(self,
        instance_id: str,
        dnszone_id: str,
        lb_id: str,
        *,
        x_correlation_id: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Delete a load balancer.

        Delete a load balancer.

        :param str instance_id: The unique identifier of a service instance.
        :param str dnszone_id: The unique identifier of a DNS zone.
        :param str lb_id: The unique identifier of a load balancer.
        :param str x_correlation_id: (optional) Uniquely identifying a request.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if instance_id is None:
            raise ValueError('instance_id must be provided')
        if dnszone_id is None:
            raise ValueError('dnszone_id must be provided')
        if lb_id is None:
            raise ValueError('lb_id must be provided')
        headers = {
            'X-Correlation-ID': x_correlation_id
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='delete_load_balancer')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        path_param_keys = ['instance_id', 'dnszone_id', 'lb_id']
        path_param_values = self.encode_path_vars(instance_id, dnszone_id, lb_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/instances/{instance_id}/dnszones/{dnszone_id}/load_balancers/{lb_id}'.format(**path_param_dict)
        request = self.prepare_request(method='DELETE',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response


    def get_load_balancer(self,
        instance_id: str,
        dnszone_id: str,
        lb_id: str,
        *,
        x_correlation_id: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Get a load balancer.

        Get details of a load balancer.

        :param str instance_id: The unique identifier of a service instance.
        :param str dnszone_id: The unique identifier of a DNS zone.
        :param str lb_id: The unique identifier of a load balancer.
        :param str x_correlation_id: (optional) Uniquely identifying a request.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `LoadBalancer` object
        """

        if instance_id is None:
            raise ValueError('instance_id must be provided')
        if dnszone_id is None:
            raise ValueError('dnszone_id must be provided')
        if lb_id is None:
            raise ValueError('lb_id must be provided')
        headers = {
            'X-Correlation-ID': x_correlation_id
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='get_load_balancer')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        path_param_keys = ['instance_id', 'dnszone_id', 'lb_id']
        path_param_values = self.encode_path_vars(instance_id, dnszone_id, lb_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/instances/{instance_id}/dnszones/{dnszone_id}/load_balancers/{lb_id}'.format(**path_param_dict)
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response


    def update_load_balancer(self,
        instance_id: str,
        dnszone_id: str,
        lb_id: str,
        *,
        name: str = None,
        description: str = None,
        enabled: bool = None,
        ttl: int = None,
        fallback_pool: str = None,
        default_pools: List[str] = None,
        az_pools: List['LoadBalancerAzPoolsItem'] = None,
        x_correlation_id: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Update the properties of a load balancer.

        Update the properties of a load balancer.

        :param str instance_id: The unique identifier of a service instance.
        :param str dnszone_id: The unique identifier of a DNS zone.
        :param str lb_id: The unique identifier of a load balancer.
        :param str name: (optional) Name of the load balancer.
        :param str description: (optional) Descriptive text of the load balancer.
        :param bool enabled: (optional) Whether the load balancer is enabled.
        :param int ttl: (optional) Time to live in second.
        :param str fallback_pool: (optional) The pool ID to use when all other
               pools are detected as unhealthy.
        :param List[str] default_pools: (optional) A list of pool IDs ordered by
               their failover priority. Pools defined here are used by default, or when
               region_pools are not configured for a given region.
        :param List[LoadBalancerAzPoolsItem] az_pools: (optional) Map availability
               zones to pool IDs.
        :param str x_correlation_id: (optional) Uniquely identifying a request.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `LoadBalancer` object
        """

        if instance_id is None:
            raise ValueError('instance_id must be provided')
        if dnszone_id is None:
            raise ValueError('dnszone_id must be provided')
        if lb_id is None:
            raise ValueError('lb_id must be provided')
        if az_pools is not None:
            az_pools = [convert_model(x) for x in az_pools]
        headers = {
            'X-Correlation-ID': x_correlation_id
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='update_load_balancer')
        headers.update(sdk_headers)

        data = {
            'name': name,
            'description': description,
            'enabled': enabled,
            'ttl': ttl,
            'fallback_pool': fallback_pool,
            'default_pools': default_pools,
            'az_pools': az_pools
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        path_param_keys = ['instance_id', 'dnszone_id', 'lb_id']
        path_param_values = self.encode_path_vars(instance_id, dnszone_id, lb_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/instances/{instance_id}/dnszones/{dnszone_id}/load_balancers/{lb_id}'.format(**path_param_dict)
        request = self.prepare_request(method='PUT',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request)
        return response

    #########################
    # Pools
    #########################


    def list_pools(self,
        instance_id: str,
        *,
        x_correlation_id: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        List load balancer pools.

        List the load balancer pools.

        :param str instance_id: The unique identifier of a service instance.
        :param str x_correlation_id: (optional) Uniquely identifying a request.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ListPools` object
        """

        if instance_id is None:
            raise ValueError('instance_id must be provided')
        headers = {
            'X-Correlation-ID': x_correlation_id
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='list_pools')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        path_param_keys = ['instance_id']
        path_param_values = self.encode_path_vars(instance_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/instances/{instance_id}/pools'.format(**path_param_dict)
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response


    def create_pool(self,
        instance_id: str,
        *,
        name: str = None,
        origins: List['OriginInput'] = None,
        description: str = None,
        enabled: bool = None,
        healthy_origins_threshold: int = None,
        monitor: str = None,
        notification_channel: str = None,
        healthcheck_region: str = None,
        healthcheck_subnets: List[str] = None,
        x_correlation_id: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Create a load balancer pool.

        Create a load balancer pool.

        :param str instance_id: The unique identifier of a service instance.
        :param str name: (optional) Name of the load balancer pool.
        :param List[OriginInput] origins: (optional) The list of origins within
               this pool. Traffic directed at this pool is balanced across all currently
               healthy origins, provided the pool itself is healthy.
        :param str description: (optional) Descriptive text of the load balancer
               pool.
        :param bool enabled: (optional) Whether the load balancer pool is enabled.
        :param int healthy_origins_threshold: (optional) The minimum number of
               origins that must be healthy for this pool to serve traffic. If the number
               of healthy origins falls below this number, the pool will be marked
               unhealthy and we will failover to the next available pool.
        :param str monitor: (optional) The ID of the load balancer monitor to be
               associated to this pool.
        :param str notification_channel: (optional) The notification channel.
        :param str healthcheck_region: (optional) Health check region of VSIs.
        :param List[str] healthcheck_subnets: (optional) Health check subnet CRN.
        :param str x_correlation_id: (optional) Uniquely identifying a request.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `Pool` object
        """

        if instance_id is None:
            raise ValueError('instance_id must be provided')
        if origins is not None:
            origins = [convert_model(x) for x in origins]
        headers = {
            'X-Correlation-ID': x_correlation_id
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='create_pool')
        headers.update(sdk_headers)

        data = {
            'name': name,
            'origins': origins,
            'description': description,
            'enabled': enabled,
            'healthy_origins_threshold': healthy_origins_threshold,
            'monitor': monitor,
            'notification_channel': notification_channel,
            'healthcheck_region': healthcheck_region,
            'healthcheck_subnets': healthcheck_subnets
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        path_param_keys = ['instance_id']
        path_param_values = self.encode_path_vars(instance_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/instances/{instance_id}/pools'.format(**path_param_dict)
        request = self.prepare_request(method='POST',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request)
        return response


    def delete_pool(self,
        instance_id: str,
        pool_id: str,
        *,
        x_correlation_id: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Delete a load balancer pool.

        Delete a load balancer pool.

        :param str instance_id: The unique identifier of a service instance.
        :param str pool_id: The unique identifier of a load balancer pool.
        :param str x_correlation_id: (optional) Uniquely identifying a request.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if instance_id is None:
            raise ValueError('instance_id must be provided')
        if pool_id is None:
            raise ValueError('pool_id must be provided')
        headers = {
            'X-Correlation-ID': x_correlation_id
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='delete_pool')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        path_param_keys = ['instance_id', 'pool_id']
        path_param_values = self.encode_path_vars(instance_id, pool_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/instances/{instance_id}/pools/{pool_id}'.format(**path_param_dict)
        request = self.prepare_request(method='DELETE',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response


    def get_pool(self,
        instance_id: str,
        pool_id: str,
        *,
        x_correlation_id: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Get a load balancer pool.

        Get details of a load balancer pool.

        :param str instance_id: The unique identifier of a service instance.
        :param str pool_id: The unique identifier of a load balancer pool.
        :param str x_correlation_id: (optional) Uniquely identifying a request.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `Pool` object
        """

        if instance_id is None:
            raise ValueError('instance_id must be provided')
        if pool_id is None:
            raise ValueError('pool_id must be provided')
        headers = {
            'X-Correlation-ID': x_correlation_id
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='get_pool')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        path_param_keys = ['instance_id', 'pool_id']
        path_param_values = self.encode_path_vars(instance_id, pool_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/instances/{instance_id}/pools/{pool_id}'.format(**path_param_dict)
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response


    def update_pool(self,
        instance_id: str,
        pool_id: str,
        *,
        name: str = None,
        description: str = None,
        enabled: bool = None,
        healthy_origins_threshold: int = None,
        origins: List['OriginInput'] = None,
        monitor: str = None,
        notification_channel: str = None,
        healthcheck_region: str = None,
        healthcheck_subnets: List[str] = None,
        x_correlation_id: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Update the properties of a load balancer pool.

        Update the properties of a load balancer pool.

        :param str instance_id: The unique identifier of a service instance.
        :param str pool_id: The unique identifier of a load balancer pool.
        :param str name: (optional) Name of the load balancer pool.
        :param str description: (optional) Descriptive text of the load balancer
               pool.
        :param bool enabled: (optional) Whether the load balancer pool is enabled.
        :param int healthy_origins_threshold: (optional) The minimum number of
               origins that must be healthy for this pool to serve traffic. If the number
               of healthy origins falls below this number, the pool will be marked
               unhealthy and we will failover to the next available pool.
        :param List[OriginInput] origins: (optional) The list of origins within
               this pool. Traffic directed at this pool is balanced across all currently
               healthy origins, provided the pool itself is healthy.
        :param str monitor: (optional) The ID of the load balancer monitor to be
               associated to this pool.
        :param str notification_channel: (optional) The notification channel.
        :param str healthcheck_region: (optional) Health check region of VSIs.
        :param List[str] healthcheck_subnets: (optional) Health check subnet CRNs.
        :param str x_correlation_id: (optional) Uniquely identifying a request.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `Pool` object
        """

        if instance_id is None:
            raise ValueError('instance_id must be provided')
        if pool_id is None:
            raise ValueError('pool_id must be provided')
        if origins is not None:
            origins = [convert_model(x) for x in origins]
        headers = {
            'X-Correlation-ID': x_correlation_id
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='update_pool')
        headers.update(sdk_headers)

        data = {
            'name': name,
            'description': description,
            'enabled': enabled,
            'healthy_origins_threshold': healthy_origins_threshold,
            'origins': origins,
            'monitor': monitor,
            'notification_channel': notification_channel,
            'healthcheck_region': healthcheck_region,
            'healthcheck_subnets': healthcheck_subnets
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        path_param_keys = ['instance_id', 'pool_id']
        path_param_values = self.encode_path_vars(instance_id, pool_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/instances/{instance_id}/pools/{pool_id}'.format(**path_param_dict)
        request = self.prepare_request(method='PUT',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request)
        return response

    #########################
    # Monitors
    #########################


    def list_monitors(self,
        instance_id: str,
        *,
        x_correlation_id: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        List load balancer monitors.

        List the load balancer monitors.

        :param str instance_id: The unique identifier of a service instance.
        :param str x_correlation_id: (optional) Uniquely identifying a request.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ListMonitors` object
        """

        if instance_id is None:
            raise ValueError('instance_id must be provided')
        headers = {
            'X-Correlation-ID': x_correlation_id
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='list_monitors')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        path_param_keys = ['instance_id']
        path_param_values = self.encode_path_vars(instance_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/instances/{instance_id}/monitors'.format(**path_param_dict)
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response


    def create_monitor(self,
        instance_id: str,
        *,
        name: str = None,
        type: str = None,
        description: str = None,
        port: int = None,
        interval: int = None,
        retries: int = None,
        timeout: int = None,
        method: str = None,
        path: str = None,
        headers_: List['HealthcheckHeader'] = None,
        allow_insecure: bool = None,
        expected_codes: str = None,
        expected_body: str = None,
        x_correlation_id: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Create a load balancer monitor.

        Create a load balancer monitor.

        :param str instance_id: The unique identifier of a service instance.
        :param str name: (optional) The name of the load balancer monitor.
        :param str type: (optional) The protocol to use for the health check.
               Currently supported protocols are 'HTTP','HTTPS' and 'TCP'.
        :param str description: (optional) Descriptive text of the load balancer
               monitor.
        :param int port: (optional) Port number to connect to for the health check.
               Required for TCP checks. HTTP and HTTPS checks should only define the port
               when using a non-standard port (HTTP: default 80, HTTPS: default 443).
        :param int interval: (optional) The interval between each health check.
               Shorter intervals may improve failover time, but will increase load on the
               origins as we check from multiple locations.
        :param int retries: (optional) The number of retries to attempt in case of
               a timeout before marking the origin as unhealthy. Retries are attempted
               immediately.
        :param int timeout: (optional) The timeout (in seconds) before marking the
               health check as failed.
        :param str method: (optional) The method to use for the health check
               applicable to HTTP/HTTPS based checks, the default value is 'GET'.
        :param str path: (optional) The endpoint path to health check against. This
               parameter is only valid for HTTP and HTTPS monitors.
        :param List[HealthcheckHeader] headers_: (optional) The HTTP request
               headers to send in the health check. It is recommended you set a Host
               header by default. The User-Agent header cannot be overridden. This
               parameter is only valid for HTTP and HTTPS monitors.
        :param bool allow_insecure: (optional) Do not validate the certificate when
               monitor use HTTPS. This parameter is currently only valid for HTTPS
               monitors.
        :param str expected_codes: (optional) The expected HTTP response code or
               code range of the health check. This parameter is only valid for HTTP and
               HTTPS monitors.
        :param str expected_body: (optional) A case-insensitive sub-string to look
               for in the response body. If this string is not found, the origin will be
               marked as unhealthy. This parameter is only valid for HTTP and HTTPS
               monitors.
        :param str x_correlation_id: (optional) Uniquely identifying a request.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `Monitor` object
        """

        if instance_id is None:
            raise ValueError('instance_id must be provided')
        if headers_ is not None:
            headers_ = [convert_model(x) for x in headers_]
        headers = {
            'X-Correlation-ID': x_correlation_id
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='create_monitor')
        headers.update(sdk_headers)

        data = {
            'name': name,
            'type': type,
            'description': description,
            'port': port,
            'interval': interval,
            'retries': retries,
            'timeout': timeout,
            'method': method,
            'path': path,
            'headers': headers_,
            'allow_insecure': allow_insecure,
            'expected_codes': expected_codes,
            'expected_body': expected_body
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        path_param_keys = ['instance_id']
        path_param_values = self.encode_path_vars(instance_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/instances/{instance_id}/monitors'.format(**path_param_dict)
        request = self.prepare_request(method='POST',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request)
        return response


    def delete_monitor(self,
        instance_id: str,
        monitor_id: str,
        *,
        x_correlation_id: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Delete a load balancer monitor.

        Delete a load balancer monitor.

        :param str instance_id: The unique identifier of a service instance.
        :param str monitor_id: The unique identifier of a load balancer monitor.
        :param str x_correlation_id: (optional) Uniquely identifying a request.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if instance_id is None:
            raise ValueError('instance_id must be provided')
        if monitor_id is None:
            raise ValueError('monitor_id must be provided')
        headers = {
            'X-Correlation-ID': x_correlation_id
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='delete_monitor')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        path_param_keys = ['instance_id', 'monitor_id']
        path_param_values = self.encode_path_vars(instance_id, monitor_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/instances/{instance_id}/monitors/{monitor_id}'.format(**path_param_dict)
        request = self.prepare_request(method='DELETE',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response


    def get_monitor(self,
        instance_id: str,
        monitor_id: str,
        *,
        x_correlation_id: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Get a load balancer monitor.

        Get details of a load balancer monitor.

        :param str instance_id: The unique identifier of a service instance.
        :param str monitor_id: The unique identifier of a load balancer monitor.
        :param str x_correlation_id: (optional) Uniquely identifying a request.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `Monitor` object
        """

        if instance_id is None:
            raise ValueError('instance_id must be provided')
        if monitor_id is None:
            raise ValueError('monitor_id must be provided')
        headers = {
            'X-Correlation-ID': x_correlation_id
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='get_monitor')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        path_param_keys = ['instance_id', 'monitor_id']
        path_param_values = self.encode_path_vars(instance_id, monitor_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/instances/{instance_id}/monitors/{monitor_id}'.format(**path_param_dict)
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response


    def update_monitor(self,
        instance_id: str,
        monitor_id: str,
        *,
        name: str = None,
        description: str = None,
        type: str = None,
        port: int = None,
        interval: int = None,
        retries: int = None,
        timeout: int = None,
        method: str = None,
        path: str = None,
        headers_: List['HealthcheckHeader'] = None,
        allow_insecure: bool = None,
        expected_codes: str = None,
        expected_body: str = None,
        x_correlation_id: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Update the properties of a load balancer monitor.

        Update the properties of a load balancer monitor.

        :param str instance_id: The unique identifier of a service instance.
        :param str monitor_id: The unique identifier of a load balancer monitor.
        :param str name: (optional) The name of the load balancer monitor.
        :param str description: (optional) Descriptive text of the load balancer
               monitor.
        :param str type: (optional) The protocol to use for the health check.
               Currently supported protocols are 'HTTP','HTTPS' and 'TCP'.
        :param int port: (optional) Port number to connect to for the health check.
               Required for TCP checks. HTTP and HTTPS checks should only define the port
               when using a non-standard port (HTTP: default 80, HTTPS: default 443).
        :param int interval: (optional) The interval between each health check.
               Shorter intervals may improve failover time, but will increase load on the
               origins as we check from multiple locations.
        :param int retries: (optional) The number of retries to attempt in case of
               a timeout before marking the origin as unhealthy. Retries are attempted
               immediately.
        :param int timeout: (optional) The timeout (in seconds) before marking the
               health check as failed.
        :param str method: (optional) The method to use for the health check
               applicable to HTTP/HTTPS based checks, the default value is 'GET'.
        :param str path: (optional) The endpoint path to health check against. This
               parameter is only valid for HTTP and HTTPS monitors.
        :param List[HealthcheckHeader] headers_: (optional) The HTTP request
               headers to send in the health check. It is recommended you set a Host
               header by default. The User-Agent header cannot be overridden. This
               parameter is only valid for HTTP and HTTPS monitors.
        :param bool allow_insecure: (optional) Do not validate the certificate when
               monitor use HTTPS. This parameter is currently only valid for HTTP and
               HTTPS monitors.
        :param str expected_codes: (optional) The expected HTTP response code or
               code range of the health check. This parameter is only valid for HTTP and
               HTTPS monitors.
        :param str expected_body: (optional) A case-insensitive sub-string to look
               for in the response body. If this string is not found, the origin will be
               marked as unhealthy. This parameter is only valid for HTTP and HTTPS
               monitors.
        :param str x_correlation_id: (optional) Uniquely identifying a request.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `Monitor` object
        """

        if instance_id is None:
            raise ValueError('instance_id must be provided')
        if monitor_id is None:
            raise ValueError('monitor_id must be provided')
        if headers_ is not None:
            headers_ = [convert_model(x) for x in headers_]
        headers = {
            'X-Correlation-ID': x_correlation_id
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='update_monitor')
        headers.update(sdk_headers)

        data = {
            'name': name,
            'description': description,
            'type': type,
            'port': port,
            'interval': interval,
            'retries': retries,
            'timeout': timeout,
            'method': method,
            'path': path,
            'headers': headers_,
            'allow_insecure': allow_insecure,
            'expected_codes': expected_codes,
            'expected_body': expected_body
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        path_param_keys = ['instance_id', 'monitor_id']
        path_param_values = self.encode_path_vars(instance_id, monitor_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/instances/{instance_id}/monitors/{monitor_id}'.format(**path_param_dict)
        request = self.prepare_request(method='PUT',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request)
        return response


##############################################################################
# Models
##############################################################################


class LoadBalancerAzPoolsItem():
    """
    LoadBalancerAzPoolsItem.

    :attr str availability_zone: (optional) Availability zone.
    :attr List[str] pools: (optional) List of load balancer pools.
    """

    def __init__(self,
                 *,
                 availability_zone: str = None,
                 pools: List[str] = None) -> None:
        """
        Initialize a LoadBalancerAzPoolsItem object.

        :param str availability_zone: (optional) Availability zone.
        :param List[str] pools: (optional) List of load balancer pools.
        """
        self.availability_zone = availability_zone
        self.pools = pools

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'LoadBalancerAzPoolsItem':
        """Initialize a LoadBalancerAzPoolsItem object from a json dictionary."""
        args = {}
        if 'availability_zone' in _dict:
            args['availability_zone'] = _dict.get('availability_zone')
        if 'pools' in _dict:
            args['pools'] = _dict.get('pools')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a LoadBalancerAzPoolsItem object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'availability_zone') and self.availability_zone is not None:
            _dict['availability_zone'] = self.availability_zone
        if hasattr(self, 'pools') and self.pools is not None:
            _dict['pools'] = self.pools
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this LoadBalancerAzPoolsItem object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'LoadBalancerAzPoolsItem') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'LoadBalancerAzPoolsItem') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class PoolHealthcheckVsisItem():
    """
    PoolHealthcheckVsisItem.

    :attr str subnet: (optional) Health check VSI subnet CRN.
    :attr str ipv4_address: (optional) healthcheck VSI ip address.
    :attr str ipv4_cidr_block: (optional) ipv4 cidr block.
    :attr str vpc: (optional) vpc crn.
    """

    def __init__(self,
                 *,
                 subnet: str = None,
                 ipv4_address: str = None,
                 ipv4_cidr_block: str = None,
                 vpc: str = None) -> None:
        """
        Initialize a PoolHealthcheckVsisItem object.

        :param str subnet: (optional) Health check VSI subnet CRN.
        :param str ipv4_address: (optional) healthcheck VSI ip address.
        :param str ipv4_cidr_block: (optional) ipv4 cidr block.
        :param str vpc: (optional) vpc crn.
        """
        self.subnet = subnet
        self.ipv4_address = ipv4_address
        self.ipv4_cidr_block = ipv4_cidr_block
        self.vpc = vpc

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'PoolHealthcheckVsisItem':
        """Initialize a PoolHealthcheckVsisItem object from a json dictionary."""
        args = {}
        if 'subnet' in _dict:
            args['subnet'] = _dict.get('subnet')
        if 'ipv4_address' in _dict:
            args['ipv4_address'] = _dict.get('ipv4_address')
        if 'ipv4_cidr_block' in _dict:
            args['ipv4_cidr_block'] = _dict.get('ipv4_cidr_block')
        if 'vpc' in _dict:
            args['vpc'] = _dict.get('vpc')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a PoolHealthcheckVsisItem object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'subnet') and self.subnet is not None:
            _dict['subnet'] = self.subnet
        if hasattr(self, 'ipv4_address') and self.ipv4_address is not None:
            _dict['ipv4_address'] = self.ipv4_address
        if hasattr(self, 'ipv4_cidr_block') and self.ipv4_cidr_block is not None:
            _dict['ipv4_cidr_block'] = self.ipv4_cidr_block
        if hasattr(self, 'vpc') and self.vpc is not None:
            _dict['vpc'] = self.vpc
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this PoolHealthcheckVsisItem object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'PoolHealthcheckVsisItem') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'PoolHealthcheckVsisItem') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class ResourceRecordInputRdata():
    """
    Content of the resource record.

    """

    def __init__(self) -> None:
        """
        Initialize a ResourceRecordInputRdata object.

        """
        msg = "Cannot instantiate base class. Instead, instantiate one of the defined subclasses: {0}".format(
                  ", ".join(['ResourceRecordInputRdataRdataARecord', 'ResourceRecordInputRdataRdataAaaaRecord', 'ResourceRecordInputRdataRdataCnameRecord', 'ResourceRecordInputRdataRdataMxRecord', 'ResourceRecordInputRdataRdataSrvRecord', 'ResourceRecordInputRdataRdataTxtRecord', 'ResourceRecordInputRdataRdataPtrRecord']))
        raise Exception(msg)

class ResourceRecordUpdateInputRdata():
    """
    Content of the resource record.

    """

    def __init__(self) -> None:
        """
        Initialize a ResourceRecordUpdateInputRdata object.

        """
        msg = "Cannot instantiate base class. Instead, instantiate one of the defined subclasses: {0}".format(
                  ", ".join(['ResourceRecordUpdateInputRdataRdataARecord', 'ResourceRecordUpdateInputRdataRdataAaaaRecord', 'ResourceRecordUpdateInputRdataRdataCnameRecord', 'ResourceRecordUpdateInputRdataRdataMxRecord', 'ResourceRecordUpdateInputRdataRdataSrvRecord', 'ResourceRecordUpdateInputRdataRdataTxtRecord', 'ResourceRecordUpdateInputRdataRdataPtrRecord']))
        raise Exception(msg)

class Dnszone():
    """
    DNS zone details.

    :attr str id: (optional) Unique identifier of a DNS zone.
    :attr str created_on: (optional) the time when a DNS zone is created.
    :attr str modified_on: (optional) the recent time when a DNS zone is modified.
    :attr str instance_id: (optional) Unique identifier of a service instance.
    :attr str name: (optional) Name of DNS zone.
    :attr str description: (optional) The text describing the purpose of a DNS zone.
    :attr str state: (optional) State of DNS zone.
    :attr str label: (optional) The label of a DNS zone.
    """

    def __init__(self,
                 *,
                 id: str = None,
                 created_on: str = None,
                 modified_on: str = None,
                 instance_id: str = None,
                 name: str = None,
                 description: str = None,
                 state: str = None,
                 label: str = None) -> None:
        """
        Initialize a Dnszone object.

        :param str id: (optional) Unique identifier of a DNS zone.
        :param str created_on: (optional) the time when a DNS zone is created.
        :param str modified_on: (optional) the recent time when a DNS zone is
               modified.
        :param str instance_id: (optional) Unique identifier of a service instance.
        :param str name: (optional) Name of DNS zone.
        :param str description: (optional) The text describing the purpose of a DNS
               zone.
        :param str state: (optional) State of DNS zone.
        :param str label: (optional) The label of a DNS zone.
        """
        self.id = id
        self.created_on = created_on
        self.modified_on = modified_on
        self.instance_id = instance_id
        self.name = name
        self.description = description
        self.state = state
        self.label = label

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Dnszone':
        """Initialize a Dnszone object from a json dictionary."""
        args = {}
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        if 'created_on' in _dict:
            args['created_on'] = _dict.get('created_on')
        if 'modified_on' in _dict:
            args['modified_on'] = _dict.get('modified_on')
        if 'instance_id' in _dict:
            args['instance_id'] = _dict.get('instance_id')
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        if 'description' in _dict:
            args['description'] = _dict.get('description')
        if 'state' in _dict:
            args['state'] = _dict.get('state')
        if 'label' in _dict:
            args['label'] = _dict.get('label')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Dnszone object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        if hasattr(self, 'created_on') and self.created_on is not None:
            _dict['created_on'] = self.created_on
        if hasattr(self, 'modified_on') and self.modified_on is not None:
            _dict['modified_on'] = self.modified_on
        if hasattr(self, 'instance_id') and self.instance_id is not None:
            _dict['instance_id'] = self.instance_id
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'description') and self.description is not None:
            _dict['description'] = self.description
        if hasattr(self, 'state') and self.state is not None:
            _dict['state'] = self.state
        if hasattr(self, 'label') and self.label is not None:
            _dict['label'] = self.label
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this Dnszone object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'Dnszone') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'Dnszone') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class StateEnum(str, Enum):
        """
        State of DNS zone.
        """
        PENDING_NETWORK_ADD = 'pending_network_add'
        ACTIVE = 'active'
        DISABLED = 'disabled'
        PENDING_DELETE = 'pending_delete'
        DELETED = 'deleted'


class FirstHref():
    """
    href.

    :attr str href: (optional) href.
    """

    def __init__(self,
                 *,
                 href: str = None) -> None:
        """
        Initialize a FirstHref object.

        :param str href: (optional) href.
        """
        self.href = href

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'FirstHref':
        """Initialize a FirstHref object from a json dictionary."""
        args = {}
        if 'href' in _dict:
            args['href'] = _dict.get('href')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a FirstHref object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'href') and self.href is not None:
            _dict['href'] = self.href
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this FirstHref object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'FirstHref') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'FirstHref') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class HealthcheckHeader():
    """
    The HTTP header of health check request.

    :attr str name: The name of HTTP request header.
    :attr List[str] value: The value of HTTP request header.
    """

    def __init__(self,
                 name: str,
                 value: List[str]) -> None:
        """
        Initialize a HealthcheckHeader object.

        :param str name: The name of HTTP request header.
        :param List[str] value: The value of HTTP request header.
        """
        self.name = name
        self.value = value

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'HealthcheckHeader':
        """Initialize a HealthcheckHeader object from a json dictionary."""
        args = {}
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        else:
            raise ValueError('Required property \'name\' not present in HealthcheckHeader JSON')
        if 'value' in _dict:
            args['value'] = _dict.get('value')
        else:
            raise ValueError('Required property \'value\' not present in HealthcheckHeader JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a HealthcheckHeader object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'value') and self.value is not None:
            _dict['value'] = self.value
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this HealthcheckHeader object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'HealthcheckHeader') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'HealthcheckHeader') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class ListDnszones():
    """
    List DNS zones response.

    :attr List[Dnszone] dnszones: An array of DNS zones.
    :attr int offset: Specify how many DNS zones to skip over, the default value is
          0.
    :attr int limit: Specify how many DNS zones are returned, the default value is
          10.
    :attr int total_count: Total number of DNS zones.
    :attr FirstHref first: href.
    :attr NextHref next: (optional) href.
    """

    def __init__(self,
                 dnszones: List['Dnszone'],
                 offset: int,
                 limit: int,
                 total_count: int,
                 first: 'FirstHref',
                 *,
                 next: 'NextHref' = None) -> None:
        """
        Initialize a ListDnszones object.

        :param List[Dnszone] dnszones: An array of DNS zones.
        :param int offset: Specify how many DNS zones to skip over, the default
               value is 0.
        :param int limit: Specify how many DNS zones are returned, the default
               value is 10.
        :param int total_count: Total number of DNS zones.
        :param FirstHref first: href.
        :param NextHref next: (optional) href.
        """
        self.dnszones = dnszones
        self.offset = offset
        self.limit = limit
        self.total_count = total_count
        self.first = first
        self.next = next

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ListDnszones':
        """Initialize a ListDnszones object from a json dictionary."""
        args = {}
        if 'dnszones' in _dict:
            args['dnszones'] = [Dnszone.from_dict(x) for x in _dict.get('dnszones')]
        else:
            raise ValueError('Required property \'dnszones\' not present in ListDnszones JSON')
        if 'offset' in _dict:
            args['offset'] = _dict.get('offset')
        else:
            raise ValueError('Required property \'offset\' not present in ListDnszones JSON')
        if 'limit' in _dict:
            args['limit'] = _dict.get('limit')
        else:
            raise ValueError('Required property \'limit\' not present in ListDnszones JSON')
        if 'total_count' in _dict:
            args['total_count'] = _dict.get('total_count')
        else:
            raise ValueError('Required property \'total_count\' not present in ListDnszones JSON')
        if 'first' in _dict:
            args['first'] = FirstHref.from_dict(_dict.get('first'))
        else:
            raise ValueError('Required property \'first\' not present in ListDnszones JSON')
        if 'next' in _dict:
            args['next'] = NextHref.from_dict(_dict.get('next'))
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ListDnszones object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'dnszones') and self.dnszones is not None:
            _dict['dnszones'] = [x.to_dict() for x in self.dnszones]
        if hasattr(self, 'offset') and self.offset is not None:
            _dict['offset'] = self.offset
        if hasattr(self, 'limit') and self.limit is not None:
            _dict['limit'] = self.limit
        if hasattr(self, 'total_count') and self.total_count is not None:
            _dict['total_count'] = self.total_count
        if hasattr(self, 'first') and self.first is not None:
            _dict['first'] = self.first.to_dict()
        if hasattr(self, 'next') and self.next is not None:
            _dict['next'] = self.next.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ListDnszones object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ListDnszones') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ListDnszones') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class ListLoadBalancers():
    """
    List Global Load Balancers response.

    :attr List[LoadBalancer] load_balancers: An array of Global Load Balancers.
    :attr int offset: Page number.
    :attr int limit: Number of Global Load Balancers per page.
    :attr int count: Number of Global Load Balancers.
    :attr int total_count: Total number of Global Load Balancers.
    :attr FirstHref first: href.
    :attr NextHref next: href.
    """

    def __init__(self,
                 load_balancers: List['LoadBalancer'],
                 offset: int,
                 limit: int,
                 count: int,
                 total_count: int,
                 first: 'FirstHref',
                 next: 'NextHref') -> None:
        """
        Initialize a ListLoadBalancers object.

        :param List[LoadBalancer] load_balancers: An array of Global Load
               Balancers.
        :param int offset: Page number.
        :param int limit: Number of Global Load Balancers per page.
        :param int count: Number of Global Load Balancers.
        :param int total_count: Total number of Global Load Balancers.
        :param FirstHref first: href.
        :param NextHref next: href.
        """
        self.load_balancers = load_balancers
        self.offset = offset
        self.limit = limit
        self.count = count
        self.total_count = total_count
        self.first = first
        self.next = next

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ListLoadBalancers':
        """Initialize a ListLoadBalancers object from a json dictionary."""
        args = {}
        if 'load_balancers' in _dict:
            args['load_balancers'] = [LoadBalancer.from_dict(x) for x in _dict.get('load_balancers')]
        else:
            raise ValueError('Required property \'load_balancers\' not present in ListLoadBalancers JSON')
        if 'offset' in _dict:
            args['offset'] = _dict.get('offset')
        else:
            raise ValueError('Required property \'offset\' not present in ListLoadBalancers JSON')
        if 'limit' in _dict:
            args['limit'] = _dict.get('limit')
        else:
            raise ValueError('Required property \'limit\' not present in ListLoadBalancers JSON')
        if 'count' in _dict:
            args['count'] = _dict.get('count')
        else:
            raise ValueError('Required property \'count\' not present in ListLoadBalancers JSON')
        if 'total_count' in _dict:
            args['total_count'] = _dict.get('total_count')
        else:
            raise ValueError('Required property \'total_count\' not present in ListLoadBalancers JSON')
        if 'first' in _dict:
            args['first'] = FirstHref.from_dict(_dict.get('first'))
        else:
            raise ValueError('Required property \'first\' not present in ListLoadBalancers JSON')
        if 'next' in _dict:
            args['next'] = NextHref.from_dict(_dict.get('next'))
        else:
            raise ValueError('Required property \'next\' not present in ListLoadBalancers JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ListLoadBalancers object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'load_balancers') and self.load_balancers is not None:
            _dict['load_balancers'] = [x.to_dict() for x in self.load_balancers]
        if hasattr(self, 'offset') and self.offset is not None:
            _dict['offset'] = self.offset
        if hasattr(self, 'limit') and self.limit is not None:
            _dict['limit'] = self.limit
        if hasattr(self, 'count') and self.count is not None:
            _dict['count'] = self.count
        if hasattr(self, 'total_count') and self.total_count is not None:
            _dict['total_count'] = self.total_count
        if hasattr(self, 'first') and self.first is not None:
            _dict['first'] = self.first.to_dict()
        if hasattr(self, 'next') and self.next is not None:
            _dict['next'] = self.next.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ListLoadBalancers object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ListLoadBalancers') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ListLoadBalancers') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class ListMonitors():
    """
    List load balancer monitors response.

    :attr List[Monitor] monitors: An array of load balancer monitors.
    :attr int offset: Page number.
    :attr int limit: Number of load balancer monitors per page.
    :attr int count: Number of load balancers.
    :attr int total_count: Total number of load balancers.
    :attr FirstHref first: href.
    :attr NextHref next: href.
    """

    def __init__(self,
                 monitors: List['Monitor'],
                 offset: int,
                 limit: int,
                 count: int,
                 total_count: int,
                 first: 'FirstHref',
                 next: 'NextHref') -> None:
        """
        Initialize a ListMonitors object.

        :param List[Monitor] monitors: An array of load balancer monitors.
        :param int offset: Page number.
        :param int limit: Number of load balancer monitors per page.
        :param int count: Number of load balancers.
        :param int total_count: Total number of load balancers.
        :param FirstHref first: href.
        :param NextHref next: href.
        """
        self.monitors = monitors
        self.offset = offset
        self.limit = limit
        self.count = count
        self.total_count = total_count
        self.first = first
        self.next = next

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ListMonitors':
        """Initialize a ListMonitors object from a json dictionary."""
        args = {}
        if 'monitors' in _dict:
            args['monitors'] = [Monitor.from_dict(x) for x in _dict.get('monitors')]
        else:
            raise ValueError('Required property \'monitors\' not present in ListMonitors JSON')
        if 'offset' in _dict:
            args['offset'] = _dict.get('offset')
        else:
            raise ValueError('Required property \'offset\' not present in ListMonitors JSON')
        if 'limit' in _dict:
            args['limit'] = _dict.get('limit')
        else:
            raise ValueError('Required property \'limit\' not present in ListMonitors JSON')
        if 'count' in _dict:
            args['count'] = _dict.get('count')
        else:
            raise ValueError('Required property \'count\' not present in ListMonitors JSON')
        if 'total_count' in _dict:
            args['total_count'] = _dict.get('total_count')
        else:
            raise ValueError('Required property \'total_count\' not present in ListMonitors JSON')
        if 'first' in _dict:
            args['first'] = FirstHref.from_dict(_dict.get('first'))
        else:
            raise ValueError('Required property \'first\' not present in ListMonitors JSON')
        if 'next' in _dict:
            args['next'] = NextHref.from_dict(_dict.get('next'))
        else:
            raise ValueError('Required property \'next\' not present in ListMonitors JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ListMonitors object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'monitors') and self.monitors is not None:
            _dict['monitors'] = [x.to_dict() for x in self.monitors]
        if hasattr(self, 'offset') and self.offset is not None:
            _dict['offset'] = self.offset
        if hasattr(self, 'limit') and self.limit is not None:
            _dict['limit'] = self.limit
        if hasattr(self, 'count') and self.count is not None:
            _dict['count'] = self.count
        if hasattr(self, 'total_count') and self.total_count is not None:
            _dict['total_count'] = self.total_count
        if hasattr(self, 'first') and self.first is not None:
            _dict['first'] = self.first.to_dict()
        if hasattr(self, 'next') and self.next is not None:
            _dict['next'] = self.next.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ListMonitors object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ListMonitors') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ListMonitors') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class ListPermittedNetworks():
    """
    List permitted networks response.

    :attr List[PermittedNetwork] permitted_networks: An array of permitted networks.
    :attr int offset: Specify how many permitted networks to skip over, the default
          value is 0.
    :attr int limit: Specify how many permitted networks are returned, the default
          value is 10.
    :attr int total_count: Total number of permitted networks.
    :attr FirstHref first: href.
    :attr NextHref next: (optional) href.
    """

    def __init__(self,
                 permitted_networks: List['PermittedNetwork'],
                 offset: int,
                 limit: int,
                 total_count: int,
                 first: 'FirstHref',
                 *,
                 next: 'NextHref' = None) -> None:
        """
        Initialize a ListPermittedNetworks object.

        :param List[PermittedNetwork] permitted_networks: An array of permitted
               networks.
        :param int offset: Specify how many permitted networks to skip over, the
               default value is 0.
        :param int limit: Specify how many permitted networks are returned, the
               default value is 10.
        :param int total_count: Total number of permitted networks.
        :param FirstHref first: href.
        :param NextHref next: (optional) href.
        """
        self.permitted_networks = permitted_networks
        self.offset = offset
        self.limit = limit
        self.total_count = total_count
        self.first = first
        self.next = next

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ListPermittedNetworks':
        """Initialize a ListPermittedNetworks object from a json dictionary."""
        args = {}
        if 'permitted_networks' in _dict:
            args['permitted_networks'] = [PermittedNetwork.from_dict(x) for x in _dict.get('permitted_networks')]
        else:
            raise ValueError('Required property \'permitted_networks\' not present in ListPermittedNetworks JSON')
        if 'offset' in _dict:
            args['offset'] = _dict.get('offset')
        else:
            raise ValueError('Required property \'offset\' not present in ListPermittedNetworks JSON')
        if 'limit' in _dict:
            args['limit'] = _dict.get('limit')
        else:
            raise ValueError('Required property \'limit\' not present in ListPermittedNetworks JSON')
        if 'total_count' in _dict:
            args['total_count'] = _dict.get('total_count')
        else:
            raise ValueError('Required property \'total_count\' not present in ListPermittedNetworks JSON')
        if 'first' in _dict:
            args['first'] = FirstHref.from_dict(_dict.get('first'))
        else:
            raise ValueError('Required property \'first\' not present in ListPermittedNetworks JSON')
        if 'next' in _dict:
            args['next'] = NextHref.from_dict(_dict.get('next'))
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ListPermittedNetworks object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'permitted_networks') and self.permitted_networks is not None:
            _dict['permitted_networks'] = [x.to_dict() for x in self.permitted_networks]
        if hasattr(self, 'offset') and self.offset is not None:
            _dict['offset'] = self.offset
        if hasattr(self, 'limit') and self.limit is not None:
            _dict['limit'] = self.limit
        if hasattr(self, 'total_count') and self.total_count is not None:
            _dict['total_count'] = self.total_count
        if hasattr(self, 'first') and self.first is not None:
            _dict['first'] = self.first.to_dict()
        if hasattr(self, 'next') and self.next is not None:
            _dict['next'] = self.next.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ListPermittedNetworks object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ListPermittedNetworks') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ListPermittedNetworks') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class ListPools():
    """
    List load balancer pools response.

    :attr List[Pool] pools: An array of load balancer pools.
    :attr int offset: Page number.
    :attr int limit: Number of load balancer pools per page.
    :attr int count: Number of load balancers.
    :attr int total_count: Total number of load balancers.
    :attr FirstHref first: href.
    :attr NextHref next: href.
    """

    def __init__(self,
                 pools: List['Pool'],
                 offset: int,
                 limit: int,
                 count: int,
                 total_count: int,
                 first: 'FirstHref',
                 next: 'NextHref') -> None:
        """
        Initialize a ListPools object.

        :param List[Pool] pools: An array of load balancer pools.
        :param int offset: Page number.
        :param int limit: Number of load balancer pools per page.
        :param int count: Number of load balancers.
        :param int total_count: Total number of load balancers.
        :param FirstHref first: href.
        :param NextHref next: href.
        """
        self.pools = pools
        self.offset = offset
        self.limit = limit
        self.count = count
        self.total_count = total_count
        self.first = first
        self.next = next

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ListPools':
        """Initialize a ListPools object from a json dictionary."""
        args = {}
        if 'pools' in _dict:
            args['pools'] = [Pool.from_dict(x) for x in _dict.get('pools')]
        else:
            raise ValueError('Required property \'pools\' not present in ListPools JSON')
        if 'offset' in _dict:
            args['offset'] = _dict.get('offset')
        else:
            raise ValueError('Required property \'offset\' not present in ListPools JSON')
        if 'limit' in _dict:
            args['limit'] = _dict.get('limit')
        else:
            raise ValueError('Required property \'limit\' not present in ListPools JSON')
        if 'count' in _dict:
            args['count'] = _dict.get('count')
        else:
            raise ValueError('Required property \'count\' not present in ListPools JSON')
        if 'total_count' in _dict:
            args['total_count'] = _dict.get('total_count')
        else:
            raise ValueError('Required property \'total_count\' not present in ListPools JSON')
        if 'first' in _dict:
            args['first'] = FirstHref.from_dict(_dict.get('first'))
        else:
            raise ValueError('Required property \'first\' not present in ListPools JSON')
        if 'next' in _dict:
            args['next'] = NextHref.from_dict(_dict.get('next'))
        else:
            raise ValueError('Required property \'next\' not present in ListPools JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ListPools object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'pools') and self.pools is not None:
            _dict['pools'] = [x.to_dict() for x in self.pools]
        if hasattr(self, 'offset') and self.offset is not None:
            _dict['offset'] = self.offset
        if hasattr(self, 'limit') and self.limit is not None:
            _dict['limit'] = self.limit
        if hasattr(self, 'count') and self.count is not None:
            _dict['count'] = self.count
        if hasattr(self, 'total_count') and self.total_count is not None:
            _dict['total_count'] = self.total_count
        if hasattr(self, 'first') and self.first is not None:
            _dict['first'] = self.first.to_dict()
        if hasattr(self, 'next') and self.next is not None:
            _dict['next'] = self.next.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ListPools object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ListPools') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ListPools') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class ListResourceRecords():
    """
    List Resource Records response.

    :attr List[ResourceRecord] resource_records: An array of resource records.
    :attr int offset: Specify how many resource records to skip over, the default
          value is 0.
    :attr int limit: Specify how many resource records are returned, the default
          value is 20.
    :attr int total_count: Total number of resource records.
    :attr FirstHref first: href.
    :attr NextHref next: (optional) href.
    """

    def __init__(self,
                 resource_records: List['ResourceRecord'],
                 offset: int,
                 limit: int,
                 total_count: int,
                 first: 'FirstHref',
                 *,
                 next: 'NextHref' = None) -> None:
        """
        Initialize a ListResourceRecords object.

        :param List[ResourceRecord] resource_records: An array of resource records.
        :param int offset: Specify how many resource records to skip over, the
               default value is 0.
        :param int limit: Specify how many resource records are returned, the
               default value is 20.
        :param int total_count: Total number of resource records.
        :param FirstHref first: href.
        :param NextHref next: (optional) href.
        """
        self.resource_records = resource_records
        self.offset = offset
        self.limit = limit
        self.total_count = total_count
        self.first = first
        self.next = next

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ListResourceRecords':
        """Initialize a ListResourceRecords object from a json dictionary."""
        args = {}
        if 'resource_records' in _dict:
            args['resource_records'] = [ResourceRecord.from_dict(x) for x in _dict.get('resource_records')]
        else:
            raise ValueError('Required property \'resource_records\' not present in ListResourceRecords JSON')
        if 'offset' in _dict:
            args['offset'] = _dict.get('offset')
        else:
            raise ValueError('Required property \'offset\' not present in ListResourceRecords JSON')
        if 'limit' in _dict:
            args['limit'] = _dict.get('limit')
        else:
            raise ValueError('Required property \'limit\' not present in ListResourceRecords JSON')
        if 'total_count' in _dict:
            args['total_count'] = _dict.get('total_count')
        else:
            raise ValueError('Required property \'total_count\' not present in ListResourceRecords JSON')
        if 'first' in _dict:
            args['first'] = FirstHref.from_dict(_dict.get('first'))
        else:
            raise ValueError('Required property \'first\' not present in ListResourceRecords JSON')
        if 'next' in _dict:
            args['next'] = NextHref.from_dict(_dict.get('next'))
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ListResourceRecords object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'resource_records') and self.resource_records is not None:
            _dict['resource_records'] = [x.to_dict() for x in self.resource_records]
        if hasattr(self, 'offset') and self.offset is not None:
            _dict['offset'] = self.offset
        if hasattr(self, 'limit') and self.limit is not None:
            _dict['limit'] = self.limit
        if hasattr(self, 'total_count') and self.total_count is not None:
            _dict['total_count'] = self.total_count
        if hasattr(self, 'first') and self.first is not None:
            _dict['first'] = self.first.to_dict()
        if hasattr(self, 'next') and self.next is not None:
            _dict['next'] = self.next.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ListResourceRecords object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ListResourceRecords') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ListResourceRecords') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class LoadBalancer():
    """
    Load balancer details.

    :attr str id: (optional) Identifier of the load balancer.
    :attr str name: (optional) Name of the load balancer.
    :attr str description: (optional) Descriptive text of the load balancer.
    :attr bool enabled: (optional) Whether the load balancer is enabled.
    :attr int ttl: (optional) Time to live in second.
    :attr str health: (optional) Healthy state of the load balancer.
    :attr str fallback_pool: (optional) The pool ID to use when all other pools are
          detected as unhealthy.
    :attr List[str] default_pools: (optional) A list of pool IDs ordered by their
          failover priority. Pools defined here are used by default, or when region_pools
          are not configured for a given region.
    :attr List[LoadBalancerAzPoolsItem] az_pools: (optional) Map availability zones
          to pool IDs.
    :attr str created_on: (optional) The time when a load balancer is created.
    :attr str modified_on: (optional) The recent time when a load balancer is
          modified.
    """

    def __init__(self,
                 *,
                 id: str = None,
                 name: str = None,
                 description: str = None,
                 enabled: bool = None,
                 ttl: int = None,
                 health: str = None,
                 fallback_pool: str = None,
                 default_pools: List[str] = None,
                 az_pools: List['LoadBalancerAzPoolsItem'] = None,
                 created_on: str = None,
                 modified_on: str = None) -> None:
        """
        Initialize a LoadBalancer object.

        :param str id: (optional) Identifier of the load balancer.
        :param str name: (optional) Name of the load balancer.
        :param str description: (optional) Descriptive text of the load balancer.
        :param bool enabled: (optional) Whether the load balancer is enabled.
        :param int ttl: (optional) Time to live in second.
        :param str health: (optional) Healthy state of the load balancer.
        :param str fallback_pool: (optional) The pool ID to use when all other
               pools are detected as unhealthy.
        :param List[str] default_pools: (optional) A list of pool IDs ordered by
               their failover priority. Pools defined here are used by default, or when
               region_pools are not configured for a given region.
        :param List[LoadBalancerAzPoolsItem] az_pools: (optional) Map availability
               zones to pool IDs.
        :param str created_on: (optional) The time when a load balancer is created.
        :param str modified_on: (optional) The recent time when a load balancer is
               modified.
        """
        self.id = id
        self.name = name
        self.description = description
        self.enabled = enabled
        self.ttl = ttl
        self.health = health
        self.fallback_pool = fallback_pool
        self.default_pools = default_pools
        self.az_pools = az_pools
        self.created_on = created_on
        self.modified_on = modified_on

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'LoadBalancer':
        """Initialize a LoadBalancer object from a json dictionary."""
        args = {}
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        if 'description' in _dict:
            args['description'] = _dict.get('description')
        if 'enabled' in _dict:
            args['enabled'] = _dict.get('enabled')
        if 'ttl' in _dict:
            args['ttl'] = _dict.get('ttl')
        if 'health' in _dict:
            args['health'] = _dict.get('health')
        if 'fallback_pool' in _dict:
            args['fallback_pool'] = _dict.get('fallback_pool')
        if 'default_pools' in _dict:
            args['default_pools'] = _dict.get('default_pools')
        if 'az_pools' in _dict:
            args['az_pools'] = [LoadBalancerAzPoolsItem.from_dict(x) for x in _dict.get('az_pools')]
        if 'created_on' in _dict:
            args['created_on'] = _dict.get('created_on')
        if 'modified_on' in _dict:
            args['modified_on'] = _dict.get('modified_on')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a LoadBalancer object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'description') and self.description is not None:
            _dict['description'] = self.description
        if hasattr(self, 'enabled') and self.enabled is not None:
            _dict['enabled'] = self.enabled
        if hasattr(self, 'ttl') and self.ttl is not None:
            _dict['ttl'] = self.ttl
        if hasattr(self, 'health') and self.health is not None:
            _dict['health'] = self.health
        if hasattr(self, 'fallback_pool') and self.fallback_pool is not None:
            _dict['fallback_pool'] = self.fallback_pool
        if hasattr(self, 'default_pools') and self.default_pools is not None:
            _dict['default_pools'] = self.default_pools
        if hasattr(self, 'az_pools') and self.az_pools is not None:
            _dict['az_pools'] = [x.to_dict() for x in self.az_pools]
        if hasattr(self, 'created_on') and self.created_on is not None:
            _dict['created_on'] = self.created_on
        if hasattr(self, 'modified_on') and self.modified_on is not None:
            _dict['modified_on'] = self.modified_on
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this LoadBalancer object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'LoadBalancer') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'LoadBalancer') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class HealthEnum(str, Enum):
        """
        Healthy state of the load balancer.
        """
        HEALTHY = 'HEALTHY'
        DEGRADED = 'DEGRADED'
        CRITICAL = 'CRITICAL'


class Monitor():
    """
    Load balancer monitor details.

    :attr str id: (optional) Identifier of the load balancer monitor.
    :attr str name: (optional) The name of the load balancer monitor.
    :attr str description: (optional) Descriptive text of the load balancer monitor.
    :attr str type: (optional) The protocol to use for the health check. Currently
          supported protocols are 'HTTP','HTTPS' and 'TCP'.
    :attr int port: (optional) Port number to connect to for the health check.
          Required for TCP checks. HTTP and HTTPS checks should only define the port when
          using a non-standard port (HTTP: default 80, HTTPS: default 443).
    :attr int interval: (optional) The interval between each health check. Shorter
          intervals may improve failover time, but will increase load on the origins as we
          check from multiple locations.
    :attr int retries: (optional) The number of retries to attempt in case of a
          timeout before marking the origin as unhealthy. Retries are attempted
          immediately.
    :attr int timeout: (optional) The timeout (in seconds) before marking the health
          check as failed.
    :attr str method: (optional) The method to use for the health check applicable
          to HTTP/HTTPS based checks, the default value is 'GET'.
    :attr str path: (optional) The endpoint path to health check against. This
          parameter is only valid for HTTP and HTTPS monitors.
    :attr List[HealthcheckHeader] headers_: (optional) The HTTP request headers to
          send in the health check. It is recommended you set a Host header by default.
          The User-Agent header cannot be overridden. This parameter is only valid for
          HTTP and HTTPS monitors.
    :attr bool allow_insecure: (optional) Do not validate the certificate when
          monitor use HTTPS. This parameter is currently only valid for HTTPS monitors.
    :attr str expected_codes: (optional) The expected HTTP response code or code
          range of the health check. This parameter is only valid for HTTP and HTTPS
          monitors.
    :attr str expected_body: (optional) A case-insensitive sub-string to look for in
          the response body. If this string is not found, the origin will be marked as
          unhealthy. This parameter is only valid for HTTP and HTTPS monitors.
    :attr str created_on: (optional) the time when a load balancer monitor is
          created.
    :attr str modified_on: (optional) the recent time when a load balancer monitor
          is modified.
    """

    def __init__(self,
                 *,
                 id: str = None,
                 name: str = None,
                 description: str = None,
                 type: str = None,
                 port: int = None,
                 interval: int = None,
                 retries: int = None,
                 timeout: int = None,
                 method: str = None,
                 path: str = None,
                 headers_: List['HealthcheckHeader'] = None,
                 allow_insecure: bool = None,
                 expected_codes: str = None,
                 expected_body: str = None,
                 created_on: str = None,
                 modified_on: str = None) -> None:
        """
        Initialize a Monitor object.

        :param str id: (optional) Identifier of the load balancer monitor.
        :param str name: (optional) The name of the load balancer monitor.
        :param str description: (optional) Descriptive text of the load balancer
               monitor.
        :param str type: (optional) The protocol to use for the health check.
               Currently supported protocols are 'HTTP','HTTPS' and 'TCP'.
        :param int port: (optional) Port number to connect to for the health check.
               Required for TCP checks. HTTP and HTTPS checks should only define the port
               when using a non-standard port (HTTP: default 80, HTTPS: default 443).
        :param int interval: (optional) The interval between each health check.
               Shorter intervals may improve failover time, but will increase load on the
               origins as we check from multiple locations.
        :param int retries: (optional) The number of retries to attempt in case of
               a timeout before marking the origin as unhealthy. Retries are attempted
               immediately.
        :param int timeout: (optional) The timeout (in seconds) before marking the
               health check as failed.
        :param str method: (optional) The method to use for the health check
               applicable to HTTP/HTTPS based checks, the default value is 'GET'.
        :param str path: (optional) The endpoint path to health check against. This
               parameter is only valid for HTTP and HTTPS monitors.
        :param List[HealthcheckHeader] headers_: (optional) The HTTP request
               headers to send in the health check. It is recommended you set a Host
               header by default. The User-Agent header cannot be overridden. This
               parameter is only valid for HTTP and HTTPS monitors.
        :param bool allow_insecure: (optional) Do not validate the certificate when
               monitor use HTTPS. This parameter is currently only valid for HTTPS
               monitors.
        :param str expected_codes: (optional) The expected HTTP response code or
               code range of the health check. This parameter is only valid for HTTP and
               HTTPS monitors.
        :param str expected_body: (optional) A case-insensitive sub-string to look
               for in the response body. If this string is not found, the origin will be
               marked as unhealthy. This parameter is only valid for HTTP and HTTPS
               monitors.
        :param str created_on: (optional) the time when a load balancer monitor is
               created.
        :param str modified_on: (optional) the recent time when a load balancer
               monitor is modified.
        """
        self.id = id
        self.name = name
        self.description = description
        self.type = type
        self.port = port
        self.interval = interval
        self.retries = retries
        self.timeout = timeout
        self.method = method
        self.path = path
        self.headers_ = headers_
        self.allow_insecure = allow_insecure
        self.expected_codes = expected_codes
        self.expected_body = expected_body
        self.created_on = created_on
        self.modified_on = modified_on

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Monitor':
        """Initialize a Monitor object from a json dictionary."""
        args = {}
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        if 'description' in _dict:
            args['description'] = _dict.get('description')
        if 'type' in _dict:
            args['type'] = _dict.get('type')
        if 'port' in _dict:
            args['port'] = _dict.get('port')
        if 'interval' in _dict:
            args['interval'] = _dict.get('interval')
        if 'retries' in _dict:
            args['retries'] = _dict.get('retries')
        if 'timeout' in _dict:
            args['timeout'] = _dict.get('timeout')
        if 'method' in _dict:
            args['method'] = _dict.get('method')
        if 'path' in _dict:
            args['path'] = _dict.get('path')
        if 'headers' in _dict:
            args['headers_'] = [HealthcheckHeader.from_dict(x) for x in _dict.get('headers')]
        if 'allow_insecure' in _dict:
            args['allow_insecure'] = _dict.get('allow_insecure')
        if 'expected_codes' in _dict:
            args['expected_codes'] = _dict.get('expected_codes')
        if 'expected_body' in _dict:
            args['expected_body'] = _dict.get('expected_body')
        if 'created_on' in _dict:
            args['created_on'] = _dict.get('created_on')
        if 'modified_on' in _dict:
            args['modified_on'] = _dict.get('modified_on')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Monitor object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'description') and self.description is not None:
            _dict['description'] = self.description
        if hasattr(self, 'type') and self.type is not None:
            _dict['type'] = self.type
        if hasattr(self, 'port') and self.port is not None:
            _dict['port'] = self.port
        if hasattr(self, 'interval') and self.interval is not None:
            _dict['interval'] = self.interval
        if hasattr(self, 'retries') and self.retries is not None:
            _dict['retries'] = self.retries
        if hasattr(self, 'timeout') and self.timeout is not None:
            _dict['timeout'] = self.timeout
        if hasattr(self, 'method') and self.method is not None:
            _dict['method'] = self.method
        if hasattr(self, 'path') and self.path is not None:
            _dict['path'] = self.path
        if hasattr(self, 'headers_') and self.headers_ is not None:
            _dict['headers'] = [x.to_dict() for x in self.headers_]
        if hasattr(self, 'allow_insecure') and self.allow_insecure is not None:
            _dict['allow_insecure'] = self.allow_insecure
        if hasattr(self, 'expected_codes') and self.expected_codes is not None:
            _dict['expected_codes'] = self.expected_codes
        if hasattr(self, 'expected_body') and self.expected_body is not None:
            _dict['expected_body'] = self.expected_body
        if hasattr(self, 'created_on') and self.created_on is not None:
            _dict['created_on'] = self.created_on
        if hasattr(self, 'modified_on') and self.modified_on is not None:
            _dict['modified_on'] = self.modified_on
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this Monitor object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'Monitor') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'Monitor') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class MethodEnum(str, Enum):
        """
        The method to use for the health check applicable to HTTP/HTTPS based checks, the
        default value is 'GET'.
        """
        GET = 'GET'
        HEAD = 'HEAD'


class NextHref():
    """
    href.

    :attr str href: (optional) href.
    """

    def __init__(self,
                 *,
                 href: str = None) -> None:
        """
        Initialize a NextHref object.

        :param str href: (optional) href.
        """
        self.href = href

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'NextHref':
        """Initialize a NextHref object from a json dictionary."""
        args = {}
        if 'href' in _dict:
            args['href'] = _dict.get('href')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a NextHref object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'href') and self.href is not None:
            _dict['href'] = self.href
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this NextHref object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'NextHref') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'NextHref') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class Origin():
    """
    Origin server.

    :attr str name: (optional) The name of the origin server.
    :attr str description: (optional) Description of the origin server.
    :attr str address: (optional) The address of the origin server. It can be a
          hostname or an IP address.
    :attr bool enabled: (optional) Whether the origin server is enabled.
    :attr bool health: (optional) The health state of the origin server.
    :attr str health_failure_reason: (optional) The failure reason of the origin
          server if it is unhealthy.
    """

    def __init__(self,
                 *,
                 name: str = None,
                 description: str = None,
                 address: str = None,
                 enabled: bool = None,
                 health: bool = None,
                 health_failure_reason: str = None) -> None:
        """
        Initialize a Origin object.

        :param str name: (optional) The name of the origin server.
        :param str description: (optional) Description of the origin server.
        :param str address: (optional) The address of the origin server. It can be
               a hostname or an IP address.
        :param bool enabled: (optional) Whether the origin server is enabled.
        :param bool health: (optional) The health state of the origin server.
        :param str health_failure_reason: (optional) The failure reason of the
               origin server if it is unhealthy.
        """
        self.name = name
        self.description = description
        self.address = address
        self.enabled = enabled
        self.health = health
        self.health_failure_reason = health_failure_reason

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Origin':
        """Initialize a Origin object from a json dictionary."""
        args = {}
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        if 'description' in _dict:
            args['description'] = _dict.get('description')
        if 'address' in _dict:
            args['address'] = _dict.get('address')
        if 'enabled' in _dict:
            args['enabled'] = _dict.get('enabled')
        if 'health' in _dict:
            args['health'] = _dict.get('health')
        if 'health_failure_reason' in _dict:
            args['health_failure_reason'] = _dict.get('health_failure_reason')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Origin object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'description') and self.description is not None:
            _dict['description'] = self.description
        if hasattr(self, 'address') and self.address is not None:
            _dict['address'] = self.address
        if hasattr(self, 'enabled') and self.enabled is not None:
            _dict['enabled'] = self.enabled
        if hasattr(self, 'health') and self.health is not None:
            _dict['health'] = self.health
        if hasattr(self, 'health_failure_reason') and self.health_failure_reason is not None:
            _dict['health_failure_reason'] = self.health_failure_reason
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this Origin object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'Origin') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'Origin') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class OriginInput():
    """
    The request data of origin server.

    :attr str name: (optional) The name of the origin server.
    :attr str description: (optional) Description of the origin server.
    :attr str address: (optional) The address of the origin server. It can be a
          hostname or an IP address.
    :attr bool enabled: (optional) Whether the origin server is enabled.
    """

    def __init__(self,
                 *,
                 name: str = None,
                 description: str = None,
                 address: str = None,
                 enabled: bool = None) -> None:
        """
        Initialize a OriginInput object.

        :param str name: (optional) The name of the origin server.
        :param str description: (optional) Description of the origin server.
        :param str address: (optional) The address of the origin server. It can be
               a hostname or an IP address.
        :param bool enabled: (optional) Whether the origin server is enabled.
        """
        self.name = name
        self.description = description
        self.address = address
        self.enabled = enabled

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'OriginInput':
        """Initialize a OriginInput object from a json dictionary."""
        args = {}
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        if 'description' in _dict:
            args['description'] = _dict.get('description')
        if 'address' in _dict:
            args['address'] = _dict.get('address')
        if 'enabled' in _dict:
            args['enabled'] = _dict.get('enabled')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a OriginInput object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'description') and self.description is not None:
            _dict['description'] = self.description
        if hasattr(self, 'address') and self.address is not None:
            _dict['address'] = self.address
        if hasattr(self, 'enabled') and self.enabled is not None:
            _dict['enabled'] = self.enabled
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this OriginInput object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'OriginInput') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'OriginInput') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class PermittedNetwork():
    """
    Permitted network details.

    :attr str id: (optional) Unique identifier of a permitted network.
    :attr str created_on: (optional) The time when a permitted network is created.
    :attr str modified_on: (optional) The recent time when a permitted network is
          modified.
    :attr PermittedNetworkVpc permitted_network: (optional) Permitted network data
          for VPC.
    :attr str type: (optional) The type of a permitted network.
    :attr str state: (optional) The state of a permitted network.
    """

    def __init__(self,
                 *,
                 id: str = None,
                 created_on: str = None,
                 modified_on: str = None,
                 permitted_network: 'PermittedNetworkVpc' = None,
                 type: str = None,
                 state: str = None) -> None:
        """
        Initialize a PermittedNetwork object.

        :param str id: (optional) Unique identifier of a permitted network.
        :param str created_on: (optional) The time when a permitted network is
               created.
        :param str modified_on: (optional) The recent time when a permitted network
               is modified.
        :param PermittedNetworkVpc permitted_network: (optional) Permitted network
               data for VPC.
        :param str type: (optional) The type of a permitted network.
        :param str state: (optional) The state of a permitted network.
        """
        self.id = id
        self.created_on = created_on
        self.modified_on = modified_on
        self.permitted_network = permitted_network
        self.type = type
        self.state = state

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'PermittedNetwork':
        """Initialize a PermittedNetwork object from a json dictionary."""
        args = {}
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        if 'created_on' in _dict:
            args['created_on'] = _dict.get('created_on')
        if 'modified_on' in _dict:
            args['modified_on'] = _dict.get('modified_on')
        if 'permitted_network' in _dict:
            args['permitted_network'] = PermittedNetworkVpc.from_dict(_dict.get('permitted_network'))
        if 'type' in _dict:
            args['type'] = _dict.get('type')
        if 'state' in _dict:
            args['state'] = _dict.get('state')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a PermittedNetwork object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        if hasattr(self, 'created_on') and self.created_on is not None:
            _dict['created_on'] = self.created_on
        if hasattr(self, 'modified_on') and self.modified_on is not None:
            _dict['modified_on'] = self.modified_on
        if hasattr(self, 'permitted_network') and self.permitted_network is not None:
            _dict['permitted_network'] = self.permitted_network.to_dict()
        if hasattr(self, 'type') and self.type is not None:
            _dict['type'] = self.type
        if hasattr(self, 'state') and self.state is not None:
            _dict['state'] = self.state
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this PermittedNetwork object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'PermittedNetwork') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'PermittedNetwork') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class TypeEnum(str, Enum):
        """
        The type of a permitted network.
        """
        VPC = 'vpc'


    class StateEnum(str, Enum):
        """
        The state of a permitted network.
        """
        ACTIVE = 'ACTIVE'
        REMOVAL_IN_PROGRESS = 'REMOVAL_IN_PROGRESS'


class PermittedNetworkVpc():
    """
    Permitted network data for VPC.

    :attr str vpc_crn: CRN string uniquely identifies a VPC.
    """

    def __init__(self,
                 vpc_crn: str) -> None:
        """
        Initialize a PermittedNetworkVpc object.

        :param str vpc_crn: CRN string uniquely identifies a VPC.
        """
        self.vpc_crn = vpc_crn

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'PermittedNetworkVpc':
        """Initialize a PermittedNetworkVpc object from a json dictionary."""
        args = {}
        if 'vpc_crn' in _dict:
            args['vpc_crn'] = _dict.get('vpc_crn')
        else:
            raise ValueError('Required property \'vpc_crn\' not present in PermittedNetworkVpc JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a PermittedNetworkVpc object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'vpc_crn') and self.vpc_crn is not None:
            _dict['vpc_crn'] = self.vpc_crn
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this PermittedNetworkVpc object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'PermittedNetworkVpc') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'PermittedNetworkVpc') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class Pool():
    """
    Load balancer pool details.

    :attr str id: (optional) Identifier of the load balancer pool.
    :attr str name: (optional) Name of the load balancer pool.
    :attr str description: (optional) Descriptive text of the load balancer pool.
    :attr bool enabled: (optional) Whether the load balancer pool is enabled.
    :attr int healthy_origins_threshold: (optional) The minimum number of origins
          that must be healthy for this pool to serve traffic. If the number of healthy
          origins falls below this number, the pool will be marked unhealthy and we will
          failover to the next available pool.
    :attr List[Origin] origins: (optional) The list of origins within this pool.
          Traffic directed at this pool is balanced across all currently healthy origins,
          provided the pool itself is healthy.
    :attr str monitor: (optional) The ID of the load balancer monitor to be
          associated to this pool.
    :attr str notification_channel: (optional) The notification channel.
    :attr str health: (optional) Healthy state of the load balancer pool.
    :attr str healthcheck_region: (optional) Health check region of VSIs.
    :attr List[str] healthcheck_subnets: (optional) Health check subnet CRNs.
    :attr List[PoolHealthcheckVsisItem] healthcheck_vsis: (optional) Health check
          VSI information.
    :attr str created_on: (optional) the time when a load balancer pool is created.
    :attr str modified_on: (optional) the recent time when a load balancer pool is
          modified.
    """

    def __init__(self,
                 *,
                 id: str = None,
                 name: str = None,
                 description: str = None,
                 enabled: bool = None,
                 healthy_origins_threshold: int = None,
                 origins: List['Origin'] = None,
                 monitor: str = None,
                 notification_channel: str = None,
                 health: str = None,
                 healthcheck_region: str = None,
                 healthcheck_subnets: List[str] = None,
                 healthcheck_vsis: List['PoolHealthcheckVsisItem'] = None,
                 created_on: str = None,
                 modified_on: str = None) -> None:
        """
        Initialize a Pool object.

        :param str id: (optional) Identifier of the load balancer pool.
        :param str name: (optional) Name of the load balancer pool.
        :param str description: (optional) Descriptive text of the load balancer
               pool.
        :param bool enabled: (optional) Whether the load balancer pool is enabled.
        :param int healthy_origins_threshold: (optional) The minimum number of
               origins that must be healthy for this pool to serve traffic. If the number
               of healthy origins falls below this number, the pool will be marked
               unhealthy and we will failover to the next available pool.
        :param List[Origin] origins: (optional) The list of origins within this
               pool. Traffic directed at this pool is balanced across all currently
               healthy origins, provided the pool itself is healthy.
        :param str monitor: (optional) The ID of the load balancer monitor to be
               associated to this pool.
        :param str notification_channel: (optional) The notification channel.
        :param str health: (optional) Healthy state of the load balancer pool.
        :param str healthcheck_region: (optional) Health check region of VSIs.
        :param List[str] healthcheck_subnets: (optional) Health check subnet CRNs.
        :param List[PoolHealthcheckVsisItem] healthcheck_vsis: (optional) Health
               check VSI information.
        :param str created_on: (optional) the time when a load balancer pool is
               created.
        :param str modified_on: (optional) the recent time when a load balancer
               pool is modified.
        """
        self.id = id
        self.name = name
        self.description = description
        self.enabled = enabled
        self.healthy_origins_threshold = healthy_origins_threshold
        self.origins = origins
        self.monitor = monitor
        self.notification_channel = notification_channel
        self.health = health
        self.healthcheck_region = healthcheck_region
        self.healthcheck_subnets = healthcheck_subnets
        self.healthcheck_vsis = healthcheck_vsis
        self.created_on = created_on
        self.modified_on = modified_on

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Pool':
        """Initialize a Pool object from a json dictionary."""
        args = {}
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        if 'description' in _dict:
            args['description'] = _dict.get('description')
        if 'enabled' in _dict:
            args['enabled'] = _dict.get('enabled')
        if 'healthy_origins_threshold' in _dict:
            args['healthy_origins_threshold'] = _dict.get('healthy_origins_threshold')
        if 'origins' in _dict:
            args['origins'] = [Origin.from_dict(x) for x in _dict.get('origins')]
        if 'monitor' in _dict:
            args['monitor'] = _dict.get('monitor')
        if 'notification_channel' in _dict:
            args['notification_channel'] = _dict.get('notification_channel')
        if 'health' in _dict:
            args['health'] = _dict.get('health')
        if 'healthcheck_region' in _dict:
            args['healthcheck_region'] = _dict.get('healthcheck_region')
        if 'healthcheck_subnets' in _dict:
            args['healthcheck_subnets'] = _dict.get('healthcheck_subnets')
        if 'healthcheck_vsis' in _dict:
            args['healthcheck_vsis'] = [PoolHealthcheckVsisItem.from_dict(x) for x in _dict.get('healthcheck_vsis')]
        if 'created_on' in _dict:
            args['created_on'] = _dict.get('created_on')
        if 'modified_on' in _dict:
            args['modified_on'] = _dict.get('modified_on')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Pool object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'description') and self.description is not None:
            _dict['description'] = self.description
        if hasattr(self, 'enabled') and self.enabled is not None:
            _dict['enabled'] = self.enabled
        if hasattr(self, 'healthy_origins_threshold') and self.healthy_origins_threshold is not None:
            _dict['healthy_origins_threshold'] = self.healthy_origins_threshold
        if hasattr(self, 'origins') and self.origins is not None:
            _dict['origins'] = [x.to_dict() for x in self.origins]
        if hasattr(self, 'monitor') and self.monitor is not None:
            _dict['monitor'] = self.monitor
        if hasattr(self, 'notification_channel') and self.notification_channel is not None:
            _dict['notification_channel'] = self.notification_channel
        if hasattr(self, 'health') and self.health is not None:
            _dict['health'] = self.health
        if hasattr(self, 'healthcheck_region') and self.healthcheck_region is not None:
            _dict['healthcheck_region'] = self.healthcheck_region
        if hasattr(self, 'healthcheck_subnets') and self.healthcheck_subnets is not None:
            _dict['healthcheck_subnets'] = self.healthcheck_subnets
        if hasattr(self, 'healthcheck_vsis') and self.healthcheck_vsis is not None:
            _dict['healthcheck_vsis'] = [x.to_dict() for x in self.healthcheck_vsis]
        if hasattr(self, 'created_on') and self.created_on is not None:
            _dict['created_on'] = self.created_on
        if hasattr(self, 'modified_on') and self.modified_on is not None:
            _dict['modified_on'] = self.modified_on
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this Pool object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'Pool') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'Pool') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class HealthEnum(str, Enum):
        """
        Healthy state of the load balancer pool.
        """
        HEALTHY = 'HEALTHY'
        DEGRADED = 'DEGRADED'
        CRITICAL = 'CRITICAL'


    class HealthcheckRegionEnum(str, Enum):
        """
        Health check region of VSIs.
        """
        US_SOUTH = 'us-south'
        US_EAST = 'us-east'
        EU_GB = 'eu-gb'
        EU_DU = 'eu-du'
        AU_SYD = 'au-syd'
        JP_TOK = 'jp-tok'


class ResourceRecord():
    """
    Resource record details.

    :attr str id: (optional) Identifier of the resource record.
    :attr str created_on: (optional) the time when a resource record is created.
    :attr str modified_on: (optional) the recent time when a resource record is
          modified.
    :attr str name: (optional) Name of the resource record.
    :attr str type: (optional) Type of the resource record.
    :attr int ttl: (optional) Time to live in second.
    :attr object rdata: (optional) Content of the resource record.
    :attr str service: (optional) Only used for SRV record.
    :attr str protocol: (optional) Only used for SRV record.
    """

    def __init__(self,
                 *,
                 id: str = None,
                 created_on: str = None,
                 modified_on: str = None,
                 name: str = None,
                 type: str = None,
                 ttl: int = None,
                 rdata: object = None,
                 service: str = None,
                 protocol: str = None) -> None:
        """
        Initialize a ResourceRecord object.

        :param str id: (optional) Identifier of the resource record.
        :param str created_on: (optional) the time when a resource record is
               created.
        :param str modified_on: (optional) the recent time when a resource record
               is modified.
        :param str name: (optional) Name of the resource record.
        :param str type: (optional) Type of the resource record.
        :param int ttl: (optional) Time to live in second.
        :param object rdata: (optional) Content of the resource record.
        :param str service: (optional) Only used for SRV record.
        :param str protocol: (optional) Only used for SRV record.
        """
        self.id = id
        self.created_on = created_on
        self.modified_on = modified_on
        self.name = name
        self.type = type
        self.ttl = ttl
        self.rdata = rdata
        self.service = service
        self.protocol = protocol

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ResourceRecord':
        """Initialize a ResourceRecord object from a json dictionary."""
        args = {}
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        if 'created_on' in _dict:
            args['created_on'] = _dict.get('created_on')
        if 'modified_on' in _dict:
            args['modified_on'] = _dict.get('modified_on')
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        if 'type' in _dict:
            args['type'] = _dict.get('type')
        if 'ttl' in _dict:
            args['ttl'] = _dict.get('ttl')
        if 'rdata' in _dict:
            args['rdata'] = _dict.get('rdata')
        if 'service' in _dict:
            args['service'] = _dict.get('service')
        if 'protocol' in _dict:
            args['protocol'] = _dict.get('protocol')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ResourceRecord object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        if hasattr(self, 'created_on') and self.created_on is not None:
            _dict['created_on'] = self.created_on
        if hasattr(self, 'modified_on') and self.modified_on is not None:
            _dict['modified_on'] = self.modified_on
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'type') and self.type is not None:
            _dict['type'] = self.type
        if hasattr(self, 'ttl') and self.ttl is not None:
            _dict['ttl'] = self.ttl
        if hasattr(self, 'rdata') and self.rdata is not None:
            _dict['rdata'] = self.rdata
        if hasattr(self, 'service') and self.service is not None:
            _dict['service'] = self.service
        if hasattr(self, 'protocol') and self.protocol is not None:
            _dict['protocol'] = self.protocol
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ResourceRecord object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ResourceRecord') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ResourceRecord') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class TypeEnum(str, Enum):
        """
        Type of the resource record.
        """
        A = 'A'
        AAAA = 'AAAA'
        CNAME = 'CNAME'
        MX = 'MX'
        SRV = 'SRV'
        TXT = 'TXT'
        PTR = 'PTR'


class ResourceRecordInputRdataRdataARecord(ResourceRecordInputRdata):
    """
    The content of type-A resource record.

    :attr str ip: IPv4 address.
    """

    def __init__(self,
                 ip: str) -> None:
        """
        Initialize a ResourceRecordInputRdataRdataARecord object.

        :param str ip: IPv4 address.
        """
        # pylint: disable=super-init-not-called
        self.ip = ip

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ResourceRecordInputRdataRdataARecord':
        """Initialize a ResourceRecordInputRdataRdataARecord object from a json dictionary."""
        args = {}
        if 'ip' in _dict:
            args['ip'] = _dict.get('ip')
        else:
            raise ValueError('Required property \'ip\' not present in ResourceRecordInputRdataRdataARecord JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ResourceRecordInputRdataRdataARecord object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'ip') and self.ip is not None:
            _dict['ip'] = self.ip
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ResourceRecordInputRdataRdataARecord object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ResourceRecordInputRdataRdataARecord') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ResourceRecordInputRdataRdataARecord') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class ResourceRecordInputRdataRdataAaaaRecord(ResourceRecordInputRdata):
    """
    The content of type-AAAA resource record.

    :attr str ip: IPv6 address.
    """

    def __init__(self,
                 ip: str) -> None:
        """
        Initialize a ResourceRecordInputRdataRdataAaaaRecord object.

        :param str ip: IPv6 address.
        """
        # pylint: disable=super-init-not-called
        self.ip = ip

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ResourceRecordInputRdataRdataAaaaRecord':
        """Initialize a ResourceRecordInputRdataRdataAaaaRecord object from a json dictionary."""
        args = {}
        if 'ip' in _dict:
            args['ip'] = _dict.get('ip')
        else:
            raise ValueError('Required property \'ip\' not present in ResourceRecordInputRdataRdataAaaaRecord JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ResourceRecordInputRdataRdataAaaaRecord object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'ip') and self.ip is not None:
            _dict['ip'] = self.ip
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ResourceRecordInputRdataRdataAaaaRecord object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ResourceRecordInputRdataRdataAaaaRecord') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ResourceRecordInputRdataRdataAaaaRecord') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class ResourceRecordInputRdataRdataCnameRecord(ResourceRecordInputRdata):
    """
    The content of type-CNAME resource record.

    :attr str cname: Canonical name.
    """

    def __init__(self,
                 cname: str) -> None:
        """
        Initialize a ResourceRecordInputRdataRdataCnameRecord object.

        :param str cname: Canonical name.
        """
        # pylint: disable=super-init-not-called
        self.cname = cname

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ResourceRecordInputRdataRdataCnameRecord':
        """Initialize a ResourceRecordInputRdataRdataCnameRecord object from a json dictionary."""
        args = {}
        if 'cname' in _dict:
            args['cname'] = _dict.get('cname')
        else:
            raise ValueError('Required property \'cname\' not present in ResourceRecordInputRdataRdataCnameRecord JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ResourceRecordInputRdataRdataCnameRecord object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'cname') and self.cname is not None:
            _dict['cname'] = self.cname
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ResourceRecordInputRdataRdataCnameRecord object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ResourceRecordInputRdataRdataCnameRecord') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ResourceRecordInputRdataRdataCnameRecord') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class ResourceRecordInputRdataRdataMxRecord(ResourceRecordInputRdata):
    """
    The content of type-MX resource record.

    :attr str exchange: Hostname of Exchange server.
    :attr int preference: Preference of the MX record.
    """

    def __init__(self,
                 exchange: str,
                 preference: int) -> None:
        """
        Initialize a ResourceRecordInputRdataRdataMxRecord object.

        :param str exchange: Hostname of Exchange server.
        :param int preference: Preference of the MX record.
        """
        # pylint: disable=super-init-not-called
        self.exchange = exchange
        self.preference = preference

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ResourceRecordInputRdataRdataMxRecord':
        """Initialize a ResourceRecordInputRdataRdataMxRecord object from a json dictionary."""
        args = {}
        if 'exchange' in _dict:
            args['exchange'] = _dict.get('exchange')
        else:
            raise ValueError('Required property \'exchange\' not present in ResourceRecordInputRdataRdataMxRecord JSON')
        if 'preference' in _dict:
            args['preference'] = _dict.get('preference')
        else:
            raise ValueError('Required property \'preference\' not present in ResourceRecordInputRdataRdataMxRecord JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ResourceRecordInputRdataRdataMxRecord object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'exchange') and self.exchange is not None:
            _dict['exchange'] = self.exchange
        if hasattr(self, 'preference') and self.preference is not None:
            _dict['preference'] = self.preference
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ResourceRecordInputRdataRdataMxRecord object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ResourceRecordInputRdataRdataMxRecord') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ResourceRecordInputRdataRdataMxRecord') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class ResourceRecordInputRdataRdataPtrRecord(ResourceRecordInputRdata):
    """
    The content of type-PTR resource record.

    :attr str ptrdname: Hostname of the relevant A or AAAA record.
    """

    def __init__(self,
                 ptrdname: str) -> None:
        """
        Initialize a ResourceRecordInputRdataRdataPtrRecord object.

        :param str ptrdname: Hostname of the relevant A or AAAA record.
        """
        # pylint: disable=super-init-not-called
        self.ptrdname = ptrdname

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ResourceRecordInputRdataRdataPtrRecord':
        """Initialize a ResourceRecordInputRdataRdataPtrRecord object from a json dictionary."""
        args = {}
        if 'ptrdname' in _dict:
            args['ptrdname'] = _dict.get('ptrdname')
        else:
            raise ValueError('Required property \'ptrdname\' not present in ResourceRecordInputRdataRdataPtrRecord JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ResourceRecordInputRdataRdataPtrRecord object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'ptrdname') and self.ptrdname is not None:
            _dict['ptrdname'] = self.ptrdname
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ResourceRecordInputRdataRdataPtrRecord object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ResourceRecordInputRdataRdataPtrRecord') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ResourceRecordInputRdataRdataPtrRecord') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class ResourceRecordInputRdataRdataSrvRecord(ResourceRecordInputRdata):
    """
    The content of type-SRV resource record.

    :attr int port: Port number of the target server.
    :attr int priority: Priority of the SRV record.
    :attr str target: Hostname of the target server.
    :attr int weight: Weight of distributing queries among multiple target servers.
    """

    def __init__(self,
                 port: int,
                 priority: int,
                 target: str,
                 weight: int) -> None:
        """
        Initialize a ResourceRecordInputRdataRdataSrvRecord object.

        :param int port: Port number of the target server.
        :param int priority: Priority of the SRV record.
        :param str target: Hostname of the target server.
        :param int weight: Weight of distributing queries among multiple target
               servers.
        """
        # pylint: disable=super-init-not-called
        self.port = port
        self.priority = priority
        self.target = target
        self.weight = weight

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ResourceRecordInputRdataRdataSrvRecord':
        """Initialize a ResourceRecordInputRdataRdataSrvRecord object from a json dictionary."""
        args = {}
        if 'port' in _dict:
            args['port'] = _dict.get('port')
        else:
            raise ValueError('Required property \'port\' not present in ResourceRecordInputRdataRdataSrvRecord JSON')
        if 'priority' in _dict:
            args['priority'] = _dict.get('priority')
        else:
            raise ValueError('Required property \'priority\' not present in ResourceRecordInputRdataRdataSrvRecord JSON')
        if 'target' in _dict:
            args['target'] = _dict.get('target')
        else:
            raise ValueError('Required property \'target\' not present in ResourceRecordInputRdataRdataSrvRecord JSON')
        if 'weight' in _dict:
            args['weight'] = _dict.get('weight')
        else:
            raise ValueError('Required property \'weight\' not present in ResourceRecordInputRdataRdataSrvRecord JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ResourceRecordInputRdataRdataSrvRecord object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'port') and self.port is not None:
            _dict['port'] = self.port
        if hasattr(self, 'priority') and self.priority is not None:
            _dict['priority'] = self.priority
        if hasattr(self, 'target') and self.target is not None:
            _dict['target'] = self.target
        if hasattr(self, 'weight') and self.weight is not None:
            _dict['weight'] = self.weight
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ResourceRecordInputRdataRdataSrvRecord object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ResourceRecordInputRdataRdataSrvRecord') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ResourceRecordInputRdataRdataSrvRecord') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class ResourceRecordInputRdataRdataTxtRecord(ResourceRecordInputRdata):
    """
    The content of type-TXT resource record.

    :attr str text: Human readable text.
    """

    def __init__(self,
                 text: str) -> None:
        """
        Initialize a ResourceRecordInputRdataRdataTxtRecord object.

        :param str text: Human readable text.
        """
        # pylint: disable=super-init-not-called
        self.text = text

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ResourceRecordInputRdataRdataTxtRecord':
        """Initialize a ResourceRecordInputRdataRdataTxtRecord object from a json dictionary."""
        args = {}
        if 'text' in _dict:
            args['text'] = _dict.get('text')
        else:
            raise ValueError('Required property \'text\' not present in ResourceRecordInputRdataRdataTxtRecord JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ResourceRecordInputRdataRdataTxtRecord object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'text') and self.text is not None:
            _dict['text'] = self.text
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ResourceRecordInputRdataRdataTxtRecord object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ResourceRecordInputRdataRdataTxtRecord') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ResourceRecordInputRdataRdataTxtRecord') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class ResourceRecordUpdateInputRdataRdataARecord(ResourceRecordUpdateInputRdata):
    """
    The content of type-A resource record.

    :attr str ip: IPv4 address.
    """

    def __init__(self,
                 ip: str) -> None:
        """
        Initialize a ResourceRecordUpdateInputRdataRdataARecord object.

        :param str ip: IPv4 address.
        """
        # pylint: disable=super-init-not-called
        self.ip = ip

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ResourceRecordUpdateInputRdataRdataARecord':
        """Initialize a ResourceRecordUpdateInputRdataRdataARecord object from a json dictionary."""
        args = {}
        if 'ip' in _dict:
            args['ip'] = _dict.get('ip')
        else:
            raise ValueError('Required property \'ip\' not present in ResourceRecordUpdateInputRdataRdataARecord JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ResourceRecordUpdateInputRdataRdataARecord object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'ip') and self.ip is not None:
            _dict['ip'] = self.ip
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ResourceRecordUpdateInputRdataRdataARecord object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ResourceRecordUpdateInputRdataRdataARecord') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ResourceRecordUpdateInputRdataRdataARecord') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class ResourceRecordUpdateInputRdataRdataAaaaRecord(ResourceRecordUpdateInputRdata):
    """
    The content of type-AAAA resource record.

    :attr str ip: IPv6 address.
    """

    def __init__(self,
                 ip: str) -> None:
        """
        Initialize a ResourceRecordUpdateInputRdataRdataAaaaRecord object.

        :param str ip: IPv6 address.
        """
        # pylint: disable=super-init-not-called
        self.ip = ip

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ResourceRecordUpdateInputRdataRdataAaaaRecord':
        """Initialize a ResourceRecordUpdateInputRdataRdataAaaaRecord object from a json dictionary."""
        args = {}
        if 'ip' in _dict:
            args['ip'] = _dict.get('ip')
        else:
            raise ValueError('Required property \'ip\' not present in ResourceRecordUpdateInputRdataRdataAaaaRecord JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ResourceRecordUpdateInputRdataRdataAaaaRecord object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'ip') and self.ip is not None:
            _dict['ip'] = self.ip
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ResourceRecordUpdateInputRdataRdataAaaaRecord object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ResourceRecordUpdateInputRdataRdataAaaaRecord') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ResourceRecordUpdateInputRdataRdataAaaaRecord') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class ResourceRecordUpdateInputRdataRdataCnameRecord(ResourceRecordUpdateInputRdata):
    """
    The content of type-CNAME resource record.

    :attr str cname: Canonical name.
    """

    def __init__(self,
                 cname: str) -> None:
        """
        Initialize a ResourceRecordUpdateInputRdataRdataCnameRecord object.

        :param str cname: Canonical name.
        """
        # pylint: disable=super-init-not-called
        self.cname = cname

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ResourceRecordUpdateInputRdataRdataCnameRecord':
        """Initialize a ResourceRecordUpdateInputRdataRdataCnameRecord object from a json dictionary."""
        args = {}
        if 'cname' in _dict:
            args['cname'] = _dict.get('cname')
        else:
            raise ValueError('Required property \'cname\' not present in ResourceRecordUpdateInputRdataRdataCnameRecord JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ResourceRecordUpdateInputRdataRdataCnameRecord object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'cname') and self.cname is not None:
            _dict['cname'] = self.cname
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ResourceRecordUpdateInputRdataRdataCnameRecord object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ResourceRecordUpdateInputRdataRdataCnameRecord') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ResourceRecordUpdateInputRdataRdataCnameRecord') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class ResourceRecordUpdateInputRdataRdataMxRecord(ResourceRecordUpdateInputRdata):
    """
    The content of type-MX resource record.

    :attr str exchange: Hostname of Exchange server.
    :attr int preference: Preference of the MX record.
    """

    def __init__(self,
                 exchange: str,
                 preference: int) -> None:
        """
        Initialize a ResourceRecordUpdateInputRdataRdataMxRecord object.

        :param str exchange: Hostname of Exchange server.
        :param int preference: Preference of the MX record.
        """
        # pylint: disable=super-init-not-called
        self.exchange = exchange
        self.preference = preference

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ResourceRecordUpdateInputRdataRdataMxRecord':
        """Initialize a ResourceRecordUpdateInputRdataRdataMxRecord object from a json dictionary."""
        args = {}
        if 'exchange' in _dict:
            args['exchange'] = _dict.get('exchange')
        else:
            raise ValueError('Required property \'exchange\' not present in ResourceRecordUpdateInputRdataRdataMxRecord JSON')
        if 'preference' in _dict:
            args['preference'] = _dict.get('preference')
        else:
            raise ValueError('Required property \'preference\' not present in ResourceRecordUpdateInputRdataRdataMxRecord JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ResourceRecordUpdateInputRdataRdataMxRecord object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'exchange') and self.exchange is not None:
            _dict['exchange'] = self.exchange
        if hasattr(self, 'preference') and self.preference is not None:
            _dict['preference'] = self.preference
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ResourceRecordUpdateInputRdataRdataMxRecord object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ResourceRecordUpdateInputRdataRdataMxRecord') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ResourceRecordUpdateInputRdataRdataMxRecord') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class ResourceRecordUpdateInputRdataRdataPtrRecord(ResourceRecordUpdateInputRdata):
    """
    The content of type-PTR resource record.

    :attr str ptrdname: Hostname of the relevant A or AAAA record.
    """

    def __init__(self,
                 ptrdname: str) -> None:
        """
        Initialize a ResourceRecordUpdateInputRdataRdataPtrRecord object.

        :param str ptrdname: Hostname of the relevant A or AAAA record.
        """
        # pylint: disable=super-init-not-called
        self.ptrdname = ptrdname

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ResourceRecordUpdateInputRdataRdataPtrRecord':
        """Initialize a ResourceRecordUpdateInputRdataRdataPtrRecord object from a json dictionary."""
        args = {}
        if 'ptrdname' in _dict:
            args['ptrdname'] = _dict.get('ptrdname')
        else:
            raise ValueError('Required property \'ptrdname\' not present in ResourceRecordUpdateInputRdataRdataPtrRecord JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ResourceRecordUpdateInputRdataRdataPtrRecord object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'ptrdname') and self.ptrdname is not None:
            _dict['ptrdname'] = self.ptrdname
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ResourceRecordUpdateInputRdataRdataPtrRecord object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ResourceRecordUpdateInputRdataRdataPtrRecord') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ResourceRecordUpdateInputRdataRdataPtrRecord') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class ResourceRecordUpdateInputRdataRdataSrvRecord(ResourceRecordUpdateInputRdata):
    """
    The content of type-SRV resource record.

    :attr int port: Port number of the target server.
    :attr int priority: Priority of the SRV record.
    :attr str target: Hostname of the target server.
    :attr int weight: Weight of distributing queries among multiple target servers.
    """

    def __init__(self,
                 port: int,
                 priority: int,
                 target: str,
                 weight: int) -> None:
        """
        Initialize a ResourceRecordUpdateInputRdataRdataSrvRecord object.

        :param int port: Port number of the target server.
        :param int priority: Priority of the SRV record.
        :param str target: Hostname of the target server.
        :param int weight: Weight of distributing queries among multiple target
               servers.
        """
        # pylint: disable=super-init-not-called
        self.port = port
        self.priority = priority
        self.target = target
        self.weight = weight

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ResourceRecordUpdateInputRdataRdataSrvRecord':
        """Initialize a ResourceRecordUpdateInputRdataRdataSrvRecord object from a json dictionary."""
        args = {}
        if 'port' in _dict:
            args['port'] = _dict.get('port')
        else:
            raise ValueError('Required property \'port\' not present in ResourceRecordUpdateInputRdataRdataSrvRecord JSON')
        if 'priority' in _dict:
            args['priority'] = _dict.get('priority')
        else:
            raise ValueError('Required property \'priority\' not present in ResourceRecordUpdateInputRdataRdataSrvRecord JSON')
        if 'target' in _dict:
            args['target'] = _dict.get('target')
        else:
            raise ValueError('Required property \'target\' not present in ResourceRecordUpdateInputRdataRdataSrvRecord JSON')
        if 'weight' in _dict:
            args['weight'] = _dict.get('weight')
        else:
            raise ValueError('Required property \'weight\' not present in ResourceRecordUpdateInputRdataRdataSrvRecord JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ResourceRecordUpdateInputRdataRdataSrvRecord object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'port') and self.port is not None:
            _dict['port'] = self.port
        if hasattr(self, 'priority') and self.priority is not None:
            _dict['priority'] = self.priority
        if hasattr(self, 'target') and self.target is not None:
            _dict['target'] = self.target
        if hasattr(self, 'weight') and self.weight is not None:
            _dict['weight'] = self.weight
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ResourceRecordUpdateInputRdataRdataSrvRecord object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ResourceRecordUpdateInputRdataRdataSrvRecord') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ResourceRecordUpdateInputRdataRdataSrvRecord') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class ResourceRecordUpdateInputRdataRdataTxtRecord(ResourceRecordUpdateInputRdata):
    """
    The content of type-TXT resource record.

    :attr str text: Human readable text.
    """

    def __init__(self,
                 text: str) -> None:
        """
        Initialize a ResourceRecordUpdateInputRdataRdataTxtRecord object.

        :param str text: Human readable text.
        """
        # pylint: disable=super-init-not-called
        self.text = text

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ResourceRecordUpdateInputRdataRdataTxtRecord':
        """Initialize a ResourceRecordUpdateInputRdataRdataTxtRecord object from a json dictionary."""
        args = {}
        if 'text' in _dict:
            args['text'] = _dict.get('text')
        else:
            raise ValueError('Required property \'text\' not present in ResourceRecordUpdateInputRdataRdataTxtRecord JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ResourceRecordUpdateInputRdataRdataTxtRecord object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'text') and self.text is not None:
            _dict['text'] = self.text
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ResourceRecordUpdateInputRdataRdataTxtRecord object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ResourceRecordUpdateInputRdataRdataTxtRecord') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ResourceRecordUpdateInputRdataRdataTxtRecord') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other
